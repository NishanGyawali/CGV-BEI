import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from matplotlib.patches import Circle
import random

plt.style.use("dark_background")

# =====================================================
# GLOBAL STATE
# =====================================================
control_points = [[1, 1], [3, 6], [6, 2], [9, 7]]
selected_point = None
score = 0
q_index = 0

# =====================================================
# MATHEMATICS
# =====================================================
def de_casteljau(points, t):
    levels = [np.array(points)]
    while len(levels[-1]) > 1:
        next_level = []
        for i in range(len(levels[-1]) - 1):
            p = (1 - t) * levels[-1][i] + t * levels[-1][i + 1]
            next_level.append(p)
        levels.append(np.array(next_level))
    return levels

def bezier_curve(points, resolution=300):
    curve = []
    for t in np.linspace(0, 1, resolution):
        levels = de_casteljau(points, t)
        curve.append(levels[-1][0])
    return np.array(curve)

# =====================================================
# FIGURE LAYOUT
# =====================================================
fig = plt.figure(figsize=(13,8))

ax = fig.add_axes([0.05,0.1,0.6,0.8])
ax_q = fig.add_axes([0.7,0.35,0.28,0.5])
ax_q.axis("off")

t_slider = Slider(plt.axes([0.15,0.03,0.4,0.03]),
                  "Parameter t",0,1,valinit=0.5)

# =====================================================
# DRAW CURVE
# =====================================================
def draw():
    ax.cla()
    ax.set_xlim(0,10)
    ax.set_ylim(0,10)
    ax.set_aspect("equal")
    ax.grid(alpha=0.3)
    ax.set_title(f"Bézier Curve (Degree {len(control_points)-1})",
                 color="#00f5ff")

    pts = np.array(control_points)

    # Control polygon
    ax.plot(pts[:,0], pts[:,1], "--", color="gray")

    # Control points
    for p in pts:
        ax.add_patch(Circle((p[0],p[1]),0.2,color="#ff66ff"))

    # Curve
    curve = bezier_curve(control_points)
    ax.plot(curve[:,0],curve[:,1],color="#00f5ff",linewidth=3)

    # Point on curve
    levels = de_casteljau(control_points,t_slider.val)
    point = levels[-1][0]
    ax.scatter(point[0],point[1],color="yellow",s=100)

    fig.canvas.draw_idle()

# =====================================================
# MOUSE INTERACTION
# =====================================================
def on_press(event):
    global selected_point
    if event.inaxes != ax:
        return
    for i,p in enumerate(control_points):
        if np.hypot(event.xdata-p[0],event.ydata-p[1])<0.3:
            selected_point = i

def on_release(event):
    global selected_point
    selected_point=None

def on_motion(event):
    if selected_point is None or event.inaxes!=ax:
        return
    control_points[selected_point]=[event.xdata,event.ydata]
    draw()

fig.canvas.mpl_connect("button_press_event",on_press)
fig.canvas.mpl_connect("button_release_event",on_release)
fig.canvas.mpl_connect("motion_notify_event",on_motion)

# =====================================================
# ADD / REMOVE CONTROL POINTS
# =====================================================
def add_point(event):
    if len(control_points) < 8:
        control_points.append([
            random.uniform(1,9),
            random.uniform(1,9)
        ])
        draw()

def remove_point(event):
    if len(control_points) > 2:
        control_points.pop()
        draw()

btn_add = Button(plt.axes([0.72,0.15,0.12,0.06]),
                 "Add Point",
                 color="#444444",
                 hovercolor="#888888")
btn_add.label.set_color("white")
btn_add.on_clicked(add_point)

btn_remove = Button(plt.axes([0.86,0.15,0.12,0.06]),
                    "Remove Point",
                    color="#444444",
                    hovercolor="#888888")
btn_remove.label.set_color("white")
btn_remove.on_clicked(remove_point)

# =====================================================
# INTERACTIVE QUIZ SYSTEM (PARAMETER-BASED FINAL Q)
# =====================================================

score = 0
q_index = 0
buttons = []

questions = [
("Curve lies inside polygon due to:",
 ["A) Convex Hull","B) Symmetry","C) Periodicity"],"A","static"),

("Higher degree gives:",
 ["A) More flexibility","B) Less control","C) Linearity"],"A","static"),

("Move slider so t > 0.7.\nWhere is the yellow point?",
 ["A) Near first control point",
  "B) Near last control point",
  "C) Always center"],"B","parameter")
]


def display_question():
    ax_q.cla()
    ax_q.axis("off")

    # Final result → Pie Chart
    if q_index >= len(questions):
        correct_pct = score / len(questions)
        incorrect_pct = 1 - correct_pct

        sizes = [correct_pct, incorrect_pct]
        colors = ["#00f5ff", "#444444"]

        wedges, _ = ax_q.pie(
            sizes,
            colors=colors,
            startangle=90,
            counterclock=False,
            wedgeprops=dict(width=0.35)
        )

        # Center text
        ax_q.text(0, 0.1,
                  "Score",
                  ha="center",
                  fontsize=12,
                  color="white")

        ax_q.text(0, -0.1,
                  f"{int(correct_pct*100)}%",
                  ha="center",
                  fontsize=20,
                  color="#ffd700",
                  weight="bold")

        ax_q.set_aspect("equal")
        fig.canvas.draw_idle()
        return

    # Otherwise → show circular question panel
    circle = Circle((0.5,0.5),0.45,
                    transform=ax_q.transAxes,
                    color="#1a1a2e")
    ax_q.add_patch(circle)

    q = questions[q_index]

    ax_q.text(0.5,0.75,
              q[0],
              ha="center",
              fontsize=11,
              color="white",
              wrap=True)

    for i,opt in enumerate(q[1]):
        ax_q.text(0.5,0.6-i*0.12,
                  opt,
                  ha="center",
                  fontsize=10,
                  color="#dddddd")

    fig.canvas.draw_idle()
   
    # FINAL RESULT INSIDE CIRCLE
    if q_index >= len(questions):
        pct = int((score/len(questions))*100)

        ax_q.text(0.5,0.6,
                  "Final Score",
                  ha="center",
                  fontsize=14,
                  color="white")

        ax_q.text(0.5,0.45,
                  f"{score}/{len(questions)}",
                  ha="center",
                  fontsize=22,
                  color="#ffd700",
                  weight="bold")

        ax_q.text(0.5,0.30,
                  f"{pct}%",
                  ha="center",
                  fontsize=16,
                  color="#00f5ff")

        fig.canvas.draw_idle()
        return

    q = questions[q_index]

    ax_q.text(0.5,0.75,
              q[0],
              ha="center",
              fontsize=11,
              color="white",
              wrap=True)

    for i,opt in enumerate(q[1]):
        ax_q.text(0.5,0.6-i*0.12,
                  opt,
                  ha="center",
                  fontsize=10,
                  color="#dddddd")

    fig.canvas.draw_idle()


def answer(letter):
    global score, q_index

    if q_index >= len(questions):
        return

    question, options, correct, q_type = questions[q_index]

    # PARAMETER-BASED LOGIC
    if q_type == "parameter":
        t_val = t_slider.val
        if t_val > 0.7:
            real_answer = "B"
        else:
            real_answer = "A"
    else:
        real_answer = correct

    if letter == real_answer:
        score += 1

    q_index += 1
    display_question()


# =====================================================
# BUTTON CREATION (STABLE)
# =====================================================

def create_buttons():
    global buttons
    letters = ["A","B","C"]
    buttons.clear()

    for i,l in enumerate(letters):
        ax_btn = plt.axes([0.75+i*0.08,0.25,0.07,0.06])
        btn = Button(ax_btn,
                     l,
                     color="#333333",
                     hovercolor="#777777")

        btn.label.set_color("white")

        def make_callback(letter):
            return lambda event: answer(letter)

        btn.on_clicked(make_callback(l))
        buttons.append(btn)


create_buttons()
display_question()

# =====================================================
# EVENTS
# =====================================================
t_slider.on_changed(lambda val: draw())

draw()
plt.show()
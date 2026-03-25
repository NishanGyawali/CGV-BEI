import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from matplotlib.patches import Wedge

plt.style.use("dark_background")

# -------------------------------------------------
# FIGURE & LAYOUT
# -------------------------------------------------
fig = plt.figure(figsize=(15, 8))
gs = fig.add_gridspec(3, 3, height_ratios=[3, 1, 1], width_ratios=[3, 1, 0.05])

ax = fig.add_subplot(gs[:, 0])
ax_mcq = fig.add_subplot(gs[0, 1])
ax_ctrl = fig.add_subplot(gs[1:, 1])

plt.subplots_adjust(wspace=0.35, hspace=0.4)

# -------------------------------------------------
# COMPLEX PLANE
# -------------------------------------------------
def setup_plane():
    ax.cla()
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.25)
    ax.axhline(0, color="#ff4fd8", lw=1)
    ax.axvline(0, color="#ff4fd8", lw=1)
    ax.set_title("Arrow = Turn + Stretch",
                 fontsize=16, color="#ff7bff", weight="bold")

setup_plane()

# -------------------------------------------------
# STATE
# -------------------------------------------------
mag = 2.0
angle = 0.0
z = mag * np.exp(1j * angle)

# -------------------------------------------------
# DRAW
# -------------------------------------------------
def draw():
    setup_plane()
    ax.quiver(0, 0, z.real, z.imag,
              angles="xy", scale_units="xy", scale=1,
              color="#00f5ff", width=0.02)
    ax.text(z.real*0.6, z.imag*0.6, "arrow",
            color="#00f5ff", fontsize=13, weight="bold")
    fig.canvas.draw_idle()

draw()

# -------------------------------------------------
# SLIDERS
# -------------------------------------------------
ax_ctrl.axis("off")

s_mag = Slider(
    plt.axes([0.66, 0.30, 0.25, 0.02]),
    "Stretch", 0.5, 4, valinit=mag, color="#00f5ff"
)

s_ang = Slider(
    plt.axes([0.66, 0.24, 0.25, 0.02]),
    "Turn", 0, 360, valinit=0, color="#ff66ff"
)

def slider_update(val):
    global z
    z = s_mag.val * np.exp(1j * np.deg2rad(s_ang.val))
    draw()

s_mag.on_changed(slider_update)
s_ang.on_changed(slider_update)

# -------------------------------------------------
# ROTATE BUTTON
# -------------------------------------------------
def rotate_once(event):
    global z
    z *= 1j
    draw()

btn_i = Button(
    plt.axes([0.70, 0.15, 0.18, 0.06]),
    "Rotate Same Way",
    color="#b26cff",
    hovercolor="#ffccff"
)
btn_i.label.set_color("black")
btn_i.on_clicked(rotate_once)

# -------------------------------------------------
# MCQs
# -------------------------------------------------
ax_mcq.axis("off")
score = 0
q_index = 0
wrong = []

questions = [
    ("Q1\nMove the TURN slider.\nWhat does the arrow do?",
     ["A) Changes color", "B) Turns around the center", "C) Breaks", "D) Shrinks"], "B"),

    ("Q2\nMove the STRETCH slider.\nWhat changes?",
     ["A) Direction", "B) Length", "C) Color", "D) Position"], "B"),

    ("Q3\nPress 'Rotate Same Way'multiple times.\nWhat happened?",
     ["A) It flipped", "B) It turned the same amount", "C) It got longer", "D) Nothing"], "B"),

    ("Q4\nPress it FOUR times.\nWhere is the arrow?",
     ["A) Somewhere new", "B) Opposite", "C) Back to start", "D) Smaller"], "C"),

    ("Q5\nRepeated presses trace which shape?",
     ["A) Line", "B) Square", "C) Circle", "D) Zigzag"], "C"),

    ("Q6\nIf two arrows have same length.\nWhat must be different?",
     ["A) Center", "B) Turn amount", "C) Stretch", "D) Nothing"], "B"),

    ("Q7\nTurning exactly half a circle,\nwhere will it point?",
     ["A) Same way", "B) Opposite", "C) Random", "D) Up"], "B"),

    ("Q8\nChoose the true statement:",
     ["A) Turning changes length",
      "B) Stretching changes turn",
      "C) Turning & stretching are independent",
      "D) Turning breaks arrow"], "C"),
]

q_text = ax_mcq.text(0.02, 0.75, questions[0][0],
                     fontsize=15, color="#eeeeee", weight="bold")

opt_texts = [
    ax_mcq.text(0.02, 0.55 - i*0.16, questions[0][1][i],
                fontsize=13, color="#cccccc")
    for i in range(4)
]

feedback = ax_mcq.text(0.5, -0.25, "",
                       ha="center", fontsize=16, color="#00f5ff")

# -------------------------------------------------
# ANSWER HANDLER
# -------------------------------------------------
def answer(letter):
    global score, q_index

    if letter == questions[q_index][2]:
        score += 1
        feedback.set_text("✔ Correct")
        feedback.set_color("#ffd700") 
    else:
        feedback.set_text("✘ Move sliders & observe")
        wrong.append(q_index + 1)
        feedback.set_color("#ff66ff")

    fig.canvas.draw_idle()
    plt.pause(0.2)

    q_index += 1
    if q_index < len(questions):
        q_text.set_text(questions[q_index][0])
        for i in range(4):
            opt_texts[i].set_text(questions[q_index][1][i])
        feedback.set_text("")
    else:
        show_result()

# -------------------------------------------------
# BUTTONS A–D  (FINAL FIX)
# -------------------------------------------------
letters = ["A", "B", "C", "D"]
colors = ["#ff66ff", "#7b5cff", "#ff003c", "#ffcc00"]
buttons = []

for i, l in enumerate(letters):
    axb = plt.axes([0.66 + i*0.06, 0.02, 0.055, 0.07])
    btn = Button(axb, l, color=colors[i], hovercolor="#ffffff")
    btn.label.set_color("black")
    btn.on_clicked(lambda e, x=l: answer(x))
    buttons.append(btn)   # ✅ CORRECT

# -------------------------------------------------
# RESULTS
# -------------------------------------------------
def show_result():
    ax_mcq.cla()
    ax_mcq.axis("off")

    pct = score / len(questions) * 100

    ring = Wedge((0.5, 0.55), 0.3, 0, pct*3.6,
                 facecolor="#2E8B57", edgecolor="#ff66ff")
    ax_mcq.add_patch(ring)

    ax_mcq.text(0.5, 0.55, f"{int(pct)}%",
                ha="center", va="center",
                fontsize=26, color="white", weight="bold")

    remark = "Mastery Achieved 🚀" if pct >= 85 else \
             "Solid Intuition 🧠" if pct >= 60 else \
             "Replay & Explore 🔄"

    ax_mcq.text(0.5, 0.2, remark,
                ha="center", fontsize=16, color="#ffcc00")

    if wrong:
        ax_mcq.text(0.5, 0.05,
                    f"Mistakes in Q: {wrong}",
                    ha="center", fontsize=12, color="#ff6666")

plt.show()

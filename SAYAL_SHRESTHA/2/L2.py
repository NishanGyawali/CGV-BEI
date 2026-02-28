import matplotlib.pyplot as plt

# Dark aesthetic style
plt.style.use('dark_background')


def dda_line(x1, y1, x2, y2):
    xes, yes = [], []

    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))

    if steps == 0:
        return [x1], [y1]

    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1
    for _ in range(steps + 1):
        xes.append(round(x))
        yes.append(round(y))
        x += x_inc
        y += y_inc

    return xes, yes


def draw_axis(x1, y1, x2, y2, color, label):
    xes, yes = dda_line(x1, y1, x2, y2)
    plt.plot(
        xes, yes,
        marker='o',
        linestyle='-',
        color=color,
        linewidth=2,
        label=label
    )


# ---------- AXES LIMIT ----------
L = 10   # length of axes

plt.figure(figsize=(7, 7))

# X-axis
draw_axis(-L, 0, L, 0, 'cyan', 'X-axis')

# Y-axis
draw_axis(0, -L, 0, L, 'magenta', 'Y-axis')

# Origin
plt.scatter(0, 0, color='yellow', s=80, zorder=3, label='Origin (0,0)')

plt.title("Coordinate Axes using DDA Algorithm  Roll:41")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True, linestyle='--', alpha=0.4)
plt.axis('equal')
plt.legend()
plt.show()

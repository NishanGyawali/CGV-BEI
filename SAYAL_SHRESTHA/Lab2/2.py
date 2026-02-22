import matplotlib.pyplot as plt

plt.style.use('dark_background')

def dda_line(x1, y1, x2, y2):
    xes, yes = [], []

    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))

    # Handle single-point case
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


def plot_line(x1, y1, x2, y2, label, color):
    xes, yes = dda_line(x1, y1, x2, y2)
    plt.plot(
        xes, yes,
        marker='o',
        linestyle='-',
        color=color,
        linewidth=2,
        markersize=5,
        label=label
    )


plt.figure(figsize=(8, 8))

# |m| < 1
plot_line(0, 0, 140, 70, "Slope |m| < 1", "cyan")

# |m| > 1
plot_line(0, 0, 70, 140, "Slope |m| > 1", "magenta")

# Horizontal line (m = 0)
plot_line(2, 70, 140, 70, "Horizontal line", "yellow")

# Vertical line (m = ∞)
plot_line(70, 2, 70, 140, "Vertical line", "lime")

# Negative slope
plot_line(0, 140, 140, 0, "Negative slope", "orange")

plt.title("DDA – All Slope Cases    Roll: 41", fontsize=14)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True, linestyle="--", alpha=0.4)
plt.axis("equal")
plt.legend()
plt.show()

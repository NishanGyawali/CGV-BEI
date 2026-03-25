import matplotlib.pyplot as plt

plt.style.use('dark_background')


def dda_line(x1, y1, x2, y2):
    xes, yes = [], []

    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))

    # Single point case
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


def plot_dda(x1, y1, x2, y2):
    xes, yes = dda_line(x1, y1, x2, y2)

    plt.figure(figsize=(7, 7))
    plt.plot(
        xes, yes,
        marker='o',
        linestyle='-',
        linewidth=2,
        markersize=6,
        color='cyan',
        label='DDA Line'
    )

    plt.scatter([x1, x2], [y1, y2], color='red', s=80, zorder=3, label='Endpoints')

    plt.title("DDA(User Input)  Roll: 41", fontsize=14)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.axis('equal')
    plt.legend()
    plt.show()


# -------- USER INPUT --------
print("Enter the endpoints of the line:")

x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

plot_dda(x1, y1, x2, y2)

#Draw lines with different slopes (m < 1, m > 1, horizontal, vertical, negative).
import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2):
    xes, yes = [], []
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))
    x_inc = dx / steps
    y_inc = dy / steps
    x, y = x1, y1

    for _ in range(steps + 1):
        xes.append(round(x))
        yes.append(round(y))
        x += x_inc
        y += y_inc

    return xes, yes


def plot_line(x1, y1, x2, y2, title):
    x, y = dda_line(x1, y1, x2, y2)
    plt.plot(x, y, marker='o')
    plt.title(title)
    plt.grid(True)
    plt.axis('equal')
    plt.show()


# Different slope cases
plot_line(2, 3, 15, 9, "Slope < 1")
plot_line(3, 2, 7, 15, "Slope > 1")
plot_line(2, 5, 15, 5, "Horizontal Line")
plot_line(6, 2, 6, 15, "Vertical Line")
plot_line(2, 15, 15, 5, "Negative Slope")

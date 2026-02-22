#Use DDA to draw the axes of a simple coordinate system.
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


def draw_axes(limit):
    # X-axis
    x, y = dda_line(-limit, 0, limit, 0)
    plt.plot(x, y, marker='o', label='X-axis')

    # Y-axis
    x, y = dda_line(0, -limit, 0, limit)
    plt.plot(x, y, marker='o', label='Y-axis')

    plt.title("Coordinate Axes using DDA")
    plt.grid(True)
    plt.axis('equal')
    plt.legend()
    plt.show()


# Example
draw_axes(10)

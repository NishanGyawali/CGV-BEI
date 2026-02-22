#Extend the DDA program to draw a rectangle given two opposite corners.
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


def draw_rectangle(x1, y1, x2, y2):
    # Other two corners
    x3, y3 = x1, y2
    x4, y4 = x2, y1

    # Draw four sides
    for (xa, ya, xb, yb) in [
        (x1, y1, x3, y3),
        (x3, y3, x2, y2),
        (x2, y2, x4, y4),
        (x4, y4, x1, y1)
    ]:
        x, y = dda_line(xa, ya, xb, yb)
        plt.plot(x, y, marker='o')

    plt.title("Rectangle using DDA")
    plt.grid(True)
    plt.axis('equal')
    plt.show()


# Example
draw_rectangle(2, 3, 12, 10)

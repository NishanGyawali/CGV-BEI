#2.Use DDA to draw the axes of a simple coordinate system (X and Y axes).

import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2):
    xs, ys = [], []
    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))
    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1
    for _ in range(steps + 1):
        xs.append(round(x))
        ys.append(round(y))
        x += x_inc
        y += y_inc
    return xs, ys

def draw_line(x1, y1, x2, y2):
    xs, ys = dda_line(x1, y1, x2, y2)
    plt.plot(xs, ys, linewidth=4, color='blue')

if __name__ == "__main__":
    plt.figure(figsize=(10, 10))
    plt.axis("equal")
    plt.grid(True)
    draw_line(-8, 0, 8, 0)   # X-axis
    draw_line(0, -8, 0, 8)   # Y-axis

    plt.show()
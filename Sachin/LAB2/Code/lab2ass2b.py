
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
    plt.plot(xs, ys)

if __name__ == "__main__":
    plt.figure(figsize=(6, 6))
    plt.axis("equal")
    plt.grid(True)

    draw_line(-10, 0, 10, 0)
    draw_line(0, -10, 0, 10)

    plt.show()

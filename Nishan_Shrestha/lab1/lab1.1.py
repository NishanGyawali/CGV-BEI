import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2):
    x_list = []
    y_list = []

    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))

    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1

    for _ in range(steps + 1):
        x_list.append(round(x))
        y_list.append(round(y))
        x += x_inc
        y += y_inc

    return x_list, y_list


def draw_line(x1, y1, x2, y2):
    xs, ys = dda_line(x1, y1, x2, y2)
    plt.plot(xs, ys, marker="o")


def draw_rectangle(x1, y1, x3, y3):
    x2, y2 = x3, y1
    x4, y4 = x1, y3

    draw_line(x1, y1, x2, y2)
    draw_line(x2, y2, x3, y3)
    draw_line(x3, y3, x4, y4)
    draw_line(x4, y4, x1, y1)


if __name__ == "__main__":
    x1, y1 = 3, 3
    x3, y3 = 10, 6

    plt.figure(figsize=(6, 6))
    plt.title("Rectangle Drawn Using DDA")
    plt.grid(True)
    plt.axis("equal")

    draw_rectangle(x1, y1, x3, y3)

    plt.show()
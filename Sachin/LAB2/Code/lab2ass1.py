import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2):
    x_coords = []
    y_coords = []

    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))

    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1

    for _ in range(steps + 1):
        x_coords.append(round(x))
        y_coords.append(round(y))
        x += x_inc
        y += y_inc

    return x_coords, y_coords


def plot_dda(x1, y1, x2, y2):
    xs, ys = dda_line(x1, y1, x2, y2)

    plt.figure(figsize=(6, 6))
    plt.plot(xs, ys, marker='o', linestyle='-', linewidth=1)
    plt.title("DDA Line Drawing Algorithm")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis("equal")
    plt.show()


if __name__ == "__main__":
    plot_dda(2, 3, 12, 8)

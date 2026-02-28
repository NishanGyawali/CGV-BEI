
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


def plot_line(x1, y1, x2, y2, label):
    xs, ys = dda_line(x1, y1, x2, y2)
    plt.plot(xs, ys, marker='o', linestyle='-', label=label)


if __name__ == "__main__":
    plt.figure(figsize=(7, 7))
    plt.title("DDA Line Drawing – Various Slopes")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis("equal")

   
    plot_line(2, 2, 12, 6, "Slope < 1")

    
    plot_line(2, 2, 6, 14, "Slope > 1")

    
    plot_line(2, 8, 12, 8, "Horizontal line")

    
    plot_line(6, 2, 6, 14, "Vertical line")


    plot_line(12, 12, 4, 4, "Negative slope")

    
    plt.legend()
    plt.show()

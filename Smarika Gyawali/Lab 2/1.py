import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    x_points = []
    y_points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x2 >= x1 else -1
    sy = 1 if y2 >= y1 else -1

    x, y = x1, y1

    if dx >= dy:
        p = 2 * dy - dx
        for i in range(dx + 1):
            x_points.append(x)
            y_points.append(y)
            x += sx
            if p >= 0:
                y += sy
                p += 2 * dy - 2 * dx
            else:
                p += 2 * dy
    else:
        p = 2 * dx - dy
        for i in range(dy + 1):
            x_points.append(x)
            y_points.append(y)
            y += sy
            if p >= 0:
                x += sx
                p += 2 * dx - 2 * dy
            else:
                p += 2 * dx

    return x_points, y_points


def plot_bresenham(x1, y1, x2, y2):
    x, y = bresenham_line(x1, y1, x2, y2)

    plt.figure(figsize=(6, 6))
    plt.plot(x, y, marker='o', linestyle='-', color='green')
    plt.title("Bresenham Line Drawing Algorithm")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')
    plt.show()

plot_bresenham(2, 3, 10, 8)

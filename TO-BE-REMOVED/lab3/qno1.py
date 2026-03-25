import matplotlib.pyplot as plt

def bresenham(x1, y1, x2, y2):
    x_points = []
    y_points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    x, y = x1, y1

    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    if dx > dy:
        p = 2 * dy - dx
        while x != x2:
            x_points.append(x)
            y_points.append(y)
            x += sx
            if p < 0:
                p += 2 * dy
            else:
                y += sy
                p += 2 * (dy - dx)
    else:
        p = 2 * dx - dy
        while y != y2:
            x_points.append(x)
            y_points.append(y)
            y += sy
            if p < 0:
                p += 2 * dx
            else:
                x += sx
                p += 2 * (dx - dy)

    x_points.append(x2)
    y_points.append(y2)

    plt.plot(x_points, y_points)


bresenham(2, 2, 10, 6)

plt.title("Bresenham's Line Drawing Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.gca().set_aspect('equal')
plt.grid(True)
plt.show()

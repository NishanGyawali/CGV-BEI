import matplotlib.pyplot as plt

def bresenham(x1, y1, x2, y2):
    x, y = x1, y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    x_points = []
    y_points = []

    if dx > dy:
        p = 2 * dy - dx
        for i in range(dx + 1):
            x_points.append(x)
            y_points.append(y)
            x += sx
            if p >= 0:
                y += sy
                p += 2 * (dy - dx)
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
                p += 2 * (dx - dy)
            else:
                p += 2 * dx

    return x_points, y_points


# Example
x_bre, y_bre = bresenham(2, 2, 10, 6)
plt.plot(x_bre, y_bre, 'o-', label="Bresenham")
plt.title("Bresenham Line Drawing")
plt.grid()
plt.legend()
plt.show()

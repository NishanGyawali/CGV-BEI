#Implement Bresenham’s algorithm
import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    xes, yes = [], []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x2 >= x1 else -1
    sy = 1 if y2 >= y1 else -1

    x, y = x1, y1

    # Case 1: Slope <= 1 (more horizontal)
    if dx >= dy:
        p = 2 * dy - dx
        for _ in range(dx + 1):
            xes.append(x)
            yes.append(y)

            x += sx
            if p >= 0:
                y += sy
                p += 2 * dy - 2 * dx
            else:
                p += 2 * dy

    # Case 2: Slope > 1 (more vertical)
    else:
        p = 2 * dx - dy
        for _ in range(dy + 1):
            xes.append(x)
            yes.append(y)

            y += sy
            if p >= 0:
                x += sx
                p += 2 * dx - 2 * dy
            else:
                p += 2 * dx

    return xes, yes


def plot_bresenham(x1, y1, x2, y2):
    xes, yes = bresenham_line(x1, y1, x2, y2)

    plt.figure(figsize=(6, 6))
    plt.plot(xes, yes, marker='o', linestyle='-', color='green')
    plt.title("Bresenham Line Drawing Algorithm")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')
    plt.show()


# Example
plot_bresenham(2, 3, 10, 8)

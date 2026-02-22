#1.Implement Bresenham’s algorithm as shown.
import matplotlib .pyplot as plt
def bresenham_line (x1 , y1 , x2 , y2):
    xes , yes = [], []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x2 >= x1 else -1
    sy = 1 if y2 >= y1 else -1
    x, y = x1 , y1
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
    return xes , yes
def plot_bresenham (x1 , y1 , x2 , y2):
    xes , yes = bresenham_line (x1 , y1 , x2 , y2)
    plt.figure(figsize =(6, 6))
    plt.plot(xes , yes , marker='o', linestyle ='-', color='red')
    plt.title(" Bresenham Line Drawing Algorithm ")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')
    plt.show()
plot_bresenham(2, 5, 10, 7)
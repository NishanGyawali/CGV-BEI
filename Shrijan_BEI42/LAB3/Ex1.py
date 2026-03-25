import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    xes, yes = [], []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x2 >= x1 else -1
    sy = 1 if y2 >= y1 else -1
    x, y = int(x1), int(y1)
    steps = None
    if dx >= dy:
        steps = dx
        p = 2 * dy - dx
        for _ in range(dx + 1):
            xes.append(int(x))
            yes.append(int(y))
            x += sx
            if p >= 0:
                y += sy
                p += 2 * dy - 2 * dx
            else:
                p += 2 * dy
    else:
        steps = dy
        p = 2 * dx - dy
        for _ in range(dy + 1):
            xes.append(int(x))
            yes.append(int(y))
            y += sy
            if p >= 0:
                x += sx
                p += 2 * dx - 2 * dy
            else:
                p += 2 * dx

    return xes, yes, steps

def plot_bresenham(x1, y1, x2, y2):
    xes, yes, steps_bres = bresenham_line(x1, y1, x2, y2)
    plt.figure(figsize=(6, 6))
    plt.plot(xes, yes, marker='o', color='blue')
    plt.title("Bresenham Line Drawing Algorithm")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')
    plt.show()
    return steps_bres

def DDA_line(x1, y1, x2, y2):
    xes, yes = [], []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    steps = int(max(dx, dy))
    xinc = int(dx / steps) if steps != 0 else 0
    yinc = int(dy / steps) if steps != 0 else 0
    x = int(x1)
    y = int(y1)
    for i in range(steps + 1):  # inclusive endpoint
        xes.append(int(x))
        yes.append(int(y))
        x += xinc
        y += yinc
    return xes, yes, steps

def plot_DDA(x1, y1, x2, y2):
    xes, yes, steps_dda = DDA_line(x1, y1, x2, y2)
    plt.figure(figsize=(6, 6))
    plt.plot(xes, yes, marker='o', color='red')
    plt.title("DDA Line Drawing Algorithm")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')
    plt.show()
    return steps_dda

if __name__ == "__main__":
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    steps_bresenham = plot_bresenham(x1, y1, x2, y2)
    steps_dda = plot_DDA(x1, y1, x2, y2)
    print(f"Number of steps in Bresenham: {steps_bresenham}")
    print(f"Number of steps in DDA: {steps_dda}")
    plot_bresenham(x1, y1, x2, y2)
    plot_DDA(x1, y1, x2, y2)
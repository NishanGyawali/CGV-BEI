import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    xes, yes = [], []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    lx = 1 if x2 >= x1 else -1  
    sy = 1 if y2 >= y1 else -1
    x, y = x1, y1
    
    if dx >= dy:
        p = 2 * dy - dx
        for _ in range(dx + 1):
            xes.append(x)
            yes.append(y)
            x += lx
            if p >= 0:
                y += sy
                p += 2 * dy - 2 * dx
            else:
                p += 2 * dy
    else:
        p = 2 * dx - dy
        for _ in range(dy + 1):
            xes.append(x)
            yes.append(y)
            y += sy
            if p >= 0:
                x += lx
                p += 2 * dx - 2 * dy
            else:
                p += 2 * dx

    return xes, yes

def dda_line(x1, y1, x2, y2):
    xes, yes = [], []
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))
    x_inc = dx / steps
    y_inc = dy / steps
    x, y = x1, y1
    
    for _ in range(steps + 1):
        xes.append(round(x))
        yes.append(round(y))
        x += x_inc
        y += y_inc

    return xes, yes

def plot_lines(x1, y1, x2, y2):
    # Set the dark background
    plt.style.use('dark_background')

    plt.figure(figsize=(10, 10))

    # Bresenham Line
    x_bresenham, y_bresenham = bresenham_line(x1, y1, x2, y2)
    plt.plot(x_bresenham, y_bresenham, marker='o', linestyle='-', color='magenta', label='Bresenham')

    # DDA Line
    x_dda, y_dda = dda_line(x1, y1, x2, y2)
    plt.plot(x_dda, y_dda, marker='x', linestyle='--', color='yellow', label='DDA')

    plt.title("Bresenham vs DDA Line Drawing Algorithm Roll 41")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True, color='white')
    plt.axis('equal')
    plt.legend()
    plt.xlim(min(x1, x2) - 1, max(x1, x2) + 1)  # Adjust x limits for visibility
    plt.ylim(min(y1, y2) - 1, max(y1, y2) + 1)  # Adjust y limits for visibility
    plt.show()


octants = [
    (0, 40, 40, 0),  
]

for (x1, y1, x2, y2) in octants:
    plot_lines(x1, y1, x2, y2)

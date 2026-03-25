import matplotlib.pyplot as plt


def dda_line(x1, y1, x2, y2):
    x_points = []
    y_points = []

    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))

    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1
    for i in range(steps + 1):
        x_points.append(round(x))
        y_points.append(round(y))
        x += x_inc
        y += y_inc

    return x_points, y_points


def dda_rectangle(x1, y1, x2, y2):
    
    x3, y3 = x1, y2
    x4, y4 = x2, y1

    
    sides = []
    sides.append(dda_line(x1, y1, x3, y3))  
    sides.append(dda_line(x3, y3, x2, y2))  
    sides.append(dda_line(x2, y2, x4, y4))  
    sides.append(dda_line(x4, y4, x1, y1))  

    return sides


def plot_rectangle(x1, y1, x2, y2):
    sides = dda_rectangle(x1, y1, x2, y2)
    plt.figure(figsize=(6,6))

    for side in sides:
        x, y = side
        plt.plot(x, y, 'o-', color='blue')  

    plt.title(f"DDA Rectangle from ({x1},{y1}) to ({x2},{y2})")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')
    plt.show()

plot_rectangle(2, 3, 10, 8)

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


def plot_axes(length=10):
    plt.figure(figsize=(6,6))

    
    x_axis = dda_line(-length, 0, length, 0)
    plt.plot(x_axis[0], x_axis[1], 'o-', color='red', label='X-axis')

    
    y_axis = dda_line(0, -length, 0, length)
    plt.plot(y_axis[0], y_axis[1], 'o-', color='green', label='Y-axis')

    
    plt.text(length+0.5, 0, 'X', fontsize=12)
    plt.text(0, length+0.5, 'Y', fontsize=12)

    plt.title("Coordinate System Using DDA")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')
    plt.legend()
    plt.show()
plot_axes(length=10)
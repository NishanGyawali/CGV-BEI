import matplotlib.pyplot as plt

def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))

    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1

    x_points = []
    y_points = []

    for i in range(steps + 1):
        x_points.append(round(x))
        y_points.append(round(y))
        x += x_inc
        y += y_inc

    return x_points, y_points


# Example
x_dda, y_dda = dda(2, 2, 10, 6)
plt.plot(x_dda, y_dda, 'o-', label="DDA")
plt.title("DDA Line Drawing")
plt.grid()
plt.legend()
plt.show()

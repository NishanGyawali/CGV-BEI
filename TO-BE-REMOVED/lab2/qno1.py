import matplotlib.pyplot as plt


def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))
    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1
    x_points = []
    y_points = []

    for _ in range(steps + 1):
        x_points.append(round(x))
        y_points.append(round(y))
        x += x_inc
        y += y_inc

    plt.plot(x_points, y_points)


def draw_rectangle(x1, y1, x2, y2):
    #
    x3, y3 = x1, y2
    x4, y4 = x2, y1

    dda(x1, y1, x3, y3)
    dda(x3, y3, x2, y2)
    dda(x2, y2, x4, y4)
    dda(x4, y4, x1, y1)

x1, y1 = 2, 2
x2, y2 = 8, 6

draw_rectangle(x1, y1, x2, y2)

plt.title("Rectangle using DDA Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.gca().set_aspect('equal')
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2):
    x_points = []
    y_points = []

    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))

    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1

    for i in range(steps + 1):
        x_points.append(round(x))
        y_points.append(round(y))
        x += x_inc
        y += y_inc

    return x_points, y_points
x1, y1 = 2, 2
x3, y3 = 10, 6



x2, y2 = x3, y1
x4, y4 = x1, y3


xA, yA = dda_line(x1, y1, x2, y2)
xB, yB = dda_line(x2, y2, x3, y3)
xC, yC = dda_line(x3, y3, x4, y4)
xD, yD = dda_line(x4, y4, x1, y1)

plt.figure()
plt.plot(xA, yA, marker='o')
plt.plot(xB, yB, marker='o')
plt.plot(xC, yC, marker='o')
plt.plot(xD, yD, marker='o')

plt.title("Rectangle using DDA Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
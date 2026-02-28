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

x_x, y_x = dda_line(-10, 0, 10, 0)


x_y, y_y = dda_line(0, -10, 0, 10)

plt.figure()
plt.plot(x_x, y_x, marker='o')  
plt.plot(x_y, y_y, marker='o')   

plt.title("Coordinate Axes using DDA Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axhline(0)
plt.axvline(0)
plt.show()
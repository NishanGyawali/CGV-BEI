import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))
    x_inc = dx / steps
    y_inc = dy / steps
    x, y = x1, y1
    px, py = [], []
    for _ in range(steps + 1):
        px.append(round(x))
        py.append(round(y))
        x += x_inc
        y += y_inc
    return px, py

x_min, x_max = -10, 10
y_min, y_max = -10, 10

px_x, py_x = dda_line(x_min, 0, x_max, 0)
px_y, py_y = dda_line(0, y_min, 0, y_max)

plt.plot(px_x, py_x, color='black')  # X-axis
plt.plot(px_y, py_y, color='black')  # Y-axis

plt.title("Simple Coordinate System using DDA")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.gca().set_aspect("equal", adjustable="box")
plt.grid(True)
plt.show()

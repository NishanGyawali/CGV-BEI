import matplotlib.pyplot as plt

# DDA line drawing function
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

# Draw X-axis (from -10 to 10)
dda(-10, 0, 10, 0)

# Draw Y-axis (from -10 to 10)
dda(0, -10, 0, 10)

plt.title("Coordinate Axes using DDA Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.gca().set_aspect('equal')
plt.grid(True)
plt.show()

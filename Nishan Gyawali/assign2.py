import matplotlib
matplotlib.use('TkAgg')  # For Windows compatibility
import matplotlib.pyplot as plt

def dda(x1, y1, x2, y2):
    """
    DDA algorithm to calculate points of a line from (x1, y1) to (x2, y2)
    Returns two lists: x_points, y_points
    """
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))  # Number of steps
    x_inc = dx / steps
    y_inc = dy / steps
    x_points, y_points = [], []
    x, y = x1, y1
    for _ in range(steps + 1):
        x_points.append(round(x))
        y_points.append(round(y))
        x += x_inc
        y += y_inc
    return x_points, y_points

# Define axes length (can be adjusted)
x_min, x_max = -10, 10
y_min, y_max = -10, 10

# Draw X-axis (horizontal)
x_axis_xs, x_axis_ys = dda(x_min, 0, x_max, 0)

# Draw Y-axis (vertical)
y_axis_xs, y_axis_ys = dda(0, y_min, 0, y_max)

# Plot axes
plt.figure()
plt.plot(x_axis_xs, x_axis_ys, marker='o')  # X-axis
plt.plot(y_axis_xs, y_axis_ys, marker='o')  # Y-axis

plt.title("Coordinate System using DDA")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)  # Optional reference line
plt.axvline(0, color='black', linewidth=0.5)  # Optional reference line
plt.show()

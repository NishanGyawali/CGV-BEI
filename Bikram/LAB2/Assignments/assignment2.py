# Assignment 2: Plot the axes of simple coordinate system using DDA line algorithm

import matplotlib.pyplot as plt

# DDA line function
def dda_line(x1, y1, x2, y2):
    x_list, y_list = [], []

    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))

    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1

    for _ in range(steps + 1):
        x_list.append(round(x))
        y_list.append(round(y))
        x += x_inc
        y += y_inc

    return x_list, y_list

# Function to plot DDA line
def plot_dda_line(x1, y1, x2, y2, color='black'):
    xes, yes = dda_line(x1, y1, x2, y2)
    plt.plot(xes, yes, marker='o', linestyle='-', color=color)

# --- Set axis limits ---
x_min = -10
x_max = 10
y_min = -10
y_max = 10

# Plot X-axis and Y-axis
plt.figure(figsize=(6,6))
plot_dda_line(x_min, 0, x_max, 0, 'red')   # X-axis
plot_dda_line(0, y_min, 0, y_max, 'blue')  # Y-axis

plt.title("X and Y Axes using DDA")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis('equal')
plt.show()
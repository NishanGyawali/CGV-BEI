# Task 2: Plot lines with different slopes using the DDA algorithm

import matplotlib.pyplot as plt

# DDA line function
def dda_line(x1, y1, x2, y2):
    """
    Compute the DDA line coordinates from (x1,y1) to (x2,y2)
    Returns lists of x and y coordinates
    """
    x_list, y_list = [], []

    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))  # number of steps

    x_inc = dx / steps  # increment in x
    y_inc = dy / steps  # increment in y

    x = x1
    y = y1

    for _ in range(steps + 1):
        x_list.append(round(x))
        y_list.append(round(y))
        x += x_inc
        y += y_inc

    return x_list, y_list

# Function to plot line using DDA
def plot_dda_line(x1, y1, x2, y2, color='blue'):
    xes, yes = dda_line(x1, y1, x2, y2)
    plt.plot(xes, yes, marker='o', linestyle='-', color=color)

# Plot multiple lines
plt.figure(figsize=(6,6))

# Slope < 1
plot_dda_line(2, 2, 12, 6, 'red')
# Slope > 1
plot_dda_line(2, 2, 6, 12, 'green')
# Horizontal
plot_dda_line(2, 5, 12, 5, 'blue')
# Vertical
plot_dda_line(5, 2, 5, 12, 'orange')
# Negative slope
plot_dda_line(2, 12, 12, 2, 'purple')

plt.title("DDA Lines with Different Slopes")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis('equal')
plt.show()
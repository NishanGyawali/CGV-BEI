# Task 3: Plot lines with different slopes taking user input

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

# --- User input ---
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

xes, yes = dda_line(x1, y1, x2, y2)

# Plot the line
plt.figure(figsize=(6,6))
plt.plot(xes, yes, marker='o', linestyle='-', color='blue')
plt.title(f"DDA Line from ({x1},{y1}) to ({x2},{y2})")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis('equal')
plt.show()
# Assignment 1: Plot a rectangle using DDA line algorithm with user input for corners

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
def plot_dda_line(x1, y1, x2, y2, color='blue'):
    xes, yes = dda_line(x1, y1, x2, y2)
    plt.plot(xes, yes, marker='o', linestyle='-', color=color)

# --- User input for rectangle corners ---
x1 = int(input("Enter x1 (corner 1): "))
y1 = int(input("Enter y1 (corner 1): "))
x2 = int(input("Enter x2 (opposite corner 2): "))
y2 = int(input("Enter y2 (opposite corner 2): "))

# Compute other two corners
x3, y3 = x1, y2
x4, y4 = x2, y1

# Plot rectangle using DDA lines
plt.figure(figsize=(6,6))
plot_dda_line(x1, y1, x3, y3, 'red')   # Left vertical
plot_dda_line(x3, y3, x2, y2, 'green') # Top horizontal
plot_dda_line(x2, y2, x4, y4, 'blue')  # Right vertical
plot_dda_line(x4, y4, x1, y1, 'purple')# Bottom horizontal

plt.title(f"Rectangle using DDA from ({x1},{y1}) to ({x2},{y2})")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis('equal')
plt.show()
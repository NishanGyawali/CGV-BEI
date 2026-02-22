# Task 1: Implement the DDA line drawing algorithm in Python

import matplotlib.pyplot as plt

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

# Test the function
x_coords, y_coords = dda_line(2, 3, 15, 9)
print("X coordinates:", x_coords)
print("Y coordinates:", y_coords)
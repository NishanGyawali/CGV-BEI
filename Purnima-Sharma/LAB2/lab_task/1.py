#Implement the DDA algorithm as a function that returns x and y coordinate lists.
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

    for _ in range(steps + 1):
        x_points.append(round(x))
        y_points.append(round(y))
        x += x_inc
        y += y_inc

    return x_points, y_points


# Example test
x, y = dda_line(2, 3, 15, 9)
print("X coordinates:", x)
print("Y coordinates:", y)

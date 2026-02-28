# Question 2: Draw circles with different radii and centres

import matplotlib.pyplot as plt

def plot8(pts, xc, yc, x, y):
    pts.extend([
        (xc + x, yc + y), (xc - x, yc + y),
        (xc + x, yc - y), (xc - x, yc - y),
        (xc + y, yc + x), (xc - y, yc + x),
        (xc + y, yc - x), (xc - y, yc - x)
    ])

def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r
    points = []
    plot8(points, xc, yc, x, y)

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * x + 1 - 2 * y
        plot8(points, xc, yc, x, y)

    return points

circles = [(0, 0, 20), (40, 20, 15), (-30, -10, 25)]

all_points = []
for xc, yc, r in circles:
    all_points.extend(midpoint_circle(xc, yc, r))

x_vals = [p[0] for p in all_points]
y_vals = [p[1] for p in all_points]

plt.scatter(x_vals, y_vals, s=5)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()
plt.show()
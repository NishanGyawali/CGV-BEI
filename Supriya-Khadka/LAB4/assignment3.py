# Question 3: Draw concentric circles (Target Pattern)

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

center_x, center_y = 0, 0
radii = [10, 20, 30, 40, 50]

all_points = []
for r in radii:
    all_points.extend(midpoint_circle(center_x, center_y, r))

x_vals = [p[0] for p in all_points]
y_vals = [p[1] for p in all_points]

plt.scatter(x_vals, y_vals, s=5)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()
plt.show()

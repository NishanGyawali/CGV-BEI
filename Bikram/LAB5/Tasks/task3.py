# Task 3: Compare point spacing in Region 1 vs Region 2

import matplotlib.pyplot as plt

def plot_ellipse_points(xc, yc, x, y, xs, ys):
    points = [
        ( x + xc,  y + yc),
        (-x + xc,  y + yc),
        ( x + xc, -y + yc),
        (-x + xc, -y + yc),
    ]
    for px, py in points:
        xs.append(px)
        ys.append(py)

def midpoint_ellipse_regions(rx, ry, xc=0, yc=0):
    rx2 = rx * rx
    ry2 = ry * ry

    x = 0
    y = ry

    xs1, ys1 = [], []  # Region 1 points
    xs2, ys2 = [], []  # Region 2 points

    # Region 1
    p1 = ry2 - (rx2 * ry) + 0.25 * rx2
    plot_ellipse_points(xc, yc, x, y, xs1, ys1)

    while 2 * ry2 * x <= 2 * rx2 * y:
        x += 1
        if p1 < 0:
            p1 += 2 * ry2 * x + ry2
        else:
            y -= 1
            p1 += 2 * ry2 * x - 2 * rx2 * y + ry2
        plot_ellipse_points(xc, yc, x, y, xs1, ys1)

    # Region 2
    p2 = (ry2 * (x + 0.5) ** 2) + (rx2 * (y - 1) ** 2) - (rx2 * ry2)

    while y >= 0:
        if p2 > 0:
            y -= 1
            p2 -= 2 * rx2 * y + rx2
        else:
            x += 1
            y -= 1
            p2 += 2 * ry2 * x - 2 * rx2 * y + rx2
        plot_ellipse_points(xc, yc, x, y, xs2, ys2)

    return xs1, ys1, xs2, ys2

xs1, ys1, xs2, ys2 = midpoint_ellipse_regions(40, 20)

plt.figure(figsize=(7,7))
plt.scatter(xs1, ys1, s=10, label="Region 1")
plt.scatter(xs2, ys2, s=10, label="Region 2")
plt.title("Midpoint Ellipse: Region 1 vs Region 2 Point Spacing")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.show()
import matplotlib.pyplot as plt
import math

def plot_ellipse_points(xc, yc, x, y, xs, ys):
    pts = [
        ( x + xc,  y + yc),
        (-x + xc,  y + yc),
        ( x + xc, -y + yc),
        (-x + xc, -y + yc),
    ]
    for px, py in pts:
        xs.append(px)
        ys.append(py)

def distance_list(xs, ys):
    d = []
    for i in range(1, len(xs)):
        dx = xs[i] - xs[i-1]
        dy = ys[i] - ys[i-1]
        d.append(math.sqrt(dx*dx + dy*dy))
    return d

def midpoint_ellipse_spacing(rx, ry, xc=0, yc=0):
    rx2 = rx * rx
    ry2 = ry * ry

    x = 0
    y = ry

    # Separate lists for regions
    x1, y1 = [], []   # Region 1
    x2, y2 = [], []   # Region 2

    # -------- Region 1 --------
    p1 = ry2 - (rx2 * ry) + 0.25 * rx2
    plot_ellipse_points(xc, yc, x, y, x1, y1)

    while 2 * ry2 * x <= 2 * rx2 * y:
        x += 1
        if p1 < 0:
            p1 += 2 * ry2 * x + ry2
        else:
            y -= 1
            p1 += 2 * ry2 * x - 2 * rx2 * y + ry2
        plot_ellipse_points(xc, yc, x, y, x1, y1)

    # -------- Region 2 --------
    p2 = (ry2 * (x + 0.5) ** 2) + (rx2 * (y - 1) ** 2) - (rx2 * ry2)

    while y >= 0:
        if p2 > 0:
            y -= 1
            p2 -= 2 * rx2 * y + rx2
        else:
            x += 1
            y -= 1
            p2 += 2 * ry2 * x - 2 * rx2 * y + rx2
        plot_ellipse_points(xc, yc, x, y, x2, y2)

    return x1, y1, x2, y2


# -------- Run --------
rx, ry = 10, 6
x1, y1, x2, y2 = midpoint_ellipse_spacing(rx, ry)

# Compute average spacing
d1 = distance_list(x1, y1)
d2 = distance_list(x2, y2)

print("Average point spacing:")
print("Region 1 =", sum(d1)/len(d1))
print("Region 2 =", sum(d2)/len(d2))

# -------- Plot --------
plt.figure(figsize=(6, 6))
plt.scatter(x1, y1, color='blue', s=12, label="Region 1 (Dense)")
plt.scatter(x2, y2, color='red', s=12, label="Region 2 (Sparse)")
plt.gca().set_aspect('equal')
plt.title("Point Spacing Comparison in Midpoint Ellipse")
plt.legend()
plt.grid(True)
plt.show()

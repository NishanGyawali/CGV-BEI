import matplotlib.pyplot as plt

def plot_ellipse_points(xc, yc, x, y, xes, yes):
    pts = [
        ( x + xc,  y + yc),
        (-x + xc,  y + yc),
        ( x + xc, -y + yc),
        (-x + xc, -y + yc),
    ]
    for px, py in pts:
        xes.append(px)
        yes.append(py)

def midpoint_ellipse(rx, ry, xc=0, yc=0):
    rx2 = rx * rx
    ry2 = ry * ry

    x = 0
    y = ry
    xes, yes = [], []

    # Region 1
    p1 = ry2 - (rx2 * ry) + 0.25 * rx2
    plot_ellipse_points(xc, yc, x, y, xes, yes)

    while 2 * ry2 * x <= 2 * rx2 * y:
        x += 1
        if p1 < 0:
            p1 += 2 * ry2 * x + ry2
        else:
            y -= 1
            p1 += 2 * ry2 * x - 2 * rx2 * y + ry2
        plot_ellipse_points(xc, yc, x, y, xes, yes)

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
        plot_ellipse_points(xc, yc, x, y, xes, yes)

    return xes, yes


# -------- Multiple Ellipses --------
ellipses = [
    (10, 6, 0, 0),     # rx, ry, xc, yc
    (6, 3, 15, 5),
    (8, 12, -12, -5),
    (4, 7, -15, 10)
]

plt.figure(figsize=(6, 6))

for rx, ry, xc, yc in ellipses:
    x_pts, y_pts = midpoint_ellipse(rx, ry, xc, yc)
    plt.scatter(x_pts, y_pts, s=10)

plt.gca().set_aspect('equal')
plt.title("Ellipses with Different Radii and Centres\n(Midpoint Ellipse Algorithm)")
plt.grid(True)
plt.show()

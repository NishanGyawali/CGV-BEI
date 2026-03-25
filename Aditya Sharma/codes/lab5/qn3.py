import matplotlib.pyplot as plt

def plot_ellipse_points(xc, yc, x, y, r1x, r1y, r2x, r2y, region):
    pts = [
        ( x+xc,  y+yc),
        (-x+xc,  y+yc),
        ( x+xc, -y+yc),
        (-x+xc, -y+yc)
    ]
    for px, py in pts:
        if region == 1:
            r1x.append(px)
            r1y.append(py)
        else:
            r2x.append(px)
            r2y.append(py)

def midpoint_ellipse(rx, ry, xc=0, yc=0):
    rx2 = rx * rx
    ry2 = ry * ry

    x = 0
    y = ry

    r1x, r1y = [], []
    r2x, r2y = [], []

    # Region 1 decision parameter
    p1 = ry2 - rx2 * ry + 0.25 * rx2

    plot_ellipse_points(xc, yc, x, y, r1x, r1y, r2x, r2y, 1)

    while 2 * ry2 * x <= 2 * rx2 * y:
        x += 1
        if p1 < 0:
            p1 += 2 * ry2 * x + ry2
        else:
            y -= 1
            p1 += 2 * ry2 * x - 2 * rx2 * y + ry2
        plot_ellipse_points(xc, yc, x, y, r1x, r1y, r2x, r2y, 1)

    # Region 2 decision parameter
    p2 = (ry2 * (x + 0.5)**2) + (rx2 * (y - 1)**2) - (rx2 * ry2)

    while y >= 0:
        y -= 1
        if p2 > 0:
            p2 += rx2 - 2 * rx2 * y
        else:
            x += 1
            p2 += 2 * ry2 * x + rx2 - 2 * rx2 * y
        plot_ellipse_points(xc, yc, x, y, r1x, r1y, r2x, r2y, 2)

    return r1x, r1y, r2x, r2y


r1x, r1y, r2x, r2y = midpoint_ellipse(30, 15)

#For The Plot 
plt.figure(figsize=(6,6))
plt.scatter(r1x, r1y, color='red', s=10, label='Region 1')
plt.scatter(r2x, r2y, color='blue', s=10, label='Region 2')
plt.title("Point Spacing in Region 1 vs Region 2")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
import matplotlib.pyplot as plt

plt.style.use('dark_background')

def plot_ellipse_points(xc, yc, x, y, xes, yes, region):
    pts = [
        (x + xc, y + yc),
        (-x + xc, y + yc),
        (x + xc, -y + yc),
        (-x + xc, -y + yc),
    ]
    for px, py in pts:
        xes.append(px)
        yes.append(py)
        if region == 1:
            plt.scatter(px, py, color='cyan', s=1)  # Points from Region 1 in cyan
        else:
            plt.scatter(px, py, color='magenta', s=1)  # Points from Region 2 in magenta

def midpoint_ellipse(rx, ry, xc=0, yc=0):
    rx2 = rx * rx
    ry2 = ry * ry
    x = 0
    y = ry
    xes, yes = [], []

    # Region 1
    p1 = ry2 - (rx2 * ry) + 0.25 * rx2
    plot_ellipse_points(xc, yc, x, y, xes, yes, region=1)

    while 2 * ry2 * x <= 2 * rx2 * y:
        x += 1
        if p1 < 0:
            p1 += 2 * ry2 * x + ry2
        else:
            y -= 1
            p1 += 2 * ry2 * x - 2 * rx2 * y + ry2

        plot_ellipse_points(xc, yc, x, y, xes, yes, region=1)

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

        plot_ellipse_points(xc, yc, x, y, xes, yes, region=2)

    return xes, yes

def plot_midpoint_ellipse(rx, ry, xc=0, yc=0):
    plt.figure(figsize=(8, 8))
    plt.title("Midpoint Ellipse Algorithm - Regions Comparison")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')

    midpoint_ellipse(rx, ry, xc, yc)
    plt.show()

# Example
plot_midpoint_ellipse(300, 150, 0, 0)

import matplotlib.pyplot as plt


def plot_ellipse_points(xc, yc, x, y, xs, ys):
    if x == 0 and y == 0:
        xs.append(xc)
        ys.append(yc)
    elif x == 0:
        xs.extend([xc, xc])
        ys.extend([y + yc, -y + yc])
    elif y == 0:
        xs.extend([x + xc, -x + xc])
        ys.extend([yc, yc])
    else:
        xs.extend([x + xc, -x + xc, x + xc, -x + xc])
        ys.extend([y + yc, y + yc, -y + yc, -y + yc])


def midpoint_ellipse(rx, ry, xc=0, yc=0):
    rx2 = rx * rx
    ry2 = ry * ry

    x = 0
    y = ry

    xs, ys = [], []

    p1 = ry2 - (rx2 * ry) + 0.25 * rx2
    plot_ellipse_points(xc, yc, x, y, xs, ys)

    while 2 * ry2 * x <= 2 * rx2 * y:
        x += 1
        if p1 < 0:
            p1 += 2 * ry2 * x + ry2
        else:
            y -= 1
            p1 += 2 * ry2 * x - 2 * rx2 * y + ry2
        plot_ellipse_points(xc, yc, x, y, xs, ys)

    p2 = (ry2 * (x + 0.5) ** 2) + (rx2 * (y - 1) ** 2) - (rx2 * ry2)

    while y >= 0:
        if p2 > 0:
            y -= 1
            p2 -= 2 * rx2 * y + rx2
        else:
            x += 1
            y -= 1
            p2 += 2 * ry2 * x - 2 * rx2 * y + rx2
        plot_ellipse_points(xc, yc, x, y, xs, ys)

    return xs, ys


def plot_midpoint_ellipse(rx, ry, xc=0, yc=0):
    xs, ys = midpoint_ellipse(rx, ry, xc, yc)

    plt.figure(figsize=(6, 6))
    plt.scatter(xs, ys, marker=".", color="purple")
    plt.title("Midpoint Ellipse Algorithm")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis("equal")
    plt.show()


if __name__ == "__main__":
    plot_midpoint_ellipse(30, 15, 0, 0)
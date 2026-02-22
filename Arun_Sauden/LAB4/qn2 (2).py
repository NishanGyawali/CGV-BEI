import matplotlib.pyplot as plt


def plot_circle_points(xc, yc, x, y, xes, yes):
    pts = [
        ( x + xc,  y + yc),
        (-x + xc,  y + yc),
        ( x + xc, -y + yc),
        (-x + xc, -y + yc),
        ( y + xc,  x + yc),
        (-y + xc,  x + yc),
        ( y + xc, -x + yc),
        (-y + xc, -x + yc),
    ]

    for px, py in pts:
        xes.append(px)
        yes.append(py)


def midpoint_circle(r, xc, yc):
    x = 0
    y = r
    p = 1 - r

    xes = []
    yes = []

    plot_circle_points(xc, yc, x, y, xes, yes)

    while x < y:
        x += 1

        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * x - 2 * y + 1

        plot_circle_points(xc, yc, x, y, xes, yes)

    return xes, yes


if __name__ == "__main__":

    circles = [
        (30, 0, 0),     
        (50, 80, 80),
        (20, -60, 40),
        (40, -80, -60),
        (25, 60, -40)
    ]

    plt.figure()

    for r, xc, yc in circles:
        xes, yes = midpoint_circle(r, xc, yc)
        plt.scatter(xes, yes, s=10, label=f"r={r}, ({xc},{yc})")

    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("Multiple Circles using Midpoint Circle Algorithm")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.legend()
    plt.show()

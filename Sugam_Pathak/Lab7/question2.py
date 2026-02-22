import matplotlib
matplotlib.use("TkAgg")   # or "Qt5Agg"
import matplotlib.pyplot as plt


def liang_barsky(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    dx = x2 - x1
    dy = y2 - y1

    u1, u2 = 0.0, 1.0

    p = [-dx, dx, -dy, dy]
    q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]

    for i in range(4):
        if p[i] == 0:
            if q[i] < 0:
                return None
        else:
            t = q[i] / p[i]
            if p[i] < 0:
                if t > u2:
                    return None
                u1 = max(u1, t)
            else:
                if t < u1:
                    return None
                u2 = min(u2, t)

    nx1 = x1 + u1 * dx
    ny1 = y1 + u1 * dy
    nx2 = x1 + u2 * dx
    ny2 = y1 + u2 * dy

    return nx1, ny1, nx2, ny2


def draw(original, clipped, xmin, ymin, xmax, ymax):
    # Draw clipping window
    plt.plot(
        [xmin, xmax, xmax, xmin, xmin],
        [ymin, ymin, ymax, ymax, ymin],
        'k'
    )

    x1, y1, x2, y2 = original
    plt.plot([x1, x2], [y1, y2], 'r--', label="Original")

    if clipped is not None:
        cx1, cy1, cx2, cy2 = clipped
        plt.plot([cx1, cx2], [cy1, cy2], 'b', linewidth=2, label="Clipped")

    plt.legend()
    plt.title("Liang–Barsky Line Clipping")
    plt.axis("equal")
    plt.show()


xmin, ymin = 10, 10
xmax, ymax = 100, 100

original = (0, 0, 120, 120)
clipped = liang_barsky(*original, xmin, ymin, xmax, ymax)
draw(original, clipped, xmin, ymin, xmax, ymax)

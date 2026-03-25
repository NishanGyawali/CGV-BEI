import math
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


def midpoint_ellipse_split(rx, ry, xc=0, yc=0):
    rx2 = rx * rx
    ry2 = ry * ry

    x = 0
    y = ry

    r1x, r1y = [], []
    r2x, r2y = [], []

    p1 = ry2 - (rx2 * ry) + 0.25 * rx2
    plot_ellipse_points(xc, yc, x, y, r1x, r1y)

    while 2 * ry2 * x <= 2 * rx2 * y:
        x += 1
        if p1 < 0:
            p1 += 2 * ry2 * x + ry2
        else:
            y -= 1
            p1 += 2 * ry2 * x - 2 * rx2 * y + ry2
        plot_ellipse_points(xc, yc, x, y, r1x, r1y)

    p2 = (ry2 * (x + 0.5) ** 2) + (rx2 * (y - 1) ** 2) - (rx2 * ry2)

    while y >= 0:
        if p2 > 0:
            y -= 1
            p2 -= 2 * rx2 * y + rx2
        else:
            x += 1
            y -= 1
            p2 += 2 * ry2 * x - 2 * rx2 * y + rx2
        plot_ellipse_points(xc, yc, x, y, r2x, r2y)

    allx = r1x + r2x
    ally = r1y + r2y
    return (r1x, r1y), (r2x, r2y), (allx, ally)


def step_stats(xs, ys):
    d = []
    for i in range(1, len(xs)):
        dx = xs[i] - xs[i - 1]
        dy = ys[i] - ys[i - 1]
        d.append(math.hypot(dx, dy))
    if not d:
        return 0.0, 0.0, 0.0
    return (sum(d) / len(d)), min(d), max(d)


def compare_region_spacing(rx, ry, xc=0, yc=0, show_plot=True):
    (r1x, r1y), (r2x, r2y), (xs, ys) = midpoint_ellipse_split(rx, ry, xc, yc)

    r1_avg, r1_min, r1_max = step_stats(r1x, r1y)
    r2_avg, r2_min, r2_max = step_stats(r2x, r2y)

    print(f"Ellipse: rx={rx}, ry={ry}, center=({xc},{yc})")
    print(f"Region 1: points={len(r1x)}  avg_step={r1_avg:.3f}  min={r1_min:.3f}  max={r1_max:.3f}")
    print(f"Region 2: points={len(r2x)}  avg_step={r2_avg:.3f}  min={r2_min:.3f}  max={r2_max:.3f}")

    if show_plot:
        plt.figure(figsize=(7, 7))
        plt.scatter(r1x, r1y, marker=".", s=12, label="Region 1")
        plt.scatter(r2x, r2y, marker=".", s=12, label="Region 2")
        plt.title("Midpoint Ellipse: Region 1 vs Region 2")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.axis("equal")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    compare_region_spacing(30, 15, 0, 0, show_plot=True)
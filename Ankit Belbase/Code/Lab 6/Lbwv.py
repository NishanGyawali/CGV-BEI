import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def liang_barsky(x1,y1,x2,y2,xmin,xmax,ymin,ymax):
    dx = x2 - x1
    dy = y2 - y1
    p = [-dx, dx, -dy, dy]
    q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]
    u1 = 0
    u2 = 1
    for i in range(4):
        if p[i] == 0:
            if q[i] < 0:
                return None
        else:
            t = q[i] / p[i]
            if p[i] < 0:
                u1 = max(u1, t)
            else:
                u2 = min(u2, t)
    if u1 > u2:
        return None
    return (x1 + u1 * dx, y1 + u1 * dy), (x1 + u2 * dx, y1 + u2 * dy)


def visualize_liang_barsky(x1, y1, x2, y2, xmin, xmax, ymin, ymax):
    result = liang_barsky(x1, y1, x2, y2, xmin, xmax, ymin, ymax)

    fig, ax = plt.subplots(figsize=(8, 6))

    clipping_window = Rectangle(
        (xmin, ymin),
        xmax - xmin,
        ymax - ymin,
        linewidth=2,
        edgecolor="black",
        facecolor="none",
        label="Clipping Window",
    )
    ax.add_patch(clipping_window)

    ax.plot([x1, x2], [y1, y2], "r--", linewidth=2, label="Original Line")

    if result:
        (cx1, cy1), (cx2, cy2) = result
        ax.plot([cx1, cx2], [cy1, cy2], "g", linewidth=3, label="Clipped Line")
        ax.scatter([cx1, cx2], [cy1, cy2], c="blue", zorder=5, label="Clip Points")
        print("Clipped line segment:", result)
    else:
        print("Line is completely outside the clipping window.")

    margin = 1
    ax.set_xlim(min(x1, x2, xmin) - margin, max(x1, x2, xmax) + margin)
    ax.set_ylim(min(y1, y2, ymin) - margin, max(y1, y2, ymax) + margin)

    ax.set_title("Liang-Barsky Line Clipping Visualization")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend(loc="best")
    plt.show()

x1, y1 = 1, 2   
x2, y2 = 4, 5
xmin, xmax = 2, 3
ymin, ymax = 3, 4

visualize_liang_barsky(x1, y1, x2, y2, xmin, xmax, ymin, ymax)

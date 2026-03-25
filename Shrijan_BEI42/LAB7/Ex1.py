import matplotlib.pyplot as plt

def liang_barsky(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    dx = x2 - x1
    dy = y2 - y1
    u1 = 0
    u2 = 1
    p = [-dx, dx, -dy, dy]
    q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]
    i = 0
    while i < 4:
        if p[i] == 0:
            if q[i] < 0:
                return None
        else:
            t = q[i] / p[i]
            if p[i] < 0:
                if t > u1:
                    u1 = t
            else:
                if t < u2:
                    u2 = t
        i = i + 1
    if u1 > u2:
        return None
    nx1 = x1 + u1 * dx
    ny1 = y1 + u1 * dy
    nx2 = x1 + u2 * dx
    ny2 = y1 + u2 * dy
    return nx1, ny1, nx2, ny2

def draw(original, clipped, xmin, ymin, xmax, ymax):
    plt.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin])
    x1, y1, x2, y2 = original
    plt.plot([x1, x2], [y1, y2], '--')
    if clipped is not None:
        cx1, cy1, cx2, cy2 = clipped
        plt.plot([cx1, cx2], [cy1, cy2])
    plt.title("Liang - Barsky Line Clipping")
    plt.axis("equal")
    plt.grid(True)
    plt.savefig("Assignments/liang_barsky.png")
    plt.show()

if __name__ == "__main__":
    xmin, ymin, xmax, ymax = 10, 10, 100, 100
    x1, y1 = 5, 5
    x2, y2 = 150, 150
    original = (x1, y1, x2, y2)
    clipped = liang_barsky(x1, y1, x2, y2, xmin, ymin, xmax, ymax)
    draw(original, clipped, xmin, ymin, xmax, ymax)

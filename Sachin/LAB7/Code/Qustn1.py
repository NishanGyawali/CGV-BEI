def liang_barsky(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    """Perform Liang-Barsky line clipping.

    Prints the clipped line coordinates if the segment intersects the
    rectangular window, otherwise reports that the line is outside.
    Returns a tuple (nx1, ny1, nx2, ny2) for the clipped line, or
    None if the line is outside.
    """
    dx = x2 - x1
    dy = y2 - y1

    u1 = 0.0
    u2 = 1.0

    p = [-dx, dx, -dy, dy]
    q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]

    for pi, qi in zip(p, q):
        if pi == 0:
            if qi < 0:
                print("Line is outside the window")
                return None
            # Line is parallel and inside for this boundary: continue
        else:
            t = qi / pi
            if pi < 0:
                if t > u1:
                    u1 = t
            else:
                if t < u2:
                    u2 = t

    if u1 > u2:
        print("Line is outside the window")
        return None

    nx1 = x1 + u1 * dx
    ny1 = y1 + u1 * dy
    nx2 = x1 + u2 * dx
    ny2 = y1 + u2 * dy

    print("Clipped Line:", nx1, ny1, nx2, ny2)
    return nx1, ny1, nx2, ny2


if __name__ == "__main__":
    xmin = 10
    ymin = 10
    xmax = 100
    ymax = 100

    # Example: a line from (0, 0) to (120, 120)
    liang_barsky(0, 0, 120, 120, xmin, ymin, xmax, ymax)

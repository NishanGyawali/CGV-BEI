# Liang-Barsky Line Clipping (Simple)

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
                print("Line is outside the window")
                return
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
        print("Line is outside the window")
        return

    nx1 = x1 + u1 * dx
    ny1 = y1 + u1 * dy
    nx2 = x1 + u2 * dx
    ny2 = y1 + u2 * dy
    print("Clipped Line:", nx1, ny1, nx2, ny2)


# Example usage
if __name__ == "__main__":
    xmin = 10
    ymin = 10
    xmax = 100
    ymax = 100

    liang_barsky(0, 0, 120, 120, xmin, ymin, xmax, ymax)

  
def liang_barsky(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    dx = x2 - x1
    dy = y2 - y1

    p = [-dx, dx, -dy, dy]
    q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]

    u1 = 0.0
    u2 = 1.0

    for i in range(4):
        if p[i] == 0:
            # Line is parallel to clipping edge
            if q[i] < 0:
                return False, None, None, None, None
        else:
            t = q[i] / p[i]
            if p[i] < 0:
                u1 = max(u1, t)
            else:
                u2 = min(u2, t)

    if u1 > u2:
        return False, None, None, None, None

    cx1 = x1 + u1 * dx
    cy1 = y1 + u1 * dy
    cx2 = x1 + u2 * dx
    cy2 = y1 + u2 * dy

    return True, cx1, cy1, cx2, cy2

# Clipping window
xmin, ymin = 100, 100
xmax, ymax = 300, 300

# Line endpoints
x1, y1 = 50, 150
x2, y2 = 350, 250

visible, cx1, cy1, cx2, cy2 = liang_barsky(x1, y1, x2, y2, xmin, ymin, xmax, ymax)

if visible:
    print("Line is visible after clipping:")
    print(f"({cx1:.2f}, {cy1:.2f}) -> ({cx2:.2f}, {cy2:.2f})")
else:
    print("Line is completely outside the clipping window.")
import matplotlib.pyplot as plt

# -------- DDA Algorithm --------
def dda_line(x1, y1, x2, y2):
    xes, yes = [], []

    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))
    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1
    for _ in range(steps + 1):
        xes.append(round(x))
        yes.append(round(y))
        x += x_inc
        y += y_inc

    return xes, yes


# -------- Bresenham Algorithm --------
def bresenham_line(x1, y1, x2, y2):
    xes, yes = [], []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x2 >= x1 else -1
    sy = 1 if y2 >= y1 else -1

    x, y = x1, y1

    if dx >= dy:
        p = 2 * dy - dx
        for _ in range(dx + 1):
            xes.append(x)
            yes.append(y)
            x += sx
            if p >= 0:
                y += sy
                p += 2 * dy - 2 * dx
            else:
                p += 2 * dy
    else:
        p = 2 * dx - dy
        for _ in range(dy + 1):
            xes.append(x)
            yes.append(y)
            y += sy
            if p >= 0:
                x += sx
                p += 2 * dx - 2 * dy
            else:
                p += 2 * dx

    return xes, yes


# -------- Octant Lines --------
lines = [
    (0, 0, 8, 3),     # Octant 1
    (0, 0, 3, 8),     # Octant 2
    (0, 0, -3, 8),    # Octant 3
    (0, 0, -8, 3),    # Octant 4
    (0, 0, -8, -3),   # Octant 5
    (0, 0, -3, -8),   # Octant 6
    (0, 0, 3, -8),    # Octant 7
    (0, 0, 8, -3),    # Octant 8
]

# -------- Plot on Single Graph --------
plt.figure(figsize=(8, 8))

for x1, y1, x2, y2 in lines:
    xd, yd = dda_line(x1, y1, x2, y2)
    xb, yb = bresenham_line(x1, y1, x2, y2)

    plt.plot(xd, yd, 'r--o', markersize=4, label='DDA' if (x2, y2) == (8, 3) else "")
    plt.plot(xb, yb, 'g-s', markersize=4, label='Bresenham' if (x2, y2) == (8, 3) else "")

plt.title("DDA vs Bresenham Line Drawing (All Octants)")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()

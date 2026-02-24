import matplotlib.pyplot as plt

# -------- DDA LINE --------
def dda(x1, y1, x2, y2):
    points = []
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))

    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1
    for _ in range(steps + 1):
        points.append((round(x), round(y)))
        x += x_inc
        y += y_inc
    return points


# -------- BRESENHAM LINE (works for all octants) --------
def bresenham(x1, y1, x2, y2):
    points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    err = dx - dy

    x, y = x1, y1
    while True:
        points.append((x, y))
        if x == x2 and y == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy
    return points


# -------- TEST LINES IN DIFFERENT OCTANTS --------
lines = [
    (0, 0, 8, 3),    # Octant 1
    (0, 0, 3, 8),    # Octant 2
    (0, 0, -3, 8),   # Octant 3
    (0, 0, -8, 3),   # Octant 4
    (0, 0, -8, -3),  # Octant 5
    (0, 0, -3, -8),  # Octant 6
    (0, 0, 3, -8),   # Octant 7
    (0, 0, 8, -3)    # Octant 8
]

plt.figure()

for (x1, y1, x2, y2) in lines:
    dda_pts = dda(x1, y1, x2, y2)
    bre_pts = bresenham(x1, y1, x2, y2)

    # Separate x and y
    dx, dy = zip(*dda_pts)
    bx, by = zip(*bre_pts)

    # Plot
    plt.scatter(dx, dy, marker='o')      # DDA points
    plt.scatter(bx, by, marker='x')      # Bresenham points

plt.axhline(0)
plt.axvline(0)
plt.grid(True)
plt.title("Comparison of DDA (o) and Bresenham (x) Lines in All Octants")
plt.show()
import matplotlib.pyplot as plt

def liang_barsky(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    dx = x2 - x1
    dy = y2 - y1

    p = [-dx, dx, -dy, dy]
    q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]

    u1, u2 = 0.0, 1.0

    for pi, qi in zip(p, q):
        if pi == 0:
            if qi < 0:
                return None  # Line is outside
        else:
            t = qi / pi
            if pi < 0:
                u1 = max(u1, t)
            else:
                u2 = min(u2, t)

    if u1 > u2:
        return None

    cx1 = x1 + u1 * dx
    cy1 = y1 + u1 * dy
    cx2 = x1 + u2 * dx
    cy2 = y1 + u2 * dy

    return cx1, cy1, cx2, cy2


# ----------- INPUT VALUES -------------
xmin, ymin = 2, 2
xmax, ymax = 8, 6

x1, y1 = 1, 4
x2, y2 = 9, 5
# -------------------------------------

clipped = liang_barsky(x1, y1, x2, y2, xmin, ymin, xmax, ymax)

# ----------- VISUALIZATION ------------
plt.figure(figsize=(7, 5))

# Original line
plt.plot([x1, x2], [y1, y2], 'r--', label='Original Line')

# Clipping window
plt.plot(
    [xmin, xmax, xmax, xmin, xmin],
    [ymin, ymin, ymax, ymax, ymin],
    'b', linewidth=2, label='Clipping Window'
)

# Clipped line
if clipped:
    cx1, cy1, cx2, cy2 = clipped
    plt.plot([cx1, cx2], [cy1, cy2], 'g', linewidth=3, label='Clipped Line')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Liang–Barsky Line Clipping Algorithm')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
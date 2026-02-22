import matplotlib.pyplot as plt

def liang_barsky(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    dx = x2 - x1
    dy = y2 - y1

    p = [-dx, dx, -dy, dy]
    q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]

    u1, u2 = 0.0, 1.0

    for i in range(4):
        if p[i] == 0:
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


# -------------------------
# Predefined values
# -------------------------
xmin, ymin = 100, 100
xmax, ymax = 300, 300

x1, y1 = 50, 150
x2, y2 = 350, 250

visible, cx1, cy1, cx2, cy2 = liang_barsky(
    x1, y1, x2, y2, xmin, ymin, xmax, ymax
)

# -------------------------
# Visualization
# -------------------------
plt.figure(figsize=(6, 6))

# Clipping window
plt.plot(
    [xmin, xmax, xmax, xmin, xmin],
    [ymin, ymin, ymax, ymax, ymin],
    'k-', linewidth=2, label="Clipping Window"
)

# Original line
plt.plot(
    [x1, x2],
    [y1, y2],
    'r--', linewidth=2, label="Original Line"
)

# Clipped line
if visible:
    plt.plot(
        [cx1, cx2],
        [cy1, cy2],
        'g-', linewidth=3, label="Clipped Line"
    )
    plt.scatter([cx1, cx2], [cy1, cy2], color='blue', zorder=5)
    plt.text(cx1, cy1, f"({cx1:.1f}, {cy1:.1f})", fontsize=9)
    plt.text(cx2, cy2, f"({cx2:.1f}, {cy2:.1f})", fontsize=9)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Liang–Barsky Line Clipping")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.show()

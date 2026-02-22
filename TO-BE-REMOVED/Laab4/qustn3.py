
import matplotlib.pyplot as plt

def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r   # initial decision parameter

    points = []

    while x <= y:
        # 8-way symmetry
        points.extend([
            (xc + x, yc + y),
            (xc - x, yc + y),
            (xc + x, yc - y),
            (xc - x, yc - y),
            (xc + y, yc + x),
            (xc - y, yc + x),
            (xc + y, yc - x),
            (xc - y, yc - x)
        ])

        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1

    return points

# --- User input for concentric circles ---
xc = int(input("Enter x-coordinate of center: "))
yc = int(input("Enter y-coordinate of center: "))
n = int(input("Enter number of concentric circles: "))

radii = []
for i in range(n):
    r = int(input(f"Enter radius for circle {i+1}: "))
    radii.append(r)

# Color palette (will cycle if more circles than colors)
colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'brown']

# Plot concentric circles with different colors
for idx, r in enumerate(radii):
    circle_points = midpoint_circle(xc, yc, r)
    color = colors[idx % len(colors)]  # cycle through colors
    for (x, y) in circle_points:
        plt.plot(x, y, marker='o', color=color, markersize=2)

plt.gca().set_aspect('equal', adjustable='box')
plt.title("Concentric Circles - Midpoint Circle Drawing Algorithm")
plt.grid(True)
plt.show()

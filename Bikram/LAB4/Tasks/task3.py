# Task 3: Draw a target pattern using concentric circles with different radii and the same center using the Midpoint Circle Algorithm.

import matplotlib.pyplot as plt

# Function to plot 8 symmetric points of a circle
def plot_circle_points(xc, yc, x, y, xes, yes):
    pts = [
        ( x + xc,  y + yc),
        (-x + xc,  y + yc),
        ( x + xc, -y + yc),
        (-x + xc, -y + yc),
        ( y + xc,  x + yc),
        (-y + xc,  x + yc),
        ( y + xc, -x + yc),
        (-y + xc, -x + yc)
    ]
    for px, py in pts:
        xes.append(px)
        yes.append(py)

# Midpoint Circle Algorithm
def midpoint_circle(r, xc=0, yc=0):
    x = 0
    y = r
    p = 1 - r
    xes, yes = [], []

    plot_circle_points(xc, yc, x, y, xes, yes)

    while x < y:
        x += 1
        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * (x - y) + 1
        plot_circle_points(xc, yc, x, y, xes, yes)

    return xes, yes

# Plot concentric circles (same center, different radii)
def plot_concentric_circles(radii, xc=0, yc=0):
    plt.figure(figsize=(6, 6))
    colors = ['red', 'green', 'blue', 'purple', 'orange', 'brown']

    for i, r in enumerate(radii):
        xes, yes = midpoint_circle(r, xc, yc)
        plt.scatter(xes, yes, marker='.', color=colors[i % len(colors)], label=f"Radius = {r}")

    plt.title("Concentric Circles (Target Pattern) - Midpoint Circle Algorithm")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')
    plt.legend()
    plt.show()

# Radii for concentric circles
radii = [5, 10, 15, 20, 25, 30]

# Center of all circles
xc, yc = 0, 0

# Draw target pattern
plot_concentric_circles(radii, xc, yc)
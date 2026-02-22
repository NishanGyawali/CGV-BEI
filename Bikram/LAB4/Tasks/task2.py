# Task 2: Circles with Different Radii and Centers

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

# Plot function for multiple circles
def plot_multiple_circles(circles):
    """
    circles: list of tuples [(radius, xc, yc), ...]
    """
    plt.figure(figsize=(6,6))
    colors = ['red', 'green', 'blue', 'purple', 'orange', 'brown', 'cyan']

    for i, (r, xc, yc) in enumerate(circles):
        xes, yes = midpoint_circle(r, xc, yc)
        plt.scatter(xes, yes, marker='.', color=colors[i % len(colors)], label=f"R={r}, Center=({xc},{yc})")

    plt.title("Circles with Different Radii and Centers")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')
    plt.legend()
    plt.show()

# Define circles (radius, xc, yc)
circle_params = [
    (10, 0, 0),
    (20, 15, 10),
    (25, -20, -10),
    (15, 10, -15),
    (30, -10, 20)
]

# Plot all circles
plot_multiple_circles(circle_params)
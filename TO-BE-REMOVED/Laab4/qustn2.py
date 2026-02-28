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

# --- User input for multiple circles ---
n = int(input("Enter number of circles: "))

circles = []
for i in range(n):
    xc = int(input(f"Enter x-coordinate of center for circle {i+1}: "))
    yc = int(input(f"Enter y-coordinate of center for circle {i+1}: "))
    r = int(input(f"Enter radius for circle {i+1}: "))
    circles.append((xc, yc, r))

# Plot all circles
for (xc, yc, r) in circles:
    circle_points = midpoint_circle(xc, yc, r)
    for (x, y) in circle_points:
        plt.plot(x, y, 'bo')  # blue dots

plt.gca().set_aspect('equal', adjustable='box')
plt.title("Multiple Circles - Midpoint Circle Drawing Algorithm")
plt.grid(True)
plt.show()

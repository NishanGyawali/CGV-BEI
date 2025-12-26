import matplotlib.pyplot as plt

def plot_circle_points(xc, yc, x, y, x_points, y_points):
    # Using 8-way symmetry
    x_points.extend([xc + x, xc - x, xc + x, xc - x,
                     xc + y, xc - y, xc + y, xc - y])
    y_points.extend([yc + y, yc + y, yc - y, yc - y,
                     yc + x, yc + x, yc - x, yc - x])

def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r

    x_points = []
    y_points = []

    plot_circle_points(xc, yc, x, y, x_points, y_points)

    while x < y:
        x += 1
        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * (x - y) + 1

        plot_circle_points(xc, yc, x, y, x_points, y_points)

    return x_points, y_points

# Driver code
xc = int(input("Enter x-coordinate of center: "))
yc = int(input("Enter y-coordinate of center: "))
r = int(input("Enter radius: "))

x_points, y_points = midpoint_circle(xc, yc, r)

plt.figure(figsize=(6, 6))
plt.scatter(x_points, y_points, color='blue')
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Midpoint Circle Drawing Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

def midpoint_circle(xc, yc, r):
    x_points = []
    y_points = []

    x = 0
    y = r
    p = 1 - r

    while x <= y:
        x_points.extend([xc + x, xc - x, xc + x, xc - x, xc + y, xc - y, xc + y, xc - y])
        y_points.extend([yc + y, yc + y, yc - y, yc - y, yc + x, yc + x, yc - x, yc - x])

        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1

    return x_points, y_points


center_x, center_y = 0, 0
radii = [5, 10, 15, 20, 25]

plt.figure(figsize=(6,6))

for i, r in enumerate(radii):
    x, y = midpoint_circle(center_x, center_y, r)
    plt.plot(x, y, 'o', label=f'Radius={r}')

plt.title("Concentric Circles - Target Pattern")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()

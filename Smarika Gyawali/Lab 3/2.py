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


circles = [(0, 0, 5), (10, 5, 8), (-5, -5, 3)]
plt.figure(figsize=(8,8))

for xc, yc, r in circles:
    x, y = midpoint_circle(xc, yc, r)
    plt.plot(x, y, 'o', label=f'Center=({xc},{yc}), r={r}')

plt.title("Midpoint Circle Algorithm - Multiple Circles")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()
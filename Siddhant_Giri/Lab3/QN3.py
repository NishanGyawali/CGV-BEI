import matplotlib.pyplot as plt

# -------- MIDPOINT CIRCLE FUNCTION --------
def midpoint_circle(xc, yc, r):
    points = []

    x = 0
    y = r
    p = 1 - r

    while x <= y:
        points.extend([
            (xc + x, yc + y),
            (xc - x, yc + y),
            (xc + x, yc - y),
            (xc - x, yc - y),
            (xc + y, yc + x),
            (xc - y, yc + x),
            (xc + y, yc - x),
            (xc - y, yc - x),
        ])

        x += 1
        if p < 0:
            p += 2*x + 1
        else:
            y -= 1
            p += 2*(x - y) + 1

    return points


# -------- DRAW CONCENTRIC CIRCLES --------
xc, yc = 0, 0          # common center
radii = [3, 6, 9, 12, 15]   # multiple radii (target pattern)

plt.figure()

for r in radii:
    pts = midpoint_circle(xc, yc, r)
    x, y = zip(*pts)
    plt.scatter(x, y)

plt.axhline(0)
plt.axvline(0)
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Concentric Circles using Midpoint Circle Algorithm")
plt.show()
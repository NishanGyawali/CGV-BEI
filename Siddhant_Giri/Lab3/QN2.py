import matplotlib.pyplot as plt

def plot_circle_points(xc, yc, x, y, xes, yes):
    points = [
        ( x + xc,  y + yc),
        (-x + xc,  y + yc),
        ( x + xc, -y + yc),
        (-x + xc, -y + yc),
        ( y + xc,  x + yc),
        (-y + xc,  x + yc),
        ( y + xc, -x + yc),
        (-y + xc, -x + yc)
    ]
    for px, py in points:
        xes.append(px)
        yes.append(py)


def midpoint_circle(r, xc, yc):
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


# -------- Draw circles with different radii and centres --------
circles = [
    (10, 0, 0),
    (15, 12, 8),
    (8, -10, -6)
]

plt.figure(figsize=(6, 6))

for r, xc, yc in circles:
    xes, yes = midpoint_circle(r, xc, yc)
    plt.scatter(xes, yes, marker='.')

plt.title("Midpoint Circle: Different Radii and Centres")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis('equal')
plt.show()
import matplotlib.pyplot as plt
def plot_circle_points(xc, yc, x, y, xs, ys):
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
        xs.append(px)
        ys.append(py)

def midpoint_circle(r, xc, yc):
    x = 0
    y = r
    p = 1 - r
    xs, ys = [], []

    plot_circle_points(xc, yc, x, y, xs, ys)

    while x < y:
        x += 1
        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * (x - y) + 1
        plot_circle_points(xc, yc, x, y, xs, ys)
    return xs, ys
r = int(input("Enter radius: "))
xc = int(input("Enter center x: "))
yc = int(input("Enter center y: "))
xs, ys = midpoint_circle(r, xc, yc)
plt.figure(figsize=(6, 6))
plt.scatter(xs, ys, s=20)
plt.title("Midpoint Circle Algorithm")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis("equal")
plt.grid(True)
plt.show()

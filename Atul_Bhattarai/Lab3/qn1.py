import matplotlib.pyplot as plt  # type: ignore

def plot_circle_points(xc, yc, x, y, xs, ys):
    pts = [
        ( x + xc , y + yc),
        (-x + xc , y + yc),
        ( x + xc , -y + yc),
        (-x + xc , -y + yc),
        ( y + xc , x + yc),
        (-y + xc , x + yc),
        ( y + xc , -x + yc),
        (-y + xc , -x + yc),
    ]
    for px, py in pts:
        xs.append(px)
        ys.append(py)

def midpoint_circle(r, xc=0, yc=0):
    r = int(abs(r))
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

def plot_midpoint_circle(r, xc=0, yc=0):
    xs, ys = midpoint_circle(r, xc, yc)
    plt.figure(figsize=(6, 6))
    plt.scatter(xs, ys, marker='.', color='green')
    plt.title("Midpoint Circle Algorithm")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')
    plt.show()

if __name__ == '__main__':
    plot_midpoint_circle(50)
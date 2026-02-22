import matplotlib.pyplot as plt

def plot_circle_points(xc, yc, x, y, xes, yes):
    pts = [
        (x + xc, y + yc),
        (-x + xc, y + yc),
        (x + xc, -y + yc),
        (-x + xc, -y + yc),
        (y + xc, x + yc),
        (-y + xc, x + yc),
        (y + xc, -x + yc),
        (-y + xc, -x + yc),
    ]
    for px, py in pts:
        xes.append(px)
        yes.append(py)

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

def draw_concentric_circles(center_x=0, center_y=0, num_circles=5, max_radius=500):
    plt.figure(figsize=(8, 8))

    step = max_radius // num_circles
    
    for i in range(num_circles):
        radius = max_radius - i * step
        if radius > 0:
            xes, yes = midpoint_circle(radius, center_x, center_y)
            plt.scatter(xes, yes, color='red', s=10, label=f'Radius={radius}')
    plt.title("Concentric Circles")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.axis('equal')
    plt.show()
draw_concentric_circles(0, 0, 5, 500)


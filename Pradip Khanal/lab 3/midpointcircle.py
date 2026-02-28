import matplotlib.pyplot as plt
def plot_circle_points(xc, yc, x, y, xes, yes):
    points = [
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y),
        (xc + y, yc + x),
        (xc - y, yc + x),
        (xc + y, yc - x),
        (xc - y, yc - x)
    ]
    for px,py in points:
        xes.append(px)
        yes.append(py)

def midpoint_circle_algorithm(xc, yc, r):
    x = 0
    y = r
    d = 1 - r
    xes = []
    yes = []
    plot_circle_points(xc, yc, x, y, xes, yes)

    while x < y:
        if d < 0:
            d = d + 2 * x + 1
        else:
            d = d + 2 * (x - y) + 1
            y -= 1
        x += 1
        plot_circle_points(xc, yc, x, y, xes, yes)

    return xes, yes
    
def plot_midpoint_circle(xc, yc, r):    
    xes, yes = midpoint_circle_algorithm(xc, yc, r)
    plt.figure(figsize=(6,6))
    plt.scatter(xes , yes , marker='.', color='red')
    plt.title(f'Midpoint Circle Algorithm: Center=({xc},{yc}), Radius={r}')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.axis('equal')
    plt.grid(True)
    plt.show()

plot_midpoint_circle(0, 0, 10)
    
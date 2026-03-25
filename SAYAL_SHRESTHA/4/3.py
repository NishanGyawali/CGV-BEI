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
plt.style.use('dark_background')
def midpoint_circle(r, xc=0, yc=0):
    x = 0
    y = r
    p = 1 - r
    xes, yes = [], []
    plot_circle_points(xc, yc, x, y, xes, yes)
    
    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        plot_circle_points(xc, yc, x, y, xes, yes)
    
    return xes, yes

def plot_concentric_circles(radius_list, xc=0, yc=0):
    plt.figure(figsize=(8, 8))
    for radius in radius_list:
        xes, yes = midpoint_circle(radius, xc, yc)
        plt.scatter(xes, yes, marker='.', label=f'Radius: {radius}')

    plt.title("Concentric Circles (Midpoint Algorithm) Roll: 41")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')
    plt.legend()
    plt.show()

# Example usage
concentric_radii = [105, 150, 215, 260, 300]  # Radii for concentric circles
plot_concentric_circles(concentric_radii)

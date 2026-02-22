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

def plot_circles(radius_list, center_list):
    plt.figure(figsize=(8, 8))
    for i, radius in enumerate(radius_list):
        xc, yc = center_list[i]
        xes, yes = midpoint_circle(radius, xc, yc)
        plt.scatter(xes, yes, marker='.', label=f'Circle with radius {radius} at center ({xc}, {yc})')
    
    plt.title("Circles with Different Radii and Centers Roll: 41")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')
    plt.legend()
    plt.show()

# Example usage
radii = [100, 150, 200]  # Different radii
centers = [(0, 0), (100, 100), (200, -100)]  # Different centers
plot_circles(radii, centers)

import matplotlib.pyplot as plt
def plot_ellipse(x_center, y_center, x, y, x_es, y_es):
    pts=[
        (x+x_center, y+y_center),
        (-x+x_center, y+y_center),
        (-x+x_center, -y+y_center),
        (x+x_center, -y+y_center)
    ]
    for px, py in pts:
        x_es.append( px )
        y_es.append( py )
def ellipse_midpoint(rx, ry, x_center=0, y_center=0):
    x_es = []
    y_es = []
    x = 0
    y = ry

    p1 = (ry**2) - (rx**2 * ry) + (0.25 * rx**2)
    plot_ellipse(x_center, y_center, x, y, x_es, y_es)
    while (2 * ry**2 * x) < (2 * rx**2 * y):
        x += 1
        if p1 < 0:
            p1 = p1 + (2 * ry**2 * x) + (ry**2)
        else:
            y -= 1
            p1 = p1 + (2 * ry**2 * x) - (2 * rx**2 * y) + (ry**2)
        plot_ellipse(x_center, y_center, x, y, x_es, y_es)  

    p2 = (ry**2) * ((x + 0.5)**2) + (rx**2) * ((y - 1)**2) - (rx**2 * ry**2)
    while y > 0:
        y -= 1
        if p2 > 0:
            p2 = p2 - (2 * rx**2 * y) + (rx**2)
        else:
            x += 1
            p2 = p2 + (2 * ry**2 * x) - (2 * rx**2 * y) + (rx**2)
        plot_ellipse(x_center, y_center, x, y, x_es, y_es)
    return x_es, y_es

def main():
    rx = int(input("Radius towards x: "))
    ry = int(input("Radius towards y: "))
    x_center = float(input("Center x: "))
    y_center = float(input("Center y: "))
    x_es, y_es = ellipse_midpoint(rx, ry, x_center, y_center)
    plt.figure(figsize=(6,6))
    plt.scatter(x_es, y_es, marker='.', color='black')
    plt.title("Midpoint Ellipse Algorithm")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')
    plt.show()    

if __name__ == "__main__":
    main()

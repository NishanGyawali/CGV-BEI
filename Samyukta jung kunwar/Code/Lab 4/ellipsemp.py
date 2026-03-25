import matplotlib.pyplot as plt
def plot_ellipse_points(xc,yc,x,y,xes, yess):
    pts=[
        (x+xc, y+yc),
        (-x+xc, y+yc),
        (x+xc, -y+yc),
        (-x+xc, -y+yc)
    ]
    for px,py in pts:
        xes.append(px)
        yess.append(py)

def ellipse_midpoint(rx, ry, xc=0, yc=0):
    rx2 =rx * rx
    ry2 =ry * ry
    x = 0
    y = ry
    xes,yes = [],[]

    # Initial decision parameter of region 1
    p1 = ry2 - (rx2 * ry) + (0.25 * rx2)
    plot_ellipse_points(xc,yc,x,y,xes,yes)

    while (2 * ry2 * x) < (2 * rx2 * y):
        x += 1
        if p1 < 0:
            p1 = p1 + (2 * ry2 * x) + ry2
        else:
            y -= 1
            p1 = p1 + (2 * ry2 * x) - (2 * rx2 * y) + ry2
        plot_ellipse_points(xc,yc,x,y,xes,yes)
    # Initial decision parameter of region 2
    p2 = (ry2 * (x + 0.5) ** 2) + (rx2 * (y - 1) ** 2) - (rx2 * ry2)
    while y > 0:
        y -= 1
        if p2 > 0:
            p2 = p2 - (2 * rx2 * y) + rx2
        else:
            x += 1
            p2 = p2 + (2 * ry2 * x) - (2 * rx2 * y) + rx2
        plot_ellipse_points(xc,yc,x,y,xes,yes)
    return xes, yes

def plot_midpoint_ellipse(rx, ry, xc=0, yc=0):
    xes, yes = ellipse_midpoint(rx, ry, xc, yc)
    plt.figure()
    plt.plot(xes, yes, 'b.')
    plt.title(f'Ellipse with rx={rx}, ry={ry}, center=({xc},{yc}) using Midpoint Algorithm')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.axis('equal')
    plt.grid()
    plt.show()

plot_midpoint_ellipse(100, 50, 0, 0)

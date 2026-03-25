import matplotlib.pyplot as plt

def midpoint_ellipse_region_points(xc, yc, rx, ry):
    region1_points = []
    region2_points = []

    x = 0
    y = ry

    rx2 = rx * rx
    ry2 = ry * ry
    two_rx2 = 2 * rx2
    two_ry2 = 2 * ry2

    # Region 1
    p1 = ry2 - (rx2 * ry) + (0.25 * rx2)
    dx = 0
    dy = two_rx2 * y

    while dx < dy:
        region1_points.append((xc + x, yc + y))
        x += 1
        dx += two_ry2
        if p1 < 0:
            p1 += ry2 + dx
        else:
            y -= 1
            dy -= two_rx2
            p1 += ry2 + dx - dy

    # Region 2
    p2 = ry2 * ((x + 0.5)**2) + rx2 * ((y - 1)**2) - rx2 * ry2
    while y >= 0:
        region2_points.append((xc + x, yc + y))
        y -= 1
        dy -= two_rx2
        if p2 > 0:
            p2 += rx2 - dy
        else:
            x += 1
            dx += two_ry2
            p2 += rx2 - dy + dx

    return region1_points, region2_points

xc, yc, rx, ry = 0, 0, 12, 8
r1, r2 = midpoint_ellipse_region_points(xc, yc, rx, ry)

plt.figure(figsize=(6,6))
r1_x, r1_y = zip(*r1)
r2_x, r2_y = zip(*r2)
plt.plot(r1_x, r1_y, 'o', color='blue', label='Region 1 Points')
plt.plot(r2_x, r2_y, 'o', color='red', label='Region 2 Points')
plt.title("Midpoint Ellipse Algorithm - Point Spacing Comparison")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()
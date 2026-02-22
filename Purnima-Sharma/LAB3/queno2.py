#2. Draw lines for different octants and compare visually with DDA lines.

import matplotlib.pyplot as plt
def bresenham(x1, y1, x2, y2):
    x_points = []
    y_points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    x, y = x1, y1
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    if dx > dy:
        p = 2*dy - dx
        for i in range(dx + 1):
            x_points.append(x)
            y_points.append(y)
            x += sx
            if p >= 0:
                y += sy
                p += 2*(dy - dx)
            else:
                p += 2*dy
    else:
        p = 2*dx - dy
        for i in range(dy + 1):
            x_points.append(x)
            y_points.append(y)
            y += sy
            if p >= 0:
                x += sx
                p += 2*(dx - dy)
            else:
                p += 2*dx

    return x_points, y_points
def dda(x1, y1, x2, y2):
    x_points = []
    y_points = []

    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))

    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1
    for i in range(steps + 1):
        x_points.append(round(x))
        y_points.append(round(y))
        x += x_inc
        y += y_inc

    return x_points, y_points


# Test lines from different octants
lines = [
    (2, 2, 8, 5),
    (2, 2, 5, 8),
    (2, 2, -5, 8),
    (2, 2, -8, 5)
]

plt.figure(figsize=(6, 6))

for line in lines:
    x1, y1, x2, y2 = line

    bx, by = bresenham(x1, y1, x2, y2)
    dx, dy = dda(x1, y1, x2, y2)

    plt.plot(bx, by, 'go-')   
    plt.plot(dx, dy, 'rx--') 

plt.title("Bresenham vs DDA Line Drawing")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.grid(True)
plt.axis('equal')
plt.show()

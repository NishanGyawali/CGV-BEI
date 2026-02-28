import matplotlib.pyplot as plt


def dda(x0, y0, x1, y1):
    points = []

    dx = x1 - x0
    dy = y1 - y0

    steps = int(max(abs(dx), abs(dy)))

    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x0, y0

    for _ in range(steps + 1):
        points.append((round(x), round(y)))
        x += x_inc
        y += y_inc
    
    return points

def bresenham(x0, y0, x1, y1):
    points = []

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1

    err = dx - dy

    while True:
        points.append((x0, y0))

        if x0 == x1 and y0 == y1:
            break

        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

    return points


octant_lines = [
    (1, 1, 8, 3),   
    (1, 1, 3, 8),  
    (1, 1, -3, 8),  
    (1, 1, -8, 3),   
    (1, 1, -8, -3),  
    (1, 1, -3, -8), 
    (1, 1, 3, -8),   
    (1, 1, 8, -3),  
]

colors = ["red","green","blue","orange","purple","brown","black","cyan"]


plt.figure(figsize=(10, 10))
plt.title("Bresenham vs DDA Line Drawing (All 8 Octants)")
plt.grid(True)

for i, (x0, y0, x1, y1) in enumerate(octant_lines):
    b_points = bresenham(x0, y0, x1, y1)
    d_points = dda(x0, y0, x1, y1)

    bx, by = zip(*b_points)
    dx, dy = zip(*d_points)

    plt.plot(bx, by, color=colors[i], label=f"Bresenham Octant {i+1}")

    plt.plot(dx, dy, "--", color=colors[i], alpha=0.6, label=f"DDA Octant {i+1}")

plt.legend(loc="upper left", fontsize=8)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.axis("equal")
plt.show()

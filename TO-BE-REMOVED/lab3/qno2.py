import matplotlib.pyplot as plt


def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))
    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1
    xs, ys = [], []

    for _ in range(steps + 1):
        xs.append(round(x))
        ys.append(round(y))
        x += x_inc
        y += y_inc

    return xs, ys


def bresenham(x1, y1, x2, y2):
    xs, ys = [], []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1

    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    if dx > dy:
        p = 2 * dy - dx
        while x != x2:
            xs.append(x)
            ys.append(y)
            x += sx
            if p < 0:
                p += 2 * dy
            else:
                y += sy
                p += 2 * (dy - dx)
    else:
        p = 2 * dx - dy
        while y != y2:
            xs.append(x)
            ys.append(y)
            y += sy
            if p < 0:
                p += 2 * dx
            else:
                x += sx
                p += 2 * (dx - dy)

    xs.append(x2)
    ys.append(y2)
    return xs, ys


lines = [
    (0, 0, 8, 3),    
    (0, 0, 3, 8),    
    (0, 0, -3, 8),   
    (0, 0, -8, 3),   
    (0, 0, -8, -3),  
    (0, 0, -3, -8),  
    (0, 0, 3, -8),  
    (0, 0, 8, -3)    
]

plt.figure()

for x1, y1, x2, y2 in lines:
    x_dda, y_dda = dda(x1, y1, x2, y2)
    x_bre, y_bre = bresenham(x1, y1, x2, y2)

    plt.plot(x_dda, y_dda, linestyle='dashed')   
    plt.plot(x_bre, y_bre, marker='o', linestyle='none')  

plt.title("DDA vs Bresenham for Different Octants")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.gca().set_aspect('equal')
plt.grid(True)
plt.show()

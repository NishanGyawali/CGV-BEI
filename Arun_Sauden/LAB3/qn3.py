import matplotlib.pyplot as plt
def dda(x1, y1, x2, y2):
    additions = 0
    multiplications = 0

    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))
    multiplications += 1

    x_inc = dx / steps
    y_inc = dy / steps
    multiplications += 2

    x, y = x1, y1
    x_points, y_points = [], []

    for _ in range(steps):
        x_points.append(round(x))
        y_points.append(round(y))
        x += x_inc
        y += y_inc
        additions += 2

    return x_points, y_points, additions, multiplications

def bresenham(x1, y1, x2, y2):
    additions = 0
    multiplications = 0  
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    additions += 2

    p = 2 * dy - dx
    multiplications += 1
    additions += 1

    x, y = x1, y1
    x_points, y_points = [], []

    for _ in range(dx):
        x_points.append(x)
        y_points.append(y)

        if p >= 0:
            y += 1
            p += 2 * (dy - dx)
            additions += 3
            multiplications += 1
        else:
            p += 2 * dy
            additions += 1
            multiplications += 1

        x += 1
        additions += 1

    return x_points, y_points, additions, multiplications

x1, y1, x2, y2 = 2, 2, 12, 8

dda_x, dda_y, dda_add, dda_mul = dda(x1, y1, x2, y2)
b_x, b_y, b_add, b_mul = bresenham(x1, y1, x2, y2)

print("DDA -> Additions:", dda_add, "Multiplications:", dda_mul)
print("Bresenham -> Additions:", b_add, "Multiplications:", b_mul)
plt.plot(dda_x, dda_y, 'ro-', label="DDA")
plt.plot(b_x, b_y, 'bs-', label="Bresenham")
plt.legend()
plt.grid(True)
plt.title("DDA vs Bresenham Line Drawing")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()


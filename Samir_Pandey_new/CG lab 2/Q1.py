
import matplotlib.pyplot as plt
def bresenham(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1
    p = dx - dy
    X, Y = [], []
    while True:
        X.append(x)
        Y.append(y)
        if x == x2 and y == y2:
            break
        e2 = 2 * p
        if e2 > -dy:
            p -= dy
            x += sx
        if e2 < dx:
            p += dx
            y += sy
    return X,Y
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
x,y = bresenham(x1, y1, x2, y2)
plt.plot(x,y,'o-',color='green')
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()

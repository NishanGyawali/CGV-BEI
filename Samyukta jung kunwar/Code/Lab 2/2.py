import matplotlib.pyplot as plt

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

dx = abs(x2 - x1)
dy = abs(y2 - y1)
dx_s = x2 - x1
dy_s = y2 - y1

# Bresenham's Line Algorithm
sx = 1 if x2 >= x1 else -1
sy = 1 if y2 >= y1 else -1

xcord1, ycord1 = [], []
x, y = x1, y1

if dx >= dy:
    p = 2 * dy - dx
    for _ in range(dx + 1):
        xcord1.append(x)
        ycord1.append(y)
        x += sx
        if p >= 0:
            y += sy
            p += 2 * dy - 2 * dx
        else:
            p += 2 * dy
else:
    p = 2 * dx - dy
    for _ in range(dy + 1):
        xcord1.append(x)
        ycord1.append(y)
        y += sy
        if p >= 0:
            x += sx
            p += 2 * dx - 2 * dy
        else:
            p += 2 * dx

# DDA Line Algorithm
steps = max(abs(dx_s), abs(dy_s))
xcord, ycord = [], []

if steps == 0:
    xcord, ycord = [x1], [y1]
else:
    xinc = dx_s / steps
    yinc = dy_s / steps
    xd, yd = float(x1), float(y1)  # Changed variable names to xd, yd
    for i in range(steps + 1):
        xcord.append(round(xd))
        ycord.append(round(yd))
        xd += xinc
        yd += yinc

# Plot both algorithms
plt.plot(xcord1, ycord1, marker='o', linestyle='-', color='blue', label='Bresenham', markersize=8)
plt.plot(xcord, ycord, marker='s', linestyle='--', color='red', label='DDA', markersize=6)
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()
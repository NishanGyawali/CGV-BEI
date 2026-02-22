#Draw lines for different octants and compare visually with DDA lines.

import matplotlib.pyplot as plt
import numpy as np

# --------------------- Bresenham's Algorithm ---------------------
def bresenham_line(x1, y1, x2, y2):
    xes, yes = [], []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x2 >= x1 else -1
    sy = 1 if y2 >= y1 else -1
    x, y = x1, y1

    if dx >= dy:
        p = 2*dy - dx
        for _ in range(dx + 1):
            xes.append(x)
            yes.append(y)
            x += sx
            if p >= 0:
                y += sy
                p += 2*dy - 2*dx
            else:
                p += 2*dy
    else:
        p = 2*dx - dy
        for _ in range(dy + 1):
            xes.append(x)
            yes.append(y)
            y += sy
            if p >= 0:
                x += sx
                p += 2*dx - 2*dy
            else:
                p += 2*dx

    return xes, yes

# --------------------- DDA Algorithm ---------------------
def dda_line(x1, y1, x2, y2):
    xes, yes = [], []
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    Xinc = dx / steps
    Yinc = dy / steps
    x = x1
    y = y1
    for _ in range(steps + 1):
        xes.append(round(x))
        yes.append(round(y))
        x += Xinc
        y += Yinc
    return xes, yes

# --------------------- Plotting ---------------------
# Lines in all 8 octants
lines = [
    (0, 0, 8, 3),   # Octant 1
    (0, 0, 3, 8),   # Octant 2
    (0, 0, -3, 8),  # Octant 3
    (0, 0, -8, 3),  # Octant 4
    (0, 0, -8, -3), # Octant 5
    (0, 0, -3, -8), # Octant 6
    (0, 0, 3, -8),  # Octant 7
    (0, 0, 8, -3)   # Octant 8
]

plt.figure(figsize=(12, 6))

for i, (x1, y1, x2, y2) in enumerate(lines):
    # Bresenham
    x_b, y_b = bresenham_line(x1, y1, x2, y2)
    plt.plot(x_b, y_b, 'o-', label=f'Bresenham Octant {i+1}')

plt.title("Bresenham Lines in All Octants")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()

# DDA Comparison
plt.figure(figsize=(12, 6))

for i, (x1, y1, x2, y2) in enumerate(lines):
    # DDA
    x_d, y_d = dda_line(x1, y1, x2, y2)
    plt.plot(x_d, y_d, 'x--', label=f'DDA Octant {i+1}')

plt.title("DDA Lines in All Octants")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()

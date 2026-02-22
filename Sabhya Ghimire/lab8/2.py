import numpy as np
import matplotlib.pyplot as plt
def bresenham_line(x0, y0, x1, y1):
    xes, yes = [], []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x1 >= x0 else -1
    sy = 1 if y1 >= y0 else -1
    x, y = x0, y0

    if dx >= dy:
        p = 2 * dy - dx
        for _ in range(dx + 1):
            xes.append(x)
            yes.append(y)
            x += sx
            if p >= 0:
                y += sy
                p += 2 * dy - 2 * dx
            else:
                p += 2 * dy
    else:
        p = 2 * dx - dy
        for _ in range(dy + 1):
            xes.append(x)
            yes.append(y)
            y += sy
            if p >= 0:
                x += sx
                p += 2 * dx - 2 * dy
            else:
                p += 2 * dx
    return np.array(xes), np.array(yes)
def apply_transform(x, y, M):
    pts = np.vstack([x, y, np.ones_like(x)])
    t = M @ pts
    return t[0], t[1]
# -------- MAIN --------
x0, y0, x1, y1 = 2, 2, 15, 10
x, y = bresenham_line(x0, y0, x1, y1)
xm = (x0 + x1) / 2
ym = (y0 + y1) / 2   # midpoint
S = np.array([[2, 0, 0],
              [0, 0.5, 0],
              [0, 0, 1]])
T1 = np.array([[1, 0, -xm],
               [0, 1, -ym],
               [0, 0, 1]])
T2 = np.array([[1, 0, xm],
               [0, 1, ym],
               [0, 0, 1]])
M = T2 @ S @ T1
xs, ys = apply_transform(x, y, M)

plt.plot(x, y, 'b*-', label="Original Line")
plt.plot(xs, ys, 'go--', label="Scaled about Midpoint")
plt.legend()
plt.grid()
plt.axis('equal')
plt.title("Scaling about Midpoint")
plt.show()
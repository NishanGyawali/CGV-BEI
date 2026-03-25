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
        p = 2*dy - dx
        for _ in range(dx+1):
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
        for _ in range(dy+1):
            xes.append(x)
            yes.append(y)
            y += sy
            if p >= 0:
                x += sx
                p += 2*dx - 2*dy
            else:
                p += 2*dx

    return np.array(xes), np.array(yes)

def fixed_point_scaling(x_coords, y_coords, xf, yf, sx, sy):

    T1 = np.array([[1,0,-xf],
                   [0,1,-yf],
                   [0,0,1]])

    S = np.array([[sx,0,0],
                  [0,sy,0],
                  [0,0,1]])


    T2 = np.array([[1,0,xf],
                   [0,1,yf],
                   [0,0,1]])

    composite = T2 @ S @ T1

    points = np.vstack([x_coords, y_coords, np.ones_like(x_coords)])
    transformed = composite @ points

    return transformed[0], transformed[1]


x0, y0, x1, y1 = 2, 3, 10, 8
x, y = bresenham_line(x0, y0, x1, y1)


xs, ys = fixed_point_scaling(x, y, x0, y0, 2, 0.5)

plt.plot(x, y, 'b-*', label="Original")
plt.plot(xs, ys, 'r--o', label="Scaled (Fixed Point)")
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()

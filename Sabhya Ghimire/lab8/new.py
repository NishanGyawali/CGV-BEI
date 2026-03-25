import numpy as np
import matplotlib.pyplot as plt


# ------------------ Bresenham Line Algorithm ------------------
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


# ------------------ 2D Transformation ------------------
def apply_2d_transformation(x_coords, y_coords, M):
    points = np.vstack([
        x_coords,
        y_coords,
        np.ones_like(x_coords)
    ])
    transformed = M @ points
    return transformed[0], transformed[1]


# ------------------ Main Function ------------------
def plot_all_transformations(x0, y0, x1, y1):
    x_orig, y_orig = bresenham_line(x0, y0, x1, y1)

    # ------------------ 1. Scaling about starting point ------------------
    xf, yf = x0, y0
    S = np.array([[2, 0, 0],
                  [0, 0.5, 0],
                  [0, 0, 1]])

    T1 = np.array([[1, 0, -xf],
                   [0, 1, -yf],
                   [0, 0, 1]])

    T2 = np.array([[1, 0, xf],
                   [0, 1, yf],
                   [0, 0, 1]])

    M_start = T2 @ S @ T1
    x_start, y_start = apply_2d_transformation(x_orig, y_orig, M_start)

    # ------------------ 2. Scaling about midpoint ------------------
    xm = (x0 + x1) / 2
    ym = (y0 + y1) / 2

    T1m = np.array([[1, 0, -xm],
                    [0, 1, -ym],
                    [0, 0, 1]])

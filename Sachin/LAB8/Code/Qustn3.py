
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
            xes.append(x); yes.append(y)
            x += sx
            if p >= 0:
                y += sy
                p += 2 * dy - 2 * dx
            else:
                p += 2 * dy
    else:
        p = 2 * dx - dy
        for _ in range(dy + 1):
            xes.append(x); yes.append(y)
            y += sy
            if p >= 0:
                x += sx
                p += 2 * dx - 2 * dy
            else:
                p += 2 * dx

    return np.array(xes), np.array(yes)


def apply_2d_transformation(x_coords, y_coords, M):
    pts = np.vstack([x_coords, y_coords, np.ones_like(x_coords)])
    out = M @ pts
    return out[0], out[1]


def fixed_point_scaling_matrix(sx, sy, xf, yf):
    T_to_origin = np.array([
        [1, 0, -xf],
        [0, 1, -yf],
        [0, 0,  1]
    ], dtype=float)

    S = np.array([
        [sx, 0,  0],
        [0,  sy, 0],
        [0,  0,  1]
    ], dtype=float)

    T_back = np.array([
        [1, 0, xf],
        [0, 1, yf],
        [0, 0,  1]
    ], dtype=float)

    return T_back @ S @ T_to_origin


def plot_scaling_comparison(x0, y0, x1, y1, sx=2.0, sy=0.5):
    # Original line points
    x_orig, y_orig = bresenham_line(x0, y0, x1, y1)

    # Fixed point 1: starting point
    xf1, yf1 = x0, y0
    M_start = fixed_point_scaling_matrix(sx, sy, xf1, yf1)
    x_start_scaled, y_start_scaled = apply_2d_transformation(x_orig, y_orig, M_start)

    # Fixed point 2: midpoint
    xf2 = (x0 + x1) / 2.0
    yf2 = (y0 + y1) / 2.0
    M_mid = fixed_point_scaling_matrix(sx, sy, xf2, yf2)
    x_mid_scaled, y_mid_scaled = apply_2d_transformation(x_orig, y_orig, M_mid)

    plt.figure(figsize=(9, 6))

    plt.plot(x_orig, y_orig, marker='*', linestyle='-', label='Original line')

    plt.plot(x_start_scaled, y_start_scaled, marker='o', linestyle='--',
             label='Scaled about start point')

    plt.plot(x_mid_scaled, y_mid_scaled, marker='s', linestyle=':',
             label='Scaled about midpoint')

    plt.scatter([xf1], [yf1], marker='x', s=120, label='Start fixed point')
    plt.scatter([xf2], [yf2], marker='D', s=80, label='Midpoint fixed point')

    plt.title("Fixed-Point Scaling: Start Point vs Midpoint")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')
    plt.legend()
    plt.show()


# Example
plot_scaling_comparison(2, 3, 10, 8, sx=2.0, sy=0.5)

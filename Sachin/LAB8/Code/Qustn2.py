
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
    """Scale about fixed point (xf, yf) using homogeneous coordinates."""
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


def plot_fixed_point_scaled_line(x0, y0, x1, y1, sx=2.0, sy=0.5):
    # Original line points
    x_orig, y_orig = bresenham_line(x0, y0, x1, y1)

    # Fixed point = starting point
    xf, yf = x0, y0

    # Fixed-point scaling transform
    M = fixed_point_scaling_matrix(sx, sy, xf, yf)

    # Transformed points
    x_scaled, y_scaled = apply_2d_transformation(x_orig, y_orig, M)

    # Verify fixed point unchanged (for your understanding)
    # print("Start:", (x0, y0), "Scaled start:", (x_scaled[0], y_scaled[0]))

    plt.figure(figsize=(8, 6))
    plt.plot(x_orig, y_orig, marker='*', linestyle='-', label='Original line')
    plt.plot(x_scaled, y_scaled, marker='o', linestyle='--',
             label=f'Scaled about start (sx={sx}, sy={sy})')
    plt.scatter([xf], [yf], marker='x', s=100, label='Fixed point (start)')

    plt.title("Fixed-Point Scaling of a Line About Its Starting Point")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')
    plt.legend()
    plt.show()


# Example
plot_fixed_point_scaled_line(2, 3, 10, 8, sx=2.0, sy=0.5)

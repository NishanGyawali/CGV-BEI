
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


def rotate_about_origin(x0, y0, x1, y1, theta_deg=45):
    # Original line
    x_orig, y_orig = bresenham_line(x0, y0, x1, y1)

    # Rotation angle (degrees → radians)
    theta = np.deg2rad(theta_deg)

    # Pure rotation matrix (about origin)
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0,              0,             1]
    ])

    # Apply rotation
    x_rot, y_rot = apply_2d_transformation(
        x_orig, y_orig, rotation_matrix
    )

    # Plot
    plt.figure(figsize=(8, 6))
    plt.plot(x_orig, y_orig, marker='*', linestyle='-', label='Original line')
    plt.plot(x_rot, y_rot, marker='o', linestyle='--',
             label=f'Rotated line ({theta_deg}°)')

    plt.scatter([0], [0], marker='x', s=120, label='Origin (fixed)')
    plt.title("Pure Rotation About the Origin")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')
    plt.legend()
    plt.show()


# Example
rotate_about_origin(2, 3, 10, 8, theta_deg=45)


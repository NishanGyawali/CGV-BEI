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


def rotate_about_origin(x0, y0, x1, y1, theta):

    x_orig, y_orig = bresenham_line(x0, y0, x1, y1)

    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0,              0,             1]
    ])

   
    points = np.vstack([x_orig, y_orig, np.ones_like(x_orig)])

    rotated_points = rotation_matrix @ points

    x_rot = rotated_points[0]
    y_rot = rotated_points[1]
    
    plt.figure(figsize=(8, 6))
    plt.plot(x_orig, y_orig, marker='o',
             linestyle='-', label='Original Line')
    plt.plot(x_rot, y_rot, marker='x',
             linestyle='--', label='Rotated Line')

    plt.title("Pure Rotation About Origin")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()


theta = np.pi / 4
rotate_about_origin(2, 3, 10, 8, theta)
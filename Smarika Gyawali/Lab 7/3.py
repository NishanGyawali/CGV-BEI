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

def apply_2d_transformation(x_coords, y_coords, transformation_matrix):
    points = np.vstack([x_coords, y_coords, np.ones_like(x_coords)])
    transformed_points = transformation_matrix @ points
    return transformed_points[0], transformed_points[1]

def rotation_about_origin(x0, y0, x1, y1, angle_degrees):
    x_orig, y_orig = bresenham_line(x0, y0, x1, y1)
    theta = np.radians(angle_degrees)

    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0, 0, 1]
    ])

    x_transformed, y_transformed = apply_2d_transformation(x_orig, y_orig, rotation_matrix)

    plt.figure(figsize=(8,6))
    plt.plot(x_orig, y_orig, marker='*', color='blue', linestyle='-', label='Original Line')
    plt.plot(x_transformed, y_transformed, marker='o', color='red', linestyle='--', label=f'Rotated Line ({angle_degrees}°)')
    plt.title("Pure Rotation about Origin")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

# Hardcoded points and rotation angle
x0, y0 = 20, 30
x1, y1 = 150, 100
angle = 45
rotation_about_origin(x0, y0, x1, y1, angle)
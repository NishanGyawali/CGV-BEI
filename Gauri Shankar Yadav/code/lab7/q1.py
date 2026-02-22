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


def plot_line_with_transformations(x0, y0, x1, y1):
    # Original line
    x_orig, y_orig = bresenham_line(x0, y0, x1, y1)

    # Fixed point (starting point)
    xf, yf = x0, y0

    # Scaling matrix
    scaling_matrix = np.array([
        [2, 0, 0],
        [0, 2, 0],
        [0, 0, 1]
    ])

    # Translate fixed point to origin
    T_to_origin = np.array([
        [1, 0, -xf],
        [0, 1, -yf],
        [0, 0, 1]
    ])

    # Translate back
    T_back = np.array([
        [1, 0, xf],
        [0, 1, yf],
        [0, 0, 1]
    ])

    # Combined transformation
    transformation_matrix = T_back @ scaling_matrix @ T_to_origin

    # Apply transformation
    x_trans, y_trans = apply_2d_transformation(
        x_orig, y_orig, transformation_matrix
    )

    # Plot
    plt.figure()
    plt.plot(x_orig, y_orig, 'bo-', label="Original Line")
    plt.plot(x_trans, y_trans, 'ro-', label="Scaled about Start Point")
    plt.legend()
    plt.grid(True)
    plt.axis("equal")
    plt.title("Fixed-Point Scaling About Starting Point")
    plt.show()


# Run the program
plot_line_with_transformations(2, 3, 10, 7)





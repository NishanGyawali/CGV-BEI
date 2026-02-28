import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def make_house_base():
    pts = np.array([
        [0, 0, 0, 1],
        [2, 0, 0, 1],
        [2, 2, 0, 1],
        [0, 2, 0, 1],
        [0, 0, 1, 1],
        [2, 0, 1, 1],
        [2, 2, 1, 1],
        [0, 2, 1, 1]
    ]).T
    return pts

def make_pyramid_roof():
    pts = np.array([
        [0, 0, 1, 1],
        [2, 0, 1, 1],
        [2, 2, 1, 1],
        [0, 2, 1, 1],
        [1, 1, 2, 1]
    ]).T
    return pts

def plot_cube(ax, pts, style='b-', alpha=1.0):
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]
    xs, ys, zs = pts[0], pts[1], pts[2]
    for i, j in edges:
        ax.plot(
            [xs[i], xs[j]],
            [ys[i], ys[j]],
            [zs[i], zs[j]],
            style,
            alpha=alpha
        )

def plot_pyramid(ax, pts, style='r-', alpha=1.0):
    base_edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
    peak_edges = [(0, 4), (1, 4), (2, 4), (3, 4)]
    
    xs, ys, zs = pts[0], pts[1], pts[2]
    
    for i, j in base_edges:
        ax.plot(
            [xs[i], xs[j]],
            [ys[i], ys[j]],
            [zs[i], zs[j]],
            style,
            alpha=alpha
        )
    
    for i, j in peak_edges:
        ax.plot(
            [xs[i], xs[j]],
            [ys[i], ys[j]],
            [zs[i], zs[j]],
            style,
            alpha=alpha
        )

def transform_points(pts, M):
    return M @ pts

def create_scaling_matrix(sx, sy, sz):
    return np.array([
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1]
    ])

def create_rotation_matrix_z(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta), 0, 0],
        [np.sin(theta), np.cos(theta), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

def create_rotation_matrix_x(theta):
    return np.array([
        [1, 0, 0, 0],
        [0, np.cos(theta), -np.sin(theta), 0],
        [0, np.sin(theta), np.cos(theta), 0],
        [0, 0, 0, 1]
    ])

def create_rotation_matrix_y(theta):
    return np.array([
        [np.cos(theta), 0, np.sin(theta), 0],
        [0, 1, 0, 0],
        [-np.sin(theta), 0, np.cos(theta), 0],
        [0, 0, 0, 1]
    ])

def create_translation_matrix(tx, ty, tz):
    return np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])

def create_house_model():
    base_original = make_house_base()
    roof_original = make_pyramid_roof()
    
    S1 = create_scaling_matrix(1.2, 1.2, 1.2)
    T1 = create_translation_matrix(3, 0, 0)
    M1 = T1 @ S1
    
    R2 = create_rotation_matrix_z(np.pi / 4)
    T2 = create_translation_matrix(0, 3, 0)
    M2 = T2 @ R2
    
    R3 = create_rotation_matrix_y(np.pi / 6)
    S3 = create_scaling_matrix(0.8, 0.8, 0.8)
    T3 = create_translation_matrix(3, 3, 0)
    M3 = T3 @ R3 @ S3
    
    base_t1 = transform_points(base_original, M1)
    roof_t1 = transform_points(roof_original, M1)
    
    base_t2 = transform_points(base_original, M2)
    roof_t2 = transform_points(roof_original, M2)
    
    base_t3 = transform_points(base_original, M3)
    roof_t3 = transform_points(roof_original, M3)
    
    fig = plt.figure(figsize=(14, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    plot_cube(ax, base_original, style='b-', alpha=0.8)
    plot_pyramid(ax, roof_original, style='b-', alpha=0.8)
    
    plot_cube(ax, base_t1, style='r--', alpha=0.6)
    plot_pyramid(ax, roof_t1, style='r--', alpha=0.6)
    
    plot_cube(ax, base_t2, style='g--', alpha=0.6)
    plot_pyramid(ax, roof_t2, style='g--', alpha=0.6)
    
    plot_cube(ax, base_t3, style='m--', alpha=0.6)
    plot_pyramid(ax, roof_t3, style='m--', alpha=0.6)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D House Model with Transformations\n'
                 'Blue: Original | Red: Scaled & Translated | '
                 'Green: Rotated (Z-axis) | Magenta: Rotated (Y-axis) & Scaled')
    
    ax.view_init(elev=25, azim=45)
    
    all_points = np.hstack([
        base_original, roof_original,
        base_t1, roof_t1,
        base_t2, roof_t2,
        base_t3, roof_t3
    ])
    max_range = np.array([
        all_points[0].max() - all_points[0].min(),
        all_points[1].max() - all_points[1].min(),
        all_points[2].max() - all_points[2].min()
    ]).max() / 2.0
    mid_x = (all_points[0].max() + all_points[0].min()) * 0.5
    mid_y = (all_points[1].max() + all_points[1].min()) * 0.5
    mid_z = (all_points[2].max() + all_points[2].min()) * 0.5
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)
    
    plt.tight_layout()
    plt.show()
    
    print("House Model Transformations:")
    print("=" * 50)
    print("Original: Blue house at origin")
    print("Transformation 1 (Red): Scaled by 1.2x and translated to (3, 0, 0)")
    print("Transformation 2 (Green): Rotated 45° about Z-axis and translated to (0, 3, 0)")
    print("Transformation 3 (Magenta): Rotated 30° about Y-axis, scaled by 0.8x, and translated to (3, 3, 0)")

if __name__ == "__main__":
    create_house_model()

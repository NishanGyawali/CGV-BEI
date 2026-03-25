import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def make_unit_cube():
    pts = np.array([
        [-0.5, -0.5, -0.5, 1],
        [0.5, -0.5, -0.5, 1],
        [0.5, 0.5, -0.5, 1],
        [-0.5, 0.5, -0.5, 1],
        [-0.5, -0.5, 0.5, 1],
        [0.5, -0.5, 0.5, 1],
        [0.5, 0.5, 0.5, 1],
        [-0.5, 0.5, 0.5, 1]
    ]).T
    return pts

def plot_cube(ax, pts, style='b-', label=''):
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
            label=label if (i, j) == edges[0] else ''
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

def create_translation_matrix(tx, ty, tz):
    return np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])

def apply_transformations():
    cube_original = make_unit_cube()
    
    sx, sy, sz = 1.5, 1.5, 1.5
    theta = np.pi / 4
    tx, ty, tz = 2, 2, 2
    
    S = create_scaling_matrix(sx, sy, sz)
    R = create_rotation_matrix_z(theta)
    T = create_translation_matrix(tx, ty, tz)
    
    M = T @ R @ S
    
    cube_transformed = transform_points(cube_original, M)
    
    fig = plt.figure(figsize=(16, 12))
    ax = fig.add_subplot(111, projection='3d')
    
    plot_cube(ax, cube_original, style='b-', label='Original Cube')
    
    plot_cube(ax, cube_transformed, style='r--', label='Transformed Cube')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Transformations: Scaling, Rotation, and Translation')
    ax.legend()
    
    all_points = np.hstack((cube_original, cube_transformed))
    min_x, max_x = all_points[0].min(), all_points[0].max()
    min_y, max_y = all_points[1].min(), all_points[1].max()
    min_z, max_z = all_points[2].min(), all_points[2].max()
    x_pad = (max_x - min_x) * 0.6
    y_pad = (max_y - min_y) * 0.6
    z_pad = (max_z - min_z) * 0.6
    ax.set_xlim(min_x - x_pad, max_x + x_pad)
    ax.set_ylim(min_y - y_pad, max_y + y_pad)
    ax.set_zlim(min_z - z_pad, max_z + z_pad)
    
    ax.view_init(elev=20, azim=45)
    
    plt.tight_layout()
    plt.show()
    
    print("Transformation Applied:")
    print(f"  Scaling: ({sx}, {sy}, {sz})")
    print(f"  Rotation: {np.degrees(theta):.1f}° about Z-axis")
    print(f"  Translation: ({tx}, {ty}, {tz})")

if __name__ == "__main__":
    apply_transformations()

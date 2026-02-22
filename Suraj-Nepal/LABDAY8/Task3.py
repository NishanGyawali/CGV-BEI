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

def plot_cube(ax, pts, style='b-'):
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
            style
        )

def view_angles_comparison():
    cube = make_unit_cube()
    
    viewing_angles = [
        {'elev': 20, 'azim': 30, 'title': 'Default View (elev=20°, azim=30°)'},
        {'elev': 90, 'azim': 0, 'title': 'Top View (elev=90°, azim=0°)'},
        {'elev': 0, 'azim': 0, 'title': 'Front View (elev=0°, azim=0°)'},
        {'elev': 0, 'azim': 90, 'title': 'Side View (elev=0°, azim=90°)'},
        {'elev': 45, 'azim': 45, 'title': 'Isometric View (elev=45°, azim=45°)'},
        {'elev': 30, 'azim': 60, 'title': 'Oblique View (elev=30°, azim=60°)'}
    ]
    
    fig = plt.figure(figsize=(16, 10))
    
    for idx, view in enumerate(viewing_angles, 1):
        ax = fig.add_subplot(2, 3, idx, projection='3d')
        plot_cube(ax, cube, style='b-')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(view['title'])
        ax.view_init(elev=view['elev'], azim=view['azim'])
        
        max_range = 0.6
        ax.set_xlim(-max_range, max_range)
        ax.set_ylim(-max_range, max_range)
        ax.set_zlim(-max_range, max_range)
    
    plt.tight_layout()
    plt.show()
    
    print("\nViewing Angles Demonstration:")
    print("=" * 50)
    for view in viewing_angles:
        print(f"{view['title']}")
        print(f"  - Elevation: {view['elev']}° (vertical rotation)")
        print(f"  - Azimuth: {view['azim']}° (horizontal rotation)")
        print()

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

def transform_points(pts, M):
    return M @ pts

def interactive_viewing():
    cube = make_unit_cube()
    
    S = create_scaling_matrix(1.2, 1.2, 1.2)
    R = create_rotation_matrix_z(np.pi / 6)
    T = create_translation_matrix(0.5, 0.5, 0.5)
    M = T @ R @ S
    cube_transformed = transform_points(cube, M)
    
    projections = [
        {'elev': 20, 'azim': 30, 'name': 'Perspective'},
        {'elev': 20, 'azim': 30, 'name': 'Orthographic'}
    ]
    
    fig = plt.figure(figsize=(14, 6))
    
    ax1 = fig.add_subplot(1, 2, 1, projection='3d')
    plot_cube(ax1, cube, style='b-')
    plot_cube(ax1, cube_transformed, style='r--')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    ax1.set_title('Perspective Projection (default)')
    ax1.view_init(elev=20, azim=30)
    
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    plot_cube(ax2, cube, style='b-')
    plot_cube(ax2, cube_transformed, style='r--')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')
    ax2.set_title('Orthographic Projection')
    ax2.view_init(elev=20, azim=30)
    ax2.set_proj_type('ortho')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    view_angles_comparison()
    interactive_viewing()

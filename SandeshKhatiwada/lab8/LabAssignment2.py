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

def plot_cube(ax, pts, style='b-', label='', alpha=1.0):
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
            alpha=alpha,
            label=label if (i, j) == edges[0] else ''
        )

def transform_points(pts, M):
    return M @ pts

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

def compare_rotations():
    cube_original = make_unit_cube()
    
    theta = np.pi / 4
    
    Rx = create_rotation_matrix_x(theta)
    Ry = create_rotation_matrix_y(theta)
    Rz = create_rotation_matrix_z(theta)
    
    cube_rot_x = transform_points(cube_original, Rx)
    cube_rot_y = transform_points(cube_original, Ry)
    cube_rot_z = transform_points(cube_original, Rz)
    
    fig = plt.figure(figsize=(18, 6))
    
    ax1 = fig.add_subplot(1, 4, 1, projection='3d')
    plot_cube(ax1, cube_original, style='b-', label='Original', alpha=0.8)
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    ax1.set_title('Original Cube')
    ax1.view_init(elev=20, azim=45)
    ax1.legend()
    
    ax2 = fig.add_subplot(1, 4, 2, projection='3d')
    plot_cube(ax2, cube_original, style='b--', alpha=0.3)
    plot_cube(ax2, cube_rot_x, style='r-', label='Rotated 45°', alpha=0.8)
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')
    ax2.set_title('Rotation about X-axis\n(Red: Rotated, Blue: Original)')
    ax2.view_init(elev=20, azim=45)
    ax2.legend()
    
    ax3 = fig.add_subplot(1, 4, 3, projection='3d')
    plot_cube(ax3, cube_original, style='b--', alpha=0.3)
    plot_cube(ax3, cube_rot_y, style='g-', label='Rotated 45°', alpha=0.8)
    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    ax3.set_zlabel('Z')
    ax3.set_title('Rotation about Y-axis\n(Green: Rotated, Blue: Original)')
    ax3.view_init(elev=20, azim=45)
    ax3.legend()
    
    ax4 = fig.add_subplot(1, 4, 4, projection='3d')
    plot_cube(ax4, cube_original, style='b--', alpha=0.3)
    plot_cube(ax4, cube_rot_z, style='m-', label='Rotated 45°', alpha=0.8)
    ax4.set_xlabel('X')
    ax4.set_ylabel('Y')
    ax4.set_zlabel('Z')
    ax4.set_title('Rotation about Z-axis\n(Magenta: Rotated, Blue: Original)')
    ax4.view_init(elev=20, azim=45)
    ax4.legend()
    
    max_range = 0.6
    for ax in [ax1, ax2, ax3, ax4]:
        ax.set_xlim(-max_range, max_range)
        ax.set_ylim(-max_range, max_range)
        ax.set_zlim(-max_range, max_range)
    
    plt.tight_layout()
    plt.show()
    
    fig2 = plt.figure(figsize=(12, 8))
    ax_combined = fig2.add_subplot(111, projection='3d')
    
    T1 = create_translation_matrix(-2, 0, 0)
    T2 = create_translation_matrix(0, 0, 0)
    T3 = create_translation_matrix(2, 0, 0)
    T4 = create_translation_matrix(0, -2, 0)
    
    cube_orig_t = transform_points(cube_original, T4)
    cube_x_t = transform_points(cube_rot_x, T1)
    cube_y_t = transform_points(cube_rot_y, T2)
    cube_z_t = transform_points(cube_rot_z, T3)
    
    plot_cube(ax_combined, cube_orig_t, style='b-', label='Original', alpha=0.8)
    plot_cube(ax_combined, cube_x_t, style='r-', label='Rotated about X-axis', alpha=0.8)
    plot_cube(ax_combined, cube_y_t, style='g-', label='Rotated about Y-axis', alpha=0.8)
    plot_cube(ax_combined, cube_z_t, style='m-', label='Rotated about Z-axis', alpha=0.8)
    
    ax_combined.set_xlabel('X')
    ax_combined.set_ylabel('Y')
    ax_combined.set_zlabel('Z')
    ax_combined.set_title('Comparison of Rotations about Different Axes\n(All rotated 45°)')
    ax_combined.legend()
    ax_combined.view_init(elev=25, azim=45)
    
    plt.tight_layout()
    plt.show()
    
    print("Rotation Comparison Analysis:")
    print("=" * 60)
    print(f"Rotation angle: {np.degrees(theta):.1f}°")
    print()
    print("Rotation about X-axis:")
    print("  - Rotates around the X-axis (horizontal axis)")
    print("  - Y and Z coordinates change")
    print("  - X coordinates remain unchanged")
    print("  - Effect: Cube appears to tilt forward/backward")
    print()
    print("Rotation about Y-axis:")
    print("  - Rotates around the Y-axis (vertical axis)")
    print("  - X and Z coordinates change")
    print("  - Y coordinates remain unchanged")
    print("  - Effect: Cube appears to spin left/right")
    print()
    print("Rotation about Z-axis:")
    print("  - Rotates around the Z-axis (depth axis)")
    print("  - X and Y coordinates change")
    print("  - Z coordinates remain unchanged")
    print("  - Effect: Cube appears to rotate in the XY plane (like a top-down view)")
    print()
    print("Key Differences:")
    print("  - X-axis rotation: Affects vertical plane (YZ plane)")
    print("  - Y-axis rotation: Affects horizontal plane (XZ plane)")
    print("  - Z-axis rotation: Affects front-facing plane (XY plane)")

if __name__ == "__main__":
    compare_rotations()

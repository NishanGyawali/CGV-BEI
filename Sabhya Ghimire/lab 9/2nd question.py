import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401


def make_unit_cube():
    pts = np.array([
        [0, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 0, 1],
        [0, 1, 0, 1],
        [0, 0, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1],
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


def transform_points(pts, M):
    return M @ pts


def rotation_comparison():
    cube = make_unit_cube()
    theta = np.pi / 6  # 30 degrees

    # Rotation about X-axis
    Rx = np.array([
        [1, 0, 0, 0],
        [0, np.cos(theta), -np.sin(theta), 0],
        [0, np.sin(theta),  np.cos(theta), 0],
        [0, 0, 0, 1]
    ])

    # Rotation about Y-axis
    Ry = np.array([
        [ np.cos(theta), 0, np.sin(theta), 0],
        [ 0, 1, 0, 0],
        [-np.sin(theta), 0, np.cos(theta), 0],
        [ 0, 0, 0, 1]
    ])

    # Rotation about Z-axis
    Rz = np.array([
        [np.cos(theta), -np.sin(theta), 0, 0],
        [np.sin(theta),  np.cos(theta), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    cube_x = transform_points(cube, Rx)
    cube_y = transform_points(cube, Ry)
    cube_z = transform_points(cube, Rz)

    fig = plt.figure(figsize=(12, 8))

    ax1 = fig.add_subplot(131, projection='3d')
    plot_cube(ax1, cube, 'b-')
    plot_cube(ax1, cube_x, 'r--')
    ax1.set_title("Rotation about X-axis")

    ax2 = fig.add_subplot(132, projection='3d')
    plot_cube(ax2, cube, 'b-')
    plot_cube(ax2, cube_y, 'r--')
    ax2.set_title("Rotation about Y-axis")

    ax3 = fig.add_subplot(133, projection='3d')
    plot_cube(ax3, cube, 'b-')
    plot_cube(ax3, cube_z, 'r--')
    ax3.set_title("Rotation about Z-axis")

    for ax in [ax1, ax2, ax3]:
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.view_init(elev=20, azim=30)

    plt.tight_layout()
    plt.show()


rotation_comparison()
# This code creates a unit cube and applies rotations about the X, Y, and Z axes.
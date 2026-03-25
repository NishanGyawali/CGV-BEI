import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401


def make_unit_cube():
    return np.array([
        [0,0,0,1],[1,0,0,1],[1,1,0,1],[0,1,0,1],
        [0,0,1,1],[1,0,1,1],[1,1,1,1],[0,1,1,1]
    ]).T


def plot_cube(ax, pts, style):
    edges = [
        (0,1),(1,2),(2,3),(3,0),
        (4,5),(5,6),(6,7),(7,4),
        (0,4),(1,5),(2,6),(3,7)
    ]
    for i, j in edges:
        ax.plot([pts[0,i], pts[0,j]],
                [pts[1,i], pts[1,j]],
                [pts[2,i], pts[2,j]], style)


def transform_points(pts, M):
    return M @ pts


def cube_transform():
    cube = make_unit_cube()

    S = np.array([
        [2,0,0,0],
        [0,2,0,0],
        [0,0,2,0],
        [0,0,0,1]
    ])

    theta = np.pi / 4
    Rz = np.array([
        [np.cos(theta), -np.sin(theta), 0, 0],
        [np.sin(theta),  np.cos(theta), 0, 0],
        [0,0,1,0],
        [0,0,0,1]
    ])

    T = np.array([
        [1,0,0,2],
        [0,1,0,2],
        [0,0,1,0],
        [0,0,0,1]
    ])

    M = T @ Rz @ S
    cube_t = transform_points(cube, M)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plot_cube(ax, cube, 'b-')
    plot_cube(ax, cube_t, 'r--')
    ax.set_title("Original and Transformed Cube")
    plt.show()


cube_transform()
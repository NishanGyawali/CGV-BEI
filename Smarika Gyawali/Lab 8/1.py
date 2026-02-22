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
        [0, 1, 1, 1]
    ]).T
    return pts


def plot_cube(ax, pts, style='b-'):
    edges = [
        (0,1),(1,2),(2,3),(3,0),
        (4,5),(5,6),(6,7),(7,4),
        (0,4),(1,5),(2,6),(3,7)
    ]
    xs, ys, zs = pts[0], pts[1], pts[2]
    for i, j in edges:
        ax.plot([xs[i], xs[j]],
                [ys[i], ys[j]],
                [zs[i], zs[j]], style)


def draw_cube():
    cube = make_unit_cube()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plot_cube(ax, cube)
    ax.set_title("3D Cube")
    plt.show()


draw_cube()
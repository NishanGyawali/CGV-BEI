import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def cube_vertices(origin=(0, 0, 0), size=1.0):
    x0, y0, z0 = origin
    s = size
    return np.array([
        [x0,     y0,     z0],
        [x0 + s, y0,     z0],
        [x0 + s, y0 + s, z0],
        [x0,     y0 + s, z0],
        [x0,     y0,     z0 + s],
        [x0 + s, y0,     z0 + s],
        [x0 + s, y0 + s, z0 + s],
        [x0,     y0 + s, z0 + s],
    ], dtype=float)


def cube_faces(V):
    return [
        [V[0], V[1], V[2], V[3]],
        [V[4], V[5], V[6], V[7]],
        [V[0], V[1], V[5], V[4]],
        [V[2], V[3], V[7], V[6]],
        [V[1], V[2], V[6], V[5]],
        [V[0], V[3], V[7], V[4]],
    ]


def cube_edges():
    return [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7),
    ]


def plot_cube(ax, V, title):
    faces = cube_faces(V)
    poly = Poly3DCollection(faces, alpha=0.25)
    ax.add_collection3d(poly)

    for i, j in cube_edges():
        ax.plot([V[i, 0], V[j, 0]],
                [V[i, 1], V[j, 1]],
                [V[i, 2], V[j, 2]])

    ax.set_title(title)
    ax.set_box_aspect((1, 1, 1))


if __name__ == "__main__":
    V = cube_vertices(size=2.0)

    fig = plt.figure(figsize=(12, 10))

    views = [
        (20, 30),
        (45, 45),
        (0, 90),
        (90, 0)
    ]

    for i, (elev, azim) in enumerate(views, 1):
        ax = fig.add_subplot(2, 2, i, projection="3d")
        plot_cube(ax, V, f"elev={elev}, azim={azim}")
        ax.view_init(elev=elev, azim=azim)

    plt.tight_layout()
    plt.show()
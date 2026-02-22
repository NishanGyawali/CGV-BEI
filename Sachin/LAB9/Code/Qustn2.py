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


def Rx(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[1, 0, 0],
                     [0, c, -s],
                     [0, s,  c]], dtype=float)


def Ry(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[ c, 0, s],
                     [ 0, 1, 0],
                     [-s, 0, c]], dtype=float)


def Rz(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s, 0],
                     [s,  c, 0],
                     [0,  0, 1]], dtype=float)


def transform_points(V, S=(1, 1, 1), angles_deg=(0, 0, 0), T=(0, 0, 0), pivot=None):
    Sx, Sy, Sz = S
    ax, ay, az = np.deg2rad(angles_deg[0]), np.deg2rad(angles_deg[1]), np.deg2rad(angles_deg[2])
    R = Rz(az) @ Ry(ay) @ Rx(ax)
    M = R @ np.diag([Sx, Sy, Sz])

    Vt = V.copy()

    if pivot is None:
        pivot = Vt.mean(axis=0)
    pivot = np.array(pivot, dtype=float)

    Vt = (Vt - pivot) @ M.T + pivot
    Vt = Vt + np.array(T, dtype=float)

    return Vt


def plot_cube(ax, V, title, alpha=0.25):
    faces = cube_faces(V)
    poly = Poly3DCollection(faces, alpha=alpha)
    ax.add_collection3d(poly)

    for i, j in cube_edges():
        ax.plot([V[i, 0], V[j, 0]], [V[i, 1], V[j, 1]], [V[i, 2], V[j, 2]])

    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_box_aspect((1, 1, 1))


def set_equal_limits(ax, all_points, pad_ratio=0.15):
    mins = all_points.min(axis=0)
    maxs = all_points.max(axis=0)
    center = (mins + maxs) / 2.0
    span = (maxs - mins).max()
    pad = pad_ratio * span

    ax.set_xlim(center[0] - span / 2 - pad, center[0] + span / 2 + pad)
    ax.set_ylim(center[1] - span / 2 - pad, center[1] + span / 2 + pad)
    ax.set_zlim(center[2] - span / 2 - pad, center[2] + span / 2 + pad)


if __name__ == "__main__":
    V0 = cube_vertices(origin=(0, 0, 0), size=2.0)

    scale = (1.5, 0.8, 1.2)
    rotation_deg = (25, 40, 15)   # (x, y, z)
    translation = (3.0, -1.0, 2.0)

    V1 = transform_points(V0, S=scale, angles_deg=rotation_deg, T=translation)

    fig = plt.figure(figsize=(12, 6))
    ax1 = fig.add_subplot(121, projection="3d")
    ax2 = fig.add_subplot(122, projection="3d")

    plot_cube(ax1, V0, "Original Cube")
    plot_cube(ax2, V1, "Transformed Cube")

    all_pts = np.vstack([V0, V1])
    set_equal_limits(ax1, all_pts)
    set_equal_limits(ax2, all_pts)

    plt.tight_layout()
    plt.show()
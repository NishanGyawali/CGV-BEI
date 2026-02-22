import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def draw_cube(origin=(0, 0, 0), size=1.0, show_axes=True):
    x0, y0, z0 = origin
    s = size

    v = [
        (x0,     y0,     z0),
        (x0 + s, y0,     z0),
        (x0 + s, y0 + s, z0),
        (x0,     y0 + s, z0),
        (x0,     y0,     z0 + s),
        (x0 + s, y0,     z0 + s),
        (x0 + s, y0 + s, z0 + s),
        (x0,     y0 + s, z0 + s),
    ]

    faces = [
        [v[0], v[1], v[2], v[3]],
        [v[4], v[5], v[6], v[7]],
        [v[0], v[1], v[5], v[4]],
        [v[2], v[3], v[7], v[6]],
        [v[1], v[2], v[6], v[5]],
        [v[0], v[3], v[7], v[4]],
    ]

    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(111, projection="3d")

    poly = Poly3DCollection(faces, alpha=0.25)
    ax.add_collection3d(poly)

    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7),
    ]
    for i, j in edges:
        ax.plot([v[i][0], v[j][0]], [v[i][1], v[j][1]], [v[i][2], v[j][2]])

    xs = [p[0] for p in v]
    ys = [p[1] for p in v]
    zs = [p[2] for p in v]

    pad = 0.2 * s
    ax.set_xlim(min(xs) - pad, max(xs) + pad)
    ax.set_ylim(min(ys) - pad, max(ys) + pad)
    ax.set_zlim(min(zs) - pad, max(zs) + pad)

    ax.set_box_aspect((1, 1, 1))

    if show_axes:
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
    else:
        ax.set_axis_off()

    plt.title("Cube")
    plt.show()


if __name__ == "__main__":
    draw_cube(origin=(0, 0, 0), size=2.0, show_axes=True)
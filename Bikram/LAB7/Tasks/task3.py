# Task 3: Change viewing angles and plot the cube from different perspectives.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

def make_unit_cube():
    return np.array([
        [0,0,0,1],[1,0,0,1],[1,1,0,1],[0,1,0,1],
        [0,0,1,1],[1,0,1,1],[1,1,1,1],[0,1,1,1]
    ]).T

def plot_cube(ax, pts, style='b-'):
    edges = [(0,1),(1,2),(2,3),(3,0),
             (4,5),(5,6),(6,7),(7,4),
             (0,4),(1,5),(2,6),(3,7)]
    xs, ys, zs = pts[0], pts[1], pts[2]
    for i, j in edges:
        ax.plot([xs[i], xs[j]], [ys[i], ys[j]], [zs[i], zs[j]], style)

cube = make_unit_cube()

fig = plt.figure(figsize=(12,4))

views = [(20,30), (60,30), (20,120)]
titles = ["View 1", "View 2", "View 3"]

for i, (elev, azim) in enumerate(views, 1):
    ax = fig.add_subplot(1, 3, i, projection='3d')
    plot_cube(ax, cube, 'b-')
    ax.view_init(elev=elev, azim=azim)
    ax.set_title(titles[i-1])
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

plt.show()
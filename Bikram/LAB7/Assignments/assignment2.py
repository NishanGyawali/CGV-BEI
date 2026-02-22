# Assignment 2: Rotation about X and Y axes

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

def make_cube():
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

theta = np.pi / 4

Rx = np.array([
    [1,0,0,0],
    [0,np.cos(theta),-np.sin(theta),0],
    [0,np.sin(theta), np.cos(theta),0],
    [0,0,0,1]
])

Ry = np.array([
    [ np.cos(theta),0,np.sin(theta),0],
    [0,1,0,0],
    [-np.sin(theta),0,np.cos(theta),0],
    [0,0,0,1]
])

cube = make_cube()
cube_x = Rx @ cube
cube_y = Ry @ cube

fig = plt.figure(figsize=(10,5))

ax1 = fig.add_subplot(121, projection='3d')
plot_cube(ax1, cube_x, 'r-')
ax1.set_title("Rotation about X-axis")

ax2 = fig.add_subplot(122, projection='3d')
plot_cube(ax2, cube_y, 'g-')
ax2.set_title("Rotation about Y-axis")

plt.show()
# Assignment 1: Simple 3D House Model

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

def plot_edges(ax, pts, edges, style='b-'):
    xs, ys, zs = pts[0], pts[1], pts[2]
    for i, j in edges:
        ax.plot([xs[i], xs[j]], [ys[i], ys[j]], [zs[i], zs[j]], style)

# Cube (house base)
cube = np.array([
    [0,0,0,1],[1,0,0,1],[1,1,0,1],[0,1,0,1],
    [0,0,1,1],[1,0,1,1],[1,1,1,1],[0,1,1,1]
]).T

cube_edges = [
    (0,1),(1,2),(2,3),(3,0),
    (4,5),(5,6),(6,7),(7,4),
    (0,4),(1,5),(2,6),(3,7)
]

# Pyramid roof
roof = np.array([
    [0,0,1,1],
    [1,0,1,1],
    [1,1,1,1],
    [0,1,1,1],
    [0.5,0.5,1.5,1]   # apex
]).T

roof_edges = [(0,1),(1,2),(2,3),(3,0),(0,4),(1,4),(2,4),(3,4)]

fig = plt.figure(figsize=(7,6))
ax = fig.add_subplot(111, projection='3d')

plot_edges(ax, cube, cube_edges, 'b-')
plot_edges(ax, roof, roof_edges, 'r-')

ax.set_title("Simple 3D House Model")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.view_init(elev=20, azim=30)
plt.show()
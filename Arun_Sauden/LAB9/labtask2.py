import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D   

def create_cube():
    cube = np.array([
        [0,0,0,1],
        [1,0,0,1],
        [1,1,0,1],
        [0,1,0,1],
        [0,0,1,1],
        [1,0,1,1],
        [1,1,1,1],
        [0,1,1,1]
    ]).T
    return cube


def draw_cube(ax, pts, style='b-'):
    edges = [
        (0,1),(1,2),(2,3),(3,0),
        (4,5),(5,6),(6,7),(7,4),
        (0,4),(1,5),(2,6),(3,7)
    ]

    x, y, z = pts[0], pts[1], pts[2]

    for i, j in edges:
        ax.plot([x[i], x[j]],
                [y[i], y[j]],
                [z[i], z[j]],
                style)


def transform_points(pts, M):
    return M @ pts


cube = create_cube()


S = np.array([
    [2, 0, 0, 0],
    [0, 1.5, 0, 0],
    [0, 0, 0.5, 0],
    [0, 0, 0, 1]
])

theta = np.pi / 6
Rz = np.array([
    [np.cos(theta), -np.sin(theta), 0, 0],
    [np.sin(theta),  np.cos(theta), 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])


T = np.array([
    [1, 0, 0, 3],
    [0, 1, 0, 2],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
])

M = T @ Rz @ S

cube_transformed = transform_points(cube, M)

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

draw_cube(ax, cube, 'b-')        
draw_cube(ax, cube_transformed, 'r--')   

ax.set_title("Original and Transformed Cubes")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D   

def create_cube():
    vertices = np.array([
        [0,0,0],
        [1,0,0],
        [1,1,0],
        [0,1,0],
        [0,0,1],
        [1,0,1],
        [1,1,1],
        [0,1,1]
    ])
    return vertices
def draw_cube(ax, vertices):
    edges = [
        (0,1),(1,2),(2,3),(3,0),
        (4,5),(5,6),(6,7),(7,4),
        (0,4),(1,5),(2,6),(3,7)
    ]

    for edge in edges:
        points = vertices[list(edge)]
        ax.plot(points[:,0], points[:,1], points[:,2], 'b')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

cube_vertices = create_cube()
draw_cube(ax, cube_vertices)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("3D Cube")

plt.show()

from mpl_toolkits.mplot3d import Axes3D
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

points = [
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1],
    [0.5, 0.5, 2] 
]

edges = [
    [0, 1], [1, 2], [2, 3], [3, 0],
    [4, 5], [5, 6], [6, 7], [7, 4],
    [0, 4], [1, 5], [2, 6], [3, 7],
    [4, 8], [5, 8], [6, 8], [7, 8] 
]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for edge in edges:
    x = [points[edge[0]][0], points[edge[1]][0]]
    y = [points[edge[0]][1], points[edge[1]][1]]
    z = [points[edge[0]][2], points[edge[1]][2]]
    ax.plot3D(x, y, z, color='b')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.savefig("Assignments/pyramid.png")
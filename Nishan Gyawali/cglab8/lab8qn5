import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401


def axis_rotations():
    cube = np.array([
        [0,0,0,1],[1,0,0,1],[1,1,0,1],[0,1,0,1],
        [0,0,1,1],[1,0,1,1],[1,1,1,1],[0,1,1,1]
    ]).T

    theta = np.pi / 4

    Rx = np.array([
        [1,0,0,0],
        [0,np.cos(theta),-np.sin(theta),0],
        [0,np.sin(theta), np.cos(theta),0],
        [0,0,0,1]
    ])

    Ry = np.array([
        [np.cos(theta),0,np.sin(theta),0],
        [0,1,0,0],
        [-np.sin(theta),0,np.cos(theta),0],
        [0,0,0,1]
    ])

    Rz = np.array([
        [np.cos(theta),-np.sin(theta),0,0],
        [np.sin(theta), np.cos(theta),0,0],
        [0,0,1,0],
        [0,0,0,1]
    ])

    cubes = [Rx @ cube, Ry @ cube, Rz @ cube]
    titles = ["X-axis Rotation", "Y-axis Rotation", "Z-axis Rotation"]

    fig = plt.figure(figsize=(12,4))
    for i in range(3):
        ax = fig.add_subplot(1,3,i+1, projection='3d')
        for a,b in [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]:
            ax.plot([cubes[i][0,a], cubes[i][0,b]],
                    [cubes[i][1,a], cubes[i][1,b]],
                    [cubes[i][2,a], cubes[i][2,b]])
        ax.set_title(titles[i])

    plt.show()


axis_rotations()
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401


def cube_view():
    cube = np.array([
        [0,0,0,1],[1,0,0,1],[1,1,0,1],[0,1,0,1],
        [0,0,1,1],[1,0,1,1],[1,1,1,1],[0,1,1,1]
    ]).T

    edges = [
        (0,1),(1,2),(2,3),(3,0),
        (4,5),(5,6),(6,7),(7,4),
        (0,4),(1,5),(2,6),(3,7)
    ]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for i, j in edges:
        ax.plot([cube[0,i], cube[0,j]],
                [cube[1,i], cube[1,j]],
                [cube[2,i], cube[2,j]])

    ax.view_init(elev=45, azim=60)
    ax.set_title("Different Viewing Angle")
    plt.show()


cube_view()
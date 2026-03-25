import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401


def house_model():
    cube = np.array([
        [0,0,0,1],[1,0,0,1],[1,1,0,1],[0,1,0,1],
        [0,0,1,1],[1,0,1,1],[1,1,1,1],[0,1,1,1]
    ]).T

    roof = np.array([
        [0,0,1,1],[1,0,1,1],[1,1,1,1],[0,1,1,1],
        [0.5,0.5,1.5,1]
    ]).T

    cube_edges = [
        (0,1),(1,2),(2,3),(3,0),
        (4,5),(5,6),(6,7),(7,4),
        (0,4),(1,5),(2,6),(3,7)
    ]

    roof_edges = [
        (0,1),(1,2),(2,3),(3,0),
        (0,4),(1,4),(2,4),(3,4)
    ]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for i, j in cube_edges:
        ax.plot([cube[0,i], cube[0,j]],
                [cube[1,i], cube[1,j]],
                [cube[2,i], cube[2,j]], 'b-')

    for i, j in roof_edges:
        ax.plot([roof[0,i], roof[0,j]],
                [roof[1,i], roof[1,j]],
                [roof[2,i], roof[2,j]], 'r-')

    ax.set_title("3D House Model")
    plt.show()


house_model()
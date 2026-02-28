import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

points = np.array([
    [0, 0, 0],  # 0
    [1, 0, 0],  # 1
    [1, 1, 0],  # 2
    [0, 1, 0],  # 3
    [0, 0, 1],  # 4
    [1, 0, 1],  # 5
    [1, 1, 1],  # 6
    [0, 1, 1]   # 7
])

edges = [
    [0, 1], [1, 2], [2, 3], [3, 0],  # bottom face
    [4, 5], [5, 6], [6, 7], [7, 4],  # top face
    [0, 4], [1, 5], [2, 6], [3, 7]   # vertical edges
]

# Ask user for translation distances
dx = float(input("Enter translation distance along X-axis: "))
dy = float(input("Enter translation distance along Y-axis: "))
dz = float(input("Enter translation distance along Z-axis: "))

# Function to plot and save
def plot_cube(translated_points, title, filename):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for edge in edges:
        ax.plot3D(*zip(*translated_points[edge]), color='b')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)
    ax.view_init(elev=30, azim=45)  # Added view initialization
    fig.savefig(filename)
    print(f"Plot saved as {filename}")

# Plot X translation
translated_points_x = points + np.array([dx, 0, 0])
plot_cube(translated_points_x, 'Translated 3D Cube along X-axis', 'Assignments/x_translation.png')

# Plot Y translation
translated_points_y = points + np.array([0, dy, 0])
plot_cube(translated_points_y, 'Translated 3D Cube along Y-axis', 'Assignments/y_translation.png')

# Plot Z translation
translated_points_z = points + np.array([0, 0, dz])
plot_cube(translated_points_z, 'Translated 3D Cube along Z-axis', 'Assignments/z_translation.png')

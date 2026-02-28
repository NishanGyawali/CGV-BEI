import numpy as np
import matplotlib
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

# Ask user for rotation angles in degrees
x_angle = float(input("Enter rotation angle around X-axis in degrees: "))
y_angle = float(input("Enter rotation angle around Y-axis in degrees: "))
z_angle = float(input("Enter rotation angle around Z-axis in degrees: "))

# Convert to radians
x_rad = np.radians(x_angle)
y_rad = np.radians(y_angle)
z_rad = np.radians(z_angle)

# Rotation matrices
Rx = np.array([
    [1, 0, 0],
    [0, np.cos(x_rad), -np.sin(x_rad)],
    [0, np.sin(x_rad), np.cos(x_rad)]
])

Ry = np.array([
    [np.cos(y_rad), 0, np.sin(y_rad)],
    [0, 1, 0],
    [-np.sin(y_rad), 0, np.cos(y_rad)]
])

Rz = np.array([
    [np.cos(z_rad), -np.sin(z_rad), 0],
    [np.sin(z_rad), np.cos(z_rad), 0],
    [0, 0, 1]
])

# Function to plot and save
def plot_cube(rotated_points, title, filename):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for edge in edges:
        ax.plot3D(*zip(*rotated_points[edge]), color='b')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)
    ax.view_init(elev=30, azim=45)  # Added view initialization
    plt.show()

    print(f"Plot saved as {filename}")

# Plot X rotation
rotated_points_x = points @ Rx
plot_cube(rotated_points_x, 'Rotated 3D Cube around X-axis', 'Assignments/x_rotation.png')

# Plot Y rotation
rotated_points_y = points @ Ry
plot_cube(rotated_points_y, 'Rotated 3D Cube around Y-axis', 'Assignments/y_rotation.png')

# Plot Z rotation
rotated_points_z = points @ Rz
plot_cube(rotated_points_z, 'Rotated 3D Cube around Z-axis', 'Assignments/z_rotation.png')
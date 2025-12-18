import matplotlib.pyplot as plt

# Define coordinates for the Batman logo
# These points approximate the shape of the Batman logo, forming a closed polygon.
x = [0.0, 0.2, 0.5, 0.8, 1.0, 1.2, 1.0, 0.8, 0.5, 0.2, 0.0,
     -0.2, -0.5, -0.8, -1.0, -1.2, -1.0, -0.8, -0.5, -0.2, 0.0]
y = [0.0, 0.1, 0.2, 0.3, 0.5, 0.8, 1.0, 1.2, 1.3, 1.2, 1.1,
     1.2, 1.3, 1.2, 1.0, 0.8, 0.5, 0.3, 0.2, 0.1, 0.0]

# Fill the polygon to create the solid logo
plt.fill(x, y, color='black')

# Ensure the aspect ratio is equal so the logo isn't distorted
plt.gca().set_aspect('equal', adjustable='box')

# Remove the axes, ticks, and labels as they are not part of the logo
plt.axis('off')

# Set a title for clarity
plt.title("You like Kids N*gga")

# Display the plot
plt.show()
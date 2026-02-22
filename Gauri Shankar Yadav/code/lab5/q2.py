import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

fig, ax = plt.subplots(figsize=(6, 6))

# Create ellipses (center_x, center_y), width, height
ellipse1 = Ellipse((0, 0), width=60, height=30, edgecolor='red', fill=False)
ellipse2 = Ellipse((20, 10), width=40, height=20, edgecolor='green', fill=False)
ellipse3 = Ellipse((-20, -10), width=30, height=50, edgecolor='black', fill=False)

# Add ellipses to plot
ax.add_patch(ellipse1)
ax.add_patch(ellipse2)
ax.add_patch(ellipse3)

# Set plot properties
ax.set_aspect('equal')
ax.set_xlim(-80, 80)
ax.set_ylim(-80, 80)
ax.grid(True)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Ellipses with Different Radii and Centers")
plt.show()

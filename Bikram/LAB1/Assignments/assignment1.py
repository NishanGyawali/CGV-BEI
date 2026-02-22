# Assignment 1: Plotting a Sine Wave

import numpy as np
import matplotlib.pyplot as plt

# Generate x values from 0 to 2π
x = np.linspace(0, 2 * np.pi, 100)

# Compute sine of x
y = np.sin(x)

# Plot
plt.plot(x, y)
plt.title("Sine Wave (0 to 2π)")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()
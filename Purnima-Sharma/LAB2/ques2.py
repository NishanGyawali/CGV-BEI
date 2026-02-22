#2. Draw lines with different slopes: 𝑚 < 1, 𝑚 > 1, horizontal, vertical and negative slope.

import matplotlib.pyplot as plt

# m < 1 (gentle positive slope)
plt.plot([2, 15], [3, 8], label="m < 1")

# m > 1 (steep positive slope)
plt.plot([4, 6], [1, 12], label="m > 1")

# Horizontal line
plt.plot([1, 14], [7, 7], label="Horizontal")

# Vertical line
plt.plot([9, 9], [2, 13], label="Vertical")

# Negative slope
plt.plot([2, 12], [11, 3], label="Negative slope")

plt.title("Lines with Different Slopes")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
plt.show()
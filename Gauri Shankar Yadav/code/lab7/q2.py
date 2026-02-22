import numpy as np

def scale_line_midpoint(A, B, scale):
    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)

    midpoint = (A + B) / 2
    A_new = midpoint + scale * (A - midpoint)
    B_new = midpoint + scale * (B - midpoint)

    return A_new, B_new


# 🔹 Test values
A = [2, 3]
B = [6, 5]
scale_factor = 2

A_new, B_new = scale_line_midpoint(A, B, scale_factor)

print("Original A:", A)
print("Original B:", B)
print("Scaled A:", A_new)
print("Scaled B:", B_new)

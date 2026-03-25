# Question 3: Pure rotation about the origin using rotation matrix

import math
import matplotlib.pyplot as plt

def rotate_point_origin(x, y, theta_deg):
    theta = math.radians(theta_deg)
    # [x']   [ cosθ  -sinθ ] [x]
    # [y'] = [ sinθ   cosθ ] [y]
    xr = x * math.cos(theta) - y * math.sin(theta)
    yr = x * math.sin(theta) + y * math.cos(theta)
    return xr, yr

def rotate_line_origin(x1, y1, x2, y2, theta_deg):
    x1r, y1r = rotate_point_origin(x1, y1, theta_deg)
    x2r, y2r = rotate_point_origin(x2, y2, theta_deg)
    return x1r, y1r, x2r, y2r

# Line endpoints
x1, y1 = 20, 10
x2, y2 = 70, 40

theta = 45  # degrees

x1r, y1r, x2r, y2r = rotate_line_origin(x1, y1, x2, y2, theta)

plt.axhline(0)
plt.axvline(0)
plt.plot([x1, x2], [y1, y2], marker="o", label="Original")
plt.plot([x1r, x2r], [y1r, y2r], marker="o", label=f"Rotated {theta}° about origin")
plt.gca().set_aspect("equal", adjustable="box")
plt.grid(True)
plt.legend()
plt.show()
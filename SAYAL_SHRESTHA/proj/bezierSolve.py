import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from math import comb

plt.style.use("dark_background")

# ================== USER INPUT ==================
print("\nEnter 3D control points in format: x y z")
print("First and last points are mandatory endpoints.")
print("Type 'done' when finished entering intermediate points.\n")

# Start point
while True:
    try:
        start = input("Start point (x y z): ")
        x0, y0, z0 = map(float, start.split())
        break
    except:
        print("Invalid format. Use: x y z")

# Intermediate points
intermediate_points = []
while True:
    user_input = input("Intermediate point (or 'done'): ")
    if user_input.lower() == "done":
        break
    try:
        x, y, z = map(float, user_input.split())
        intermediate_points.append([x, y, z])
    except:
        print("Invalid format. Use: x y z")

# End point
while True:
    try:
        end = input("End point (x y z): ")
        x1, y1, z1 = map(float, end.split())
        break
    except:
        print("Invalid format. Use: x y z")

control_points = np.array([[x0, y0, z0]] + intermediate_points + [[x1, y1, z1]])
n = len(control_points) - 1
print(f"\nDegree of curve: {n}")

# ================== BERNSTEIN BASIS ==================
def bernstein(k, n, t):
    return comb(n, k) * (t**k) * ((1 - t)**(n - k))

# ================== BÉZIER CURVE ==================
def bezier_curve(points, resolution=200):
    curve = []
    for t in np.linspace(0, 1, resolution):
        P = np.zeros(3)
        for k in range(n + 1):
            P += bernstein(k, n, t) * points[k]
        curve.append(P)
    return np.array(curve)

def bezier_point(points, t):
    P = np.zeros(3)
    for k in range(n + 1):
        P += bernstein(k, n, t) * points[k]
    return P

curve = bezier_curve(control_points)

# ================== PARAMETRIC EQUATIONS ==================
def bezier_parametric_eq(points):
    n = len(points) - 1
    x_eq = " + ".join([f"{comb(n,k)}*{points[k,0]}*t**{k}*(1-t)**{n-k}" for k in range(n+1)])
    y_eq = " + ".join([f"{comb(n,k)}*{points[k,1]}*t**{k}*(1-t)**{n-k}" for k in range(n+1)])
    z_eq = " + ".join([f"{comb(n,k)}*{points[k,2]}*t**{k}*(1-t)**{n-k}" for k in range(n+1)])
    return x_eq, y_eq, z_eq


x_eq, y_eq, z_eq = bezier_parametric_eq(control_points)

print("\nParametric equations (Bernstein form):")
print(f"x(t) = {x_eq}")
print(f"y(t) = {y_eq}")
print(f"z(t) = {z_eq}")

# ================== 3D FIGURE ==================
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
plt.subplots_adjust(bottom=0.15)

def draw(t_val):
    ax.cla()
    # Control polygon
    ax.plot(control_points[:,0],
            control_points[:,1],
            control_points[:,2],
            "--", color="gray")
    # Control points
    ax.scatter(control_points[:,0],
               control_points[:,1],
               control_points[:,2],
               color="magenta", s=60)
    # Bézier curve
    ax.plot(curve[:,0],
            curve[:,1],
            curve[:,2],
            color="cyan", linewidth=2)
    # P(t)
    point = bezier_point(control_points, t_val)
    ax.scatter(point[0], point[1], point[2],
               color="yellow", s=120)

    ax.set_title(f"3D Bézier Curve (Degree {n})", color="white")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.grid(True)
    fig.canvas.draw_idle()

# Slider
ax_slider = plt.axes([0.2, 0.05, 0.6, 0.03])
t_slider = Slider(ax_slider, "t", 0, 1, valinit=0.5)
t_slider.on_changed(draw)

draw(0.5)
plt.show()
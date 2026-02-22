import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def plot_circle_points(xc, yc, x, y, xes, yes):
    pts = [
        ( x + xc,  y + yc),
        (-x + xc,  y + yc),
        ( x + xc, -y + yc),
        (-x + xc, -y + yc),
        ( y + xc,  x + yc),
        (-y + xc,  x + yc),
        ( y + xc, -x + yc),
        (-y + xc, -x + yc)
    ]
    for px, py in pts:
        xes.append(px)
        yes.append(py)

def midpoint_circle(r, xc=0, yc=0):
    x = 0
    y = r
    p = 1 - r
    xes, yes = [], []
    plot_circle_points(xc, yc, x, y, xes, yes)

    while x < y:
        x += 1
        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * (x - y) + 1
        plot_circle_points(xc, yc, x, y, xes, yes) 

    return xes, yes

def plot_midpoint_circle(r, xc=0, yc=0):
    xes, yes = midpoint_circle(r, xc, yc)
    plt.scatter(xes, yes, color='red', s=10)

if __name__ == "__main__":
    import os
    os.makedirs("Assignments", exist_ok=True)
    plt.figure(figsize=(6, 6))
    for i in range(100, 100 + 8 * 50, 50):
        plot_midpoint_circle(i, 0, 0)
    plt.title("Midpoint Circle Algorithm - Concentric Circles")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')
    plt.savefig("Assignments/concentric_circle.png")
    plt.close()


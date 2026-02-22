import matplotlib.pyplot as plt
plt.style.use('dark_background')
def dda_line(x1, y1, x2, y2):
    xes, yes = [], []

    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))

    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1

    for _ in range(steps + 1):
        xes.append(round(x))
        yes.append(round(y))
        x += x_inc
        y += y_inc

    return xes, yes


def plot_dda(x1, y1, x2, y2):
    xes, yes = dda_line(x1, y1, x2, y2)

    plt.figure(figsize=(6, 6))
    plt.plot(xes, yes, marker='o', linestyle='-', color='orange')
    plt.title("DDA Line Drawing Algorithm Roll no: 41")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')
    plt.show()


# Example plot
plot_dda(2, 3, 150, 200)

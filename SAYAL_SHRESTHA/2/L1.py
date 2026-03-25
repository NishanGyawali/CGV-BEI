import matplotlib.pyplot as plt

plt.style.use('dark_background')


def dda_line(x1, y1, x2, y2):
    xes, yes = [], []

    dx = x2 - x1

    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))

    if steps == 0:
        return [x1], [y1]

    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1
    for _ in range(steps + 1):
        xes.append(round(x))
        yes.append(round(y))
        x += x_inc
        y += y_inc

    return xes, yes


def draw_line(x1, y1, x2, y2, color='cyan'):
    xes, yes = dda_line(x1, y1, x2, y2)
    plt.plot(xes, yes, marker='o', linestyle='-', color=color, linewidth=2)


def draw_rectangle(x1, y1, x2, y2):
    # Other two corners
    x3, y3 = x1, y2
    x4, y4 = x2, y1

    # Four sides
    draw_line(x1, y1, x3, y3, 'lime')
    draw_line(x3, y3, x2, y2, 'lime')
    draw_line(x2, y2, x4, y4, 'lime')
    draw_line(x4, y4, x1, y1, 'lime')

    # Mark corners
    plt.scatter([x1, x2, x3, x4],
                [y1, y2, y3, y4],
                color='red', s=70)


# -------- USER INPUT --------
print("Enter two opposite corners of the rectangle:")
x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

plt.figure(figsize=(7, 7))
draw_rectangle(x1, y1, x2, y2)
plt.title("Rectangle using DDA Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True, linestyle='--', alpha=0.4)
plt.axis('equal')
plt.show()

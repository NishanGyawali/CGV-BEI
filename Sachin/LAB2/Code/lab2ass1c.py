
import matplotlib.pyplot as plt


def dda_line(x1, y1, x2, y2):
    
    x_coords = []
    y_coords = []

    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))

    
    if steps == 0:
        return [round(x1)], [round(y1)]

    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1

    for _ in range(steps + 1):
        x_coords.append(round(x))
        y_coords.append(round(y))
        x += x_inc
        y += y_inc

    return x_coords, y_coords


def plot_line(x1, y1, x2, y2, label):
    xs, ys = dda_line(x1, y1, x2, y2)
    plt.plot(xs, ys, marker='o', linestyle='-', label=label)


def get_point(prompt):
    """
    Prompt the user for a point. Accepts either "x y" or "x,y" formats.
    Returns a tuple of floats (x, y).
    """
    while True:
        s = input(prompt).strip()
        
        s = s.replace(",", " ")
        parts = s.split()
        if len(parts) != 2:
            print("Please enter exactly two numbers separated by a space or comma (e.g. 2 3 or 2,3).")
            continue
        try:
            x = float(parts[0])
            y = float(parts[1])
            return x, y
        except ValueError:
            print("Invalid numbers. Please enter numeric values (integers or floats).")


if __name__ == "__main__":
    print("DDA Line Drawing — enter the endpoints for the line to plot.")
    print("You can enter integers or floats, separated by a space or comma.")
    x1, y1 = get_point("Enter x1,y1 (e.g. 2,2): ")
    x2, y2 = get_point("Enter x2,y2 (e.g. 12,6): ")

    plt.figure(figsize=(7, 7))
    plt.title(f"DDA Line from ({x1}, {y1}) to ({x2}, {y2})")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis("equal")

    plot_line(x1, y1, x2, y2, f"Line ({x1},{y1}) → ({x2},{y2})")

    plt.legend()
    plt.show()
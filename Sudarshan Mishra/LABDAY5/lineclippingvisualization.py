import matplotlib.pyplot as plt
INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8
def compute_code(x, y, x_min, y_min, x_max, y_max):
    code = INSIDE
    if x < x_min:
        code += LEFT
    elif x > x_max:
        code += RIGHT
    if y < y_min:
        code += BOTTOM
    elif y > y_max:
        code += TOP
    return code
def cohen_sutherland_clip(x0, y0, x1, y1, x_min, y_min, x_max, y_max):
    code0 = compute_code(x0, y0, x_min, y_min, x_max, y_max)
    code1 = compute_code(x1, y1, x_min, y_min, x_max, y_max)
    while True:
        if (code0 == 0 and code1 == 0):
            return x0, y0, x1, y1
        elif (code0 & code1) != 0:
            return None
        else:
            if code0 != 0:
                code_out = code0
            else:
                code_out = code1
            if code_out & TOP:
                x = x0 + (x1 - x0) * (y_max - y0) / (y1 - y0)
                y = y_max
            elif code_out & BOTTOM:
                x = x0 + (x1 - x0) * (y_min - y0) / (y1 - y0)
                y = y_min
            elif code_out & RIGHT:
                y = y0 + (y1 - y0) * (x_max - x0) / (x1 - x0)
                x = x_max
            elif code_out & LEFT:
                y = y0 + (y1 - y0) * (x_min - x0) / (x1 - x0)
                x = x_min
            if code_out == code0:
                x0, y0 = x, y
                code0 = compute_code(x0, y0, x_min, y_min, x_max, y_max)
            else:
                x1, y1 = x, y
                code1 = compute_code(x1, y1, x_min, y_min, x_max, y_max)

def draw(original, clipped, x_min, y_min, x_max, y_max):
    plt.plot([x_min, x_max, x_max, x_min, x_min],
             [y_min, y_min, y_max, y_max, y_min], 'k-')
    x1, y1, x2, y2 = original
    plt.plot([x1, x2], [y1, y2], '--', label='Original')
    if clipped is not None:
        cx1, cy1, cx2, cy2 = clipped
        plt.plot([cx1, cx2], [cy1, cy2], 'r-', linewidth=2, label='Clipped')
    plt.title("Cohen-Sutherland Line Clipping")
    plt.axis('equal')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    x0 = float(input("Enter x0 : "))
    y0 = float(input("Enter y0 : "))
    x1 = float(input("Enter x1 : "))
    y1 = float(input("Enter y1 : "))
    x_min = float(input("Enter x_min : "))
    y_min = float(input("Enter y_min : "))
    x_max = float(input("Enter x_max : "))
    y_max = float(input("Enter y_max : "))
    original = (x0, y0, x1, y1)
    clipped = cohen_sutherland_clip(x0, y0, x1, y1, x_min, y_min, x_max, y_max)
    if clipped is None:
        print("Line is outside the clipping window")
        print("Clipped Line: ({}, {}) to ({}, {})".format(x0, y0, x1, y1))
    else:
        print("Clipped Line: ({}, {}) to ({}, {})".format(*clipped))
    draw(original, clipped, x_min, y_min, x_max, y_max)
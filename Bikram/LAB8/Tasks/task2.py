# Task 2: Cohen-Sutherland Line Clipping (Enhanced with Visualization)

import matplotlib.pyplot as plt

# Region codes
INSIDE = 0
LEFT   = 1
RIGHT  = 2
BOTTOM = 4
TOP    = 8

def find_code(x, y, xmin, ymin, xmax, ymax):
    code = INSIDE
    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP
    return code

def cohen_sutherland(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    code1 = find_code(x1, y1, xmin, ymin, xmax, ymax)
    code2 = find_code(x2, y2, xmin, ymin, xmax, ymax)

    while True:
        if code1 == 0 and code2 == 0:
            return x1, y1, x2, y2  # Completely inside
        elif (code1 & code2) != 0:
            return None  # Completely outside
        else:
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            # Intersection calculations
            if code_out & TOP:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            # Replace the point outside with intersection
            if code_out == code1:
                x1, y1 = x, y
                code1 = find_code(x1, y1, xmin, ymin, xmax, ymax)
            else:
                x2, y2 = x, y
                code2 = find_code(x2, y2, xmin, ymin, xmax, ymax)

def draw(original, clipped, xmin, ymin, xmax, ymax):
    # Draw clipping window
    plt.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin], 'k-', label='Clipping Window')
    
    # Original line (dashed)
    x1, y1, x2, y2 = original
    plt.plot([x1, x2], [y1, y2], 'b--', label='Original Line')
    
    # Clipped line (solid)
    if clipped is not None:
        cx1, cy1, cx2, cy2 = clipped
        plt.plot([cx1, cx2], [cy1, cy2], 'r-', linewidth=2, label='Clipped Line')

    plt.title("Cohen-Sutherland Line Clipping")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis("equal")
    plt.legend()
    plt.show()

# Example usage
xmin, ymin = 10, 10
xmax, ymax = 100, 100
original = (0, 0, 120, 120)
clipped = cohen_sutherland(*original, xmin, ymin, xmax, ymax)
draw(original, clipped, xmin, ymin, xmax, ymax)
import matplotlib.pyplot as plt

# Define the regions
INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8

def find_code(x, y, xmin, ymin, xmax, ymax):
    code = INSIDE
    if x < xmin:
        code = code + LEFT
    elif x > xmax:
        code = code + RIGHT
    if y < ymin:
        code = code + BOTTOM
    elif y > ymax:
        code = code + TOP
    return code

def cohen_sutherland(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    code1 = find_code(x1, y1, xmin, ymin, xmax, ymax)
    code2 = find_code(x2, y2, xmin, ymin, xmax, ymax)

    while True:
        if code1 == 0 and code2 == 0:  # Both endpoints are inside
            return x1, y1, x2, y2
        elif (code1 & code2) != 0:  # Both endpoints are outside
            return None
        
        # Choose an endpoint to clip
        if code1 != 0:
            code_out = code1
        else:
            code_out = code2

        # Find the intersection point
        if code_out & TOP:  # point is above the clip window
            x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
            y = ymax
        elif code_out & BOTTOM:  # point is below the clip window
            x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
            y = ymin
        elif code_out & RIGHT:  # point is to the right of the clip window
            y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
            x = xmax
        elif code_out & LEFT:  # point is to the left of the clip window
            y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
            x = xmin

        # Replace the outside point with the intersection point
        if code_out == code1:
            x1, y1 = x, y
            code1 = find_code(x1, y1, xmin, ymin, xmax, ymax)
        else:
            x2, y2 = x, y
            code2 = find_code(x2, y2, xmin, ymin, xmax, ymax)

def draw(original, clipped, xmin, ymin, xmax, ymax):
    # Draw the clipping rectangle
    plt.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin], 'b-')
    
    # Draw the original line segment
    x1, y1, x2, y2 = original
    plt.plot([x1, x2], [y1, y2], 'r--', label='Original Line Segment')
    
    # Draw the clipped line segment if it exists
    if clipped is not None:
        cx1, cy1, cx2, cy2 = clipped
        plt.plot([cx1, cx2], [cy1, cy2], 'g-', label='Clipped Line Segment')
    
    plt.title("Cohen-Sutherland Line Clipping Roll no 41")
    plt.axis("equal")
    plt.grid(True)
    plt.legend()
    plt.show()

# Define the clipping window and the original line
xmin, ymin = 10, 10
xmax, ymax = 100, 100
original = (0, 0, 120, 120)

# Perform the clipping
clipped = cohen_sutherland(0, 0, 120, 120, xmin, ymin, xmax, ymax)

# Draw the results
draw(original, clipped, xmin, ymin, xmax, ymax)

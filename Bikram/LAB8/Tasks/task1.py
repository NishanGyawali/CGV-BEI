# Task 1: Cohen-Sutherland Line Clipping (Basic)

INSIDE = 0  # 0000
LEFT   = 1  # 0001
RIGHT  = 2  # 0010
BOTTOM = 4  # 0100
TOP    = 8  # 1000

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
        # If both endpoints are inside
        if code1 == 0 and code2 == 0:
            print(f"Clipped Line: ({x1}, {y1}) to ({x2}, {y2})")
            break
        # If both endpoints share an outside region
        elif (code1 & code2) != 0:
            print("Line is outside the window")
            break
        else:
            # Choose a point outside the window
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            # Find intersection
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

# Example usage
xmin, ymin = 10, 10
xmax, ymax = 100, 100
cohen_sutherland(0, 0, 120, 120, xmin, ymin, xmax, ymax)
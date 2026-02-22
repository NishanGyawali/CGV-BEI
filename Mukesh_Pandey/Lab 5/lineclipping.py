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
            print("Line is inside the clipping window")
            print("Clipped Line: ({}, {}) to ({}, {})".format(x0, y0, x1, y1))
            break
        elif (code0 & code1) != 0:
            print("Line is outside the clipping window")
            print("Clipped Line: ({}, {}) to ({}, {})".format(x0, y0, x1, y1))
            break
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
                x0 = x 
                y0 = y
                code0 = compute_code(x0, y0, x_min, y_min, x_max, y_max)
            else:
                x1 = x
                y1 = y
                code1 = compute_code(x1, y1, x_min, y_min, x_max, y_max)
if __name__ == "__main__":
    x0 = float(input("Enter x0 : "))
    y0 = float(input("Enter y0 : "))
    x1 = float(input("Enter x1 : "))
    y1 = float(input("Enter y1 : "))
    x_min = float(input("Enter x_min : "))
    y_min = float(input("Enter y_min : "))
    x_max = float(input("Enter x_max : "))
    y_max = float(input("Enter y_max : "))
    cohen_sutherland_clip(x0, y0, x1, y1, x_min, y_min, x_max, y_max)
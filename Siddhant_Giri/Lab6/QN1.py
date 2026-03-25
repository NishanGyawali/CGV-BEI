# Cohen–Sutherland Line Clipping Algorithm

INSIDE = 0   # 0000
LEFT   = 1   # 0001
RIGHT  = 2   # 0010
BOTTOM = 4   # 0100
TOP    = 8   # 1000

def find_code(x, y, x_min, y_min, x_max, y_max):
    code = INSIDE
    if x < x_min:
        code |= LEFT
    elif x > x_max:
        code |= RIGHT
    if y < y_min:
        code |= BOTTOM
    elif y > y_max:
        code |= TOP
    return code

# Cohen–Sutherland line clipping function
def cohen_sutherland_clip(x1, y1, x2, y2, x_min, y_min, x_max, y_max):
    code1 = find_code(x1, y1, x_min, y_min, x_max, y_max)
    code2 = find_code(x2, y2, x_min, y_min, x_max, y_max)

    while True:
        if code1 == 0 and code2 == 0:
            print("Clipped Line:", x1, y1, x2, y2)
            break

        elif (code1 & code2) != 0:
            print("Line is completely outside the clipping window")
            break

        else:
            code_out = code1 if code1 != 0 else code2

            if code_out & TOP:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min

            if code_out == code1:
                x1, y1 = x, y
                code1 = find_code(x1, y1, x_min, y_min, x_max, y_max)
            else:
                x2, y2 = x, y
                code2 = find_code(x2, y2, x_min, y_min, x_max, y_max)

# -------- Example Usage --------
x_min, y_min = 100, 100
x_max, y_max = 300, 300

# Line endpoints
x1, y1 = 50, 150
x2, y2 = 350, 250

cohen_sutherland_clip(x1, y1, x2, y2, x_min, y_min, x_max, y_max)
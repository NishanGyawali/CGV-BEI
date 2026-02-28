inside = 0
left = 1
right = 2
bottom = 4
top = 8

def find_code(x, y, x_min, y_min, x_max, y_max):
    code = inside
    if x < x_min:
        code |= left
    elif x > x_max:
        code |= right
    if y < y_min:
        code |= bottom
    elif y > y_max:
        code |= top
    return code
    
def cohen_sutherland_clip(x1, y1, x2, y2, x_min, y_min, x_max, y_max):  
    code_1 = find_code(x1, y1, x_min, y_min, x_max, y_max)
    code_2 = find_code(x2, y2, x_min, y_min, x_max, y_max)

    while True:
        if (code_1 == 0 and code_2 == 0):
            print("Clipped Line:",x1,y1,x2,y2)
            break
        elif (code_1 & code_2) != 0:
            print("Line is completely outside the clipping window")
            break
        else:
            if code_1 != 0:
                code_out = code_1
            else:
                code_out = code_2

            if code_out & top:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            elif code_out & bottom:
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
            elif code_out & right:
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
            elif code_out & left:
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min

            if code_out == code_1:
                x1, y1 = x, y
                code_1 = find_code(x1, y1, x_min, y_min, x_max, y_max)
            else:
                x2, y2 = x, y
                code_2 = find_code(x2, y2, x_min, y_min, x_max, y_max)
# Example usage:
x_min, y_min = 100, 100
x_max, y_max = 300, 300
x1, y1 = 50, 150
x2, y2 = 350, 250
cohen_sutherland_clip(x1, y1, x2, y2, x_min, y_min, x_max, y_max)



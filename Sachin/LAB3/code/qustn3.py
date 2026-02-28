
# -------- DDA with operation count --------
def dda_line_ops(x1, y1, x2, y2):
    add = 0
    mul = 0

    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))

    # divisions (treated as multiplications cost)
    mul += 2
    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1

    for _ in range(int(steps)):
        x += x_inc   # addition
        y += y_inc   # addition
        add += 2

    return add, mul


# -------- Bresenham with operation count --------
def bresenham_line_ops(x1, y1, x2, y2):
    add = 0
    mul = 0

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # initial multiplications
    mul += 2
    p = 2 * dy - dx

    x, y = x1, y1

    for _ in range(dx):
        x += 1
        add += 1

        if p >= 0:
            y += 1
            p += 2 * dy - 2 * dx
            add += 3
            mul += 2
        else:
            p += 2 * dy
            add += 1
            mul += 1

    return add, mul


# -------- Test & Compare --------
x1, y1, x2, y2 = 2, 3, 10, 8

dda_add, dda_mul = dda_line_ops(x1, y1, x2, y2)
bres_add, bres_mul = bresenham_line_ops(x1, y1, x2, y2)

print("DDA Algorithm:")
print("Additions =", dda_add)
print("Multiplications =", dda_mul)

print("\nBresenham Algorithm:")
print("Additions =", bres_add)
print("Multiplications =", bres_mul)

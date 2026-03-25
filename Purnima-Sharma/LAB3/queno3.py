#3. Compare the number of integer additions and multiplications used by DDA and Bresenham.

def compare_dda_bresenham_ops(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    steps = max(dx, dy)

    dda_adds = steps * 2
    dda_mults = 0
    dda_adds_int = dda_adds

    bres_adds = steps + 1
    bres_adds += steps + 1
    bres_adds_int = bres_adds
    bres_mults = 0

    print(f"DDA: {dda_adds_int} additions, {dda_mults} multiplications")
    print(f"Bresenham: {bres_adds_int} additions, {bres_mults} multiplications")

if __name__ == "__main__":
    x1, y1, x2, y2 = 1, 5, 10, 5
    compare_dda_bresenham_ops(x1, y1, x2, y2)
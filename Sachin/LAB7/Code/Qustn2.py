"""Liang-Barsky line clipping with plotting demo.

Run this module to see the clipping result plotted with matplotlib.
"""
from typing import Optional, Tuple
import matplotlib.pyplot as plt

PointAndLine = Tuple[float, float, float, float]


def liang_barsky(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    xmin: float,
    ymin: float,
    xmax: float,
    ymax: float,
) -> Optional[PointAndLine]:
    """Perform Liang-Barsky line clipping.

    Returns (nx1, ny1, nx2, ny2) for the clipped segment, or None if
    the line lies completely outside the clipping window.
    """
    dx = x2 - x1
    dy = y2 - y1

    u1 = 0.0
    u2 = 1.0

    p = [-dx, dx, -dy, dy]
    q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]

    for pi, qi in zip(p, q):
        if pi == 0:
            if qi < 0:
                # Line is parallel to this boundary and outside
                return None
            # Line is parallel and inside for this boundary; continue
        else:
            t = qi / pi
            if pi < 0:
                if t > u1:
                    u1 = t
            else:
                if t < u2:
                    u2 = t

    if u1 > u2:
        return None

    nx1 = x1 + u1 * dx
    ny1 = y1 + u1 * dy
    nx2 = x1 + u2 * dx
    ny2 = y1 + u2 * dy

    return nx1, ny1, nx2, ny2


def draw(original: PointAndLine, clipped: Optional[PointAndLine], xmin: float, ymin: float, xmax: float, ymax: float) -> None:
    """Draw the clipping window, original line, and clipped line (if present)."""
    # Draw clipping rectangle
    rect_x = [xmin, xmax, xmax, xmin, xmin]
    rect_y = [ymin, ymin, ymax, ymax, ymin]
    plt.plot(rect_x, rect_y, color="black")

    x1, y1, x2, y2 = original
    # Original line dashed
    plt.plot([x1, x2], [y1, y2], linestyle="--", color="gray", label="Original")

    if clipped is not None:
        cx1, cy1, cx2, cy2 = clipped
        plt.plot([cx1, cx2], [cy1, cy2], linestyle="-", color="red", linewidth=2, label="Clipped")

    plt.title("Liang-Barsky Line Clipping")
    plt.axis("equal")
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    xmin = 10
    ymin = 10
    xmax = 100
    ymax = 100

    original = (0.0, 0.0, 120.0, 120.0)
    clipped = liang_barsky(*original, xmin, ymin, xmax, ymax)

    draw(original, clipped, xmin, ymin, xmax, ymax)

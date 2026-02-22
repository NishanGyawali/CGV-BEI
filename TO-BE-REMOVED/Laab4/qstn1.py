#!/usr/bin/env python3
"""
Midpoint Circle Drawing Algorithm (matplotlib) with interactive user input for radius.

Usage:
    python midpoint_circle_matplotlib.py         # will prompt for radius (and optional center)
    python midpoint_circle_matplotlib.py --r 30  # uses radius 30 without prompts
    python midpoint_circle_matplotlib.py --r 30 --xc 10 --yc -5

Requires: matplotlib
"""
import argparse
import sys
import matplotlib.pyplot as plt


def plot_circle_points(xc, yc, x, y, xes, yes):
    """Add the eight symmetric points for the computed (x, y)."""
    pts = [
        ( x + xc,  y + yc),
        (-x + xc,  y + yc),
        ( x + xc, -y + yc),
        (-x + xc, -y + yc),
        ( y + xc,  x + yc),
        (-y + xc,  x + yc),
        ( y + xc, -x + yc),
        (-y + xc, -x + yc),
    ]
    for px, py in pts:
        xes.append(px)
        yes.append(py)


def midpoint_circle(r, xc=0, yc=0):
    """Return two lists (xes, yes) of integer pixel coordinates for the circle."""
    if r < 0:
        raise ValueError("Radius must be non-negative")

    x = 0
    y = r
    p = 1 - r
    xes, yes = [], []

    plot_circle_points(xc, yc, x, y, xes, yes)

    while x < y:
        x += 1
        if p < 0:
            # choose E
            p = p + 2 * x + 1
        else:
            # choose SE
            y -= 1
            p = p + 2 * (x - y) + 1
        plot_circle_points(xc, yc, x, y, xes, yes)

    return xes, yes


def plot_midpoint_circle(r, xc=0, yc=0):
    xes, yes = midpoint_circle(r, xc, yc)
    plt.figure(figsize=(6, 6))
    plt.scatter(xes, yes, marker='.', color='red', label='Midpoint pixels')
    plt.title(f"Midpoint Circle Algorithm (r={r}, center=({xc},{yc}))")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.show()


def prompt_int(prompt_text, default=None, allow_negative=False):
    """Prompt the user for an integer, with optional default. Returns int or None if cancelled."""
    while True:
        try:
            raw = input(f"{prompt_text}{' ['+str(default)+']' if default is not None else ''}: ").strip()
            if raw == "" and default is not None:
                return int(default)
            val = int(raw)
            if (not allow_negative) and val < 0:
                print("Please enter a non-negative integer.")
                continue
            return val
        except KeyboardInterrupt:
            print("\nInterrupted by user.")
            sys.exit(1)
        except Exception:
            print("Invalid input — please enter an integer.")


def main():
    ap = argparse.ArgumentParser(description="Midpoint Circle Drawing Algorithm (matplotlib) with user input")
    ap.add_argument("--r", type=int, help="radius (integer, non-negative). If omitted you'll be prompted.")
    ap.add_argument("--xc", type=int, default=0, help="x-coordinate of center (default 0)")
    ap.add_argument("--yc", type=int, default=0, help="y-coordinate of center (default 0)")
    args = ap.parse_args()

    if args.r is None:
        r = prompt_int("Enter radius (non-negative integer)", default=None, allow_negative=False)
    else:
        if args.r < 0:
            print("Radius must be non-negative.", file=sys.stderr)
            sys.exit(1)
        r = args.r

    # Allow optionally prompting for center if user wants (press Enter to keep defaults)
    print(f"Using center defaults xc={args.xc}, yc={args.yc}. Press Enter to accept or type new integer values.")
    xc = prompt_int("Enter xc", default=args.xc, allow_negative=True)
    yc = prompt_int("Enter yc", default=args.yc, allow_negative=True)

    plot_midpoint_circle(r, xc, yc)


if __name__ == "__main__":
    main()
    
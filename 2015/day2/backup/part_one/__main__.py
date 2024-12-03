"""
Day 2: I Was Told There Would Be No Math (Part One)
"""
import sys


def calculate_amount_of_paper(l, w, h):
    """
    l: length
    w: width
    h: height
    """
    side_lw = (l*w)
    side_wh = (w*h)
    side_hl = (h*l)

    surface_area = 2*(side_lw + side_wh + side_hl)

    sides = [side_lw, side_wh, side_hl]
    sides.sort()
    extra = sides[0]

    return (surface_area + extra)


total = 0
file = sys.argv[1]
with open(file, mode="r", encoding="utf-8") as file:
    for line in file:
        split = line.strip().split("x")
        total += calculate_amount_of_paper(int(split[0]), int(split[1]), int(split[2]))

print(f"Total Amount of Paper: {total}")

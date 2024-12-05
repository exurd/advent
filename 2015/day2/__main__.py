"""
Day 2: I Was Told There Would Be No Math
"""
import sys


def calculate_amount_of_paper(l, w, h):
    """
    Calculates amount of paper needed for a present.

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


def calculate_amount_of_ribbon(l, w, h):
    """
    Calculates amount of ribbon needed for a present.

    l: length
    w: width
    h: height
    """
    # get two of the smallest perimeters
    peri = [l, w, h]
    peri.sort()

    # smallest + smallest + second smallest + second smallest
    ribbon_length = (peri[0] + peri[0] + peri[1] + peri[1])

    # for bow
    cubic_meter = (l * w * h)

    return (ribbon_length + cubic_meter)

if __name__ == "__main__":
    total_paper = 0
    total_ribbon = 0
    file = sys.argv[1]
    with open(file, mode="r", encoding="utf-8") as file:
        for line in file:
            split = line.strip().split("x")

            total_paper += calculate_amount_of_paper(int(split[0]), int(split[1]), int(split[2]))
            total_ribbon += calculate_amount_of_ribbon(int(split[0]), int(split[1]), int(split[2]))

    print(f"Total Amount of Paper: {total_paper}")
    print(f"Total Amount of Ribbon: {total_ribbon}")

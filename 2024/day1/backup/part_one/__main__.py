"""
Day 1: Historian Hysteria (Part One)
"""

import sys
import re

exp = re.compile(r"([0-9]+) +([0-9]+)$")


def split_nums_from_(file):
    """
    Split text file into two lists, both with integers.
    """
    list_one, list_two = [], []
    with open(file, mode="r", encoding="utf-8") as file:
        for line in file:
            # split nums and put into list
            split = list(
                        filter(  # this removes empty strings from the split, see https://stackoverflow.com/a/30933281
                            None, exp.split(line.strip())
                        )
                    )
            # print(split)
            try:
                list_one.append(int(split[0])); list_two.append(int(split[1]))
            except:
                pass
    return list_one, list_two


def get_smallest_num_in_(list):
    """
    Gets the smallest number in an integer list.
    """
    smallest_num = list[0]  # set to first number in list
    for i in list:
        if smallest_num >= i:
            smallest_num = i
    return smallest_num


def calculate_differences(list_one, list_two):
    """
    Calculates the differences and returns the differences.

    example.txt should equal to 11.
    """
    difference = 0
    for i in range(len(list_one)):  # list_one should be the same length as list_two as we curated them from the same text file
        #print(list_one)
        int_one = get_smallest_num_in_(list_one)
        int_two = get_smallest_num_in_(list_two)

        # print(f"int one: {int_one}")
        # print(f"int two: {int_two}")

        difference += abs(int_one - int_two)  # subtract value and get absolute value

        # print(f"difference: {abs(int_one - int_two)}")
        # print("-----")

        # .remove() removes the 'first occurrence of value.', which is good enough without having to sort the list out
        list_one.remove(int_one)
        list_two.remove(int_two)
    return difference

file = sys.argv[1]
list_one, list_two = split_nums_from_(file)
difference = calculate_differences(list_one, list_two)
print(f"Difference: {difference}")

"""
Day 1: Historian Hysteria
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
    temp_one = list_one.copy()
    temp_two = list_two.copy()

    for i in range(len(temp_one)):  # list_one should be the same length as list_two as we curated them from the same text file
        #print(list_one)
        int_one = get_smallest_num_in_(temp_one)
        int_two = get_smallest_num_in_(temp_two)

        # print(f"int one: {int_one}")
        # print(f"int two: {int_two}")

        difference += abs(int_one - int_two)  # subtract value and get absolute value

        # print(f"difference: {abs(int_one - int_two)}")
        # print("-----")

        # .remove() removes the 'first occurrence of value.', which is good enough without having to sort the list out
        temp_one.remove(int_one)
        temp_two.remove(int_two)
    return difference


def find_matches_in_(l: list, num):
    """
    Finds every match for num and returns a count.

    Was using a "for i in" loop, but that caused 199907 to be missing from the score.
    "while True and pop" is much more reliable for this.
    """
    count = 0
    temp_two = l.copy()
    while True:  # for i in temp_two:
        i = temp_two[0]
        if i == num:
            count += 1
        temp_two.pop(0)  # temp_two.remove(num) was causing 199907 to not be counted, *and i dont know why*
        if temp_two == []:
            break
    if count != 0:
        return count
    return None


def calculate_similarity_scores(list_one, list_two):
    """
    Calculates a score by comparing list_one to list_two.

    example.txt should equal to 31.
    """
    similar_score = 0
    temp_one = list_one.copy()
    temp_two = list_two.copy()
    while True:  # list_one should be the same length as list_two as we curated them from the same text file
        try:
            #print(list_one)
            num = temp_one[0]
            amount = find_matches_in_(temp_two, num)

            if amount:
                # print(f"int: {num}")
                # print(f"amount: {amount}")
                # print(f"times: {(num * amount)}")
                similar_score += (num * amount)
                #print(f"similarity score: {similar_score}")

            temp_one.pop(0)
            #print(temp_one)
            # print("-----")
        except:
            break
    return similar_score


file = sys.argv[1]
list_one, list_two = split_nums_from_(file)
difference = calculate_differences(list_one, list_two)
print(f"Difference: {difference}")

similar_score = calculate_similarity_scores(list_one, list_two)
print(f"Similarity Score: {similar_score}")

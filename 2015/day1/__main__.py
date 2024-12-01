"""
Day 1: Not Quite Lisp
"""
import sys

file = sys.argv[1]
with open(file, mode="r", encoding="utf-8") as file:
    for line in file:
        floor = 0
        # print(line.strip())
        basement_char = None
        for i, char in enumerate(list(line.strip()), start=1):
            #print(char)
            if char == "(":
                floor += 1
            elif char == ")":
                floor -= 1

            if floor == -1 and basement_char is None:
                basement_char = i
        print(f"Floor: {floor}")
        print(f"Entered the basement at character: {basement_char}")

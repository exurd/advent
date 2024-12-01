"""
Day 1: Not Quite Lisp (Part One)
"""
import sys

file = sys.argv[1]
with open(file, mode="r", encoding="utf-8") as file:
    for line in file:
        floor = 0
        # print(line.strip())

        for char in list(line.strip()):
            #print(char)
            if char == "(":
                floor += 1
            elif char == ")":
                floor -= 1
        print(f"Floor: {floor}")

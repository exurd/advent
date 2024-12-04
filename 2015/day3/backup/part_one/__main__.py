"""
Day 3: Perfectly Spherical Houses in a Vacuum (Part One)
"""
import sys
from enum import Enum


class Instruction(Enum):
    """
    Using enums to turn text arrows into an instruction set.

    -1 and 1 correlates to up and down.
    -2 and 2 correlates to left and right.
    """
    UP = 1
    DOWN = -1
    LEFT = -2
    RIGHT = 2


def parse_instructions(string: str):
    temp_list = []
    for char in list(string):
        #print(char)
        if char == "^":
            temp_list.append(Instruction.UP)
        elif char == "v":
            temp_list.append(Instruction.DOWN)
        elif char == "<":
            temp_list.append(Instruction.LEFT)
        elif char == ">":
            temp_list.append(Instruction.RIGHT)
    return temp_list


class Santa:
    """
    There's only one Santa.
    
    Oh, except in that one Christmas film where three Santas fight over a bike,
    but I just realised that the actual point of the movie was that to the children
    there *is* only one Santa and it's the one that they believe in.

    Thankfully, it's not this one I'm currently writing up. Code be dammed.

    (Just to clarify, only one Santa instance for each code run. MULTIPLE SANTAS IS A BAD CASE.)
    """
    def __init__(self):
        """Start Santa at X coordinate 0, Y coordinate 0."""
        self.location = {"x": 0, "y": 0}
        # use tuples and sets to keep unique locations found
        self.location_history = set()
        self.location_history.add((self.location["x"], self.location["y"]))


    def move(self, instruct:Instruction):
        """Moves Santa with an instruction. Adds the location to the history."""
        if isinstance(instruct, Instruction):
            num = instruct.value
            if abs(num) == 2:  # check if it's a left/right instruction
                if num < 0:
                    self.location["x"] -= 1
                else:
                    self.location["x"] += 1
            if num < 0:
                self.location["y"] -= 1
            else:
                self.location["y"] += 1
            self.location_history.add((self.location["x"], self.location["y"]))


    def __str__(self):
        return f"Ho ho ho! I'm at location {self.location}!\nI have given at least 1 present to {len(self.location_history)} houses!"


file = sys.argv[1]
with open(file, mode="r", encoding="utf-8") as file:
    for line in file:
        print("----")
        current_santa = Santa()
        instruct_set = []

        strip = line.strip()
        instruct_set = parse_instructions(strip)

        for instruct in instruct_set:
            current_santa.move(instruct)
        print(current_santa)

# current_santa = Santa()
# print(current_santa)
# current_santa.move(Instruction.UP)
# print(current_santa)
# current_santa.move(Instruction.DOWN)
# print(current_santa)

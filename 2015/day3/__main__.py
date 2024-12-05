"""
Day 3: Perfectly Spherical Houses in a Vacuum
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
                                                                            ...welp, not anymore lol :P
    """
    def __init__(self, opposite=False):
        """
        Start Santa at X coordinate 0, Y coordinate 0.
        
        Opposite value acts like "Robo-Santa". Goes the opposite direction.
        Edit: mis-read the instructions...
        Keeping the opposite code in because I'm proud of it, dammit!
        """
        self.location = {"x": 0, "y": 0}
        # use tuples and sets to keep unique locations found
        self.location_history = set()
        self.location_history.add((self.location["x"], self.location["y"]))

        self.opposite = bool(opposite)


    def move(self, instruct:Instruction):
        """Moves Santa with an instruction. Adds the location to the history."""
        if isinstance(instruct, Instruction):
            # print(instruct)
            num = instruct.value
            if self.opposite:
                num = -abs(num) if num > 0 else abs(num)
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
            # print(self.location)


    def __str__(self):
        return f"{"Ro ro r" if self.opposite else "Ho ho h"}o! I'm at location {self.location}!\nI have given at least 1 present to {len(self.location_history)} houses!"

if __name__ == "__main__":
    file = sys.argv[1]
    with open(file, mode="r", encoding="utf-8") as file:
        for line in file:
            print("----")
            current_santa = Santa()
            current_robo_santa = Santa()
            instruct_set = []

            strip = line.strip()
            instruct_set = parse_instructions(strip)

            for i, instruct in enumerate(instruct_set):
                if i % 2 == 0:
                    current_robo_santa.move(instruct)
                else:
                    current_santa.move(instruct)
            print(current_santa)
            print(current_robo_santa)
            
            location_history_both = current_santa.location_history.union(current_robo_santa.location_history)
            print(f"Altogether, the unique amount is {len(location_history_both)}")

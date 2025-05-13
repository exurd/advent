"""
Day 7: Some Assembly Required (Part 1)
"""
import sys
import re
from enum import Enum

# Tue May 13 14:27:55 BST 2025:
# I realised that I might take long breaks on advent of code,
# so from now on I'm going to add dates to my comments (using
# `date | pbcopy` on Linux/MacOS). This will make it much easier
# to piece together what I was thinking of at the time.
#
# I don't usually do this because it makes the code a bit harder
# to read and most code comments don't need timestamps to understand
# why it was done that way.
#
# Adding what I think are the right dates to the current code comments...

# Tue May 13 14:32:40 BST 2025: only two comments? okay then

# Tue May 13 14:38:03 BST 2025: note to later self; should i be
# 1. getting the date, then writing the comment?
# or
# 2. writing the comment, then getting the date?
# going to try option 2 for the rest of this code...


# 05/12/2024: I only have one instruction that leads to wire a
# (`lx -> a`) near the top and lx should be empty, so 0??
# (No, order dosen't matter here.)


# 05/12/2024:
# s1: parse wire signal flow
#       - grab integer -> wire instructions first
#       - connect each wire class with an input and output(s)
# s2: send the signal down to the last wire
# s3: output each wire and their input signal


# Tue May 13 15:02:05 BST 2025:
# Figured it out. Since 'each wire can only get a signal from one source',
# the variable after the arrow can be placed into a list of items:
#
# {
#     "x": 123,
#     "y": 456,
#     "d": math.nan,
#     "e": math.nan,
#     "f": math.nan,
#     "g": math.nan,
#     "h": math.nan,
#     "i": math.nan
# }
#
# To solve the vars with nan values, I need to take the vars with numbers
# and insert them into the instructions. It should look a bit like:
# (<Instruction.AND: 'AND'>, 'x', 'y', 'd')
# to
# (<Instruction.AND: 'AND'>, 123, 456, 'd')
# which in the list will be turned into `"d": 72`


# regex expressions
# Tue May 13 16:34:59 BST 2025: bro didn't add + on the last [a-z]
# Tue May 13 16:36:38 BST 2025: forgot about `lx -> a`, now dealing with variable replacements
# Tue May 13 16:39:16 BST 2025: technically it can be a subset of START... let's see if that will work
# Tue May 13 16:43:13 BST 2025: ...the examples they give are very lackluster
#                               now i gotta force in support for wires that have numbers AND letters...
# Tue May 13 17:16:07 BST 2025:
#                               Instruction.NOT: [0, 'a'] -> cb [Ready to process: False]
#                               NOT ca -> cb
#                               what
# Tue May 13 17:18:48 BST 2025:
#                               in example by itself:
#                               Instruction.NOT: ca -> cb [Ready to process: False]
#                               i think i know what the problem is (fixed it)

express_nums = re.compile(r"^([0-9]+) -> ([a-z]+)$")  # 0 -> c
express_ops = re.compile(r"^([a-z0-9]+) (AND|OR) ([a-z0-9]+) -> ([a-z]+)$")  # g AND i -> j
express_lrshift = re.compile(r"^([a-z]+) (LSHIFT|RSHIFT) ([0-9]+) -> ([a-z]+)$")  # x LSHIFT 2 -> f
express_not = re.compile(r"^NOT ([a-z]+) -> ([a-z]+)$")  # NOT jd -> je
express_replace = re.compile(r"^([a-z]+) -> ([a-z]+)$")  # lx -> a


class Instruction(Enum):
    START = 0
    # REPLACE = -1
    AND = "AND"
    OR = "OR"
    LSHIFT = "LSHIFT"
    RSHIFT = "RSHIFT"
    NOT = "NOT"


# Tue May 13 16:25:53 BST 2025: thanks /u/Spataner
# https://old.reddit.com/r/learnpython/comments/17icb1j/declaring_an_unsigned_integer_16_in_python_for/k6tfaje/
uint16max = (1 << 16) - 1

vars = {}


class Wire():
    """
    ready_to_process: does the wire have the inputs needed for processing? True = Yes, False = No, None = Already processed
    """
    def __init__(self, instruction:Instruction, inputs:list, output, orig_string:str, ready_to_process=False):
        self.instruction = instruction  # see Instruction Enum above
        self.inputs = inputs  # [123], [x, y], [y]
        self.output = output  # d, e, f, g
        self.ready = ready_to_process
        self.orig = orig_string  # original line for debugging

    def __repr__(self):
        return f"{self.instruction}: {self.inputs} -> {self.output} [Ready to process: {self.ready}]"
    def __str__(self):
        return f"{self.instruction}: {self.inputs} -> {self.output} [Ready to process: {self.ready}]"

    def start_process(self):
        """Process wire and return number."""
        match self.instruction:
            case Instruction.START:
                result = self.inputs[0]
            # case Instruction.REPLACE:
            #     result = self.inputs[0]
            case Instruction.AND:
                result = (self.inputs[0] & self.inputs[1]) & uint16max
            case Instruction.OR:
                result = (self.inputs[0] | self.inputs[1]) & uint16max
            case Instruction.LSHIFT:
                result = (self.inputs[0] << self.inputs[1]) & uint16max
            case Instruction.RSHIFT:
                result = (self.inputs[0] >> self.inputs[1]) & uint16max
            case Instruction.NOT:
                result = (~self.inputs[0]) & uint16max
        self.ready = None
        return self.output, result
    
    def check_if_ready(self):
        for i in self.inputs:
            if type(i) is str:  # "x"
                return
        self.ready = True

    def solve_inputs(self):
        global vars
        for v in vars:
            if v in self.inputs:
                new_inputs = []
                for i in self.inputs:
                    if v == i:
                        new_inputs.append(vars[v])
                        continue
                    new_inputs.append(i)
                self.inputs = new_inputs
                self.check_if_ready()


def solve(wires):
    w:Wire
    for _ in range(1000):
        for w in wires:
            # print(w)
            if w.ready is not None:
                if w.ready is True:
                    output, result = w.start_process()
                    vars[output] = result
        # print(vars)
        # add number outputs from previously solved wires
        all_done = True
        for w in wires:
            if w.ready is not None and w.ready is not True:
                all_done = False
                w.solve_inputs()
            # print(w)
        if all_done is True:
            break


def convert_to_int(sting:str):
    if sting.isnumeric():
        return int(sting)
    return sting


def detect_wire_types(string:str):
    """
    Detect type of wire for string.

    (<Instruction>, INPUT(s), OUTPUT, READY TO PROCESS)
    """
    match_nums = express_nums.match(string)
    if match_nums:
        num = match_nums[1]
        output_wire = match_nums[2]
        # Tue May 13 15:11:25 BST 2025: I don't know if this should be a tuple but gonna roll with it for now
        return Wire(Instruction.START, [int(num)], output_wire, string, True)
    
    match_rep = express_replace.match(string)
    if match_rep:
        var = match_rep[1]
        output_wire = match_rep[2]
        return Wire(Instruction.START, [var], output_wire, string)

    match_ops = express_ops.match(string)
    if match_ops:
        input_wire_one = convert_to_int(match_ops[1])
        operation = match_ops[2]
        input_wire_two = convert_to_int(match_ops[3])
        output_wire = match_ops[4]
        return Wire(Instruction[operation], [input_wire_one, input_wire_two], output_wire, string)

    match_lrshift = express_lrshift.match(string)
    if match_lrshift:
        input_wire_one = convert_to_int(match_lrshift[1])
        operation = match_lrshift[2]
        number = match_lrshift[3]
        output_wire = match_lrshift[4]
        return Wire(Instruction[operation], [input_wire_one, int(number)], output_wire, string)

    match_not = express_not.match(string)
    if match_not:
        input_wire = convert_to_int(match_not[1])
        output_wire = match_not[2]
        # Tue May 13 17:20:27 BST 2025: [you]
        return Wire(Instruction.NOT, [input_wire], output_wire, string)


def parse(instructions):
    a = []
    for i in instructions:
        i = detect_wire_types(i)
        a.append(i)
    return a


instructions = []
if __name__ == "__main__":
    file = sys.argv[1]
    with open(file, mode="r", encoding="utf-8") as file:
        for line in file:
            strip = line.strip()
            instructions.append(strip)
    wires = parse(instructions)
    # print(wires)
    solve(wires)
    print("Wires done:")
    for w in wires:
        if w.ready is None:
            print(w)
    print("Wires not done:")
    for w in wires:
        if w.ready is False:
            print(w)
    print("\n")

    print("Values:")
    for v in vars:
        print(f"{v}: {vars[v]}")

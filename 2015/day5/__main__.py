"""
Day 5: Doesn't He Have Intern-Elves For This?
"""
import sys
import string as str_const

# two letter pairs
allowed = set()
for first in str_const.ascii_lowercase:
    for second in str_const.ascii_lowercase:
        allowed.add(first+second)
# print(allowed)


def check_allowed(string:str):
    """Checks if the string contains an allowed pair."""
    for pair in allowed:
        if pair in string:
            # print(string.count(pair))
            if string.count(pair) >= 2:
                return True
    return False


def check_sandwich(string:str):
    """Checks if the string contains a sandwich pair."""
    prev_char = None
    prev_prev_char = None
    for char in string:  # huh, list(string) is the same as string...
        # print(char)
        if char == prev_prev_char:
            return True
        prev_prev_char = prev_char
        prev_char = char
    return False


def nice(string:str):
    """Checks if the string is nice."""
    # print(f"Disallowed strings: {check_disallowed(string)}")
    print(f"Letter pairs: {check_allowed(string)}")
    print(f"Sandwich: {check_sandwich(string)}")
    return (check_allowed(string) and check_sandwich(string))

if __name__ == "__main__":
    nice_strings = 0
    file = sys.argv[1]
    with open(file, mode="r", encoding="utf-8") as file:
        for line in file:
            strip = line.strip()
            print(strip)
            if nice(strip):
                nice_strings += 1
            print("-----")
    print(f"Nice strings: {nice_strings}") # wrong: 158, 52

"""
Day 5: Doesn't He Have Intern-Elves For This? (Part one)
"""
import sys

disallowed = ("ab", "cd", "pq", "xy")
def check_disallowed(string:str):
    """Check if disallowed letter pairs are not in the string."""
    for pair in disallowed:
        if pair in string:
            return False
    return True


vowels = ("a", "e", "i", "o", "u")
def check_vowels(string:str):
    """Check if string contains three or more vowels."""
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return True if count >= 3 else False


def check_double(string:str):
    """Checks if the string contains a double letter pair."""
    prev_char = None
    for char in string:  # huh, list(string) is the same as string...
        # print(char)
        if char == prev_char:
            return True
        prev_char = char
    return False


def nice(string:str):
    """Checks if the string is nice."""
    # print(f"Disallowed strings: {check_disallowed(string)}")
    # print(f"Double letters: {check_double(string)}")
    # print(f"Three vowels: {check_vowels(string)}")
    return (check_disallowed(string) and check_double(string) and check_vowels(string))


nice_strings = 0
file = sys.argv[1]
with open(file, mode="r", encoding="utf-8") as file:
    for line in file:
        strip = line.strip()
        if nice(strip):
            nice_strings += 1
print(f"Nice strings: {nice_strings}")

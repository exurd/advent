"""
Day 4: The Ideal Stocking Stuffer (Part one and two; only difference is one more zero.)
"""
import sys
import re
import hashlib

express_5 = re.compile(r"^00000")
express_6 = re.compile(r"^000000")

file = sys.argv[1]
input = ""
with open(file, mode="r", encoding="utf-8") as file:
    input = file.readline().strip()

print(f"For {input}:")
def get_md5(express):
    md5_hash_hex = ""
    num = 0
    while True:
        # print(f"{input}{num}".encode("ascii"))
        md5_hash_hex = hashlib.md5(f"{input}{num}".encode("ascii")).hexdigest()
        if express.match(md5_hash_hex):
            print(f"MD5 hash: {md5_hash_hex}\nNumber: {num}")
            return md5_hash_hex, num
        num += 1

get_md5(express_5)
get_md5(express_6)

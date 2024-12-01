import sys
file = sys.argv[1]

test = []
with open(file, mode="r", encoding="utf-8") as file:
    for line in file:
        # split nums and put into list
        split = line.strip()
        # print(split)
        try:
            test.append(int(split))
        except:
            pass

seen = set()
dupes = []

for x in test:
    if x in seen:
        dupes.append(x)
    else:
        seen.add(x)

print(dupes)
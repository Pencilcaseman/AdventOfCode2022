def readFile():
    pairs = []
    with open("inputs/day4.txt", "r") as file:
        for line in file:
            elves = line.split(",")
            range = []
            for elf in elves:  # To avoid repetition
                start, end = elf.split("-")
                range.append((int(start), int(end)))
            pairs.append(range)
    return pairs


def overlaps(elf1, elf2):
    range1 = set(range(elf1[0], elf1[1] + 1))
    range2 = set(range(elf2[0], elf2[1] + 1))
    common = range1.intersection(range2)
    if any([len(common) >= len(e) for e in [range1, range2]]):
        return True
    return False


def overlapsQ2(elf1, elf2):
    range1 = set(range(elf1[0], elf1[1] + 1))
    range2 = set(range(elf2[0], elf2[1] + 1))
    common = range1.intersection(range2)
    if any([len(common) > 0 for e in [range1, range2]]):
        return True
    return False


pairs = readFile()
# pairs = [[(2, 4), (6, 8)],
#          [(2, 3), (4, 5)],
#          [(5, 7), (7, 9)],
#          [(2, 8), (3, 7)],
#          [(6, 6), (4, 6)],
#          [(2, 6), (4, 8)]]

print(pairs)

total = 0
for pair in pairs:
    if overlaps(pair[0], pair[1]):
        print("Intersecting")
        total += 1
    else:
        print("Not intersecting")

print(total)

total = 0
for pair in pairs:
    if overlapsQ2(pair[0], pair[1]):
        total += 1

print(total)

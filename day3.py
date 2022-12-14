def readFile():
    bags = []
    with open("inputs/day3.txt", "r") as file:
        for line in file:
            bags.append(line.strip())
    return bags


def splitBag(contents):
    size = len(contents)
    left, right = contents[:size // 2], contents[size // 2:]
    common = set(left).intersection(set(right))
    return left, right, list(common)[0]


def priority(val):
    if 97 <= ord(val) <= 122:
        return ord(val) - 96
    return ord(val) - 65 + 27


bags = readFile()
# bags = ["vJrwpWtwJgWrhcsFMMfFFhFp",
#         "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
#         "PmmdzqPrVvPwwTWBwg",
#         "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
#         "ttgJtRGJQctTZtZT",
#         "CrZsJsPPZsGzwwsLwLmpwMDw"]

print(bags)

for bag in bags:
    split = splitBag(bag)
    print(split, priority(split[2]))

print(sum(priority(splitBag(bag)[2]) for bag in bags))

total = 0
for i in range(0, len(bags), 3):
    first = set(bags[i])
    second = set(bags[i + 1])
    third = set(bags[i + 2])

    common = first.intersection(second).intersection(third)
    total += priority(list(common)[0])

print(total)

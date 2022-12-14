from typing import Union, Dict, Any


def readFile():
    with open("inputs/day7.txt", "r") as file:
        return file.read().split("\n")


def parseFolderStructure(listing, baseStructure=False):
    if baseStructure:
        baseStructure = {"/": {}}
    else:
        baseStructure = {}

    structure = baseStructure

    index = 0
    while index < len(listing) and listing[index] != "$ cd ..":
        if len(listing[index].strip()) == 0:
            index += 1
            continue

        if listing[index] == "$ ls":
            index += 1
            continue

        if listing[index].startswith("$ cd "):
            cd = listing[index][5:]
            structure[cd], offset = parseFolderStructure(listing[index + 1:])
            index += offset + 1
        elif listing[index].startswith("dir"):
            dirName = listing[index][4:]
            structure[dirName] = {}
        elif not listing[index].startswith("$"):
            split = listing[index].split()
            fileSize = int(split[0])
            fileName = split[1]
            structure[fileName] = fileSize

        index += 1

    return structure, index


def sumSmallerThan(structure, size, res):
    total = 0
    for key, value in structure.items():
        if isinstance(value, int):
            total += value
        else:
            total += sumSmallerThan(value, size, res)

    if total < size:
        res.append(total)

    return total


term = readFile()

# term = """$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k
# """.split("\n")

print(term)

structure = parseFolderStructure(term, True)
print(structure)

res = []
print(sumSmallerThan(structure[0], 100000, res))
print("Can Delete:", sum(res))

# Question 2

totalSize = 70000000
requiredSize = 30000000

currentlyUsed = sumSmallerThan(structure[0], 0, [])
minimumFree = requiredSize - (totalSize - currentlyUsed)
print(minimumFree)
res = []
sumSmallerThan(structure[0], totalSize, res)
for item in sorted(res):
    if item > minimumFree:
        print("Frees Size:", item)
        break

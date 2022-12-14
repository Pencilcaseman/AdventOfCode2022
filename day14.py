def readFile():
    with open("inputs/day14.txt", "r") as file:
        return file.readlines()


def parseInput(lines):
    blocks = []
    for inputLine in lines:
        inputLine = inputLine.strip()
        if len(inputLine) == 0:
            continue

        currentBlock = []

        for section in inputLine.split("->"):
            x, y = list(map(int, section.split(",")))

            if len(currentBlock) == 0:
                currentBlock.append((x, y))
            else:
                px, py = currentBlock[-1]
                incX = (1 if px < x else -1) * (px != x)
                incY = (1 if py < y else -1) * (py != y)

                if incX != 0:
                    for newX in range(px, x, incX):
                        currentBlock.append((newX, y))
                elif incY != 0:
                    for newY in range(py, y, incY):
                        currentBlock.append((x, newY))

                currentBlock.append((x, y))

        blocks += currentBlock

    return blocks


def sandSim(rocks, sandOrigin, numGrains, floor=False):
    minX = min([sandOrigin[0]] + [rock[0] for rock in rocks])
    maxX = max([sandOrigin[0]] + [rock[0] for rock in rocks])
    minY = min([sandOrigin[1]] + [rock[1] for rock in rocks])
    maxY = max([sandOrigin[1]] + [rock[1] for rock in rocks])

    # inc = (maxX - minX) // 2
    # maxX += inc
    # minX -= inc

    inc = ((maxY - minY) - (maxX - minX)) * 2
    maxX += inc
    minX -= inc

    grid = [["." for _ in range(minX, maxX)] for _ in range(minY, maxY + 3)]

    for rock in rocks:
        grid[rock[1] - minY][rock[0] - minX] = "#"

    grid[sandOrigin[1] - minY][sandOrigin[0] - minX] = "+"

    if floor:
        for i in range(len(grid[0])):
            grid[-1][i] = "#"

    gridSandOrigin = [sandOrigin[1] - minY, sandOrigin[0] - minX]
    for i in range(numGrains):
        sandPos = gridSandOrigin[:]  # Note: in (row, col) order
        moved = True
        while moved:
            moved = False

            if sandPos[0] + 1 == len(grid):
                for row in grid:
                    print("".join(map(str, row)))
                print("Fallen into the abyss")
                return i

            if grid[sandPos[0] + 1][sandPos[1]] == ".":
                sandPos[0] += 1
                moved = True
            elif grid[sandPos[0] + 1][sandPos[1] - 1] == ".":
                sandPos[0] += 1
                sandPos[1] -= 1
                moved = True
            elif grid[sandPos[0] + 1][sandPos[1] + 1] == ".":
                sandPos[0] += 1
                sandPos[1] += 1
                moved = True

        if sandPos == gridSandOrigin:
            for row in grid:
                print("".join(map(str, row)))
            print("Sand Blocked")
            return i

        grid[sandPos[0]][sandPos[1]] = "O"

    for row in grid:
        print("".join(map(str, row)))

    return numGrains


mode = "data"
if mode == "data":
    rocks = parseInput(readFile())
elif mode == "sample":
    rocks = parseInput([
        "498,4 -> 498,6 -> 496,6",
        "503,4 -> 502,4 -> 502,9 -> 494,9"
    ])
elif mode == "test":
    rocks = parseInput([
        "0,10 -> 10,10 -> 10,0 -> 0,0",

    ])
else:
    raise ValueError("Unknown Mode")

print(rocks)

maxGrains = 100000
grains = sandSim(rocks, (500, 0), maxGrains, False)
print(f"Question 1: {grains}")

grains = sandSim(rocks, (500, 0), maxGrains, True)
print(f"Question 2: {grains + 1}")

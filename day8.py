def readFile():
    grid = []
    with open("inputs/day8.txt", "r") as file:
        for line in file:
            grid.append(list(map(int, list(line.strip()))))
    return grid


def isVisible(grid, row, col, stride, origin):
    startRow = row if origin[0] is None else (len(grid) - 1) * origin[0]
    startCol = col if origin[1] is None else (len(grid[0]) - 1) * origin[1]

    highest = -1
    count = 0
    while startRow != row or startCol != col:
        if grid[startRow][startCol] > highest:
            highest = grid[startRow][startCol]

        startRow += stride[0]
        startCol += stride[1]

        count += 1

    return grid[row][col] > highest


def findVisible(grid):
    visible = []
    strides = (  # (row, column)
        (1, 0),  # Down
        (-1, 0),  # Up
        (0, 1),  # Right
        (0, -1),  # Left
    )

    origins = (  # (row, column)
        (0, None),  # Down
        (1, None),  # Up
        (None, 0),  # Right
        (None, 1),  # Left
    )

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            for stride, origin in zip(strides, origins):
                if isVisible(grid, row, col, stride, origin):
                    if (row, col) not in visible:
                        visible.append((row, col))

    return visible


def isEdge(grid, row, col):
    return row == 0 or col == 0 or row == len(grid) - 1 or col == len(grid[0]) - 1


def isOverEdge(grid, row, col):
    return row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0])


def calculateScenicScore(grid, row, col):
    strides = (  # (row, column)
        (1, 0),  # Down
        (-1, 0),  # Up
        (0, 1),  # Right
        (0, -1),  # Left
    )

    score = 1
    treeHeight = grid[row][col]

    # Check edge
    if isEdge(grid, row, col):
        return 0  # On Edge

    for stride in strides:
        tmpScore = 0
        tmpRow = row + stride[0]
        tmpCol = col + stride[1]

        while not isOverEdge(grid, tmpRow, tmpCol):
            if treeHeight >= grid[tmpRow][tmpCol]:
                tmpScore += 1
                if treeHeight == grid[tmpRow][tmpCol]:
                    break
            else:
                tmpScore += 1
                break

            tmpRow += stride[0]
            tmpCol += stride[1]

        print("Temporary: ", stride, tmpScore)
        score *= tmpScore

    return score


grid = None
if True:
    grid = readFile()
else:
    grid = [[3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0]]

for row in grid:
    for col in row:
        print(col, end=" ")
    print()

visible = findVisible(grid)
print(visible)
print(f"{len(visible)} trees are visible from the outside")

strides = (  # (row, column)
    (1, 0),  # Down
    (-1, 0),  # Up
    (0, 1),  # Right
    (0, -1),  # Left
)

origins = (  # (row, column)
    (0, None),  # Down
    (1, None),  # Up
    (None, 0),  # Right
    (None, 1),  # Left
)

row = 3
col = 2
for stride, origin in zip(strides, origins):
    if isVisible(grid, row, col, stride, origin):
        print("Tree is visible with", stride, "from", origin)

# Question 2
print(calculateScenicScore(grid, row, col))

maxScenicScore = 0
maxScenicPos = None

for row in range(len(grid)):
    for col in range(len(grid[row])):
        scenicScore = calculateScenicScore(grid, row, col)
        if scenicScore > maxScenicScore:
            maxScenicScore = scenicScore
            maxScenicPos = (row, col)

print("Max Scenic Score:", maxScenicScore)
print("Max Scenic Position:", maxScenicPos)

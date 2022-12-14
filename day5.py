def readFile():
    data = [[] for _ in range(9)]
    moves = []
    parseData = True
    with open("inputs/day5.txt", "r") as file:
        for line in file:
            if line == "\n":
                parseData = False
                continue

            if parseData:
                stack = 0
                index = 1
                while index < len(line):
                    if 65 <= ord(line[index]) <= 90:
                        data[stack].insert(0, line[index])

                    index += 4
                    stack += 1
            else:
                tmp = line.split()
                moves.append((int(tmp[1]), int(tmp[3]) - 1, int(tmp[5]) - 1))

    return data, moves


def moveCrates(stacks, moves):
    tmp = stacks[:]

    for move in moves:
        moveN = move[0]
        moveFrom = move[1]
        moveTo = move[2]

        for _ in range(moveN):
            tmp[moveTo].append(tmp[moveFrom].pop())

    return tmp


def moveCratesQ2(stacks, moves):
    tmp = stacks[:]

    for move in moves:
        moveN = move[0]
        moveFrom = move[1]
        moveTo = move[2]

        tmp[moveTo] += tmp[moveFrom][-moveN:]
        for _ in range(moveN):
            tmp[moveFrom].pop()

    return tmp


stacks, moves = readFile()
# stacks = [
#     ["Z", "N"],
#     ["M", "C", "D"],
#     ["P"]
# ]
#
# moves = [
#     (1, 1, 0),
#     (3, 0, 2),
#     (2, 1, 0),
#     (1, 0, 1)
# ]

moved = moveCratesQ2(stacks, moves)
print("".join([stack[-1] for stack in moved]))

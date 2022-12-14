def readFile():
    output = []
    with open("inputs/day9.txt", "r") as file:
        for line in file:
            split = line.split()
            output.append((split[0], int(split[1])))
    return output


def arrangement(head, tail):
    samePoint = head == tail

    adjacent = any([
        tail[0] == head[0] and tail[1] + 1 == head[1],  # Below
        tail[0] == head[0] and tail[1] - 1 == head[1],  # Above
        tail[0] + 1 == head[0] and tail[1] == head[1],  # Left
        tail[0] - 1 == head[0] and tail[1] == head[1]  # Right
    ])

    diagonal = any([
        tail[0] + 1 == head[0] and tail[1] - 1 == head[1],  # up, right
        tail[0] - 1 == head[0] and tail[1] - 1 == head[1],  # up, left
        tail[0] + 1 == head[0] and tail[1] + 1 == head[1],  # down, right
        tail[0] - 1 == head[0] and tail[1] + 1 == tail[1]  # down, left
    ])

    return samePoint, adjacent, diagonal


def ropeSim(moves):
    pointsReached = []
    ropeHead = [0, 0]
    ropeTail = [0, 0]

    for move in moves:
        for _ in range(move[1]):
            if move[0] == "R":
                ropeHead[0] += 1
            elif move[0] == "L":
                ropeHead[0] -= 1
            elif move[0] == "U":
                ropeHead[1] += 1
            elif move[0] == "D":
                ropeHead[1] -= 1

            # Move tail

            currentArrangement = arrangement(ropeHead, ropeTail)

            if any(currentArrangement):
                print("Touching")
            else:
                print("Not touching")

                dx = ropeHead[0] - ropeTail[0]
                dy = ropeHead[1] - ropeTail[1]

                print(dx, dy)

                if dx == 0:  # Same x value -- change y
                    ropeTail[1] += 1 if dy > 0 else -1
                elif dy == 0:
                    ropeTail[0] += 1 if dx > 0 else -1
                elif abs(dx) != abs(dy):  # Diagonal
                    ropeTail[0] += 1 if dx > 0 else -1
                    ropeTail[1] += 1 if dy > 0 else -1

            print("Head:", ropeHead, "    Tail:", ropeTail)

            if ropeTail not in pointsReached:
                pointsReached.append(ropeTail[:])

    return pointsReached


def ropeSim2(moves):
    pointsReached = []
    rope = [[0, 0] for _ in range(10)]

    for move in moves:
        for _ in range(move[1]):
            if move[0] == "R":
                rope[0][0] += 1
            elif move[0] == "L":
                rope[0][0] -= 1
            elif move[0] == "U":
                rope[0][1] += 1
            elif move[0] == "D":
                rope[0][1] -= 1

            # Move tail

            for i in range(1, len(rope)):
                currentArrangement = arrangement(rope[i - 1], rope[i])
                if not any(currentArrangement):
                    dx = rope[i - 1][0] - rope[i][0]
                    dy = rope[i - 1][1] - rope[i][1]

                    if dx == 0:  # Same x value -- change y
                        rope[i][1] += 1 if dy > 0 else -1
                    elif dy == 0:
                        rope[i][0] += 1 if dx > 0 else -1
                    elif (abs(dx) != abs(dy)) or (abs(dx) == abs(dy) and abs(dx) == 2):  # Diagonal or Special case?
                        rope[i][0] += 1 if dx > 0 else -1
                        rope[i][1] += 1 if dy > 0 else -1

            print("Rope: ", rope)

            if rope[-1] not in pointsReached:
                pointsReached.append(rope[-1][:])

        print("")

    return pointsReached


mode = "data"
if mode == "data":
    moves = readFile()
elif mode == "sample1":
    moves = [("R", 4),
             ("U", 4),
             ("L", 3),
             ("D", 1),
             ("R", 4),
             ("D", 1),
             ("L", 5),
             ("R", 2)]
elif mode == "sample2":
    moves = [
        ("R", 5),
        ("U", 8),
        ("L", 8),
        ("D", 3),
        ("R", 17),
        ("D", 10),
        ("L", 25),
        ("U", 20)
    ]
elif mode == "test":
    moves = [("R", 5),
             ("U", 8),
             ("L", 8)]
else:
    raise RuntimeError("Invalid Mode")

print(moves)

print("Question 1")
points = ropeSim(moves)
print(points)
print(len(points))

print("Question 2")
points = ropeSim2(moves)
print(points)
print(len(points))

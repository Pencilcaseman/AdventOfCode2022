import math


def readFile():
    lines = []
    with open("inputs/day12.txt", "r") as file:
        for line in file:
            lines.append(line.strip())
    return lines


def findPOI(lines):
    src = None
    dst = None

    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == "S":
                src = (row, col)
            elif lines[row][col] == "E":
                dst = (row, col)

    return src, dst


def canStep(src, dst):
    return ord(dst) <= ord(src) + 1


def textToGraph(text):
    layout = text[:]
    for i in range(len(layout)):
        layout[i] = layout[i].replace("S", "a").replace("E", "z")
    graph = {}

    for row in range(len(layout)):
        for col in range(len(layout[row])):
            currentTile = layout[row][col]
            neighbors = []

            if row > 0 and canStep(currentTile, layout[row - 1][col]):
                neighbors.append((row - 1, col))
            if col > 0 and canStep(currentTile, layout[row][col - 1]):
                neighbors.append((row, col - 1))
            if row < len(layout) - 1 and canStep(currentTile, layout[row + 1][col]):
                neighbors.append((row + 1, col))
            if col < len(layout[row]) - 1 and canStep(currentTile, layout[row][col + 1]):
                neighbors.append((row, col + 1))

            graph[(row, col)] = neighbors

    return graph


def textToReverseGraph(text):
    layout = text[:]
    for i in range(len(layout)):
        layout[i] = layout[i].replace("S", "a").replace("E", "z")
    graph = {}

    for row in range(len(layout)):
        for col in range(len(layout[row])):
            currentTile = layout[row][col]
            neighbors = []

            if row > 0 and canStep(layout[row - 1][col], currentTile):
                neighbors.append((row - 1, col))
            if col > 0 and canStep(layout[row][col - 1], currentTile):
                neighbors.append((row, col - 1))
            if row < len(layout) - 1 and canStep(layout[row + 1][col], currentTile):
                neighbors.append((row + 1, col))
            if col < len(layout[row]) - 1 and canStep(layout[row][col + 1], currentTile):
                neighbors.append((row, col + 1))

            graph[(row, col)] = neighbors

    return graph


def dijkstra(src, dst, graph):
    current = {}

    for key, value in graph.items():
        current[key] = {
            "prev": None,
            "dist": math.inf,
            "nextTo": value,
            "seen": False
        }

    current[src] = {
        "prev": None,
        "dist": 0,
        "nextTo": graph[src],
        "seen": False
    }

    for _ in range(len(graph.keys())):
        notSeen = list(filter(lambda x: not current[x]["seen"], graph.keys()))
        if len(notSeen) == 0:
            break
        currentNode = min(notSeen, key=lambda x: current[x]["dist"])

        for neighbor in graph[currentNode]:
            if not current[neighbor]["seen"]:
                newDist = current[currentNode]["dist"] + 1
                if newDist < current[neighbor]["dist"]:
                    current[neighbor]["dist"] = newDist
                    current[neighbor]["prev"] = currentNode

        current[currentNode]["seen"] = True

    # return current

    path = [current[dst]]
    while path[0]["prev"] is not None:
        path.insert(0, current[path[0]["prev"]])
    return path, current


def reverseDijkstra(src, dst, graph):
    current = {}

    for key, value in graph.items():
        current[key] = {
            "prev": None,
            "dist": math.inf,
            "nextTo": value,
            "seen": False
        }

    current[dst] = {
        "prev": None,
        "dist": 0,
        "nextTo": graph[src],
        "seen": False
    }

    for _ in range(len(graph.keys())):
        notSeen = list(filter(lambda x: not current[x]["seen"], graph.keys()))
        if len(notSeen) == 0:
            break
        currentNode = min(notSeen, key=lambda x: current[x]["dist"])

        for neighbor in graph[currentNode]:
            if not current[neighbor]["seen"]:
                newDist = current[currentNode]["dist"] + 1
                if newDist < current[neighbor]["dist"]:
                    current[neighbor]["dist"] = newDist
                    current[neighbor]["prev"] = currentNode

        current[currentNode]["seen"] = True

    # return current

    path = [current[dst]]
    while path[0]["prev"] is not None:
        path.insert(0, current[path[0]["prev"]])
    return path, current


mode = "data"
if mode == "data":
    lines = readFile()
elif mode == "sample":
    lines = [
        "Sabqponm",
        "abcryxxl",
        "accszExk",
        "acctuvwj",
        "abdefghi",
    ]
else:
    raise ValueError("Invalid Mode: " + mode)

print(lines)

graph = textToGraph(lines)
src, dst = findPOI(lines)
for key, value in graph.items():
    print(key, value)

path, structure = dijkstra(src, dst, graph)
for item in path:
    print(item)
print(f"Path contains {len(path)} items, with {path[-1]['dist']} steps")

print("Question 2")
reverseGraph = textToReverseGraph(lines)
src, dst = findPOI(lines)

path, structure = reverseDijkstra(src, dst, reverseGraph)
for item in structure.items():
    print(item)
startingPoints = list(filter(lambda x: lines[x[0]][x[1]] in ["a", "S"], structure.keys()))
print("Possible starting points:", startingPoints)

bestStartingPoint = min(startingPoints, key=lambda x: structure[x]["dist"])
print(f"Best starting point is at {bestStartingPoint}, which takes {structure[bestStartingPoint]['dist']} steps")

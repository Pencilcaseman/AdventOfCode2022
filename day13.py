import math


def readFile():
    pairs = []
    with open("inputs/day13.txt", "r") as file:
        pair = []
        for line in file:
            if line.strip() == "":
                pairs.append(pair[:])
                pair.clear()
            else:
                pair.append(eval(line.strip()))
    return pairs


mode = "data"
if mode == "data":
    textPairs = readFile()
elif mode == "sample":
    textPairs = [
        ([1, 1, 3, 1, 1],
         [1, 1, 5, 1, 1]),
        ([[1], [2, 3, 4]],
         [[1], 4]),
        ([9],
         [[8, 7, 6]]),
        ([[4, 4], 4, 4],
         [[4, 4], 4, 4, 4]),
        ([7, 7, 7, 7],
         [7, 7, 7]),
        ([],
         [3]),
        ([[[]]],
         [[]]),
        ([1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
         [1, [2, [3, [4, [5, 6, 0]]]], 8, 9])
    ]
else:
    raise ValueError("help")


def compare(lhs, rhs):
    if isinstance(lhs, int) and isinstance(rhs, int):
        if lhs < rhs:
            return "good"
        elif lhs == rhs:
            return "continue"
        return "bad"

    if isinstance(lhs, list) and isinstance(rhs, list):
        for left, right in zip(lhs, rhs):
            result = compare(left, right)
            if result != "continue":
                return result

        if len(lhs) < len(rhs):
            return "good"
        elif len(lhs) == len(rhs):
            return "continue"
        return "bad"

    if isinstance(lhs, int) and isinstance(rhs, list):
        return compare([lhs], rhs)
    if isinstance(lhs, list) and isinstance(rhs, int):
        return compare(lhs, [rhs])


def mergesort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = mergesort(items[:mid])
    right = mergesort(items[mid:])

    merged = []
    leftIndex, rightIndex = 0, 0
    while leftIndex < len(left) and rightIndex < len(right):
        if compare(left[leftIndex], right[rightIndex]) == "good":
            merged.append(left[leftIndex])
            leftIndex += 1
        else:
            merged.append(right[rightIndex])
            rightIndex += 1

    while leftIndex < len(left):
        merged.append(left[leftIndex])
        leftIndex += 1

    while rightIndex < len(right):
        merged.append(right[rightIndex])
        rightIndex += 1

    return merged


total = 0
for index, pair in enumerate(textPairs):
    if compare(pair[0], pair[1]) == "good":
        total += index + 1
print("Question 1:", total)

combined = [[[2]], [[6]]]
for pair in textPairs:
    combined.append(pair[0])
    combined.append(pair[1])

combined = mergesort(combined)
print("Question 2:", (combined.index([[2]]) + 1) * (combined.index([[6]]) + 1))

print("\nOne-Line Algorithms")


def compareMini(lhs, rhs):
    return ["continue", "good", "bad"][(lhs < rhs) + 2 * (lhs > rhs)] if isinstance(lhs, int) and isinstance(rhs, int) else next((compareMini(left, right) for left, right in zip(lhs, rhs) if compareMini(left, right) != "continue"), ["continue", "good", "bad"][(len(lhs) < len(rhs)) + 2 * (len(lhs) > len(rhs))]) if isinstance(lhs, list) and isinstance(rhs, list) else compareMini([lhs] if isinstance(lhs, int) else lhs, [rhs] if isinstance(rhs, int) else rhs)


def mergesortMini(items):
    return items if len(items) <= 1 else next((([tmp[0].pop(0) if compareMini(tmp[0][0], tmp[1][0]) == "good" else tmp[1].pop(0) for _ in range(len(tmp[0]) + len(tmp[1])) if len(tmp[0]) > 0 and len(tmp[1]) > 0] + tmp[0] + tmp[1]) for tmp in [[mergesortMini(items[:len(items) // 2]), mergesortMini(items[len(items) // 2:])]]))


solutionObject = {"compare": lambda lhs, rhs: ["continue", "good", "bad"][(lhs < rhs) + 2 * (lhs > rhs)] if isinstance(lhs, int) and isinstance(rhs, int) else next((solutionObject["compare"](left, right) for left, right in zip(lhs, rhs) if solutionObject["compare"](left, right) != "continue"), ["continue", "good", "bad"][(len(lhs) < len(rhs)) + 2 * (len(lhs) > len(rhs))]) if isinstance(lhs, list) and isinstance(rhs, list) else solutionObject["compare"]([lhs] if isinstance(lhs, int) else lhs,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                         [rhs] if isinstance(rhs, int) else rhs),
                  "mergesort": lambda items: items if len(items) <= 1 else next((([tmp[0].pop(0) if solutionObject["compare"](tmp[0][0], tmp[1][0]) == "good" else tmp[1].pop(0) for _ in range(len(tmp[0]) + len(tmp[1])) if len(tmp[0]) > 0 and len(tmp[1]) > 0] + tmp[0] + tmp[1]) for tmp in [[solutionObject["mergesort"](items[:len(items) // 2]), solutionObject["mergesort"](items[len(items) // 2:])]]))}

total = 0
for index, pair in enumerate(textPairs):
    if solutionObject["compare"](pair[0], pair[1]) == "good":
        total += index + 1
print("Question 1 (Mini):", total)

combined = [[[2]], [[6]]] + [first for first, _ in textPairs] + [second for _, second in textPairs]

combined = solutionObject["mergesort"](combined)
print("Question 2 (mini):", (combined.index([[2]]) + 1) * (combined.index([[6]]) + 1))

print(mergesortMini([3, 2, 1]))
print(solutionObject["mergesort"]([3, 2, 1]))

#
#
#
#

print("\nOne-Line Solutions")


def compareMini(lhs, rhs):
    return ["continue", "good", "bad"][(lhs < rhs) + 2 * (lhs > rhs)] if isinstance(lhs, int) and isinstance(rhs, int) else next((compareMini(left, right) for left, right in zip(lhs, rhs) if compareMini(left, right) != "continue"), ["continue", "good", "bad"][(len(lhs) < len(rhs)) + 2 * (len(lhs) > len(rhs))]) if isinstance(lhs, list) and isinstance(rhs, list) else compareMini([lhs] if isinstance(lhs, int) else lhs, [rhs] if isinstance(rhs, int) else rhs)


def mergesortMini(items):
    return items if len(items) <= 1 else next((([tmp[0].pop(0) if compareMini(tmp[0][0], tmp[1][0]) == "good" else tmp[1].pop(0) for _ in range(len(tmp[0]) + len(tmp[1])) if len(tmp[0]) > 0 and len(tmp[1]) > 0] + tmp[0] + tmp[1]) for tmp in [[mergesortMini(items[:len(items) // 2]), mergesortMini(items[len(items) // 2:])]]))


solutionObject = {"compare": lambda lhs, rhs: ["continue", "good", "bad"][(lhs < rhs) + 2 * (lhs > rhs)] if isinstance(lhs, int) and isinstance(rhs, int) else next((solutionObject["compare"](left, right) for left, right in zip(lhs, rhs) if solutionObject["compare"](left, right) != "continue"), ["continue", "good", "bad"][(len(lhs) < len(rhs)) + 2 * (len(lhs) > len(rhs))]) if isinstance(lhs, list) and isinstance(rhs, list) else solutionObject["compare"]([lhs] if isinstance(lhs, int) else lhs,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                         [rhs] if isinstance(rhs, int) else rhs),
                  "mergesort": lambda items: items if len(items) <= 1 else next((([tmp[0].pop(0) if solutionObject["compare"](tmp[0][0], tmp[1][0]) == "good" else tmp[1].pop(0) for _ in range(len(tmp[0]) + len(tmp[1])) if len(tmp[0]) > 0 and len(tmp[1]) > 0] + tmp[0] + tmp[1]) for tmp in [[solutionObject["mergesort"](items[:len(items) // 2]), solutionObject["mergesort"](items[len(items) // 2:])]]))}

print("Question 1 (Mini):", sum(index + 1 for index, pair in enumerate(textPairs) if solutionObject["compare"](pair[0], pair[1]) == "good"))
print("Question 2 (mini):", math.prod([index + 1 for index, value in enumerate(solutionObject["mergesort"]([[[2]], [[6]]] + [first for first, _ in textPairs] + [second for _, second in textPairs])) if value in [[[2]], [[6]]]]))

print([[sum(index + 1 for index, pair in enumerate(textPairs) if soln["compare"](pair[0], pair[1]) == "good"), math.prod([index + 1 for index, value in enumerate(soln["mergesort"]([[[2]], [[6]]] + [first for first, _ in textPairs] + [second for _, second in textPairs])) if value in [[[2]], [[6]]]])] for soln in [
    {"compare": lambda lhs, rhs: ["continue", "good", "bad"][(lhs < rhs) + 2 * (lhs > rhs)] if isinstance(lhs, int) and isinstance(rhs, int) else next((soln["compare"](left, right) for left, right in zip(lhs, rhs) if soln["compare"](left, right) != "continue"), ["continue", "good", "bad"][(len(lhs) < len(rhs)) + 2 * (len(lhs) > len(rhs))]) if isinstance(lhs, list) and isinstance(rhs, list) else soln["compare"]([lhs] if isinstance(lhs, int) else lhs, [rhs] if isinstance(rhs, int) else rhs),
     "mergesort": lambda items: items if len(items) <= 1 else next((([tmp[0].pop(0) if soln["compare"](tmp[0][0], tmp[1][0]) == "good" else tmp[1].pop(0) for _ in range(len(tmp[0]) + len(tmp[1])) if len(tmp[0]) > 0 and len(tmp[1]) > 0] + tmp[0] + tmp[1]) for tmp in [[soln["mergesort"](items[:len(items) // 2]), soln["mergesort"](items[len(items) // 2:])]]))}]][0])

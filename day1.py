def fileRead():
    elves = [[]]
    with open("inputs/day1.txt", "r") as file:
        for line in file:
            if line == "\n":
                elves.append([])
            else:
                elves[-1].append(int(line.strip().lower()))

    return elves


def calorieCount(elves):
    return [sum(elf) for elf in elves]


elves = fileRead()
calories = calorieCount(elves)
print(calories[calories.index(max(calories))])

total = 0
for i in range(3):
    index = calories.index(max(calories))
    total += calories.pop(index)

print(total)

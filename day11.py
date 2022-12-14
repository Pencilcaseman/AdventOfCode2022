import tqdm
from functools import reduce


class Monkey:
    def __init__(self, configStr: list[str]):
        self.number = int(configStr[0][:-1].split()[1])
        self.items = list(map(int, configStr[1].split(":")[1].split(",")))
        self.operation = configStr[2].split("=")[-1].strip()
        self.test = int(configStr[3].split()[-1])
        self.branches = [-1, -1]
        self.branches[0] = int(configStr[4].split()[-1])
        self.branches[1] = int(configStr[5].split()[-1])
        self.inspectCount = 0

    def __str__(self):
        return f"""Monkey {self.number}
    Items: {self.items}
    Operation: {self.operation}
    Test: Divisible by {self.test}
        If True: Throw to Monkey {self.branches[0]}
        If False: Throw to Monkey {self.branches[1]}
    Inspected Items: {self.inspectCount}
        """

    def __repr__(self):
        return f"Monkey {self.number}"


def parseIterable(lines):
    monkeys = []
    monkey = []
    for line in lines:
        if line.strip() == "":
            monkeys.append(monkey[:])
            monkey = []
        else:
            monkey.append(line.strip())
    monkeys.append(monkey)
    return monkeys


def readFile():
    with open("inputs/day11.txt", "r") as file:
        return parseIterable(file)


def monkeyMix(monkeysOriginal, rounds):
    monkeys = monkeysOriginal[:]
    for _ in range(rounds):
        for monkey in monkeys:
            for item in monkey.items:
                monkey.inspectCount += 1
                old = item
                new = eval(monkey.operation)
                new //= 3
                if new % monkey.test == 0:
                    monkeys[monkey.branches[0]].items.append(new)
                else:
                    monkeys[monkey.branches[1]].items.append(new)
            monkey.items = []

    return monkeys


def monkeyMix2(monkeysOriginal, rounds, mod):
    keys = monkeysOriginal[:]
    for i in tqdm.tqdm(range(rounds)):
        for monkey in keys:
            for item in monkey.items:
                monkey.inspectCount += 1
                old = item
                new = eval(monkey.operation)
                new %= mod  # 96577  # 9699690
                if new % monkey.test == 0:
                    keys[monkey.branches[0]].items.append(new)
                else:
                    keys[monkey.branches[1]].items.append(new)
            monkey.items = []

    return keys


mode = "data"
if mode == "data":
    monkeys = readFile()
elif mode == "sample":
    monkeys = parseIterable("""Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""".split("\n"))
else:
    raise ValueError(f"Invalid mode: {mode}")

monkeys = list(map(Monkey, monkeys))
print(monkeys)

old = 123
print(eval("old * 5"))

# Question 1
if False:
    postMix = monkeyMix(monkeys, 20)
    for item in postMix:
        print(item)

    counts = [monkey.inspectCount for monkey in postMix]
    print(counts)
    max1 = max(counts)
    counts.remove(max1)
    max2 = max(counts)
    print("Monkey Business:", max1 * max2)

# Question 2
mod = reduce(lambda x, y: x * y, [monkey.test for monkey in monkeys])
postMix = monkeyMix2(monkeys, 10000, mod)
for item in postMix:
    print(item)

counts = [monkey.inspectCount for monkey in postMix]
print(counts)
max1 = max(counts)
counts.remove(max1)
max2 = max(counts)
print("Monkey Business:", max1 * max2)

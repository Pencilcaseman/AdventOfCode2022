def readFile():
    out = []
    with open("inputs/day10.txt", "r") as file:
        for line in file:
            out.append(line.strip())
    return out


def cpuSim(proc):
    x = 1
    cir = 0
    tick = 1
    startOp = tick
    opTicks = 0
    signalStrength = 0

    while True:
        # print(f"Tick {tick}  |  Register Value: {x}    ({startOp}, {opTicks})")

        if (tick - 20) % 40 == 0:
            signalStrength += x * tick
            print(f"Signal Strength at Tick {tick}: {x * tick}")

        if tick == startOp + opTicks:
            # Process existing instruction
            if proc[cir] == "noop":
                pass
            elif proc[cir].startswith("addx"):
                x += int(proc[cir].split()[1])

            # Process New Instruction
            cir += 1
            if cir == len(proc):
                break

            startOp = tick
            if proc[cir] == "noop":
                opTicks = 1
            elif proc[cir].startswith("addx"):
                opTicks = 2
            else:
                raise ValueError("Invalid Instruction: " + proc[cir])

        tick += 1

    print(f"Tick {tick}  |  Register Value: {x}    ({startOp}, {opTicks})")

    return signalStrength


def cpuSim2(proc):
    x = 1
    cir = 0
    tick = 1
    startOp = tick
    opTicks = 0

    while True:
        if tick % 40 == 0:
            print()

        if abs(((tick - 1) % 40) - x) < 2:
            print("█", end="")
        else:
            print(" ", end="")

        if tick == startOp + opTicks:
            # Process existing instruction
            if proc[cir] == "noop":
                pass
            elif proc[cir].startswith("addx"):
                x += int(proc[cir].split()[1])

            # Process New Instruction
            cir += 1
            if cir == len(proc):
                break

            startOp = tick
            if proc[cir] == "noop":
                opTicks = 1
            elif proc[cir].startswith("addx"):
                opTicks = 2
            else:
                raise ValueError("Invalid Instruction: " + proc[cir])

        tick += 1


mode = "data"
if mode == "data":
    data = readFile()
elif mode == "sample":
    data = [
        "addx 15",
        "addx -11",
        "addx 6",
        "addx -3",
        "addx 5",
        "addx -1",
        "addx -8",
        "addx 13",
        "addx 4",
        "noop",
        "addx -1",
        "addx 5",
        "addx -1",
        "addx 5",
        "addx -1",
        "addx 5",
        "addx -1",
        "addx 5",
        "addx -1",
        "addx -35",
        "addx 1",
        "addx 24",
        "addx -19",
        "addx 1",
        "addx 16",
        "addx -11",
        "noop",
        "noop",
        "addx 21",
        "addx -15",
        "noop",
        "noop",
        "addx -3",
        "addx 9",
        "addx 1",
        "addx -3",
        "addx 8",
        "addx 1",
        "addx 5",
        "noop",
        "noop",
        "noop",
        "noop",
        "noop",
        "addx -36",
        "noop",
        "addx 1",
        "addx 7",
        "noop",
        "noop",
        "noop",
        "addx 2",
        "addx 6",
        "noop",
        "noop",
        "noop",
        "noop",
        "noop",
        "addx 1",
        "noop",
        "noop",
        "addx 7",
        "addx 1",
        "noop",
        "addx -13",
        "addx 13",
        "addx 7",
        "noop",
        "addx 1",
        "addx -33",
        "noop",
        "noop",
        "noop",
        "addx 2",
        "noop",
        "noop",
        "noop",
        "addx 8",
        "noop",
        "addx -1",
        "addx 2",
        "addx 1",
        "noop",
        "addx 17",
        "addx -9",
        "addx 1",
        "addx 1",
        "addx -3",
        "addx 11",
        "noop",
        "noop",
        "addx 1",
        "noop",
        "addx 1",
        "noop",
        "noop",
        "addx -13",
        "addx -19",
        "addx 1",
        "addx 3",
        "addx 26",
        "addx -30",
        "addx 12",
        "addx -1",
        "addx 3",
        "addx 1",
        "noop",
        "noop",
        "noop",
        "addx -9",
        "addx 18",
        "addx 1",
        "addx 2",
        "noop",
        "noop",
        "addx 9",
        "noop",
        "noop",
        "noop",
        "addx -1",
        "addx 2",
        "addx -37",
        "addx 1",
        "addx 3",
        "noop",
        "addx 15",
        "addx -21",
        "addx 22",
        "addx -6",
        "addx 1",
        "noop",
        "addx 2",
        "addx 1",
        "noop",
        "addx -10",
        "noop",
        "noop",
        "addx 20",
        "addx 1",
        "addx 2",
        "addx 2",
        "addx -6",
        "addx -11",
        "noop",
        "noop",
        "noop",
    ]
elif mode == "test":
    data = ["noop", "addx 3", "addx -5", "addx 11", "noop", "addx 5"]
else:
    raise ValueError("Invalid Mode")

print(data)

sig = cpuSim(data)
print(sig)

cpuSim2(data)

def readFile():
    with open("inputs/day6.txt", "r") as file:
        return file.read()


def findStartOfPacket(signal, n):
    for i in range(len(signal)):
        if len(set(signal[i: i + n])) == n:
            return i + n
    return None


signal = readFile()
print(signal)
print(findStartOfPacket(signal, 14))

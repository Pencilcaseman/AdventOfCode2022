def readFile():
    pairs = []
    with open("inputs/day2.txt", "r") as file:
        for line in file:
            split = line.split()
            pairs.append((split[0], split[1]))

    return pairs


def score(p1, p2):
    scores = {
        "A": 1,  # Rock
        "B": 2,  # Paper
        "C": 3,  # Scissors
        "X": 1,  # Rock
        "Y": 2,  # Paper
        "Z": 3,  # Scissors
    }

    p1Score = scores[p1]
    p2Score = scores[p2]

    playerScore = p2Score

    # Check the winner
    if p1Score == p2Score:
        playerScore += 3
    elif p1Score == 1 and p2Score == 2:
        playerScore += 6
    elif p1Score == 2 and p2Score == 3:
        playerScore += 6
    elif p1Score == 3 and p2Score == 1:
        playerScore += 6

    print(p1, p2, "=>", playerScore)

    return playerScore


def scorePart2(p1, wld):
    scores = {
        "A": 1,  # Rock
        "B": 2,  # Paper
        "C": 3,  # Scissors
        "X": 0,  # Rock
        "Y": 3,  # Paper
        "Z": 6,  # Scissors
    }

    playerScore = scores[wld]

    # Calculate the winning move
    if wld == "X":  # Lose
        playerScore += (scores[p1] - 1 + 2) % 3 + 1
    elif wld == "Y":  # Draw
        playerScore += scores[p1]
    elif wld == "Z":  # Win
        playerScore += (scores[p1] - 1 + 1) % 3 + 1

    return playerScore


print(readFile())
# pairs = [("A", "Y"), ("B", "X"), ("C", "Z")]
pairs = readFile()
print(sum([scorePart2(p1, p2) for p1, p2 in pairs]))

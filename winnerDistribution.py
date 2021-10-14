import gameClass

playerCount = 5
tokenCount = 1

winnerDistribution = [0] * playerCount

for i in range(50000):
    tempWinner = gameClass.game(playerCount, tokenCount).runGame()[3]
    winnerDistribution[tempWinner] += 1

print(winnerDistribution)

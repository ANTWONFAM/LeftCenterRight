import gameClass

playerCount = 5
tokenCount = 1

winnerDistribution = [0] * playerCount

for i in range(50000):
    tempGame = gameClass.game(playerCount, tokenCount)
    tempGame.gameState([0, 1, 1])  # overrides the values above
    tempWinner = tempGame.runGame()[3]
    winnerDistribution[tempWinner] += 1

print(winnerDistribution)

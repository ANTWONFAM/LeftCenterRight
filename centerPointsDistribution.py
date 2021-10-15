import gameClass

playerCount = 5
tokenCount = 1

centerPointsDistribution = [0] * (playerCount*tokenCount)

for i in range(100):
    tempGame = gameClass.game(playerCount, tokenCount)
    tempGame.setGameState([0, 1, 1])  # overrides the values above
    tempCenterPoints = tempGame.runGame()[1]
    centerPointsDistribution[tempCenterPoints] += 1

print(centerPointsDistribution)

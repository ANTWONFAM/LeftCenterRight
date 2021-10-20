import gameClass
from matplotlib import pyplot as plt

playerCount = 5
tokenCount = 1

centerPointsDistribution = [0] * (playerCount * tokenCount)
xAxis = centerPointsDistribution.copy()
for i in range(10000):
    tempGame = gameClass.game(playerCount, tokenCount)
    # tempGame.setGameState([0, 1, 1])  # overrides the values above
    tempCenterPoints = tempGame.runGame()[1]
    centerPointsDistribution[tempCenterPoints] += 1

for i in range(len(centerPointsDistribution)):
    xAxis[i] = i
print(centerPointsDistribution)
plt.bar(xAxis, centerPointsDistribution, 0.8)
plt.show()
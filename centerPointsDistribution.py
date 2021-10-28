import gameClass
from matplotlib import pyplot as plt

playerCount = 3
tokenCount = 3
gameNumber = 100000

centerPointsDistribution = [0] * (playerCount * tokenCount)
xAxis = centerPointsDistribution.copy()
for i in range(gameNumber):
    if i % 10000 == 0:
        print(i)
    tempGame = gameClass.game(playerCount, tokenCount)
    # tempGame.setGameState([1, 1, 1])  # overrides the values above
    tempCenterPoints = tempGame.runGame()[1]
    centerPointsDistribution[tempCenterPoints] += 1

for i in range(len(centerPointsDistribution)):
    xAxis[i] = i
print(centerPointsDistribution)
plt.bar(xAxis, centerPointsDistribution, 0.5)
plt.xlim(-0.5, 8.5)
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8])
plt.show()
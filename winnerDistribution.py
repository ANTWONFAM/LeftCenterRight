import gameClass
from matplotlib import pyplot as plt
import copy

playerCount = 7
tokenCount = 5

winnerDistribution = [0] * playerCount
lengthDistribution = [0] * 1000
for i in range(50000):
    tempGame = gameClass.game(playerCount, tokenCount)
    # tempGame.setGameState([1, 1, 1])  # overrides the values above
    tempData = tempGame.runGame()
    winnerDistribution[tempData[3]] += 1
    lengthDistribution[tempData[0]] += 1


print(winnerDistribution)
print(lengthDistribution)
#
# xAxis = []
# for x in range(1000):
#     xAxis.append(x+1)
#
# templist = copy.deepcopy(lengthDistribution)
#
# for i in range(len(lengthDistribution)):
#     if lengthDistribution[i] == 0:
#         xAxis.pop(i)
#
# lengthDistribution.remove(0)
# plt.scatter(xAxis,lengthDistribution)
# plt.show()
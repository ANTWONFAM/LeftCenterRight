import gameClass
from matplotlib import pyplot as plt
import copy
import collections

playerCount = 10
tokenCount = 1

rawLen = []
rawWin = []
gameNumber = 50000


for i in range(gameNumber):
    tempGame = gameClass.game(playerCount, tokenCount)
    # tempGame.setGameState([1, 1, 1])  # overrides the values above
    tempData = tempGame.runGame()
    rawWin.append(tempData[3])
    rawLen.append(tempData[0])

rawLen = collections.Counter(rawLen)
rawWin = collections.Counter(rawWin)

print (rawWin)

plt.scatter(rawLen.keys(),rawLen.values(),marker='.')
plt.xlabel('Number of Turns')
plt.ylabel('Amount of Games')
plt.show()


winPercent = []
for i in rawWin.keys():
    winPercent.append(rawWin[i]*100/gameNumber)

plt.scatter(rawWin.keys(), winPercent, marker = '.')
plt.ylabel('Win Percent')
plt.xlabel('Player #')
plt.show()
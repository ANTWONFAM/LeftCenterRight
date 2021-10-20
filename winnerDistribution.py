import gameClass
from matplotlib import pyplot as plt
import collections

playerCount = 10
tokenCount = 1
gameNumber = 1000000

def winnerDist():
    rawLen = []
    rawWin = []
    for i in range(gameNumber):
        tempGame = gameClass.game(playerCount, tokenCount)
        # tempGame.setGameState([1, 1, 1])  # overrides the values above
        tempData = tempGame.runGame()
        rawWin.append(tempData[3])
        rawLen.append(tempData[0])

    rawLen = collections.Counter(rawLen)
    rawWin = collections.Counter(rawWin)
    print (rawWin)
    return [list(rawLen.keys()),list(rawLen.values()),list(rawWin.keys()),list(rawWin.values()),rawLen,rawWin]




if __name__ == '__main__':
    lenX, lenY, winX, winY, _, _ = winnerDist()
    plt.scatter(lenX, lenY, marker='.')
    plt.xlabel('Number of Turns')
    plt.ylabel('Amount of Games')
    plt.show()

    print(type(lenX),type(lenY),type(winX),type(winY))
    print(winX)
    print(winY)
    winPercent = []
    for i in range(len(winX)):
        winPercent.append((winY[i] * 100) / gameNumber)
    print(winPercent)

    plt.scatter(winX, winPercent, marker='.')
    plt.ylabel('Win Percent')
    plt.xlabel('Player #')
    plt.show()

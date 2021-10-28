import gameClass
from matplotlib import pyplot as plt
import collections

playerCount = 40
tokenCount = 1
gameNumber = 10000000


def winnerDist(gameNo = False):
    if gameNo is True:
        return gameNumber
    rawLen = []
    rawWin = []
    for i in range(gameNumber):
        if i % 10000 == 0:
            print(i)
        tempGame = gameClass.game(playerCount, tokenCount)
        # tempGame.setGameState([1, 1, 0])  # overrides the values above
        tempData = tempGame.runGame()
        rawWin.append(tempData[3])
        rawLen.append(tempData[0])

    rawLen = collections.Counter(rawLen)
    rawWin = collections.Counter(rawWin)
    print(rawWin)
    return [list(rawLen.keys()), list(rawLen.values()), list(rawWin.keys()), list(rawWin.values()), rawLen, rawWin]


if __name__ == '__main__':
    lenX, lenY, winX, winY, _, _ = winnerDist()

    print(type(lenX), type(lenY), type(winX), type(winY))
    print(winX)
    print(winY)
    winPercent = []
    for i in range(len(winX)):
        winPercent.append((winY[i] * 100) / gameNumber)
    print(winPercent)

    plt.scatter(lenX, lenY, marker='.')
    plt.xlabel('Number of Turns')
    plt.ylabel('Amount of Games')
    plt.show()

    plt.scatter(winX, winPercent, 25, 'red')
    # plt.ylim([25, 50])
    plt.ylabel('Win Percent')
    plt.xlabel('Player #')
    plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40])
    plt.grid(True, 'both', 'y')
    plt.show()

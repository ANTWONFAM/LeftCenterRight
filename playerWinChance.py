from scipy import optimize
from numpy import arange
from matplotlib import pyplot as plt
import gameClass
import math
import collections

playerCount = 3
tokenCount = 1
gameNumber = 1000000


#normal distribution
def yEstN(R, s, m):
    first = 1/(s*math.sqrt(2*3.14))
    second = (-.5)*(((R-m)/s)**2)
    return first*(2.7**second)

def playerWinChance():
    rawLen = []
    rawWin = []
    playerWinTrack = []
    for player in range(playerCount):
        playerWinTrack.append([])
    for i in range(gameNumber):
        if i % 10000 == 0:
            print(i)
        tempGame = gameClass.game(playerCount, tokenCount)
        tempGame.setGameState([1, 1, 0])  # overrides the values above
        tempData = tempGame.runGame()
        # print (tempData[3],tempData[0])
        playerWinTrack[tempData[3]].append(tempData[0])
        # print(playerWinTrack)
        rawWin.append(tempData[3])
        rawLen.append(tempData[0])

    rawLen = collections.Counter(rawLen)
    rawWin = collections.Counter(rawWin)

    for i in range(len(playerWinTrack)):
        print(i)
        playerWinTrack[i] = collections.Counter(playerWinTrack[i])
        tempX = list(playerWinTrack[i].keys())
        tempY = list(playerWinTrack[i].values())
        total = sum(tempY)
        for j in range(len(tempY)):
            tempY[j] = tempY[j]/total

        popt, _ = optimize.curve_fit(yEstN, tempX, tempY, p0=[10, 50])
        s, m = popt
        print(s, m)
        x_line = arange(min(tempX), max(tempX), .1)
        y_line = yEstN(x_line, s, m)
        plt.plot(x_line, y_line, label='Player '+str(int(i))+' Normal Distribution\nσ = %.5f\nμ = %.5f' % (s, m))
        #plt.scatter(tempX, tempY, label='Player ' + str(int(i)))

        #plt.scatter(playerWinTrack[i].keys(),playerWinTrack[i].values(),label='Player ' + str(int(i)))

    plt.legend()
    plt.show()

    return [
        list(rawLen.keys()), list(rawLen.values()), list(rawWin.keys()), list(rawWin.values()), rawLen, rawWin]


if __name__ == '__main__':
    playerWinChance()


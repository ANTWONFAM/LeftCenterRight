import winnerDistribution
from scipy import optimize
from numpy import arange
from matplotlib import pyplot as plt
import gameClass
import winnerDistribution
import math
import numpy as np

#polynomial functions with variable R
def yEst1(R, a, b):
    return a*R+b
def yEst3(R, d, e, f, g):
    return d*(R**3)+e*(R**2)+f*R+g
#6th degree polynomial function
def yEst6(R,a,b,c,d,e,f,g):
    return a*(R**6)+b*(R**5)+c*(R**4)+d*(R**3)+e*(R**2)+f*R+g
#5th degree polynomial function
def yEst5(R,c,d,e,f,g):
    return c*(R**4)+d*(R**3)+e*(R**2)+f*R+g
#10th degree polynomial function
def yEst10(R,a,b,c,d,e,f,g,h,i,j,k):
    return h*(R**10)+i*(R**9)+j*(R**8)+k*(R**7)+a*(R**6)+b*(R**5)+c*(R**4)+d*(R**3)+e*(R**2)+f*R+g
#normal distribution
def yEstN(R, s, m):
    first = 1/(s*math.sqrt(2*3.14))
    second = (-.5)*(((R-m)/s)**2)
    return first*(2.7**second)

def probDist():
    gameNo = 100000
    for i in range(5):
        lenX, lenY, winX, winY, rawLen, rawWin = winnerDistribution.winnerDist(pC=i+3,tC=3,gN=gameNo)
        gameNo = winnerDistribution.winnerDist(gameNo=True)

        lenX.sort()
        lenY = []

        for j in lenX:
            lenY.append(rawLen[j]/gameNo)

        popt, _ = optimize.curve_fit(yEstN, lenX, lenY, p0=[10,50])
        s,m = popt
        print(s,m)
        x_line = arange(min(lenX), max(lenX), 1)
        y_line = yEstN(x_line, s, m)
        plt.plot(x_line, y_line, label='Player Number = '+str(i+3)+'\nσ = %.5f\nμ = %.5f' % (s, m))


    plt.ylabel('Percentage of Games')
    plt.xlabel('Game Length')
    #plt.scatter(lenX, lenY, color='green', marker='.')
    plt.legend()
    plt.show()

    # cumSum = np.cumsum(y_line)
    # cumSumScatter = np.cumsum(lenY)
    # plt.plot(x_line,cumSum, label='Cumulative Sum')
    # plt.scatter(lenX, lenY, color='green', marker='.')
    # plt.scatter(lenX, cumSumScatter, marker='.',color='red')
    # plt.xlabel("Game Length")
    # plt.ylabel("Percentage of Games")
    # plt.legend()
    # plt.show()

def testCase():
    x_line = arange(0, 350, 1)
    y_line = yEstN(x_line, 10, 50)
    plt.plot(x_line, y_line, color='blue', label='normal distribution')

    plt.show()


if __name__ == "__main__":
    # testCase()
    probDist()
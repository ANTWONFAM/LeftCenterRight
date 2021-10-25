from scipy import optimize
from numpy import arange
from matplotlib import pyplot as plt
import gameClass
import winnerDistribution
import math

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



def curveFit():
    lenX, lenY, winX, winY, rawLen, rawWin = winnerDistribution.winnerDist()

    lenX.sort()
    lenY = []

    for i in lenX:
        lenY.append(rawLen[i])

    winX.sort()
    winY = []

    for i in winX:
        winY.append(rawWin[i])

    # plt.scatter(lenX, lenY, color='green')
    # plt.show()

    # linear regression
    popt, _ = optimize.curve_fit(yEst1, lenX, lenY)
    a, b = popt
    print('y = %.5f * x + %.5f' % (a, b))
    x_line = arange(min(lenX), max(lenX), 1)
    y_line = yEst1(x_line, a,b)
    plt.plot(x_line, y_line, color='blue', label='1st Degree Estimation')

    # polynomial 3rd degree fit
    popt, _ = optimize.curve_fit(yEst3, lenX, lenY)
    a, b, c, d = popt
    print('y = %.5f * x^3 + %.5f * x^2 + %.5f * x + %.5f' % (a, b, c, d))
    x_line = arange(min(lenX), max(lenX), 1)
    y_line = yEst3(x_line, a, b, c, d)
    plt.plot(x_line, y_line, color='green', label='3rd Degree Estimation')

    # # normal fit
    # popt, _ = optimize.curve_fit(yEstN, lenX, lenY)
    # s, m = popt
    # print('%.5f  %.5f' % (s, m))
    # x_line = arange(min(lenX), max(lenX), 1)
    # y_line = yEstN(x_line, s,m)
    # plt.plot(x_line, y_line, color='red', label='Normal Estimation')

    # # least square fit using 6th degree polynomial
    # popt, _ = optimize.curve_fit(yEst6, lenX, lenY)
    # a, b, c, d, e, f, g = popt
    # print('y = %.5f * x^6 + %.5f * x^5 + %.5f * x^4 + %.5f * x^3 + %.5f * x^2 + %.5f * x + %.5f' % (a, b,c,d,e,f,g))
    # x_line = arange(min(lenX), max(lenX), 1)
    # y_line = yEst6(x_line, a,b,c,d,e,f,g)
    # plt.plot(x_line, y_line, color='red', label='6th Degree Estimation')

    # # least square fit using 10th degree polynomial
    # popt, _ = optimize.curve_fit(yEst10, lenX, lenY)
    # a, b, c, d, e, f, g, h,i,j,k= popt
    # print('y = %.5f * x^10 + %.5f * x^9 + %.5f * x^8 + %.5f * x^7 + %.5f * x^6 + %.5f * x^5 + %.5f * x^4 + %.5f * '
    #       'x^3 + %.5f * x^2 + %.5f * x + %.5f' % (a,b,c,d,e,f,g,h,i,j,k))
    # x_line = arange(min(lenX), max(lenX), 1)
    # y_line = yEst10(x_line,a,b,c,d,e,f,g,h,i,j,k)
    # plt.plot(x_line, y_line, color='blue', label='10th Degree Estimation')


    # scatter plot of data
    plt.scatter(lenX, lenY, color='green')

    plt.legend()
    plt.show()

    # linear regression
    popt, _ = optimize.curve_fit(yEst1, winX, winY)
    a, b = popt
    print('y = %.5f * x + %.5f' % (a, b))
    x_line = arange(min(winX), max(winX), 0.2)
    y_line = yEst1(x_line, a,b)
    plt.plot(x_line, y_line, color='blue', label='1st Degree Estimation')

    # polynomial 3rd degree fit
    popt, _ = optimize.curve_fit(yEst3, winX, winY)
    a, b, c, d = popt
    print('y = %.5f * x^3 + %.5f * x^2 + %.5f * x + %.5f' % (a, b, c, d))
    x_line = arange(min(winX), max(winX), 0.2)
    y_line = yEst3(x_line, a, b, c, d)
    plt.plot(x_line, y_line, color='green', label='3rd Degree Estimation')
    #
    # # least square fit using 6th degree polynomial
    # popt, _ = optimize.curve_fit(yEst6, winX, winY)
    # a, b, c, d, e, f, g = popt
    # print('y = %.5f * x^6 + %.5f * x^5 + %.5f * x^4 + %.5f * x^3 + %.5f * x^2 + %.5f * x + %.5f' % (a, b,c,d,e,f,g))
    # x_line = arange(min(winX), max(winX), 0.2)
    # y_line = yEst6(x_line, a,b,c,d,e,f,g)
    # plt.plot(x_line, y_line, color='red', label='6th Degree Estimation')

    # scatter plot of data
    plt.scatter(winX, winY, color='green')

    plt.legend()
    plt.show()



if __name__ == '__main__':
    curveFit()
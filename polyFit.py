from scipy import optimize
from numpy import arange
from matplotlib import pyplot as plt
import gameClass
import winnerDistribution

#polynomial functions with variable R
#6th degree polynomial function
def yEst6(R,a,b,c,d,e,f,g):
    return a*(R**6)+b*(R**5)+c*(R**4)+d*(R**3)+e*(R**2)+f*R+g
#5th degree polynomial function
def yEst5(R,c,d,e,f,g):
    return c*(R**4)+d*(R**3)+e*(R**2)+f*R+g
#10th degree polynomial function
def yEst10(R,a,b,c,d,e,f,g,h,i,j,k):
    return h*(R**10)+i*(R**9)+j*(R**8)+k*(R**7)+a*(R**6)+b*(R**5)+c*(R**4)+d*(R**3)+e*(R**2)+f*R+g



def curveFit():
    lenX, lenY, winX, winY, rawLen, rawWin = winnerDistribution.winnerDist()

    lenX.sort()
    lenY = []

    for i in lenX:
        lenY.append(rawLen[i])

    plt.scatter(lenX, lenY, color='green')
    plt.show()

    # least square fit using 6th degree polynomial
    popt, _ = optimize.curve_fit(yEst6, lenX, lenY)
    a, b, c, d, e, f, g = popt
    print('y = %.5f * x^6 + %.5f * x^5 + %.5f * x^4 + %.5f * x^3 + %.5f * x^2 + %.5f * x + %.5f' % (a, b,c,d,e,f,g))
    x_line = arange(min(lenX), max(lenX), 1)
    y_line = yEst6(x_line, a,b,c,d,e,f,g)
    print(x_line)
    print(y_line)
    plt.plot(x_line, y_line, color='red', label='6th Degree Estimation')

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


    plt.show()



if __name__ == '__main__':
    curveFit()
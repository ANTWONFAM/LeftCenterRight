import random
import numpy as np
import math
import collections
from matplotlib import pyplot as plt


class game:
    actions = {0: 'c', 1: 'c', 2: 'c', 3: 's', 4: 'l', 5: 'r'}
    turnCount = 0
    centerPoints = 0
    playerTurn = 0
    winner = None

    # default initiation, comes with player number and start points on each player
    def __init__(self, playerNo, startPoints):
        self.playerNo = playerNo
        self.startPoints = startPoints
        self.board = []  # the list that keeps track of each player and their points
        for i in range(playerNo):
            self.board.append(startPoints)

    # customize the game state, if you wanted a 4p 1v1 situation you can set gameBoard = [1,1,0,0] or [0,2,1,0] etc.
    def gameState(self, gameBoard):
        self.board = gameBoard

    # roll dice, returns an action in the form of a single letter string, see dictionary "actions" above
    def roll(self):
        i = random.randrange(6)
        return self.actions[i]

    # checks gameEnd state of self.board, returns True if game end and False otherwise
    def gameEnd(self):
        temp = 0
        for x in self.board:
            if x != 0:
                temp += 1
                self.winner = self.board.index(x)
            if temp > 1:
                return False
        return True

    def turn(self):
        self.turnCount += 1
        diceCount = 3
        if self.board[self.playerTurn] < 4:
            diceCount = self.board[self.playerTurn]
        for i in range(diceCount):
            temp = self.roll()  # temp var to store roll
            self.turnCount += 1
            if temp == 'c':  # "circle"
                None
            elif temp == 's':  # "star"
                self.board[self.playerTurn] -= 1
                self.centerPoints += 1
            elif temp == 'l':  # "left"
                self.board[self.playerTurn] -= 1
                self.board[self.playerTurn - 1] += 1
            elif temp == 'r':  # "right"
                self.board[self.playerTurn] -= 1
                try:
                    self.board[self.playerTurn + 1] += 1
                except IndexError:
                    self.board[0] += 1
        if self.playerTurn == len(self.board) - 1:
            self.playerTurn = 0
        else:
            self.playerTurn += 1
        print(self.board)

    # modifies the gameBoard such that each player rolls once, you might want to organize this to have multiple rolls
    def round(self):
        for i in range(len(self.board)):  # iteration across the indexes of the board
            self.turnCount += 1
            diceCount = 3
            if self.board[i] < 4:
                diceCount = self.board[i]
            for j in range(diceCount):
                temp = self.roll()  # temp var to store roll
                if temp == 'c':  # "circle"
                    None
                elif temp == 's':  # "star"
                    self.board[i] -= 1
                    self.centerPoints += 1
                elif temp == 'l':  # "left"
                    self.board[i] -= 1
                    self.board[i - 1] += 1
                elif temp == 'r':  # "right"
                    self.board[i] -= 1
                    try:
                        self.board[i + 1] += 1
                    except IndexError:
                        self.board[0] += 1

    # actually runs the game, checks gameEnd state in the beginning, returns the list below
    def runGameWithTracking(self):
        print(self.board)
        while not self.gameEnd():
            self.round()
            print(self.board)
        return [self.turnCount, self.centerPoints, self.board, self.winner]

    def runGame(self):
        while not self.gameEnd():
            self.round()
        return [self.turnCount, self.centerPoints, self.board, self.winner]


if __name__ == "__main__":

    turnRaw = []
    distribution = []

    for i in range(40000):
        turnRaw.append(game(4, 1).runGame()[0])

    turnRaw = collections.Counter(turnRaw)
    turns = turnRaw.keys()
    distribution = turnRaw.values()

    print(len(turns))
    print(len(distribution))

    plt.scatter(turns, distribution, )
    plt.xlabel('Number of Total Turns')
    plt.ylabel('Number of Games')
    plt.table
    plt.title('Turn Number Distribution for 100k Games of 4P1S')
    plt.show()

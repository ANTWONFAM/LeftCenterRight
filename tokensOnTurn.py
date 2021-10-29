import gameClass
from matplotlib import pyplot as plt

playerCount = 20
tokenCount = 1
gameNumber = 1000000
turnToAnalyze = 9

tokenOnPlayerDistribution = [0] * (playerCount * tokenCount)
xAxis = tokenOnPlayerDistribution.copy()
for i in range(gameNumber):
    if i % 10000 == 0:
        print(i)
    tempGame = gameClass.game(playerCount, tokenCount)
    for j in range((turnToAnalyze-1)*playerCount):
        # print(tempGame.playerTurn)
        tempGame.turn()
        # print(tempGame.board)
    # print("Done running previous turns")
    for k in range(playerCount):
        tokenOnPlayerDistribution[tempGame.playerTurn] += tempGame.board[tempGame.playerTurn]
        tempGame.turn()

    # print("Finished running game")

# print(tokenOnPlayerDistribution)
for l in range(playerCount):
    tokenOnPlayerDistribution[l] /= gameNumber
print(tokenOnPlayerDistribution)

plt.scatter([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], tokenOnPlayerDistribution)
plt.xlabel("Player #")
plt.ylabel("Avg# Tokens before 9th Turn")
plt.show()

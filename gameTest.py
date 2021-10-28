import gameClass

game1 = gameClass.game(3, 1)
game1.setGameState([1, 1, 0])
# game1.round()
# game1.round()
# print(game1.runGameWithTracking()[1])

for i in range(1000000):
    if i % 10000 == 0:
        print(i)
    tempGame = gameClass.game(3, 1)
    tempGame.setGameState([1, 1, 0])
    tempData = tempGame.runGame()

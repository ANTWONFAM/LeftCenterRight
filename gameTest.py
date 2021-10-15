import gameClass

game1 = gameClass.game(3, 4)
game1.setGameState([5, 0, 5])
# game1.round()
# game1.round()

print(game1.runGameWithTracking()[3])
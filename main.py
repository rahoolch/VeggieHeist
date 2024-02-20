
from GameEngine import GameEngine

def main():

    game = GameEngine()
    game.initializeGame()
    game.introduction()

    rem_veggies = game.remainingVeggies()

    while rem_veggies >0:

        print(f"Current Score: {game.getScore()}")
        
        game.printField()
        game.moveCaptain()

        rem_veggies = game.remainingVeggies()



if __name__ == '__main__':
    main()
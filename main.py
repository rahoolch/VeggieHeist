
from GameEngine import GameEngine

def main():

    game = GameEngine()
    game.initializeGame()
    game.introduction()

    rem_veggies = game.remainingVeggies()

    while rem_veggies >0:

        print(f"Current Score: {game.getScore()}")
        print(f"Veggies remaining: {rem_veggies}")
        
        game.printField()
        game.moveCaptain()
        game.moveRabbits()

        rem_veggies = game.remainingVeggies()

    game.gameover()
    game.highscore()



if __name__ == '__main__':
    main()
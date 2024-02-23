# Author: Rahul Chandani
# Description: This is a game engine file consisting of classes and methods
# that needs to be imported in the main class to play the game.

import os
import random
import pickle as pkl

from Veggie import Veggie
from Captain import Captain
from Rabit import Rabit



class GameEngine:
    # Initialize the constant variables of the game
    __NUMBER_VEGGIES = 30 # Veggies in the game
    __NUMBER_RABITS = 5 # Rabits to eat veggies

    __HIGHSCORE_FILE = "highscore.data"
    # Save highscores of each player with the initials of the person

    def __init__(self):
        # initializing field and other elements of the game
        self._field = []
        self._rabits = []
        self._captain = None
        self._veggies = []
        self._score = 0
        self._width = 10
        self._height = 10

    def introduction(self):
        # Let's state the rules and other features of the game at the beginning of the game

        print("Veggie Heist Welcomes you!!!!")
        print("The rabits have invaded over your farm \nyou are "
              "required to save as many veggies as possible to \n have the high score"
              "Each veggie has the points listed below. \n Play to get highscore!!!!")
        print("Veggies have points as follows: ")
        for veggie in self._veggies:
            print(veggie)
        print("R represents rabbits and you are the captain V.")
        print("Let's Start")

    
    def initVeggies(self):
        # Initialize a dictionary with value of field size and the points
        # each veggie contains
        filename = 'points.csv'
        # let's check if the file exists or not
        while not os.path.exists(filename):
            input('Write a file with name "points.csv" and press enter')
        

        # Before moving forward let's define a field of size 10x10
        # can make modifications in the size but let's define a general size of 10x10
        dimensions = [10,10]
            
        self._field = [[None for _ in range(self._width)] for _ in range(self._height)] 


        with open(filename) as input_file:
            lines = input_file.readlines()

            for line in lines:
                veggie_code = line.strip().split(',')
                veggie = Veggie(veggie_code[0], veggie_code[1], int(veggie_code[2]))
                self._veggies.append(veggie)


        for _ in range(self.__NUMBER_VEGGIES):
            occupied = True
            while occupied:
                # checking if the location randomly allocated is empty or can we put a veggie there
                x = random.randint(0,self._width-1)
                y = random.randint(0,self._height-1)

                if not self._field[y][x]:
                    self._field[y][x] = random.choice(self._veggies)
                    occupied = False

    def initCaptain(self):
        # Initialize a random position of the captain 'V' to begin the game with.
        occupied = True
        while occupied:
            x = random.randint(0, self._width - 1)
            y = random.randint(0, self._height - 1)
            if self._field[y][x] is None:
                self._captain = Captain(x,y)
                self._field[y][x] = self._captain
                occupied = False

    def initRabits(self):
        # We initially have 5 rabits and we position them anywhere inside the field to roam and eat
        # our veggies which captain needs to protect

        for _ in range(self.__NUMBER_RABITS):
            occupied = True
            while occupied:
                x = random.randint(0,self._width - 1)
                y = random.randint(0,self._height - 1)
                if self._field[y][x] is None:
                    rabit = Rabit(x,y)
                    self._rabits.append(rabit)
                    self._field[y][x] = rabit
                    occupied = False


    def initializeGame(self):
        self.initVeggies()
        self.initCaptain()
        self.initRabits()

    def printField(self):
        # Print the borders and veggies at random positions
        print("#" * (self._width * 2 + 2))
        for row in self._field:
            print("#", end="")
            for item in row:
                if isinstance(item, str):
                    symbol = item
                else:
                    symbol = " " if not item else item.get_symbol()
                print(f"{symbol} ", end="")
            print("#")
        print("#" * (self._width * 2 + 2))

    def movCapVert(self, dir):
        x = self._captain.get_x()
        y = self._captain.get_y() + dir

        # check if the new direction is in the frame or not
        if 0<= y < self._height:
            # check if there is any veggie at new position
            if isinstance(self._field[y][x],Veggie):
                veggie = self._field[y][x]
                print(f"Wow you got a {veggie.get_name()}")

                #adding the veggie to veggie list
                self._captain.add_veggies(veggie)

                # update the score
                self._score+= veggie.get_points()
                self._field[self._captain.get_y()][x] = None

                # giving captain a new position
                self._captain.set_y(y)
                self._field[y][x] = self._captain
            # if there are no veggies on location
            elif not self._field[y][x]:
                self._field[self._captain.get_y()][x] = None
                self._captain.set_y(y)
                self._field[y][x] = self._captain
            
            else:
                print("Don't step on bunnies please!! They too have feelings")
        
        else:
            print(" OOooops!!  Invalid move!!")

    def movCapHoriz(self, dir):
        x = self._captain.get_x() + dir
        y = self._captain.get_y()

        # check if the new direction is in the frame or not
        if 0<= x < len(self._field[0]):
            # check if there is any veggie at new position
            if isinstance(self._field[y][x],Veggie):
                veggie = self._field[y][x]
                print(f"Wow you got a {veggie.get_name()}")

                #adding the veggie to veggie list
                self._captain.add_veggies(veggie)

                # update the score
                self._score+= veggie.get_points()
                self._field[self._captain.get_y()][self._captain.get_x()] = None

                # giving captain a new position
                self._captain.set_x(x)
                self._field[y][x] = self._captain
            # if there are no veggies on location
            elif not self._field[y][x]:
                self._field[self._captain.get_y()][self._captain.get_x()] = None
                self._captain.set_x(x)
                self._field[y][x] = self._captain
            
            else:
                print("Don't step on bunnies please!! They too have feelings")
        
        else:
            print(" OOooops!!  Invalid move!!")
            

    def moveCaptain(self):
        # Accept user input and move the captain accordingly.
        # ASDW keys having the same as left down right and up

        keypress = input('[W]Up [S]Down [A]Left [D]Right: ').upper()

        if keypress == 'W': # up move
            # logic to move up
            self.movCapVert(-1)
        elif keypress == 'S': #down move
            self.movCapVert(1)
        elif keypress == 'A': # left move
            self.movCapHoriz(-1)
        elif keypress == 'D': # right move
            self.movCapHoriz(1)

        else:
            print(f"{keypress} is an invalid selection")

    def remainingVeggies(self):
        cnt = 0
        for row in self._field:
            for item in row:
                if isinstance(item, Veggie):
                    cnt+=1
        
        return cnt

    def getScore(self):
        # return current score
        return self._score
    
    def moveRabbits(self):
        for rabit in self._rabits:
            #Rabbits random movement
            move_x = random.choice([-1, 0, 1])
            move_y = random.choice([-1, 0, 1])
            x = rabit.get_x() + move_x
            y = rabit.get_y() + move_y

            if 0 <= x < len(self._field[0]) and 0 <= y < len(self._field):
                #If location occupied by vegetable and rabbit moves in that location, rabbit will take that position
                if isinstance(self._field[y][x], Veggie):
                    self._field[rabit.get_y()][rabit.get_x()] = None
                    rabit.set_x(x)
                    rabit.set_y(y)
                    self._field[y][x] = rabit
                    print("Hurryyy! A rabbit ate a veggie! :( ")

                elif not self._field[y][x]:
                    # If location is empty and rabbit moves in tht location, rabbit will take that position
                    self._field[rabit.get_y()][rabit.get_x()] = None
                    rabit.set_x(x)
                    rabit.set_y(y)
                    self._field[y][x] = rabit

    def gameover(self):
        # Defines when game is over i.e. All the veggies on the field gets over.

        print("Well played. Game over!")
        print(f"Congratulations on collecting {len(self._captain.get_basket())} veggies.")
        veggie_dict = {}
        for veggie in self._captain.get_basket():
            v = veggie.get_name()
            if v in veggie_dict.keys():
                veggie_dict[v] +=1
            else:
                veggie_dict[v] = 1

        for lines in veggie_dict.keys():
            print(f"You secured {veggie_dict[lines]} {lines}")
                  



        print(f"Your score is {self.getScore()}")

    # write the highscore with initials in the database
    def highscore(self):
        prev_scores = []
        
        try:
            with open(self.__HIGHSCORE_FILE,"rb") as f:
                prev_scores = pkl.load(f)
        except Exception as e:
            pass

        name = input("Input your name (upto 7 letters) to put on the leaderboard: ")[:7]
        # enter max upto 7 lettered words in the leaderboard

        score = (name.upper() , self.getScore())
        # save the scores in tuple

        prev_scores.append(score)

        prev_scores.sort(key=lambda x: x[1], reverse=True)

        leaderboard = input('Wanna see the leaderboard? y/n?: ')

        if leaderboard.lower() == 'y':
            print("Name     Score")
            for vals in prev_scores:
                print(f"{vals[0]:<5}   {vals[1]:>5}")

        with open(self.__HIGHSCORE_FILE, "wb") as file:
            pkl.dump(prev_scores, file)




        

        
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



        

        
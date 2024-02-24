# Veggie Heist

## Game Description
Veggie Heist is a game where the player tries to harvest as many vegetables as possible before the rabbits eat them all.

The player controls the Captain who can move around the game board. Rabbits hop around the board randomly eating vegetables. When Captain moves onto a space with a vegetable, he harvests it and scores points. The game continues until all vegetables have been harvested or eaten.

## Game Rules
- The game board is a 2D grid initialized with random vegetables scattered around.
- There are also a number of rabbits(R) placed randomly on the board.
- The player controls Captain's movement using W, A, S, D keys to move Up, Left, Down, Right.
- Captain can harvest vegetables by moving onto their space resulting in scoring points.
- Rabbits move randomly each turn, eating any vegetables they land on.
- Captain cannot move onto a space occupied by a rabbit.
- The game ends when all vegetables have been harvested or eaten.
- The player's final score is displayed and saved to a high score list.
- You also get an option to view the leaderboard

## Code Overview
The game is built using OOP in Python.

The main classes are:

1. `FieldInhabitant`: Base class for any entity on the game board
2. `Veggie`: Vegetable subclass of FieldInhabitant
3. `Creature`: Base class for moving objects like rabbits and Captain
4. `Captain`: Player character, subclass of Creature
5. `Rabit`: AI character, subclass of Creature
6. `GameEngine`: Handles game initialization, running the game loop, scoring, and I/O.

The `GameEngine` initializes the game board, creatures, and vegetables based on inputs set. It runs the game loop prompting for player input, moving rabbits, checking for collisions, and tracking scores.

## How to Run
To play Veggie Heist:

1. Clone the repository
2. Run `python main.py`
3. Read the rules prompted
4. Use W, A, S, D keys to move the Captain(V).
5. Try to harvest veggies before rabbits eat them all!


Enjoy playing Veggie Heist!

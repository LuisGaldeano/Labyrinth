from src.game.game import Game
from src.labyrinth.models.board import Board

labyrinth = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['#', '.', '.', '.', '#', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '#', '.', '.', '.', '.'],
             ['.', '#', '.', '.', '.', '.', '.', '#', '.'],
             ['.', '#', '.', '.', '.', '.', '.', '#', '.']]


board = Board()
game = Game()
walls_position, clean_position = board.walls(base_labyrinth=labyrinth)

attemp = game.attempt(labyrinth=labyrinth, walls_position=walls_position)
print(attemp)

# Quita el attemp de game
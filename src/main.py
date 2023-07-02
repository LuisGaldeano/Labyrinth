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

play = game.play(labyrinth=labyrinth, walls_position=walls_position)


# from src.game.game import Game
# from src.labyrinth.models.board import Board
#
#
# labyrinth = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#              ['#', '.', '.', '.', '#', '.', '.', '.', '.'],
#              ['.', '.', '.', '.', '#', '.', '.', '.', '.'],
#              ['.', '#', '.', '.', '.', '.', '.', '#', '.'],
#              ['.', '#', '.', '.', '.', '.', '.', '#', '.']]
#
#
# board = Board()
# game = Game()
# walls_position, clean_position = board.walls(base_labyrinth=labyrinth)
#
# play = game.play(labyrinth=labyrinth, walls_position=walls_position)

from src.backend.game.new_game import NewGame
from src.backend.labyrinth.models.board import Board


labyrinth = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['#', '.', '.', '.', '#', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '#', '.', '.', '.', '.'],
             ['.', '#', '.', '.', '.', '.', '.', '#', '.'],
             ['.', '#', '.', '.', '.', '.', '.', '#', '.']]


board = Board()
walls_position, clean_position = board.walls(base_labyrinth=labyrinth)
game = NewGame(labyrinth=labyrinth,walls_position=walls_position)

ap = board.actual_position(base_labyrinth=labyrinth)
nom = 0
horizontal = True
movements_allowed = {}
forbidden_movement = None
used_positions = []
tree = {}
games = 0


play = game.play(forbidden_movement=forbidden_movement, used_positions=used_positions, horizontal=horizontal, ap=ap, nom=nom, movements_allowed=movements_allowed, tree=tree, games=games)

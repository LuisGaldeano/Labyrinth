from src.labyrinth.models.board import Board
from src.labyrinth.models.movemets import Movements
from src.labyrinth.models.checks import Checks

board = Board()
movements = Movements()


# ----  ELIMINAR
labyrinth = [[".", ".", ".", ".", ".", ".", ".", ".", "."],
             ["#", ".", ".", ".", "#", ".", ".", ".", "."],
             [".", ".", ".", ".", "#", ".", ".", ".", "."],
             [".", "#", ".", ".", ".", ".", ".", "#", "."],
             [".", "#", ".", ".", ".", ".", ".", "#", "."]]
walls_position, clean_position = board.walls(base_labyrinth=labyrinth)
# ---- HASTA AQUÍ



class Game():
    @classmethod
    def attempt(cls, labyrinth, walls_position):
        posible_movement = ['right', 'left', 'up', 'down', 'orientation']
        incompatibility = {'right': 'left', 'left': 'right', 'up': 'down', 'down': 'up', 'orientation': 'orientation'}
        movements_allowed = []
        forbidden_movement = None
        used_positions = []
        end_position = [4, 8]
        horizontal = True
        board.started_position(base_labyrinth=labyrinth, rod_length=3)
        ap = board.actual_position(base_labyrinth=labyrinth)
        next_movement = []
        nom = 0
        end_game = False

        while not end_game:
            for rep, movement in enumerate(posible_movement):
                if movement == 'right':
                    accepted, next_movement_right, horizontal = movements.right(horizontal=horizontal, walls_position=walls_position,
                                                          actual_position=ap)
                    if accepted and next_movement_right not in used_positions and movement != forbidden_movement:
                        try:
                            if movements_allowed[nom]:
                                movements_allowed[nom].append(movement)
                        except:
                            movements_allowed.append([movement])
                        used_positions.append(next_movement_right)
                        forbidden_movement = incompatibility[movement]
                        next_movement = next_movement_right
                        print(f'movements_allowed = {movements_allowed}, used_positions = {used_positions}, forbidden_movement = {forbidden_movement}')

                elif movement == 'left':
                    accepted, next_movement_left, horizontal = movements.left(horizontal=horizontal, walls_position=walls_position,
                                                                              actual_position=ap)

                    if accepted and next_movement_left not in used_positions and movement != forbidden_movement:
                        movements_allowed.append([movement])
                        used_positions.append(next_movement_left)
                        forbidden_movement = incompatibility[movement]
                        next_movement = next_movement_left

                elif movement == 'up':
                    accepted, next_movement, horizontal = movements.up(horizontal=horizontal, walls_position=walls_position,
                                                                             base_labyrinth=labyrinth, actual_position=ap, nom=nom)
                    if accepted and next_movement not in used_positions and movement != forbidden_movement:
                        movements_allowed.append(movement)
                        used_positions.append(next_movement)
                        forbidden_movement = incompatibility[movement]

                elif movement == 'down':
                    accepted, next_movement_down, horizontal = movements.down(horizontal=horizontal, walls_position=walls_position,
                                                                       base_labyrinth=labyrinth, actual_position=ap)
                    if accepted and next_movement_down not in used_positions and movement != forbidden_movement:
                        try:
                            if movements_allowed[nom]:
                                movements_allowed[nom].append(movement)
                        except:
                            movements_allowed.append([movement])
                        used_positions.append(next_movement_down)
                        forbidden_movement = incompatibility[movement]
                        next_movement = next_movement_down

                elif movement == 'orientation':
                    accepted, next_movement, horizontal = movements.down(horizontal=horizontal, walls_position=walls_position,
                                                                         base_labyrinth=labyrinth, actual_position=ap)
                    if accepted and next_movement not in used_positions and movement != forbidden_movement:
                        movements_allowed.append(movement)
                        used_positions.append(next_movement)
                        forbidden_movement = incompatibility[movement]


                        if len(movements_allowed) > 0:
                            for element in next_movement:
                                if element == end_position:
                                    end_game = True
                                    return end_game
                        else:
                            end_game = True
                            return end_game

                        if horizontal:
                            horizontal = False
                        else:
                            horizontal = True

            # Ahora tienes que hacer que cada vez que salga una ruta divida

            for mov in movements_allowed:
                ap, nom = Checks.move(
                    accepted_movement=True,
                    actual_position=ap,
                    next_movement=next_movement,
                    nom=nom,
                )

                for element in ap:
                    if element == end_position:
                        end_game = True
                        return end_game


movement_allowed = Game.attempt(labyrinth=labyrinth, walls_position=walls_position)
print(movement_allowed)
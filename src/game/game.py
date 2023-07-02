from src.labyrinth.models.board import Board
from src.labyrinth.models.movemets import Movements
from src.labyrinth.models.checks import Checks

board = Board()
movements = Movements()

# ----  ELIMINAR
labyrinth = [[".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", "#", ".", ".", ".", "."],
             [".", ".", ".", ".", "#", ".", ".", ".", "."],
             [".", "#", ".", ".", ".", ".", ".", "#", "."],
             [".", "#", ".", ".", ".", ".", ".", "#", "."]]
walls_position, clean_position = board.walls(base_labyrinth=labyrinth)


# ---- HASTA AQUÍ


class Game:

    @classmethod
    def check_accepted(cls, accepted, next_movement_initial, used_positions, movement, forbidden_movement,
                       movements_allowed, nom, incompatibility, horizontal):
        if accepted and next_movement_initial not in used_positions and movement != forbidden_movement:
            try:
                if movements_allowed[nom]:
                    movements_allowed[nom].append(movement)
            except:
                movements_allowed.append([movement])
            used_positions.append(next_movement_initial)
            forbidden_movement = incompatibility[movement]
            next_movement = next_movement_initial

            if movement == 'orientation':
                if horizontal:
                    horizontal = False
                else:
                    horizontal = True

            return movements_allowed, used_positions, forbidden_movement, next_movement, horizontal

        # return movements_allowed, used_positions, forbidden_movement, next_movement_initial, horizontal

    @classmethod
    def right_movement(cls, horizontal, ap, used_positions, movement, forbidden_movement, movements_allowed, nom,
                       incompatibility):
        accepted, next_movement_right, horizontal = movements.right(horizontal=horizontal,
                                                                    walls_position=walls_position,
                                                                    actual_position=ap)

        movements_allowed, used_positions, forbidden_movement, next_movement, horizontal = Game.check_accepted(
            accepted=accepted,
            next_movement_initial=next_movement_right,
            used_positions=used_positions,
            movement=movement,
            forbidden_movement=forbidden_movement,
            movements_allowed=movements_allowed,
            nom=nom,
            incompatibility=incompatibility,
            horizontal=horizontal
        )

        # print(
        #     f'movements_allowed = {movements_allowed}, used_positions = {used_positions}, forbidden_movement = {forbidden_movement}')

        return movements_allowed, used_positions, forbidden_movement, next_movement, horizontal

    @classmethod
    def left_movement(cls, horizontal, ap, used_positions, movement, forbidden_movement, movements_allowed, nom,
                      incompatibility):
        accepted, next_movement_left, horizontal = movements.left(horizontal=horizontal,
                                                                  walls_position=walls_position,
                                                                  actual_position=ap)

        movements_allowed, used_positions, forbidden_movement, next_movement, horizontal = Game.check_accepted(
            accepted=accepted,
            next_movement_initial=next_movement_left,
            used_positions=used_positions,
            movement=movement,
            forbidden_movement=forbidden_movement,
            movements_allowed=movements_allowed,
            nom=nom,
            incompatibility=incompatibility,
            horizontal=horizontal
        )

        # print(
        #     f'movements_allowed = {movements_allowed}, used_positions = {used_positions}, forbidden_movement = {forbidden_movement}')

        return movements_allowed, used_positions, forbidden_movement, next_movement, horizontal

    @classmethod
    def up_movement(cls, horizontal, ap, used_positions, movement, forbidden_movement, movements_allowed, nom,
                    incompatibility):
        accepted, next_movement_left, horizontal = movements.up(horizontal=horizontal,
                                                                walls_position=walls_position,
                                                                actual_position=ap,
                                                                nom=nom,
                                                                base_labyrinth=labyrinth)

        movements_allowed, used_positions, forbidden_movement, next_movement, horizontal = Game.check_accepted(
            accepted=accepted,
            next_movement_initial=next_movement_left,
            used_positions=used_positions,
            movement=movement,
            forbidden_movement=forbidden_movement,
            movements_allowed=movements_allowed,
            nom=nom,
            incompatibility=incompatibility,
            horizontal=horizontal
        )

        # print(
        #     f'movements_allowed = {movements_allowed}, used_positions = {used_positions}, forbidden_movement = {forbidden_movement}')

        return movements_allowed, used_positions, forbidden_movement, next_movement, horizontal

    @classmethod
    def down_movement(cls, horizontal, ap, used_positions, movement, forbidden_movement, movements_allowed, nom,
                      incompatibility):
        accepted, next_movement_left, horizontal = movements.down(horizontal=horizontal,
                                                                  walls_position=walls_position,
                                                                  base_labyrinth=labyrinth,
                                                                  actual_position=ap)

        movements_allowed, used_positions, forbidden_movement, next_movement, horizontal = Game.check_accepted(
            accepted=accepted,
            next_movement_initial=next_movement_left,
            used_positions=used_positions,
            movement=movement,
            forbidden_movement=forbidden_movement,
            movements_allowed=movements_allowed,
            nom=nom,
            incompatibility=incompatibility,
            horizontal=horizontal
        )

        # print(
        #     f'movements_allowed = {movements_allowed}, used_positions = {used_positions}, forbidden_movement = {forbidden_movement}')

        return movements_allowed, used_positions, forbidden_movement, next_movement, horizontal

    @classmethod
    def orientation_movement(cls, horizontal, ap, used_positions, movement, forbidden_movement, movements_allowed, nom,
                             incompatibility):
        accepted, next_movement_left, horizontal = movements.change_orientation(
            horizontal=horizontal,
            walls_position=walls_position,
            base_labyrinth=labyrinth,
            actual_position=ap,
            nom=nom)

        movements_allowed, used_positions, forbidden_movement, next_movement, horizontal = Game.check_accepted(
            accepted=accepted,
            next_movement_initial=next_movement_left,
            used_positions=used_positions,
            movement=movement,
            forbidden_movement=forbidden_movement,
            movements_allowed=movements_allowed,
            nom=nom,
            incompatibility=incompatibility,
            horizontal=horizontal
        )

        # print(
        #     f'movements_allowed = {movements_allowed}, used_positions = {used_positions}, forbidden_movement = {forbidden_movement}')

        return movements_allowed, used_positions, forbidden_movement, next_movement, horizontal

    @classmethod
    def attempt(cls, posible_movement, incompatibility, movements_allowed, forbidden_movement,
                used_positions, end_position, horizontal, start, ap, next_movement, nom):
        # posible_movement = ['right', 'left', 'up', 'down', 'orientation']
        # incompatibility = {'right': 'left', 'left': 'right', 'up': 'down', 'down': 'up', 'orientation': 'orientation'}
        # movements_allowed = []
        # forbidden_movement = None
        # used_positions = []
        # end_position = [4, 8]
        # horizontal = True
        # start = board.started_position(base_labyrinth=labyrinth, rod_length=3)
        # ap = board.actual_position(base_labyrinth=labyrinth)
        # next_movement = []
        # nom = 0

        for rep, movement in enumerate(posible_movement):
            if movement == 'right':
                try:
                    movements_allowed, used_positions, forbidden_movement, next_movement, horizontal = Game.right_movement(
                        horizontal=horizontal,
                        ap=ap,
                        used_positions=used_positions,
                        movement=movement,
                        forbidden_movement=forbidden_movement,
                        movements_allowed=movements_allowed,
                        nom=nom,
                        incompatibility=incompatibility

                    )

                except:
                    pass

            elif movement == 'left':
                try:
                    movements_allowed, used_positions, forbidden_movement, next_movement, horizontal = Game.left_movement(
                        horizontal=horizontal,
                        ap=ap,
                        used_positions=used_positions,
                        movement=movement,
                        forbidden_movement=forbidden_movement,
                        movements_allowed=movements_allowed,
                        nom=nom,
                        incompatibility=incompatibility
                    )
                except:
                    pass

            elif movement == 'up':
                try:
                    movements_allowed, used_positions, forbidden_movement, next_movement, horizontal = Game.up_movement(
                        horizontal=horizontal,
                        ap=ap,
                        used_positions=used_positions,
                        movement=movement,
                        forbidden_movement=forbidden_movement,
                        movements_allowed=movements_allowed,
                        nom=nom,
                        incompatibility=incompatibility
                    )

                except:
                    pass

            elif movement == 'down':
                try:
                    movements_allowed, used_positions, forbidden_movement, next_movement, horizontal = Game.down_movement(
                        horizontal=horizontal,
                        ap=ap,
                        used_positions=used_positions,
                        movement=movement,
                        forbidden_movement=forbidden_movement,
                        movements_allowed=movements_allowed,
                        nom=nom,
                        incompatibility=incompatibility
                    )
                except:
                    pass

            elif movement == 'orientation':
                try:
                    movements_allowed, used_positions, forbidden_movement, next_movement, horizontal = Game.orientation_movement(
                        horizontal=horizontal,
                        ap=ap,
                        used_positions=used_positions,
                        movement=movement,
                        forbidden_movement=forbidden_movement,
                        movements_allowed=movements_allowed,
                        nom=nom,
                        incompatibility=incompatibility
                    )
                except:
                    pass

        return posible_movement, incompatibility, movements_allowed, forbidden_movement, used_positions, end_position, horizontal, start, ap, next_movement, nom

        # Ahora tienes que hacer que cada vez que salga una ruta divida

        # for mov in movements_allowed:
        #     ap, nom = Checks.move(
        #         accepted_movement=True,
        #         actual_position=ap,
        #         next_movement=next_movement,
        #         nom=nom,
        #     )
        #
        #     for element in ap:
        #         if element == end_position:
        #             end_game = True
        #             return end_game

    # @classmethod
    # def game(cls, posible_movement, incompatibility, movements_allowed, forbidden_movement,
    #          used_positions, end_position, horizontal, start, ap, next_movement, nom):
    #
    #     posible_movement, incompatibility, movements_allowed, forbidden_movement, used_positions, end_position, horizontal, start, ap, next_movement, nom = Game.attempt(
    #         posible_movement=posible_movement,
    #         incompatibility=incompatibility,
    #         movements_allowed=movements_allowed,
    #         forbidden_movement=forbidden_movement,
    #         used_positions=used_positions,
    #         end_position=end_position,
    #         horizontal=horizontal,
    #         start=start,
    #         ap=ap,
    #         next_movement=next_movement,
    #         nom=nom)
    #
    #     for num, mov in enumerate(movements_allowed):
    #
    #         # Aquí tienes que ejecutar el movimiento para cada uno de los mov y que se cree un bucle
    #         ap, nom = Checks.move(
    #             accepted_movement=True,
    #             actual_position=ap,
    #             next_movement=next_movement,
    #             nom=nom,
    #         )
    #
    #         posible_movement, incompatibility, movements_allowed, forbidden_movement, used_positions, end_position, horizontal, start, ap, next_movement, nom = Game.attempt(
    #             posible_movement, incompatibility, movements_allowed, forbidden_movement, used_positions, end_position,
    #             horizontal, start, ap, next_movement, nom)
    #         print(movements_allowed, nom)


posible_movement = ['right', 'left', 'up', 'down', 'orientation']
incompatibility = {'right': 'left', 'left': 'right', 'up': 'down', 'down': 'up', 'orientation': 'orientation'}
movements_allowed = []
forbidden_movement = None
used_positions = []
end_position = [4, 8]
horizontal = True
start = board.started_position(base_labyrinth=labyrinth, rod_length=3)
ap = board.actual_position(base_labyrinth=labyrinth)
next_movement = []
nom = 0

game = Game.game(posible_movement, incompatibility, movements_allowed, forbidden_movement, used_positions, end_position,
                 horizontal, start, ap, next_movement, nom)
print(game)

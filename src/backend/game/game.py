from src.backend.labyrinth.models.board import Board
from src.backend.labyrinth.models.movemets import Movements
from src.backend.labyrinth.models.checks import Checks

board = Board()
movements = Movements()


class Game:

    @classmethod
    def check_accepted(cls, accepted, next_movement_initial, used_positions, movement, forbidden_movement,
                       movements_allowed, nom, incompatibility, horizontal):
        """
        Checks if a movement is accepted and updates the game state accordingly.
        """

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

    @classmethod
    def right_movement(cls, horizontal, ap, used_positions, movement, forbidden_movement, movements_allowed, nom,
                       incompatibility, walls_position):
        """
        Executes a rightward movement in the game and updates the game state accordingly.
        """

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

        return movements_allowed, used_positions, forbidden_movement, next_movement, horizontal

    @classmethod
    def left_movement(cls, horizontal, ap, used_positions, movement, forbidden_movement, movements_allowed, nom,
                      incompatibility, walls_position):
        """
        Executes a leftward movement in the game and updates the game state accordingly.
        """

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

        return movements_allowed, used_positions, forbidden_movement, next_movement, horizontal

    @classmethod
    def up_movement(cls, horizontal, ap, used_positions, movement, forbidden_movement, movements_allowed, nom,
                    incompatibility, walls_position, labyrinth):
        """
        Executes a upward movement in the game and updates the game state accordingly.
        """

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

        return movements_allowed, used_positions, forbidden_movement, next_movement, horizontal

    @classmethod
    def down_movement(cls, horizontal, ap, used_positions, movement, forbidden_movement, movements_allowed, nom,
                      incompatibility, walls_position, labyrinth):
        """
        Executes a downward movement in the game and updates the game state accordingly.
        """

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

        return movements_allowed, used_positions, forbidden_movement, next_movement, horizontal

    @classmethod
    def orientation_movement(cls, horizontal, ap, used_positions, movement, forbidden_movement, movements_allowed, nom,
                             incompatibility, walls_position, labyrinth):
        """
        Executes a change orientation movement in the game and updates the game state accordingly.
        """

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

        return movements_allowed, used_positions, forbidden_movement, next_movement, horizontal

    @classmethod
    def attempt(cls, posible_movement, incompatibility, movements_allowed, forbidden_movement,
                used_positions, end_position, horizontal, start, ap, next_movement, nom, walls_position, labyrinth):
        """
        Attempts to make the specified movements in the game and updates the game state accordingly.
        """

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
                        incompatibility=incompatibility,
                        walls_position=walls_position

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
                        incompatibility=incompatibility,
                        walls_position=walls_position
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
                        incompatibility=incompatibility,
                        labyrinth=labyrinth,
                        walls_position=walls_position
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
                        incompatibility=incompatibility,
                        labyrinth=labyrinth,
                        walls_position=walls_position
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
                        incompatibility=incompatibility,
                        labyrinth=labyrinth,
                        walls_position=walls_position
                    )
                except:
                    pass

        return posible_movement, incompatibility, movements_allowed, forbidden_movement, used_positions, end_position, horizontal, start, ap, next_movement, nom

    @classmethod
    def game(cls, posible_movement, incompatibility, movements_allowed, forbidden_movement,
             used_positions, end_position, horizontal, start, ap, next_movement, nom, labyrinth, walls_position):
        """
        Execute the bucle
        """

        roads = []
        # end_game = False
        #
        # while not end_game:
        posible_movement, incompatibility, movements_allowed, forbidden_movement, used_positions, end_position, horizontal, start, ap, next_movement, nom = Game.attempt(
            posible_movement=posible_movement,
            incompatibility=incompatibility,
            movements_allowed=movements_allowed,
            forbidden_movement=forbidden_movement,
            used_positions=used_positions,
            end_position=end_position,
            horizontal=horizontal,
            start=start,
            ap=ap,
            next_movement=next_movement,
            nom=nom,
            walls_position=walls_position,
            labyrinth=labyrinth
        )

        for num, mov in enumerate(movements_allowed):
            for m in mov:
                if m == 'right':
                    accepted, next_movement, horizontal = movements.right(horizontal=horizontal,
                                                                          walls_position=walls_position,
                                                                          actual_position=ap)
                    ap, nom = Checks.move(
                        accepted_movement=True,
                        actual_position=ap,
                        next_movement=next_movement,
                        nom=nom,
                    )

                    posible_movement, incompatibility, movements_allowed, forbidden_movement, used_positions, end_position, horizontal, start, ap, next_movement, nom = Game.attempt(
                        posible_movement, incompatibility, movements_allowed, forbidden_movement, used_positions,
                        end_position,
                        horizontal, start, ap, next_movement, nom, walls_position, labyrinth)
                    print(movements_allowed, nom)

                elif m == 'left':
                    accepted, next_movement, horizontal = movements.left(horizontal=horizontal,
                                                                         walls_position=walls_position,
                                                                         actual_position=ap)
                    ap, nom = Checks.move(
                        accepted_movement=True,
                        actual_position=ap,
                        next_movement=next_movement,
                        nom=nom,
                    )

                    posible_movement, incompatibility, movements_allowed, forbidden_movement, used_positions, end_position, horizontal, start, ap, next_movement, nom = Game.attempt(
                        posible_movement, incompatibility, movements_allowed, forbidden_movement, used_positions,
                        end_position,
                        horizontal, start, ap, next_movement, nom, walls_position, labyrinth)
                    print(movements_allowed, nom)

                elif m == 'up':
                    accepted, next_movement, horizontal = movements.up(horizontal=horizontal,
                                                                       walls_position=walls_position,
                                                                       actual_position=ap,
                                                                       base_labyrinth=labyrinth,
                                                                       nom=nom)
                    ap, nom = Checks.move(
                        accepted_movement=True,
                        actual_position=ap,
                        next_movement=next_movement,
                        nom=nom,
                    )

                    posible_movement, incompatibility, movements_allowed, forbidden_movement, used_positions, end_position, horizontal, start, ap, next_movement, nom = Game.attempt(
                        posible_movement, incompatibility, movements_allowed, forbidden_movement, used_positions,
                        end_position,
                        horizontal, start, ap, next_movement, nom, walls_position, labyrinth)
                    print(movements_allowed, nom)

                elif m == 'down':
                    accepted, next_movement, horizontal = movements.down(horizontal=horizontal,
                                                                         walls_position=walls_position,
                                                                         actual_position=ap,
                                                                         base_labyrinth=labyrinth, )
                    ap, nom = Checks.move(
                        accepted_movement=True,
                        actual_position=ap,
                        next_movement=next_movement,
                        nom=nom,
                    )

                    posible_movement, incompatibility, movements_allowed, forbidden_movement, used_positions, end_position, horizontal, start, ap, next_movement, nom = Game.attempt(
                        posible_movement, incompatibility, movements_allowed, forbidden_movement, used_positions,
                        end_position,
                        horizontal, start, ap, next_movement, nom, walls_position, labyrinth)
                    print(movements_allowed, nom)

                elif m == 'orientation':
                    accepted, next_movement, horizontal = movements.change_orientation(horizontal=horizontal,
                                                                                       walls_position=walls_position,
                                                                                       actual_position=ap,
                                                                                       base_labyrinth=labyrinth,
                                                                                       nom=nom)
                    ap, nom = Checks.move(
                        accepted_movement=True,
                        actual_position=ap,
                        next_movement=next_movement,
                        nom=nom,
                    )

                    posible_movement, incompatibility, movements_allowed, forbidden_movement, used_positions, end_position, horizontal, start, ap, next_movement, nom = Game.attempt(
                        posible_movement, incompatibility, movements_allowed, forbidden_movement, used_positions,
                        end_position,
                        horizontal, start, ap, next_movement, nom, walls_position, labyrinth)
                    print(movements_allowed, nom)


    @classmethod
    def play(cls, labyrinth, walls_position):
        """
        Start the game
        """

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

        game = Game.game(posible_movement, incompatibility, movements_allowed, forbidden_movement, used_positions,
                         end_position, horizontal, start, ap, next_movement, nom, labyrinth, walls_position)
        print(game)

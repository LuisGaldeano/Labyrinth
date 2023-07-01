from src.labyrinth.models.checks import Checks


class Movements:
    def right(self, horizontal, walls_position, actual_position):
        next_movement = []
        if horizontal:
            for position in actual_position:
                element = [position[0], position[1] + 1]
                next_movement.append(element)

        if not horizontal:
            for position in actual_position:
                element = [position[0], position[1] + 1]
                next_movement.append(element)

        accepted_movement = Checks.check_if_valid_left_right(
            next_movement=next_movement,
            walls_position=walls_position,
        )

        return accepted_movement, next_movement, horizontal

    def left(self, horizontal, walls_position, actual_position):
        movement = 'left'
        next_movement = []
        if horizontal:
            for position in actual_position:
                element = [position[0], position[1] - 1]
                next_movement.append(element)

        if not horizontal:
            for position in actual_position:
                element = [position[0], position[1] - 1]
                next_movement.append(element)

        accepted_movement = Checks.check_if_valid_left_right(
            next_movement=next_movement,
            walls_position=walls_position,
        )

        return accepted_movement, next_movement, horizontal

    def down(self, horizontal, walls_position, base_labyrinth, actual_position):
        movement = 'down'
        next_movement = []

        if horizontal:
            # Create new movement
            for element in actual_position:
                x = [element[0] + 1, element[1]]
                next_movement.append(x)

        elif not horizontal:
            for element in actual_position:
                x = [element[0] + 1, element[1]]
                next_movement.append(x)

        accepted_movement = Checks.check_if_valid_up_down(
            horizontal=horizontal,
            movement=movement,
            actual_position=actual_position,
            next_movement=next_movement,
            walls_position=walls_position,
            base_labyrinth=base_labyrinth,
        )

        return accepted_movement, next_movement, horizontal

    def up(self, horizontal, walls_position, base_labyrinth, actual_position, nom):
        movement = 'up'
        next_movement = []

        if horizontal:
            # Create new movement
            for element in actual_position:
                x = [element[0] - 1, element[1]]
                next_movement.append(x)

        elif not horizontal:
            for element in actual_position:
                x = [element[0] - 1, element[1]]
                next_movement.append(x)

        accepted_movement = Checks.check_if_valid_up_down(
            horizontal=horizontal,
            movement=movement,
            actual_position=actual_position,
            next_movement=next_movement,
            walls_position=walls_position,
            base_labyrinth=base_labyrinth,
        )

        return accepted_movement, next_movement, horizontal


    def change_orientation(self,horizontal, walls_position, base_labyrinth, actual_position, nom):
        movement = 'orientation'

        # Create the movement
        next_movement = []
        if horizontal:
            for position, element in enumerate(actual_position):
                if position == 0:
                    x = [element[0] - 1, element[1] + 1]
                    next_movement.append(x)
                elif position == 1:
                    x = element
                    next_movement.append(x)
                elif position == 2:
                    x = [element[0] + 1, element[1] - 1]
                    next_movement.append(x)
        elif not horizontal:
            for position, element in enumerate(actual_position):
                if position == 0:
                    x = [element[0] + 1, element[1] - 1]
                    next_movement.append(x)
                elif position == 1:
                    x = element
                    next_movement.append(x)
                elif position == 2:
                    x = [element[0] - 1, element[1] + 1]
                    next_movement.append(x)

        accepted_movement = Checks.check_if_valid_orientation(
            horizontal=horizontal,
            movement=movement,
            actual_position=actual_position,
            next_movement=next_movement,
            walls_position=walls_position,
            base_labyrinth=base_labyrinth,
        )

        return accepted_movement, next_movement, horizontal



from src.backend.labyrinth.models.checks import Checks


class Movements:
    @classmethod
    def right(cls, horizontal, walls_position, actual_position):
        """
        Performs a rightward movement of the rod.

        :param horizontal: Indicates whether the movement is horizontal (True) or vertical (False).
        :param walls_position: List of wall positions in the game.
        :param actual_position: List of current positions.
        :return: A tuple containing:
            - accepted_movement (list): List of valid movements towards the right.
            - next_movement (list): List of movements resulting from moving towards the right.
            - horizontal (bool): Indicator of the movement direction (True for horizontal, False for vertical).
        """

        next_movement = []
        for position in actual_position:
            element = [position[0], position[1] + 1]
            next_movement.append(element)

        accepted_movement = Checks.check_if_valid_right(
            next_movement=next_movement,
            walls_position=walls_position,
        )

        return accepted_movement, next_movement, horizontal

    @classmethod
    def left(cls, horizontal, walls_position, actual_position):
        """
        Performs a leftward movement of the rod.

        :param horizontal: Indicates whether the movement is horizontal (True) or vertical (False).
        :param walls_position: List of wall positions in the game.
        :param actual_position: List of current positions.
        :return: A tuple containing:
            - accepted_movement (list): List of valid movements towards the left.
            - next_movement (list): List of movements resulting from moving towards the left.
            - horizontal (bool): Indicator of the movement direction (True for horizontal, False for vertical).
        """

        next_movement = []
        for position in actual_position:
            element = [position[0], position[1] - 1]
            next_movement.append(element)

        accepted_movement = Checks.check_if_valid_left(
            next_movement=next_movement,
            walls_position=walls_position,
        )

        return accepted_movement, next_movement, horizontal

    @classmethod
    def down(cls, horizontal, walls_position, base_labyrinth, actual_position):
        """
        Performs a downward movement of the rod.

        :param horizontal: Indicates whether the movement is horizontal (True) or vertical (False).
        :param walls_position: List of wall positions in the game.
        :param base_labyrinth: Base labyrinth representation.
        :param actual_position: List of current positions.
        :return: A tuple containing:
            - accepted_movement (list): List of valid movements downwards.
            - next_movement (list): List of movements resulting from moving downwards.
            - horizontal (bool): Indicator of the movement direction (True for horizontal, False for vertical).
        """

        next_movement = []

        for element in actual_position:
            x = [element[0] + 1, element[1]]
            next_movement.append(x)

        accepted_movement = Checks.check_if_valid_down(
            next_movement=next_movement,
            walls_position=walls_position,
            base_labyrinth=base_labyrinth,
        )

        return accepted_movement, next_movement, horizontal

    @classmethod
    def up(cls, horizontal, walls_position, actual_position):
        """
        Performs an upward movement of the rod.

        :param horizontal: Indicates whether the movement is horizontal (True) or vertical (False).
        :param walls_position: List of wall positions in the game.
        :param base_labyrinth: Base labyrinth representation.
        :param actual_position: List of current positions.
        :param nom: Some additional parameter description.
        :return: A tuple containing:
            - accepted_movement (list): List of valid movements upwards.
            - next_movement (list): List of movements resulting from moving upwards.
            - horizontal (bool): Indicator of the movement direction (True for horizontal, False for vertical).
        """

        next_movement = []

        for element in actual_position:
            x = [element[0] - 1, element[1]]
            next_movement.append(x)

        accepted_movement = Checks.check_if_valid_up(
            next_movement=next_movement,
            walls_position=walls_position,
        )

        return accepted_movement, next_movement, horizontal

    @classmethod
    def change_orientation(cls, horizontal, walls_position, base_labyrinth, actual_position):
        """
        Changes the orientation of the rod.

        :param horizontal: Indicates whether the movement is horizontal (True) or vertical (False).
        :param walls_position: List of wall positions in the game.
        :param base_labyrinth: Base labyrinth representation.
        :param actual_position: List of current positions.
        :param nom: Some additional parameter description.
        :return: A tuple containing:
            - accepted_movement (list): List of valid movements for changing the orientation.
            - next_movement (list): List of movements resulting from changing the orientation.
            - horizontal (bool): Indicator of the movement direction (True for horizontal, False for vertical).
        """

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
            next_movement=next_movement,
            walls_position=walls_position,
            base_labyrinth=base_labyrinth,
        )

        return accepted_movement, next_movement, horizontal

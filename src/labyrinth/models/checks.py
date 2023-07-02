class Checks:
    @classmethod
    def check_if_valid_left_right(cls, next_movement, walls_position):
        """
        Checks if the left or right movement is valid.

        :param next_movement: List of movements resulting from moving left or right.
        :param walls_position: List of wall positions in the game.
        :return: A boolean indicating if the movement is valid (True) or not (False).
        """

        for element in next_movement:
            if element in walls_position:
                return False
            elif not (0 <= element[0] <= 4):
                return False
            elif not (0 <= element[1] <= 8):
                return False
        return True

    @classmethod
    def check_if_valid_up_down(cls,horizontal, movement, actual_position, next_movement, walls_position, base_labyrinth):
        """
        Checks if the upward or downward movement is valid.

        :param horizontal: Indicates whether the movement is horizontal (True) or vertical (False).
        :param movement: The type of movement ('up' or 'down').
        :param actual_position: List of current positions.
        :param next_movement: List of movements resulting from moving upward or downward.
        :param walls_position: List of wall positions in the game.
        :param base_labyrinth: Base labyrinth representation.
        :return: A boolean indicating if the movement is valid (True) or not (False).
        """

        valid = True
        if movement == 'down':
            for element in next_movement:
                if element in walls_position:
                    valid = False
                    return valid

                elif horizontal:
                    if element[0] + 1 > (len(base_labyrinth) - 1):
                        valid = False
                        return valid
                elif not horizontal:
                    if element[0] > (len(base_labyrinth) - 1):
                        valid = False
                        return valid
            return valid

        elif movement == 'up':
            for element in next_movement:
                if element in walls_position:
                    valid = False
                    return valid
                elif horizontal:
                    if element[0] - 1 < 0:
                        valid = False
                        return valid
                elif not horizontal:
                    if element[0] < 0:
                        valid = False
                        return valid

            return valid

    @classmethod
    def check_if_valid_orientation(cls,horizontal, movement, actual_position, next_movement, walls_position, base_labyrinth):
        """
        Checks if the orientation change movement is valid.

        :param horizontal: Indicates whether the movement is horizontal (True) or vertical (False).
        :param movement: The type of movement ('orientation').
        :param actual_position: List of current positions.
        :param next_movement: List of movements resulting from changing the orientation.
        :param walls_position: List of wall positions in the game.
        :param base_labyrinth: Base labyrinth representation.
        :return: A boolean indicating if the movement is valid (True) or not (False).
        """
        valid = True
        if movement == 'orientation':
            check_box = []
            # Check if first/last row
            if not (0 < next_movement[1][0] < 4):   # len
                valid = False
                return valid

            # Check if first/last column
            if not (0 < next_movement[1][1] < 8):  # len
                valid = False
                return valid

            if horizontal:
                for element in next_movement:
                    check_box.append([element[0], element[1] - 1])
                    check_box.append(element)
                    check_box.append([element[0], element[1] + 1])
            else:
                for element in next_movement:
                    check_box.append([element[0] - 1, element[1]])
                    check_box.append(element)
                    check_box.append([element[0] + 1, element[1]])

            for element in check_box:
                if element in walls_position:
                    valid = False
                    return valid
                if 0 > element[0]:
                    valid = False
                    return valid
                if element[0] > 4:
                    valid = False
                    return valid
                if 0 > element[1]:
                    valid = False
                    return valid
                if element[1] > 8:
                    valid = False
                    return valid
        return valid

    @classmethod
    def move(cls, accepted_movement, actual_position, next_movement, nom):
        """
        Moves the character in the game.

        :param accepted_movement: Indicates if the movement is accepted (True) or not (False).
        :param actual_position: List of current positions.
        :param next_movement: List of movements resulting from the movement.
        :param nom: Current count of movements.
        :return: Tuple containing the updated position and movement count.
        """
        # Make the movement
        if accepted_movement:
            actual_position = next_movement
            nom += 1
            return actual_position, nom
        else:
            return actual_position, nom


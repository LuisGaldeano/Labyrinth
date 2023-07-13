class Board:
    def started_position(self, base_labyrinth, rod_length=3):
        """
        Sets the initial position of the character in the labyrinth.

        :param base_labyrinth: Base labyrinth representation.
        :param rod_length: Length of the rod representing the character's position (default: 3).
        """

        rod = [1] * rod_length
        base_labyrinth[0][:rod_length:] = rod

    def walls(self, base_labyrinth):
        """
        Identifies the positions of walls in the labyrinth.

        :param base_labyrinth: Base labyrinth representation.
        :return: Tuple containing lists of wall positions and clean positions.
        """
        clean_position = []
        walls_position = []
        for row, list in enumerate(base_labyrinth):
            for column, element in enumerate(list):
                position = [row, column]
                if element == '#':
                    walls_position.append(position)
                else:
                    clean_position.append(position)
        return walls_position, clean_position

    def actual_position(self, base_labyrinth):
        """
        Retrieves the current position of the character in the labyrinth.

        :param base_labyrinth: Base labyrinth representation.
        :return: List of current positions.
        """
        actual_position = []
        for row, list in enumerate(base_labyrinth):
            for column, element in enumerate(list):
                position = [row, column]
                if element == 1:
                    actual_position.append(position)
        return actual_position

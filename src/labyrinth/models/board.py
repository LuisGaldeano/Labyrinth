class Board:
    def started_position(self, base_labyrinth, rod_length=3):
        rod = [1] * rod_length
        base_labyrinth[0][:rod_length:] = rod

    def walls(self, base_labyrinth):
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
        actual_position = []
        for row, list in enumerate(base_labyrinth):
            for column, element in enumerate(list):
                position = [row, column]
                if element == 1:
                    actual_position.append(position)
        return actual_position

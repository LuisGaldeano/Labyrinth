from src.backend.labyrinth.models.board import Board
from src.backend.labyrinth.models.movemets import Movements
from src.backend.game.tree import TreeNode

board = Board()
movements = Movements()
treenode = TreeNode(value=0, content=None)

class NewGame:

    def __init__(self, labyrinth, walls_position):
        self.labyrinth = labyrinth
        self.walls_position = walls_position
        self.possible_movement = ['right', 'left', 'up', 'down', 'orientation']
        self.incompatibility = {'right': 'left', 'left': 'right', 'up': 'down', 'down': 'up', 'orientation': 'orientation'}
        self.end_position = [2, 4]
        self.start = board.started_position(base_labyrinth=labyrinth, rod_length=3)

    def check_movements_allowed(self, forbidden_movement, used_positions, horizontal, ap):

        movements_allowed = {}
        for movement in self.possible_movement:
            if movement == 'right':
                accepted_movement, next_movement, horizontal = movements.right(
                    horizontal=horizontal,
                    walls_position=self.walls_position,
                    actual_position=ap
                )
                accepted = self.check_if_accepted(
                    accepted_movement=accepted_movement,
                    next_movement_initial=next_movement,
                    used_positions=used_positions,
                    forbidden_movement=forbidden_movement,
                    movement=movement
                )
                movements_allowed[movement] = [accepted, next_movement, horizontal]

            elif movement == 'left':
                accepted_movement, next_movement, horizontal= movements.left(
                    horizontal=horizontal,
                    walls_position=self.walls_position,
                    actual_position=ap
                )
                accepted = self.check_if_accepted(
                    accepted_movement=accepted_movement,
                    next_movement_initial=next_movement,
                    used_positions=used_positions,
                    forbidden_movement=forbidden_movement,
                    movement=movement
                )
                movements_allowed[movement] = [accepted, next_movement, horizontal]

            elif movement == 'down':
                accepted_movement, next_movement, horizontal= movements.down(
                    horizontal=horizontal,
                    walls_position=self.walls_position,
                    base_labyrinth=self.labyrinth,
                    actual_position=ap
                )
                accepted = self.check_if_accepted(
                    accepted_movement=accepted_movement,
                    next_movement_initial=next_movement,
                    used_positions=used_positions,
                    forbidden_movement=forbidden_movement,
                    movement=movement
                )
                movements_allowed[movement] = [accepted, next_movement, horizontal]

            elif movement == 'up':
                accepted_movement, next_movement, horizontal= movements.up(
                    horizontal=horizontal,
                    walls_position=self.walls_position,
                    actual_position=ap
                )
                accepted = self.check_if_accepted(
                    accepted_movement=accepted_movement,
                    next_movement_initial=next_movement,
                    used_positions=used_positions,
                    forbidden_movement=forbidden_movement,
                    movement=movement
                )
                movements_allowed[movement] = [accepted, next_movement, horizontal]

            elif movement == 'orientation':
                accepted_movement, next_movement, horizontal= movements.change_orientation(
                    horizontal=horizontal,
                    walls_position=self.walls_position,
                    base_labyrinth=self.labyrinth,
                    actual_position=ap
                )
                accepted = self.check_if_accepted(
                    accepted_movement=accepted_movement,
                    next_movement_initial=next_movement,
                    used_positions=used_positions,
                    forbidden_movement=forbidden_movement,
                    movement=movement
                )
                movements_allowed[movement] = [accepted, next_movement, horizontal]

        # print(movements_allowed)
        return movements_allowed

    def check_if_accepted(self, accepted_movement, next_movement_initial, used_positions, forbidden_movement, movement):

        if accepted_movement and next_movement_initial not in used_positions and movement != forbidden_movement:
            return True

        return False

    def check_if_end(self, next_movement_initial):
        for mov in next_movement_initial:
            if mov == self.end_position:
                return True

        return False

    def execute_movement(self, next_movement, horizontal, movement, movements_allowed, nom, used_positions):

            movements_allowed[nom] = movement

            used_positions.append(next_movement)
            forbidden_movement = self.incompatibility[movement]
            ap = next_movement
            nom = nom + 1

            if movement == 'orientation':
                if horizontal:
                    horizontal = False
                else:
                    horizontal = True

            return ap, horizontal, forbidden_movement, used_positions, nom, movements_allowed

    def play(self, forbidden_movement, used_positions, horizontal, ap, nom, movements_allowed, tree, games):

        iteration = self.check_movements_allowed(forbidden_movement, used_positions, horizontal, ap)

        for movement, elements in iteration.items():
            if elements[0]:
                next_movement = elements[1]
                horizontal = elements[2]
                used_positions_copy = used_positions.copy()
                nom_copy = nom
                movements_allowed_copy = movements_allowed.copy()

                ap_copy, horizontal_copy, forbidden_movement_copy, used_positions_copy, new_nom, movements_allowed_copy = self.execute_movement(
                    next_movement=next_movement, horizontal=horizontal, movement=movement,
                    movements_allowed=movements_allowed_copy, nom=nom_copy, used_positions=used_positions_copy)

                treenode.tree(value=new_nom, content=movements_allowed_copy)

                for position in ap_copy:
                    if position == self.end_position:
                        tree[games] = [new_nom, movements_allowed_copy]
                        games += 1


                self.play(forbidden_movement_copy, used_positions_copy, horizontal_copy, ap_copy, new_nom,
                          movements_allowed_copy, tree, games)

        return tree
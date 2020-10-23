import math


class Animal:
    def __init__(self, move_range):
        self.position = None
        self.move_range = move_range

    def distance_to(self, animal) -> float:
        # COMMIT_COMMENT Bug fix - plus sign in the second bracket changed into minus sign.
        return math.sqrt((self.position[0] - animal.position[0]) ** 2 + (self.position[1] - animal.position[1]) ** 2)

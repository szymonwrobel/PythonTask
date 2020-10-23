import math
from Animal import Animal
from Sheep import Sheep


class Wolf (Animal):
    def __init__(self, move_range):
        super().__init__(move_range)
        self.position = [0.0, 0.0]

    #COMMIT_COMMENT Function's name changed
    def move(self, sheep):
        distance = self.distance_to(sheep)
        x0, y0 = self.position
        x1, y1 = sheep.position

        #COMMIT_COMMENT Bug in the formula fixed
        self.position = [x0 + self.move_range * (x1 - x0) / distance,
                         y0 + self.move_range * (y1 - y0) / distance]
        #COMMIT_COMMENT Deleted "debug print" as it already works

    #COMMIT_COMMENT Function added as it was neccessary
    def eat_sheep(self, unlucky_sheep, sheeps):
        self.position = unlucky_sheep.position
        unlucky_sheep.sheep_killed()
        sheeps.remove(unlucky_sheep)


    def find_closest_sheep(self, sheeps) -> Sheep:
        #COMMIT_COMMENT Variable name distance changed to lowest_distance
        lowest_distance = self.distance_to(sheeps[0])
        closest_sheep = sheeps[0]
        for sheep in sheeps:
            # COMMIT_COMMENT <= sign turned into < as it changes nothing bad and
            # doesnt override variables if the distances are equal
            if self.distance_to(sheep) < lowest_distance:
                lowest_distance = self.distance_to(sheep)
                closest_sheep = sheep
        return closest_sheep

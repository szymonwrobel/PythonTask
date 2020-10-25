import math
from Animal import Animal
from Sheep import Sheep


class Wolf (Animal):
    def __init__(self, move_range):
        super().__init__(move_range)
        self.position = [0.0, 0.0]

    def move(self, sheep):
        distance = self.distance_to(sheep)
        x0, y0 = self.position
        x1, y1 = sheep.position

        self.position = [x0 + self.move_range * (x1 - x0) / distance,
                         y0 + self.move_range * (y1 - y0) / distance]

    def eat_sheep(self, unlucky_sheep, sheeps):
        self.position = unlucky_sheep.position
        unlucky_sheep.sheep_killed()


    def find_closest_sheep(self, sheeps) -> Sheep:
        for sheep in sheeps:
            if sheep.alive:
                lowest_distance = self.distance_to(sheep)
                closest_sheep = sheep
                break

        for sheep in sheeps:
            if sheep.alive and self.distance_to(sheep) < lowest_distance:
                lowest_distance = self.distance_to(sheep)
                closest_sheep = sheep
        return closest_sheep

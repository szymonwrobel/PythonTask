import math
from Animal import Animal
from Sheep import Sheep


class Wolf (Animal):
    def __init__(self, move_range):
        super().__init__(move_range)
        self.position = [0.0, 0.0]

    def move_to(self, sheep):
        distance = self.distance_to(sheep)
        x0, y0 = self.position
        x1, y1 = sheep.position

        self.position = [x0 + self.move_range ** 2 * (x1 - x0) / distance,
                         y0 + self.move_range ** 2 * (y1 - y0) / distance]
        d = math.sqrt((self.position[0] - x0) ** 2 + (self.position[1] + y0) ** 2)
        print(f"Wolf moved by: {d}")

    def find_closest_sheep(self, sheeps) -> Sheep:
        distance = self.distance_to(sheeps[0])
        closest_sheep = sheeps[0]
        for sheep in sheeps:
            if self.distance_to(sheep) <= distance:
                distance = self.distance_to(sheep)
                closest_sheep = sheep
        return closest_sheep

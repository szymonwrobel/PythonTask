import math
from Animal import Animal
from Sheep import Sheep
import FileWriter as fw
import logging


class Wolf (Animal):
    def __init__(self, move_range):
        super().__init__(move_range)
        self.position = [0.0, 0.0]

    def move(self, sheep, log_level):
        fw.write_to_log(f"Function Wolf.move(self, sheep, log_level) invoked with argument self={self}, sheep={sheep}, log_level={log_level}.", logging.DEBUG, log_level)
        distance = self.distance_to(sheep, log_level)
        fw.write_to_log(f"Function Wolf.distance_to(self, animal, log_level) returned {distance}.", logging.DEBUG, log_level)
        x0, y0 = self.position
        x1, y1 = sheep.position

        self.position = [x0 + self.move_range * (x1 - x0) / distance,
                         y0 + self.move_range * (y1 - y0) / distance]

    def eat_sheep(self, unlucky_sheep, sheeps, log_level):
        fw.write_to_log(f"Function Wolf.eat_sheep(self, unlucky_sheep, sheeps, log_level) invoked with argument self={self}, unlucky_sheep={unlucky_sheep}, sheeps={sheeps}, log_level={log_level}.", logging.DEBUG, log_level)
        self.position = unlucky_sheep.position
        unlucky_sheep.sheep_killed(log_level)
        fw.write_to_log(f"Function Sheep.sheep_killed(self, log_level) returned None.", logging.DEBUG, log_level)


    def find_closest_sheep(self, sheeps, log_level) -> Sheep:
        fw.write_to_log(f"Function Wolf.find_closest_sheep(self, sheeps, log_level) invoked with argument self={self}, sheeps={sheeps}, log_level={log_level}.", logging.DEBUG, log_level)
        for sheep in sheeps:
            if sheep.alive:
                lowest_distance = self.distance_to(sheep, log_level)
                fw.write_to_log(f"Function Wolf.distance_to(self, animal, log_level) returned {lowest_distance}.", logging.DEBUG, log_level)
                closest_sheep = sheep
                break

        for sheep in sheeps:
            distance = self.distance_to(sheep, log_level)
            fw.write_to_log(f"Function Wolf.distance_to(self, animal, log_level) returned {distance}.", logging.DEBUG, log_level)
            if sheep.alive and distance < lowest_distance:
                lowest_distance = self.distance_to(sheep, log_level)
                fw.write_to_log(f"Function Wolf.distance_to(self, animal, log_level) returned {lowest_distance}.", logging.DEBUG, log_level)
                closest_sheep = sheep
        return closest_sheep

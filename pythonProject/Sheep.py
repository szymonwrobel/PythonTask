import random as rand
from Animal import Animal
import FileWriter as fw
import logging


class Sheep (Animal):
    def __init__(self, init_pos_lim, move_range, id):
        super().__init__(move_range)
        self.position = [rand.uniform(-init_pos_lim, init_pos_lim),
                         rand.uniform(-init_pos_lim, init_pos_lim)]
        self.id = id
        self.alive = True

    def move(self, log_level):
        fw.write_to_log(f"Function Sheep.move(self, log_level) invoked with argument self={self}, log_level={log_level}.", logging.DEBUG, log_level)
        direction = rand.randint(1, 4)
        if direction == 1:
            self.position[0] += self.move_range
        elif direction == 2:
            self.position[0] -= self.move_range
        elif direction == 3:
            self.position[1] += self.move_range
        elif direction == 4:
            self.position[1] -= self.move_range

    def sheep_killed(self, log_level):
        fw.write_to_log(f"Function Sheep.sheep_killed(self, log_level) invoked with argument self={self}, log_level={log_level}.", logging.DEBUG, log_level)
        self.alive = False
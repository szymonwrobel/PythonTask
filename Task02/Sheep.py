import random as rand
from Animal import Animal
import FileWriter as fw
import logging


class Sheep (Animal):
    def __init__(self, init_pos_lim, move_range, id, log_level):
        super().__init__(move_range)
        self.position = [rand.uniform(-init_pos_lim, init_pos_lim),
                         rand.uniform(-init_pos_lim, init_pos_lim)]
        self.id = id
        self.alive = True
        fw.write_to_log(f"The starting position of the sheep with id={self.id} has been set to ({self.position[0]}, {self.position[1]}).", logging.INFO, log_level)

    def move(self, log_level):
        fw.write_to_log(f"The function Sheep.move(self, log_level) invoked with argument self={self}, log_level={log_level}.", logging.DEBUG, log_level)
        x0, y0 = self.position
        direction = rand.randint(1, 4)
        if direction == 1:
            self.position[0] += self.move_range
        elif direction == 2:
            self.position[0] -= self.move_range
        elif direction == 3:
            self.position[1] += self.move_range
        elif direction == 4:
            self.position[1] -= self.move_range
        fw.write_to_log(f"The sheep with id={self.id} has moved from ({x0}, {y0}) to ({self.position[0]}, {self.position[1]}).", logging.INFO, log_level)

    def sheep_killed(self, log_level):
        fw.write_to_log(f"The function Sheep.sheep_killed(self, log_level) invoked with argument self={self}, log_level={log_level}.", logging.DEBUG, log_level)
        fw.write_to_log(f"The sheep with id={self.id} has been eaten.", logging.INFO, log_level)
        self.alive = False
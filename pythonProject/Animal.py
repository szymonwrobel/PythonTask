import math
import FileWriter as fw
import logging

class Animal:
    def __init__(self, move_range):
        self.position = None
        self.move_range = move_range

    def distance_to(self, animal, log_level) -> float:
        fw.write_to_log(f"The function Animal.distance_to(self, animal) invoked with arguments self={self}, animal={animal}, log_level={log_level}.", logging.DEBUG, log_level)
        return math.sqrt((self.position[0] - animal.position[0]) ** 2 + (self.position[1] - animal.position[1]) ** 2)

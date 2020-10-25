import random as rand
from Animal import Animal


class Sheep (Animal):
    def __init__(self, init_pos_lim, move_range, id):
        super().__init__(move_range)
        self.position = [rand.uniform(-init_pos_lim, init_pos_lim),
                         rand.uniform(-init_pos_lim, init_pos_lim)]
        self.id = id
        self.alive = True

    def move(self):
        direction = rand.randint(1, 4)
        if direction == 1:
            self.position[0] += self.move_range
        elif direction == 2:
            self.position[0] -= self.move_range
        elif direction == 3:
            self.position[1] += self.move_range
        elif direction == 4:
            self.position[1] -= self.move_range

    def sheep_killed(self):
        self.alive = False
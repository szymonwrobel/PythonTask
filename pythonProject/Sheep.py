import random as rand
from Animal import Animal


class Sheep (Animal):
    #COMMIT_COMMENT Added id and life status
    def __init__(self, init_pos_lim, move_range, id):
        super().__init__(move_range)
        # COMMIT_COMMENT Strange implementation of rand.random changed to rand.uniform
        self.position = [rand.uniform(-init_pos_lim, init_pos_lim),
                         rand.uniform(-init_pos_lim, init_pos_lim)]
        self.id = id
        self.alive = True

    def move(self):
        direction = rand.randint(1, 4)
        # COMMIT_COMMENT Bug fix - Incorrect if deleted.
        if direction == 1:
            self.position[0] += self.move_range
        elif direction == 2:
            self.position[0] -= self.move_range
        elif direction == 3:
            self.position[1] += self.move_range
        elif direction == 4:
            self.position[1] -= self.move_range

    #COMMIT_COMMENT Added function which changes alive status
    def sheep_killed(self):
        self.alive = False
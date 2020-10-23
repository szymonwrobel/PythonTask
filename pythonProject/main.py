from Sheep import Sheep
from Wolf import Wolf


sheep_move_dist = 0.5
wolf_move_dist = 2.0
turn_limit = 50


def setup(sheep_no, init_pos_lim):
    sheep_list = [Sheep(init_pos_lim, sheep_move_dist, x)
                  for x in range(sheep_no)]
    wolf = Wolf(wolf_move_dist)
    return sheep_list, wolf


def simulate(wolf, sheeps):
    for turn in range(turn_limit):
        #COMMIT_COMMENT If added to end the simulation if there is no sheep left
        # Also handling index out of range error in Wolf.distance_to function if
        # there is no sheep with index 0
        if (len(sheeps) == 0):
            return
        for sheep in sheeps:
            sheep.move()
        closest_sheep = wolf.find_closest_sheep(sheeps)
        if wolf.distance_to(closest_sheep) <= wolf.move_range:
            #COMMIT_COMMENT Changed this if
            wolf.eat_sheep(closest_sheep, sheeps)
        else:
            wolf.move(closest_sheep)

        log(turn + 1, wolf, sheeps, closest_sheep)


#COMMIT_COMMENT Changed wolf's position display, information about the eaten
# sheep and formatted output
def log(turn_count, wolf, sheeps, closest_sheep):
    print(f"Turn no: {turn_count}")
    print(f"Wolf position: ({round(wolf.position[0], 3)}, {round(wolf.position[1], 3)})")
    if (closest_sheep.alive == False):
        print(f"The sheep with number {closest_sheep.id} was eaten!")
    print(f"Sheeps alive: {len(sheeps)}")
    print("------------------------------\n")


def __main__():
    init_pos_limit = 10.0
    sheep_nr = 15

    sheeps, wolf = setup(sheep_nr, init_pos_limit)
    simulate(wolf, sheeps)


if __name__ == '__main__':
    __main__()

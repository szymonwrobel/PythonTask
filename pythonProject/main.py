from Sheep import Sheep
from Wolf import Wolf


sheep_move_dist = 0.5
wolf_move_dist = 2.0
turn_limit = 50


def setup(sheep_no, init_pos_lim):
    sheep_list = [Sheep(init_pos_lim, sheep_move_dist) for _ in range(sheep_no)]
    wolf = Wolf(wolf_move_dist)
    return sheep_list, wolf


def simulate(wolf, sheeps):
    for turn in range(turn_limit):
        for sheep in sheeps:
            sheep.move()
        closest_sheep = wolf.find_closest_sheep(sheeps)
        log(turn + 1, wolf, sheeps)
        if wolf.distance_to(closest_sheep) <= wolf.move_range:
            sheeps.remove(closest_sheep)
        else:
            wolf.move_to(closest_sheep)


def log(turn_count, wolf, sheeps):
    print(f"Turn no: {turn_count}")
    print(f"Wolf position x: {wolf.position[0]}, y: {wolf.position[1]}")
    i = 1
    print(f"Sheeps alive: {len(sheeps)}")
    for sh in sheeps:
        print(f"Sheep no. {i}, position x: {sh.position[0]}, y: {sh.position[1]}, "
              f"distance to wolf: {sh.distance_to(wolf)}")
        i += 1


def __main__():
    init_pos_limit = 10.0
    sheep_nr = 15

    sheeps, wolf = setup(sheep_nr, init_pos_limit)
    simulate(wolf, sheeps)


if __name__ == '__main__':
    __main__()

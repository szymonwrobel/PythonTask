from Sheep import Sheep
from Wolf import Wolf
import FileWriter
import argparse

def check_positive(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
    return ivalue

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--config', help='set a config file where init_pos_limit, sheep_move_dist and wolf_move_dist are stored.', metavar='FILE', dest='config_file' )
parser.add_argument('-d', '--dir', help='set a directory to save files', metavar='DIR', dest='directory')
parser.add_argument('-l', '--log', help='set a level of events to be stored in a journal', metavar='LEVEL', dest='log_level')
parser.add_argument('-r', '--rounds', help='set a number of rounds', metavar='NUM', dest='turn_limit', type=check_positive)
parser.add_argument('-s', '--sheep', help='set a number of sheep in the simulation', metavar='NUM', dest='sheep_nr', type=check_positive)
parser.add_argument('-w', '--wait', action='store_true', help='wait for user\'s input after every round', dest='wait_arg')
args = parser.parse_args()

sheep_move_dist = 0.5
wolf_move_dist = 2.0
turn_limit = 50

def setup(sheep_no, init_pos_lim):
    sheep_list = [Sheep(init_pos_lim, sheep_move_dist, x)
                  for x in range(sheep_no)]
    wolf = Wolf(wolf_move_dist)
    return sheep_list, wolf

def get_alive_sheeps(sheeps):
    i = 0
    for sheep in sheeps:
        if sheep.alive == True:
            i = i + 1
    return i

def simulate(wolf, sheeps):
    for turn in range(turn_limit):
        if get_alive_sheeps(sheeps) == 0:
            return
        for sheep in sheeps:
            if sheep.alive == True:
                sheep.move()
        closest_sheep = wolf.find_closest_sheep(sheeps)
        if wolf.distance_to(closest_sheep) <= wolf.move_range:
            wolf.eat_sheep(closest_sheep, sheeps)
        else:
            wolf.move(closest_sheep)

        log(turn + 1, wolf, sheeps, closest_sheep)
        FileWriter.write_to_json(turn + 1, wolf, sheeps)
        FileWriter.write_to_csv(turn + 1, get_alive_sheeps(sheeps))

def log(turn_count, wolf, sheeps, closest_sheep):
    print(f"Turn no: {turn_count}")
    print(f"Wolf position: ({round(wolf.position[0], 3)}, {round(wolf.position[1], 3)})")
    if closest_sheep.alive == False:
        print(f"The sheep with number {closest_sheep.id} was eaten!")
    print(f"Sheeps alive: {get_alive_sheeps(sheeps)}")
    print("------------------------------\n")


if __name__ == '__main__':
    init_pos_limit = 10.0
    sheep_nr = 15

    sheeps, wolf = setup(sheep_nr, init_pos_limit)
    simulate(wolf, sheeps)

from Sheep import Sheep
from Wolf import Wolf
import FileWriter as fw
import argparse
from configparser import ConfigParser
import msvcrt
import logging

sheep_move_dist = 0.5
wolf_move_dist = 2.0
round_limit = 50

def check_positive(value):
    try:
        ivalue = int(value)
    except (ValueError, TypeError):
        raise argparse.ArgumentTypeError("%s is an invalid positive int value." % value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
    return ivalue

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--config', help='set a config file where init_pos_limit, sheep_move_dist and wolf_move_dist are stored.', metavar='FILE', dest='config_file')
parser.add_argument('-d', '--dir', help='set a directory to save files', metavar='DIR', dest='directory')
parser.add_argument('-l', '--log', help='set a level of events (DEBUG|INFO|WARNING|ERROR|CRITICAL) to be stored in a journal', metavar='LEVEL', dest='log_level')
parser.add_argument('-r', '--rounds', help='set a number of rounds', metavar='NUM', dest='round_limit', type=check_positive)
parser.add_argument('-s', '--sheep', help='set a number of sheep in the simulation', metavar='NUM', dest='sheep_nr', type=check_positive)
parser.add_argument('-w', '--wait', action='store_true', help='wait for user\'s input after every round', dest='wait')
args = parser.parse_args()

def setup(sheep_no, init_pos_lim):
    fw.write_to_log(f"The function setup(sheep_no, init_pos_lim) invoked with arguments sheep_no={sheep_no}, init_pos_lim={init_pos_lim}, log_level={log_level}.", logging.DEBUG, log_level)
    sheep_list = [Sheep(init_pos_lim, sheep_move_dist, x, log_level)
                  for x in range(sheep_no)]
    wolf = Wolf(wolf_move_dist, log_level)
    return sheep_list, wolf

def get_alive_sheeps(sheeps):
    fw.write_to_log(f"The function get_alive_sheeps(sheeps) invoked with argument sheeps={sheeps}.", logging.DEBUG, log_level)
    i = 0
    for sheep in sheeps:
        if sheep.alive == True:
            i = i + 1
    return i

def simulate(wolf, sheeps, directory, wait):
    fw.write_to_log(f"The function simulate(wolf, sheeps, directory, wait) invoked with arguments wolf={wolf}, sheeps={sheeps}, directory={directory}, wait={wait}.", logging.DEBUG, log_level)
    for round in range(round_limit):
        if get_alive_sheeps(sheeps) == 0:
            fw.write_to_log(f"The function get_alive_sheeps(sheeps) returned 0.", logging.DEBUG, log_level)
            return
        for sheep in sheeps:
            if sheep.alive == True:
                sheep.move(log_level)
                fw.write_to_log(f"The function Sheep.move() returned None.", logging.DEBUG, log_level)
        closest_sheep = wolf.find_closest_sheep(sheeps, log_level)
        fw.write_to_log(f"The function Wolf.find_closest_sheep(sheeps) returned closest_sheep={closest_sheep}.", logging.DEBUG, log_level)
        wolfs_distance_to_closest_sheep = wolf.distance_to(closest_sheep, log_level)
        fw.write_to_log(f"The function Wolf.distance_to(self, animal, log_level) returned {wolfs_distance_to_closest_sheep}.", logging.DEBUG, log_level)
        if wolfs_distance_to_closest_sheep <= wolf.move_range:
            wolf.eat_sheep(closest_sheep, sheeps, log_level)
            fw.write_to_log(f"The function Wolf.eat_sheep(closest_sheep, sheeps) returned None.", logging.DEBUG, log_level)
        else:
            fw.write_to_log(f"The wolf now follows the sheep with id={closest_sheep.id}.", logging.INFO, log_level)
            wolf.move(closest_sheep, log_level)
            fw.write_to_log(f"The function Wolf.move(closest_sheep) returned None.", logging.DEBUG, log_level)

        alive_sheeps = get_alive_sheeps(sheeps)
        fw.write_to_log(f"The function get_alive_sheeps(sheeps) returned alive_sheeps={alive_sheeps}.", logging.DEBUG, log_level)

        log(round + 1, wolf, sheeps, closest_sheep, alive_sheeps)
        fw.write_to_log(f"The function log(round_count, wolf, sheeps, closest_sheep, alive_sheeps) returned None.", logging.DEBUG, log_level)
        fw.write_to_json(round + 1, wolf, sheeps, directory, log_level)
        fw.write_to_log(f"The function write_to_json(round_number, wolf, sheeps, directory) returned None.", logging.DEBUG, log_level)
        fw.write_to_csv(round + 1, alive_sheeps, directory, log_level)
        fw.write_to_log(f"The function write_to_csv(round_number, alive_sheeps, directory) returned None.", logging.DEBUG, log_level)
        
        if wait:
            msvcrt.getch()

def log(round_count, wolf, sheeps, closest_sheep, alive_sheeps):
    fw.write_to_log(f"The function log(round_count, wolf, sheeps, closest_sheep, alive_sheeps) invoked with arguments round_count={round_count}, wolf={wolf}, sheeps={sheeps}, closest_sheep={closest_sheep}, alive_sheeps={alive_sheeps}.", logging.DEBUG, log_level)
    print(f"Round no: {round_count}")
    print(f"Wolf position: ({round(wolf.position[0], 3)}, {round(wolf.position[1], 3)})")
    if closest_sheep.alive == False:
        print(f"The sheep with number {closest_sheep.id} was eaten!")
    print(f"Sheep alive: {alive_sheeps}")
    print("------------------------------\n")

def parse_config_file(file):
    fw.write_to_log(f"The function parse_config_file(file) invoked with arguments file={file}.", logging.DEBUG, log_level)
    config = ConfigParser()
    config.read(file)
    init_pos = config.get('Terrain', 'InitPosLimit')
    sheep_move = config.get('Movement', 'SheepMoveDist')
    wolf_move = config.get('Movement', 'WolfMoveDist')

    try:
        f_init_pos = float(init_pos)
        f_sheep_move = float(sheep_move)
        f_wolf_move = float(wolf_move)
    except (ValueError, TypeError):
        fw.write_to_log(f"At least one of the variables in the chosen config file could not be converted to a float.", logging.CRITICAL, log_level)
        raise ValueError("An input provided in a config file must be a float.")

    if f_init_pos <= 0 or f_sheep_move <= 0 or f_wolf_move <= 0:
        fw.write_to_log(f"At least one of the variables in the chosen config file was less then or equal to 0.", logging.CRITICAL, log_level)
        raise ValueError("An input provided in a config file must be greater than 0.")

    return f_init_pos, f_sheep_move, f_wolf_move    

if __name__ == '__main__':
    init_pos_limit = 10.0
    sheep_nr = 15
    directory = "pythonProject/"
    wait = False
    log_level = logging.NOTSET

    if args.log_level:
        if args.log_level == "DEBUG":
            log_level = logging.DEBUG
        elif args.log_level == "INFO":
            log_level = logging.INFO
        elif args.log_level == "WARNING":
            log_level = logging.WARNING
        elif args.log_level == "ERROR":
            log_level = logging.ERROR
        elif args.log_level == "CRITICAL":
            log_level = logging.CRITICAL
        else:
            raise ValueError("Events' level should be one of the following: DEBUG, INFO, WARNING, ERROR, CRITICAL.")
        file_path = fw.get_file_path(directory, "chase.log")
        logging.basicConfig(filename=file_path, format="%(asctime)s: %(levelname)s: %(message)s", level=log_level)
        f = open(file_path, "w+")
        f.close()
    if args.config_file:
        init_pos_limit, sheep_move_dist, wolf_move_dist = parse_config_file(args.config_file)
        fw.write_to_log(f"The function parse_config_file(file) returned init_pos_limit={init_pos_limit}, sheep_move_dist={sheep_move_dist}, wolf_move_dist={wolf_move_dist}.", logging.DEBUG, log_level)
    if args.directory:
        directory = args.directory
    if args.round_limit:
        round_limit = args.round_limit
    if args.sheep_nr:
        sheep_nr = args.sheep_nr
    if args.wait:
        wait = args.wait

    if sheep_nr > 100 and round_limit > 100:
        fw.write_to_log(f"You've set sheep_nr variable to {sheep_nr} and round_limit variable to {round_limit}. Consider choosing lower numbers for better performance.", logging.WARNING, log_level)
    
    sheeps, wolf = setup(sheep_nr, init_pos_limit)
    fw.write_to_log(f"The function setup(sheep_no, init_pos_lim) returned sheeps={sheeps}, wolf={wolf}.", logging.DEBUG, log_level)
    simulate(wolf, sheeps, directory, wait)
    fw.write_to_log(f"The function simulate(wolf, sheeps, directory, wait) returned None.", logging.DEBUG, log_level)

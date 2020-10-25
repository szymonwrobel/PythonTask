from Sheep import Sheep
from Wolf import Wolf
import json


sheep_move_dist = 0.5
wolf_move_dist = 2.0
turn_limit = 50

def write_to_json(round_number, wolf, sheeps):
    sheeps_info = []
    for sheep in sheeps:
        if sheep.alive == True:
            sheeps_info.append(f"Sheep no {sheep.id}: {sheep.position[0]}, {sheep.position[1]}")
        else:
            sheeps_info.append(f"Sheep no {sheep.id}: null")
    content = {
        "round_no": round_number,
        "wolf_pos": f"{wolf.position[0]}, {wolf.position[1]}",
        "sheeps_info": sheeps_info
    }
    if round_number == 1:
        file = open("pos.json", "w")
    else:
        file = open("pos.json", "a")
    file.write(json.dumps(content, indent = 2))
    file.close()

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
        write_to_json(turn + 1, wolf, sheeps)

def log(turn_count, wolf, sheeps, closest_sheep):
    print(f"Turn no: {turn_count}")
    print(f"Wolf position: ({round(wolf.position[0], 3)}, {round(wolf.position[1], 3)})")
    if closest_sheep.alive == False:
        print(f"The sheep with number {closest_sheep.id} was eaten!")
    print(f"Sheeps alive: {get_alive_sheeps(sheeps)}")
    print("------------------------------\n")


def __main__():
    init_pos_limit = 10.0
    sheep_nr = 15

    sheeps, wolf = setup(sheep_nr, init_pos_limit)
    simulate(wolf, sheeps)


if __name__ == '__main__':
    __main__()

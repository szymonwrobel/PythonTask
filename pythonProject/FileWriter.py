import json
import csv
import os

def write_to_csv(round_number, alive_sheeps, directory):
    file_path = get_file_path(directory, "alive.csv")
    
    # This if clears the file
    if round_number == 1:
        f = open(file_path, "w+")
        f.close()
    with open(file_path, "a", newline="") as csvfile:
        fieldnames = ["round_no", "alive_sheep"]
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writerow({"round_no": round_number, "alive_sheep": alive_sheeps})

def write_to_json(round_number, wolf, sheeps, directory):
    file_path = get_file_path(directory, "pos.json")

    sheeps_info = []
    for sheep in sheeps:
        if sheep.alive == True:
            sheeps_info.append(f"Sheep no {sheep.id}: {sheep.position[0]}, {sheep.position[1]}")
        else:
            sheeps_info.append(f"Sheep no {sheep.id}: null")
    dictionary = {
        "round" + str(round_number): {
        "round_no": round_number,
        "wolf_pos": f"{wolf.position[0]}, {wolf.position[1]}",
        "sheeps_info": sheeps_info
        }
    }
    if round_number == 1:
        f = open(file_path, "w+")
        f.close()
        file = open(file_path, "a+")
        file.write(json.dumps(dictionary, indent = 2))
        file.close()
    else:
        with open(file_path) as file:
            data = json.load(file)
        data.update(dictionary)
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)

def get_file_path(directory, file_name):
    file_dir = os.getcwd() + '\\' + directory
    if not os.path.exists(file_dir):
        os.mkdir(file_dir)
    return file_dir + '\\' + file_name
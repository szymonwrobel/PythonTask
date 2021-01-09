import json
import csv

def write_to_csv(round_number, alive_sheeps):
    # This if clears the file
    if round_number == 1:
        f = open("alive.csv", "w+")
        f.close()
    with open("alive.csv", "a", newline="") as csvfile:
        fieldnames = ["round_no", "alive_sheep"]
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writerow({"round_no": round_number, "alive_sheep": alive_sheeps})

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
        f = open("pos.json", "w+")
        f.close()
    file = open("pos.json", "a+")
    file.write(json.dumps(content, indent = 2))
    file.close()
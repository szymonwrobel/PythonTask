import json
import csv
import os
import logging

def write_to_csv(round_number, alive_sheeps, directory, log_level):
    write_to_log(f"The function write_to_csv(round_number, alive_sheeps, directory, log_level) invoked with argument round_number={round_number}, alive_sheeps={alive_sheeps}, directory={directory}, log_level={log_level}.", logging.DEBUG, log_level)
    file_path = get_file_path(directory, "alive.csv")
    write_to_log(f"The function get_file_path(directory, file_name) returned {file_path}.", logging.DEBUG, log_level)
    
    # This if clears the file
    if round_number == 1:
        f = open(file_path, "w+")
        f.close()
    with open(file_path, "a", newline="") as csvfile:
        fieldnames = ["round_no", "alive_sheep"]
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writerow({"round_no": round_number, "alive_sheep": alive_sheeps})

def write_to_json(round_number, wolf, sheeps, directory, log_level):
    write_to_log(f"The function write_to_json(round_number, wolf, sheeps, directory, log_level) invoked with argument round_number={round_number}, wolf={wolf}, sheeps={sheeps}, directory={directory}, log_level={log_level}.", logging.DEBUG, log_level)
    file_path = get_file_path(directory, "pos.json")
    write_to_log(f"The function get_file_path(directory, file_name) returned {file_path}.", logging.DEBUG, log_level)

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
        "sheep_info": sheeps_info
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

def write_to_log(message, message_log_level, log_level):
    log_dictionary = {
        logging.DEBUG: 10,
        logging.INFO: 20,
        logging.WARNING: 30,
        logging.ERROR: 40,
        logging.CRITICAL: 50,
        logging.NOTSET: 0
    }
    if log_dictionary[message_log_level] >= log_dictionary[log_level] and log_dictionary[log_level] != 0:
        if message_log_level == logging.DEBUG:
            logging.debug(message)
        elif message_log_level == logging.INFO:
            logging.info(message)
        elif message_log_level == logging.WARNING:
            logging.warning(message)
        elif message_log_level == logging.ERROR:
            logging.error(message)
        elif message_log_level == logging.CRITICAL:
            logging.critical(message)

def get_file_path(directory, file_name):
    file_dir = os.getcwd() + '\\' + directory
    if not os.path.exists(file_dir):
        os.mkdir(file_dir)
    return file_dir + '\\' + file_name
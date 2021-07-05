import json
import os
import errno

def writeToCSV(file_name, data_map, file_mode="w+"):
    
    with open(file_name, file_mode) as out_file:
        out_file.write(json.dumps(data_map))


def readFromCSV(file_name, file_mode="r+"):
    with open(file_name, file_mode) as in_file:
        return json.loads(in_file.read())


def create_directory(filename):

    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
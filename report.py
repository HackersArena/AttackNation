import os

def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    return

def write_file(path, data):
    f = open(path, 'w+')
    f.write(data)
    f.close()
    return




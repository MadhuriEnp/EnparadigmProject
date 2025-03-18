
import os

def write_to_file(data, filename='shared_data.txt'):
    with open(filename, 'w') as f:
        f.write(data)

def read_from_file(filename='shared_data.txt'):
    if not os.path.exists(filename):
        return None
    with open(filename, 'r') as f:
        return f.read()

def delete_file(filename='shared_data.txt'):
    if os.path.exists(filename):
        os.remove(filename)

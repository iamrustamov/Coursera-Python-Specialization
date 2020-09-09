import sys
import argparse
import os
import tempfile
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key')
    parser.add_argument('--val')
    return parser


def load_data():
    try:
        with open(storage_path, 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        with open(storage_path, 'w') as f:
            json.dump({}, f)
            return {}


def write_data(key, val):
    data = load_data()
    if key in data:
        data[key].append(val)
    else:
        data.update(dict([(key, [val])]))
    with open(storage_path, 'w') as f:
        json.dump(data, f)


def print_data(key):
    data = load_data()
    if key in data:
        print(", ".join(data[key]))
    else:
        print("None")


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.val:
        write_data(namespace.key, namespace.val)
    else:
        print_data(namespace.key)

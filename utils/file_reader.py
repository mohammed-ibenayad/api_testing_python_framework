import json
from pathlib import Path

# Base path detected dynamically regardless of the OS.
BASE_PATH = Path.cwd().joinpath('tests', 'data')


def read_file(file_name):
    path = get_file_with_json_extension(file_name)
    with path.open(mode='r') as f:
        return json.load(f)


def get_file_with_json_extension(file_name):
    return BASE_PATH.joinpath(file_name) if '.json' in file_name else BASE_PATH.joinpath(f'{file_name}.json')

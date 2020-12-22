import os

import yaml

BASE_FOLDER = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def get_config():
    config_file = os.path.join(BASE_FOLDER, 'config.yaml')

    with open(config_file, "r") as stream:
        return yaml.safe_load(stream)

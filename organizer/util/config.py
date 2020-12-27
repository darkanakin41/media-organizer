import os
from pathlib import Path
import yaml

from organizer.util.logger import logger

BASE_FOLDER = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def get_config():
    config_paths = [str(Path.home()), BASE_FOLDER]
    if os.getenv('MEDIA_ORGANIZER_CONFIG') is not None:
        config_paths = [os.getenv('MEDIA_ORGANIZER_CONFIG')]

    for config_path in config_paths:
        config_file = os.path.join(config_path, '.media-organizer.yaml')
        try:
            with open(config_file, "r") as stream:
                logger.debug('Config file used: %s', config_file)
                return yaml.safe_load(stream)
        except IOError:
            pass

    raise Exception('No config file found')

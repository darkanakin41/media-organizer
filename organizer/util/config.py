import os
from pathlib import Path
import yaml

from organizer.config import GlobalConfig
from organizer.util.logger import logger

BASE_FOLDER = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def get_config() -> dict:
    """
    Get the configuration
    :return:
    """

    config = GlobalConfig()

    config_paths = [BASE_FOLDER, str(Path.home())]
    if os.getenv('MEDIA_ORGANIZER_CONFIG') is not None:
        config_paths = [os.getenv('MEDIA_ORGANIZER_CONFIG')]

    config_data = None

    for config_path in config_paths:
        config_file = os.path.join(config_path, '.media-organizer.yaml')
        try:
            with open(config_file, "r") as stream:
                logger.debug('Config file used: %s', config_file)
                config_data = yaml.safe_load(stream)
        except IOError:
            pass

    if config_data is None:
        raise Exception('No config file found')

    return config.load(config_data)

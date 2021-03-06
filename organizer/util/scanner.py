import os
import re
from typing import List

from organizer import config
from organizer.util.logger import logger


def scan_folder(folder: str) -> List[str]:
    """
    Scan a folder and retrieve all media files
    :param folder: the folder to scan
    :return: the list of files found
    """
    logger.info("Processing folder %s", folder)
    extensions = config.get('input').get('extensions')
    file_extensions_regex = re.compile(extensions)

    found_files = []

    # pylint: disable=unused-variable
    for root, dirs, files in os.walk(folder):
        found_files += [os.path.join(root, f) for f in files if re.match(file_extensions_regex, f)]

    logger.info("Found %d files", len(found_files))

    return found_files


def is_ignored(file: str) -> bool:
    """
    Check if the given file is ignored
    :param file: the file
    :return: if the file is ignored or not
    """
    for ignored in config.get('input').get('ignored'):
        ignored_regex = re.compile(ignored)
        if re.match(ignored_regex, file):
            return True

    return False

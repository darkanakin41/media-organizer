import os
import sys

import guessit
from rebulk.match import MatchesDict

from organizer.processor.episode_processor import EpisodeProcessor
from organizer.processor.movie_processor import MovieProcessor
from organizer.util.logger import logger


def get_file_target(input_file: str):
    """
    Determine the file target
    :param input_file:
    :return:
    """
    data: MatchesDict = guessit.guessit(input_file)

    processor = None
    if data['type'] == 'movie':
        processor = MovieProcessor()
    elif data['type'] == 'episode':
        processor = EpisodeProcessor()

    if processor is None: # pragma: no cover
        logger.error('No processor for %s', input_file) # pragma: no cover
        sys.exit(1) # pragma: no cover

    output_data = processor.process(input_file, guessit_data=data)
    target = processor.get_output_dir(output_data, guessit_data=data)
    filename = processor.get_output_filename(data, output_data)

    return os.path.join(target, filename)


def sizeof_fmt(num, suffix='B'):
    """
    Get the size formatted
    :param num:
    :param suffix:
    :return:
    """
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.1f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f %s%s" % (num, 'Yi', suffix) # pragma: no cover

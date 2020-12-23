import os
import sys

import guessit
from rebulk.match import MatchesDict

from organizer.processor.episode_processor import EpisodeProcessor
from organizer.processor.movie_processor import MovieProcessor
from organizer.util.logger import logger


def get_file_target(input_file: str):
    data: MatchesDict = guessit.guessit(input_file)

    processor = None
    if data['type'] == 'movie':
        processor = MovieProcessor()
    elif data['type'] == 'episode':
        processor = EpisodeProcessor()

    if processor is None:
        logger.error('No processor for %s' % input_file)
        sys.exit(1)

    output_data = processor.process(input_file, guessit_data=data)
    target = processor.get_output_dir(output_data, guessit_data=data)
    filename = processor.get_output_filename(data, output_data)

    return os.path.join(target, filename)


def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.1f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f %s%s" % (num, 'Yi', suffix)

import logging
import os
import sys

import guessit
from rebulk.match import MatchesDict

from organizer.processor.episode_processor import EpisodeProcessor
from organizer.processor.movie_processor import MovieProcessor


def process_file(input_file:str):
    data: MatchesDict = guessit.guessit(input_file)

    processor = None
    if data['type'] == 'movie':
        processor = MovieProcessor()
    elif data['type'] == 'episode':
        processor = EpisodeProcessor()

    if processor is None:
        logging.error('No processor for %s' % input_file)
        sys.exit(1)

    output_data = processor.process(input_file, guessit_data=data)
    target = processor.get_output_dir(output_data, guessit_data=data)
    filename = processor.get_output_filename(data)
    print("%s --> %s" % (input_file, os.path.join(target, filename)))

def main():
    process_file("Fatman.2020.MULTi.TRUEFRENCH.1080p.BluRay.x264.AC3-Wawacity.vip.mkv")
    process_file("2018.Dieudonne.L'émancipation.mp4")
    process_file("Attack On Titan The Roar of Awakening (2018).mkv")
    process_file("Dexter S01E01 (Dexter).mkv")
    process_file("Assault Lily BOUQUET - s01e01.mkv")
    process_file("Star Trek Lower Decks - s01e01.mkv")

if __name__ == '__main__':
    main()

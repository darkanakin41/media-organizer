import os
from typing import Optional, List

from organizer import tv_db, tv_genres_db, config
from organizer.processor.abstract_processor import AbstractProcessor
from rebulk.match import MatchesDict


class EpisodeProcessor(AbstractProcessor):
    """
    The processor dedicated to Episodes type medias
    """

    def process(self, filename: str, guessit_data: MatchesDict):
        tvdb_data = self._get_tvdb_data(guessit_data['title'])
        if tvdb_data is None:
            return None

        self._update_genres(tvdb_data)

        return tvdb_data

    @staticmethod
    def _get_tvdb_data(title: str) -> Optional[any]:
        results = tv_db.search(title)

        if len(results) == 1:
            return results[0]

        for result in results:
            if result.name == title:
                return result

        return None

    @staticmethod
    def _update_genres(data) -> Optional[any]:
        data.genres = []
        for genre_id in data.genre_ids:
            genre = [tg for tg in tv_genres_db if tg.id == genre_id]
            if len(genre) == 1:
                data.genres.append(genre[0].name)

    @staticmethod
    def get_output_dirs() -> List[dict]:
        dirs = [dir for dir in config.get("output_dirs") if dir.get('type') == 'episode']
        dirs.sort(key=lambda dir: len(dir.get('filters') if dir.get('filters') is not None else []), reverse=True)
        return dirs

    def get_output_dir(self, tvdb_data, guessit_data: MatchesDict = None):
        output_dir = AbstractProcessor.get_output_dir(self, tvdb_data)
        return os.path.join(output_dir, guessit_data['title'], "Saison " + str(guessit_data['season']).zfill(2))

    def get_output_filename(self, guessit_data: MatchesDict, tvdb_data) -> str:
        return '%s - s%02de%02d.%s' % (
            guessit_data['title'],
            guessit_data['season'],
            guessit_data['episode'],
            guessit_data['container']
        )

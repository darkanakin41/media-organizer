from typing import Optional

from organizer import movie_db, movie_genres_db, config
from organizer.processor.abstract_processor import AbstractProcessor
from rebulk.match import MatchesDict


class MovieProcessor(AbstractProcessor):
    """
    The processor dedicated to Movies type medias
    """

    def process(self, filename: str, guessit_data: MatchesDict):
        tvdb_data = self._get_tvdb_data(guessit_data['title'])
        if tvdb_data is None:
            return None

        self._update_genres(tvdb_data)

        return tvdb_data

    @staticmethod
    def _get_tvdb_data(title: str) -> Optional[any]:
        results = movie_db.search(title)

        if len(results) == 1:
            return results[0]

        for result in results:
            if result.title == title:
                return result

        return None

    @staticmethod
    def _update_genres(data) -> Optional[any]:
        data.genres = []
        for genre_id in data.genre_ids:
            genre = [mg for mg in movie_genres_db if mg.id == genre_id]
            if len(genre) == 1:
                data.genres.append(genre[0].name)

    @staticmethod
    def get_output_dirs():
        dirs = [dir for dir in config.get("output_dirs") if dir.get('type') == 'movie']
        dirs.sort(key=lambda dir: len(dir.get('filters') if dir.get('filters') is not None else []), reverse=True)
        return dirs

    def get_output_dir(self, tvdb_data, guessit_data: MatchesDict = None):
        return AbstractProcessor.get_output_dir(self, tvdb_data)

    def get_output_filename(self, guessit_data: MatchesDict, tvdb_data) -> str:
        try:
            year = guessit_data['year']
        except KeyError:
            year = tvdb_data.release_date[0:4]
        return '%s (%s).%s' % (guessit_data['title'], year, guessit_data['container'])

import os

from typing import Optional, List

from rebulk.match import MatchesDict

from organizer import config
from organizer.api import tmdb_api
from organizer.processor.abstract_processor import AbstractProcessor
from organizer.util.translation import translate


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
        results = tmdb_api.tv_endpoint.search(title)

        if len(results) == 1:
            return results[0]

        for result in results:
            if result.name == title:
                return result
            if result.original_language != tmdb_api.tmdb.language:
                if translate(tmdb_api.tmdb.language, result.original_language, title) == result.original_name:
                    return result

        return None

    @staticmethod
    def _update_genres(data) -> Optional[any]:
        data.genres = []
        for genre_id in data.genre_ids:
            genre = [tg for tg in tmdb_api.genre_tv_db if tg.id == genre_id]
            if len(genre) == 1:
                data.genres.append(genre[0].name)

    @staticmethod
    def get_output_dirs() -> List[dict]:
        dirs = [dir for dir in config['output'] if dir['type'] == 'episode']
        dirs.sort(key=lambda dir: len(dir['filters'] if dir['filters'] is not None else []), reverse=True)
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

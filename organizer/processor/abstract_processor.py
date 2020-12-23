import re
from abc import ABC, abstractmethod

from rebulk.match import MatchesDict


class AbstractProcessor(ABC):

    @abstractmethod
    def process(self, filename: str, guessit_data: MatchesDict):
        pass

    @staticmethod
    @abstractmethod
    def get_output_dirs():
        pass

    @staticmethod
    def _output_dir_match_filter(tvdb_data, filters: dict):
        if filters is None:
            return True
        for field in filters.keys():
            regex = re.compile(filters[field])
            try:
                if isinstance(getattr(tvdb_data, field), list):
                    found = False
                    for value in getattr(tvdb_data, field):
                        if regex.match(value):
                            found = True
                    if not found:
                        return False
                else:
                    if not regex.match(getattr(tvdb_data, field)):
                        return False
            except AttributeError:
                return False
        return True

    def get_output_dir(self, tvdb_data):
        for output_dir in self.get_output_dirs():
            if self._output_dir_match_filter(tvdb_data, output_dir.get('filters')):
                return output_dir.get('target')
        return None

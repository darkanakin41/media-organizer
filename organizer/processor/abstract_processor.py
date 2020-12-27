import re
from abc import ABC, abstractmethod

from rebulk.match import MatchesDict


class AbstractProcessor(ABC):
    """
    An abstract media processor
    """

    @abstractmethod
    def get_output_filename(self, guessit_data: MatchesDict, tvdb_data) -> str:
        """
        Get the output file name
        :param guessit_data: the guessit call result
        :param tvdb_data: the data coming from TheTVDB
        :return:
        """

    @abstractmethod
    def process(self, filename: str, guessit_data: MatchesDict):
        """
        Process the given file
        :param filename: the full path of the file
        :param guessit_data: the guessit call result
        :return:
        """

    @staticmethod
    @abstractmethod
    def get_output_dirs():
        """
        Get output dirs
        :return:
        """

    @staticmethod
    def _output_dir_match_filter(tvdb_data, filters: dict):
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
        """
        Get the output dir based on tvdb_datas
        :param tvdb_data: the data coming from TheTVDB
        :return:
        """
        for output_dir in self.get_output_dirs():
            if self._output_dir_match_filter(tvdb_data, output_dir.get('filters')):
                return output_dir.get('target')
        return None # pragma: no cover

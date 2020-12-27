from tmdbv3api import TMDb, Movie, TV, Genre

from organizer import config


class TmDbApi:
    """
    The Movie DB api
    """

    def __init__(self):
        self.config = config['tmdb']
        if self.config['api_key'] is None or self.config['api_key'] == '':
            raise Exception('Please provide an API Key for tmdb configuration')

        self._genre_tv_db_data = None
        self._genre_movie_db_data = None

        self.tmdb = TMDb()
        self.tmdb.api_key = self.config['api_key']
        self.tmdb.language = self.config['language']
        self.tmdb.debug = self.config['debug']

    @property
    def movie_endpoint(self) -> Movie:
        """
        Get the movie endpoint
        :return:
        """
        if self.tmdb is None:
            raise Exception('No TMDB Configured')
        return Movie()

    @property
    def tv_endpoint(self) -> TV:
        """
        Get the tv endpoint
        :return:
        """
        if self.tmdb is None:
            raise Exception('No TMDB Configured')
        return TV()

    @property
    def genre_endpoint(self) -> Genre:
        """
        Get the genre endpoint
        :return:
        """
        if self.tmdb is None:
            raise Exception('No TMDB Configured')
        return Genre()

    @property
    def genre_tv_db(self):
        """
        Get the TV Genre DB Data
        :return:
        """
        if self._genre_tv_db_data is not None:
            return self._genre_tv_db_data

        self._genre_tv_db_data = self.genre_endpoint.tv_list()
        return self._genre_tv_db_data

    @property
    def genre_movie_db(self):
        """
        Get the Movie Genre DB Data
        :return:
        """
        if self._genre_movie_db_data is not None:
            return self._genre_movie_db_data

        self._genre_movie_db_data = self.genre_endpoint.movie_list()
        return self._genre_movie_db_data

from tmdbv3api import TMDb, Movie, TV, Genre

from organizer import config


class TmDbApi:
    """
    The Movie DB api
    """

    def __init__(self):
        self.config = config['tmdb']

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
        return Movie()

    @property
    def tv_endpoint(self) -> TV:
        """
        Get the tv endpoint
        :return:
        """
        return TV()

    @property
    def genre_endpoint(self) -> Genre:
        """
        Get the genre endpoint
        :return:
        """
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

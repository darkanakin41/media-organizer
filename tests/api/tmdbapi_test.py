from tmdbv3api import Movie, TV, Genre

from organizer.api.tmdbapi import TmDbApi
from tests.testutils import array_equals


class TestTmDbApi:
    """
    Test the TMDB Api
    """

    @staticmethod
    def test_movie_endpoint():
        """
        Check the movie endpoint
        :return:
        """
        assert isinstance(TmDbApi().movie_endpoint, Movie)

    @staticmethod
    def test_tv_endpoint():
        """
        Check the TV endpoint
        :return:
        """
        assert isinstance(TmDbApi().tv_endpoint, TV)

    @staticmethod
    def test_genre_endpoint():
        """
        Check the genre endpoint
        :return:
        """
        assert isinstance(TmDbApi().genre_endpoint, Genre)

    @staticmethod
    def test_genre_tv_db():
        """
        Check the TV Genre DB
        :return:
        """
        tmdbapi = TmDbApi()
        assert tmdbapi._genre_tv_db_data is None  # pylint: disable=protected-access

        genre_tv_db_data = tmdbapi.genre_endpoint.tv_list()

        tmp = tmdbapi.genre_tv_db

        array_equals(list(map(lambda x: x.name, tmp)), list(map(lambda x: x.name, genre_tv_db_data)))
        array_equals(list(map(lambda x: x.name, tmdbapi._genre_tv_db_data)),  # pylint: disable=protected-access
                     list(map(lambda x: x.name, genre_tv_db_data)))
        assert tmdbapi.genre_tv_db == tmp

    @staticmethod
    def test_genre_movie_db():
        """
        Check the Movie Genre DB
        :return:
        """
        tmdbapi = TmDbApi()
        assert tmdbapi._genre_movie_db_data is None  # pylint: disable=protected-access

        genre_movie_db_data = tmdbapi.genre_endpoint.movie_list()

        tmp = tmdbapi.genre_movie_db

        array_equals(list(map(lambda x: x.name, tmp)), list(map(lambda x: x.name, genre_movie_db_data)))
        array_equals(list(map(lambda x: x.name, tmdbapi._genre_movie_db_data)),  # pylint: disable=protected-access
                     list(map(lambda x: x.name, genre_movie_db_data)))
        assert tmdbapi.genre_movie_db == tmp

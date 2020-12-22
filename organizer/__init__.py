# -*- coding: utf-8 -*-
from tmdbv3api import TMDb, Movie, TV, Genre

from .__version__ import __version__
from .util.config import get_config

config = get_config()

tmdb = TMDb()
tmdb.api_key = config.get('thetvdb').get('api_key')
tmdb.language = config.get('thetvdb').get('language')
tmdb.debug = config.get('thetvdb').get('debug')

movie_db = Movie()
tv_db = TV()
genre_db = Genre()

tv_genres_db = genre_db.tv_list()
movie_genres_db = genre_db.movie_list()

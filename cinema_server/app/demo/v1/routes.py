# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.cinema import Cinema
from .api.cinema_available import CinemaAvailable
from .api.cinema_id import CinemaId
from .api.cinema_id_snack import CinemaIdSnack
from .api.cinema_id_movie import CinemaIdMovie
from .api.cinema_search import CinemaSearch
from .api.movie import Movie
from .api.movie_id import MovieId
from .api.movie_search import MovieSearch


routes = [
    dict(resource=Cinema, urls=['/cinema'], endpoint='cinema'),
    dict(resource=CinemaAvailable, urls=['/cinema/available'], endpoint='cinema_available'),
    dict(resource=CinemaId, urls=['/cinema/<int:id>'], endpoint='cinema_id'),
    dict(resource=CinemaIdSnack, urls=['/cinema/<int:id>/snack'], endpoint='cinema_id_snack'),
    dict(resource=CinemaIdMovie, urls=['/cinema/<int:id>/movie'], endpoint='cinema_id_movie'),
    dict(resource=CinemaSearch, urls=['/cinema/search'], endpoint='cinema_search'),
    dict(resource=Movie, urls=['/movie'], endpoint='movie'),
    dict(resource=MovieId, urls=['/movie/<int:id>'], endpoint='movie_id'),
    dict(resource=MovieSearch, urls=['/movie/search'], endpoint='movie_search'),
]
# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.all import All
from .api.movie_movie_id import MovieMovieId
from .api.cinema_cinema_id import CinemaCinemaId
from .api.available import Available
from .api.booking import Booking


routes = [
    dict(resource=All, urls=['/all'], endpoint='all'),
    dict(resource=MovieMovieId, urls=['/movie/<int:movie_id>'], endpoint='movie_movie_id'),
    dict(resource=CinemaCinemaId, urls=['/cinema/<int:cinema_id>'], endpoint='cinema_cinema_id'),
    dict(resource=Available, urls=['/available'], endpoint='available'),
    dict(resource=Booking, urls=['/booking'], endpoint='booking'),
]
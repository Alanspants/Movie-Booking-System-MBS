import requests
import json

from ..helper.getCinemaIDBySearch import get_cinema_id_by_search
from ..helper.getMovieIDBySearch import get_movie_id_by_search


def get_movie_cinema_by_name(input):

    reply = ""

    movie_info = get_movie_id_by_search(input)
    if movie_info != False:
        reply += "title: " + movie_info['title']\
                    + "\n" + movie_info['available']\
                    + "Type in: [cinema detail: cinema_id] to check the more detail about cinema\nE.g.: cinema detail: 1"
        return reply
    else:
        reply += "Sorry, there is no matched cinema"
        return reply

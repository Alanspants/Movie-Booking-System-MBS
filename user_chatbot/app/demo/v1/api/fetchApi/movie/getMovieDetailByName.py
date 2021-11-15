import requests
import json

from ..helper.getCinemaIDBySearch import get_cinema_id_by_search
from ..helper.getMovieIDBySearch import get_movie_id_by_search


def get_movie_detail_by_name(input):

    reply = ""

    movie_info = get_movie_id_by_search(input)
    movie_id = movie_info['id']
    # print(cinemas)

    if movie_info != False:
        apiUrl = 'http://127.0.0.1:9090/v1/movie/'+str(movie_id)
        result = requests.get(
            apiUrl
        )
        if result.status_code == 200:
            jsonResult = result.json()
            reply += "Below is the detail about movie [" + jsonResult['title'] + "]\n" \
                     + "Title: " + jsonResult['title'] + "\n" \
                     + "Description: " + jsonResult['description'] + "\n" \
                     + "Cast: " + jsonResult['cast'] + "\n" \
                     + movie_info['available']\
                     + "Type in: [cinema detail: cinema_id] to check the more detail about cinema\nE.g.: cinema detail: 1"
        return reply
    else:
        reply += "Sorry, there is no matched cinema"
        return reply


import requests
import json

from ..helper.getCinemaIDBySearch import get_cinema_id_by_search
from ..helper.getMovieIDBySearch import get_movie_id_by_search


def get_movie_cinema_by_name(input):

    reply = ""

    movies = get_movie_id_by_search(input)

    if len(movies) > 1:
        reply += "I found " + str(len(movies)) + " results of [" + input +  "]:\n"
        for movie in movies:
            reply += "{}: {}\n".format(
                movie['id'],
                movie['title']
            )
        reply += "Try type in more precise cinema name or use precise query [cinema detail: cinema_id].\n"
        reply += "E.g.: Show me some detail about Event Cinemas George Street.\n"
        reply += "E.g.: cinema detail: 0\n"
        return reply
    elif len(movies) == 1:
        id = movies[0]['id']
        apiUrl = 'http://127.0.0.1:9090/v1/movie/' + str(id) + "/cinema"
        result = requests.get(
            apiUrl
        )
        if result.status_code == 200:
            jsonResult = result.json()
            reply += "Below is the cinemas which are now showing [" + movies[0]['title'] + "]\n"
            for temp in jsonResult:
                reply += "{}: {}\n".format(
                    temp['id'],
                    temp['name']
                )
            reply += "Type in: [cinema detail: cinema_id] to check the more detail about cinema\nE.g.: cinema detail: 1"
            return reply
    elif len(movies) == 0:
        reply += "Sorry, there is no matched cinema"
        return reply
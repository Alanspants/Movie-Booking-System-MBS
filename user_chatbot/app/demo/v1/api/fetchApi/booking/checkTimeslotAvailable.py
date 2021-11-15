import requests

from ..helper.getCinemaIDBySearch import get_cinema_id_by_search
from ..helper.getMovieIDBySearch import get_movie_id_by_search


def check_timeslot_available(cinema_name, movie_title, date, timeslot):

    reply = ""

    movies = get_movie_id_by_search(movie_title)

    if len(movies) > 1:
        reply += "I found " + str(len(movies)) + " results of [" + movie_title +  "]:\n"
        for movie in movies:
            reply += "{}: {}\n".format(
                movie['id'],
                movie['title']
            )
        reply += "Try type in more precise movie name.\n"
        reply += "E.g.: No Time To Die.\n"
        return reply
    elif len(movies) == 0:
        return "Sorry, there is no matched movie"

    cinemas = get_cinema_id_by_search(cinema_name)
    # print(cinemas)

    if len(cinemas) > 1:
        reply += "I found " + str(len(cinemas)) + " results of [" + cinema_name +  "]:\n"
        for cinema in cinemas:
            reply += "{}: {}\n".format(
                cinema['id'],
                cinema['name']
            )
        reply += "Try type in more precise cinema name.\n"
        reply += "E.g.: Event Cinemas George Street.\n"
        return reply
    elif len(cinemas) == 0:
        return "Sorry, there is no matched cinema"

    apiUrl = 'http://127.0.0.1:9091/v1/available?cinema_id={}&movie_id={}&date={}&timeslot={}'.format(
        cinemas[0]['id'],
        movies[0]['id'],
        date,
        timeslot
    )
    result = requests.get(
        apiUrl
    )
    if result.status_code == 200:
        jsonResult = result.json()
        if bool(jsonResult['available']):
            reply += "Yes, this timeslot is available\n"
            reply += "cinema: {}\nmovie: {}\ndate: {}\ntime: {}\ntimeslot_id: {} (Use this id to book your ticket with higher precision)".format(
                cinemas[0]['name'],
                movies[0]['title'],
                date,
                timeslot,
                jsonResult['id']
            )
            return reply
        else:
            reply += "Sorry, this timeslot is not available\n"
            reply += "cinema: {}\nmovie: {}\ndate: {}\ntimeslot: {}".format(
                cinemas[0]['id'],
                movies[0]['id'],
                date,
                timeslot
            )
            return reply
    elif result.status_code == 400:
        reply += "Sorry, please use date and time formate as year-month-day hour-minute-second\nE.g.:2021-11-10 13:00"
        return reply

import requests

from ..helper.getCinemaIDBySearch import get_cinema_id_by_search
from ..helper.getMovieIDBySearch import get_movie_id_by_search
from ..helper.ticketRestriction1 import ticket_restriction1
from ..helper.ticketRestriction2 import ticket_restriction2


def check_timeslot_available(cinema_name, movie_title, date, timeslot, ticket_num, user_id):

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

    apiUrl = 'http://127.0.0.1:9091/v1/available?cinema_id={}&movie_id={}&date={}&timeslot={}&ticket_num={}'.format(
        cinemas[0]['id'],
        movies[0]['id'],
        date,
        timeslot,
        ticket_num
    )
    result = requests.get(
        apiUrl
    )
    # print(result)
    if result.status_code == 200:
        jsonResult = result.json()
        if bool(jsonResult['available']):
            if not ticket_restriction1(jsonResult['id'], date, timeslot, user_id):
                reply += "You cannot book two or more movies with same schedule."
                return reply
            if not ticket_restriction2(ticket_num, jsonResult['id'], user_id):
                reply += "You cannot book all seats for a specific timeslot of a movie."
                return reply
            reply += "Yes, this timeslot is available\n"
            reply += "cinema: {}\nmovie: {}\ndate: {}\nstart time: {}\ntickets number: {}\nseat: {}\ntimeslot_id: {}".format(
                cinemas[0]['name'],
                movies[0]['title'],
                date,
                timeslot,
                ticket_num,
                jsonResult['seat'].strip(),
                jsonResult['id']
            )
            return reply
        else:
            reply += "Sorry, this timeslot is not available\n"
            reply += "cinema: {}\nmovie: {}\ndate: {}\nstart time: {}\ntickets number:{}".format(
                cinemas[0]['id'],
                movies[0]['id'],
                date,
                timeslot,
                ticket_num
            )
            return reply
    elif result.status_code == 400:
        reply += "Sorry, please use date and time formate as year-month-day hour-minute-second\nE.g.:2021-11-10 13:00"
        return reply

import requests
import json

from ..helper.getMovieIDBySearch import get_movie_id_by_search


def get_timetable_by_movie_id(movie_id):

    reply = ""

    apiUrl = 'http://127.0.0.1:9091/v1/movie/' + str(movie_id)
    result = requests.get(
        apiUrl
    )
    jsonResult = result.json()
    # print(jsonResult)

    if len(jsonResult) == 0:
        return "Sorry, no matched movie"

    reply += "Below is all timetable of movie " + str(movie_id) + ":\n" \
             + "[timeslot_id]: cinema_name, date, start_time, seat\n"
    for i in range(len(jsonResult)):
        temp = jsonResult[i]
        reply += "------- " + temp['movie_title'] + " -------\n"
        for timeslot in temp['timetable']:
            reply += "[{}]:  {}, {}, {}, {}\n".format(
                timeslot['timeslots_id'],
                timeslot['cinema_name'],
                timeslot['date'],
                timeslot['start_time'],
                timeslot['seats']
            )
    # print(reply)
    return reply
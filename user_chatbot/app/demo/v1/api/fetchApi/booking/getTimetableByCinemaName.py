import requests
import json

from ..helper.getCinemaIDBySearch import get_cinema_id_by_search


def get_timetable_by_cinema_name(input):

    reply = ""

    cinemas = get_cinema_id_by_search(input)

    if len(cinemas) > 1:
        reply += "I found " + str(len(cinemas)) + " results of [" + input +  "]:\n"
        for cinema in cinemas:
            reply += "{}: {}\n".format(
                cinema['id'],
                cinema['name']
            )
        reply += "Try type in more precise cinema name or use precise query [cinema timetable: cinema_id].\n"
        reply += "E.g.: Show me the timetable of HOYTS Broadway.\n"
        reply += "E.g.: cinema timetable: 0\n"
        return reply
    elif len(cinemas) == 1:
        id = cinemas[0]['id']
        apiUrl = 'http://127.0.0.1:9091/v1/cinema/' + str(id)
        result = requests.get(
            apiUrl
        )
        if result.status_code == 200:
            jsonResult = result.json()
            reply += "Below is all timetable of [" + cinemas[0]['name']  + "]:\n" \
                     + "[timeslot_id]: cinema_name, date, start_time, seat\n"
            for temp in jsonResult:
                reply += "------- " + temp['movie_title'] + " -------\n"
                for timeslot in temp['timetable']:
                    reply += "[{}]:  {}, {}, {}, {}\n".format(
                        timeslot['timeslots_id'],
                        timeslot['cinema_name'],
                        timeslot['date'],
                        timeslot['start_time'],
                        timeslot['seats']
                    )
            return reply
    elif len(cinemas) == 0:
        reply += "Sorry, there is no matched cinema"
        return reply

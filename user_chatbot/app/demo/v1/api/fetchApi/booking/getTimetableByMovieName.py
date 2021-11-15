import requests
import json

from ..helper.getMovieIDBySearch import get_movie_id_by_search


def get_timetable_by_movie_name(input):

    reply = ""

    movies = get_movie_id_by_search(input)

    if len(movies) > 1:
        reply += "I found " + str(len(movies)) + " results of [" + input +  "]:\n"
        for movie in movies:
            reply += "{}: {}\n".format(
                movie['id'],
                movie['title']
            )
        reply += "Try type in more precise movie name or use precise query [movie timetable: movie_id].\n"
        reply += "E.g.: Show me the timetable about No Time To Die.\n"
        reply += "E.g.: movie timetable: 0\n"
        return reply
    elif len(movies) == 1:
        id = movies[0]['id']
        apiUrl = 'http://127.0.0.1:9091/v1/movie/' + str(id)
        result = requests.get(
            apiUrl
        )
        if result.status_code == 200:
            jsonResult = result.json()
            reply += "Below is the timetable of [" + movies[0]['title'] + "]\n"
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
    elif len(movies) == 0:
        reply += "Sorry, there is no matched cinema"
        return reply

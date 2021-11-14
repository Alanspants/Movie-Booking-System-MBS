import requests
import json

from ..helper.getCinemaIDBySearch import get_cinema_id_by_search


def get_cinema_snack_by_name(input):

    reply = ""

    cinemas = get_cinema_id_by_search(input)
    # print(cinemas)

    if len(cinemas) > 1:
        reply += "I found " + str(len(cinemas)) + " results of [" + input +  "]:\n"
        for cinema in cinemas:
            reply += "{}: {}\n".format(
                cinema['id'],
                cinema['name']
            )
        reply += "Try type in more precise cinema name or use precise query [cinema snack: cinema_id].\n"
        reply += "E.g.: What snacks are available in Event Cinemas George Street.\n"
        reply += "E.g.: cinema snack: 0\n"
        return reply
    elif len(cinemas) == 1:
        id = cinemas[0]['id']
        apiUrl = 'http://127.0.0.1:9090/v1/cinema/' + str(id) + "/snack"
        result = requests.get(
            apiUrl
        )
        if result.status_code == 200:
            jsonResult = result.json()
            reply += "[" + cinemas[0]['name'] + "] has: " + jsonResult['snacks']
        return reply
    elif len(cinemas) == 0:
        reply += "Sorry, there is no matched cinema"
        return reply


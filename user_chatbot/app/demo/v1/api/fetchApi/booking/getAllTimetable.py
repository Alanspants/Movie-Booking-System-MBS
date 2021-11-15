import requests
import json

def get_all_timetable():

    reply = ""

    apiUrl = 'http://127.0.0.1:9091/v1/all'
    result = requests.get(
        apiUrl
    )
    jsonResult = result.json()
    # print(jsonResult)

    reply += "Below is all timetable:\n" \
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
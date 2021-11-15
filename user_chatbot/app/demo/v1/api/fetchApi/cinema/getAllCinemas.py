import requests
import json

def get_all_cinemas():

    reply = ""

    apiUrl = 'http://127.0.0.1:9090/v1/cinema'
    result = requests.get(
        apiUrl
    )
    jsonResult = result.json()
    # print(jsonResult)

    reply += "I have " + str(len(jsonResult)) + " cinemas: \n"
    for i in range(len(jsonResult)):
        temp = jsonResult[i]
        reply += "{}: {}\n".format(
            i,
            temp['name']
        )
    reply += "Type in: [cinema detail: cinema_id] to check the more detail about cinema\nE.g.: cinema detail: 1\n"
    reply += "Type in: [cinema timetable: cinema_id] to check the more detail about cinema timetable\nE.g.: cinema timetable: 1"
    # print(reply)
    return reply
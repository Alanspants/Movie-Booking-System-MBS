import requests
import json

def get_cinema_movie_by_id(id):

    reply = ""

    apiUrl = 'http://127.0.0.1:9090/v1/cinema/'+str(id)+"/movie"
    result = requests.get(
        apiUrl
    )
    if result.status_code == 200:
        jsonResult = result.json()
        reply += "Below is the available movie in cinema " + str(id) + "\n"
        for i in range(len(jsonResult)):
            temp = jsonResult[i]
            reply += "{}: {}\n".format(
                temp['id'],
                temp['title']
            )
    else:
        reply = "Please input valid cinema ID."
    # print(reply)
    return reply
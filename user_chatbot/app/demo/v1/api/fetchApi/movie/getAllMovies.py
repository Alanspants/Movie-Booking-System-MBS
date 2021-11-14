import requests
import json

def get_all_movies():

    reply = ""

    apiUrl = 'http://127.0.0.1:9090/v1/movie'
    result = requests.get(
        apiUrl
    )
    jsonResult = result.json()
    # print(jsonResult)

    reply += "I found " + str(len(jsonResult)) + " movies: \n"
    for i in range(len(jsonResult)):
        temp = jsonResult[i]
        reply += "{}: {}\n".format(
            temp['id'],
            temp['title']
        )
    reply += "Type in: [movie detail: movie_id] to check the more detail about movie\nE.g.: movie detail: 1"
    # print(reply)
    return reply
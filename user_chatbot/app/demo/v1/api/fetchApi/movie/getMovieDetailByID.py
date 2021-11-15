import requests
import json

def get_movie_detail_by_id(id):

    reply = ""

    apiUrl = 'http://127.0.0.1:9090/v1/movie/'+str(id)
    result = requests.get(
        apiUrl
    )
    if result.status_code == 200:
        jsonResult = result.json()
        reply += "Below is the detail about movie " + str(id) + "\n" \
                 + "Title: " + jsonResult['title'] + "\n" \
                 + "Description: " + jsonResult['description'] + "\n" \
                 + "Cast: " + jsonResult['cast']
    else:
        reply = "Please input valid movie ID."
    # print(reply)
    return reply
import requests
import json

def search_cinema(input):

    reply = ""

    apiUrl = 'http://127.0.0.1:9090/v1/cinema/search?info={}'.format(
        input
    )
    result = requests.get(
        apiUrl
    )
    if result.status_code == 200:
        jsonResult = result.json()
        if len(jsonResult) == 1:
            reply += "I found you 1 matched result:\n"
            temp = jsonResult[0]
            reply += "Name: " + temp['name'] + "\n"\
                        + "Address: " + temp['address'] + "\n"\
                        + "Phone: " + temp['phone'] + "\n"
        if len(jsonResult) > 1:
            reply += "I found you " + str(len(jsonResult)) + " matched results:\n"
            for i in range(len(jsonResult)):
                reply += "------ " + str(i + 1) + " ------\n"
                temp = jsonResult[i]
                reply += "Name: " + temp['name'] + "\n" \
                         + "Address: " + temp['address'] + "\n" \
                         + "Phone: " + temp['phone'] + "\n"
        if len(jsonResult) == 0:
            reply += "Sorry, there is no matched cinema."
    else:
        reply = "Please input valid cinema ID."
    # print(reply)
    return reply
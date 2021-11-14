import requests
import json

def get_cinema_detail_by_id(id):

    reply = ""

    apiUrl = 'http://127.0.0.1:9090/v1/cinema/'+str(id)
    result = requests.get(
        apiUrl
    )
    if result.status_code == 200:
        jsonResult = result.json()
        reply += "Below is the detail about cinema " + str(id) + "\n"\
                + "Name: " + jsonResult['name'] + "\n"\
                + "Address: " + jsonResult['address'] + "\n"\
                + "Phone: " + jsonResult['phone']
    else:
        reply = "Please input valid cinema ID."
    # print(reply)
    return reply
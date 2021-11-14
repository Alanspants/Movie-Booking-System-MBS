import requests


def get_cinema_snack_by_id(id):

    reply = ""

    apiUrl = 'http://127.0.0.1:9090/v1/cinema/'+str(id) + "/snack"
    result = requests.get(
        apiUrl
    )
    if result.status_code == 200:
        jsonResult = result.json()
        reply += "cinema " + str(id) + " has: " + jsonResult['snacks']
    else:
        reply = "Please input valid cinema ID."
    # print(reply)
    return reply
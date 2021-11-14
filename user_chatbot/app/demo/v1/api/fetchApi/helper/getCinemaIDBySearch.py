import requests
import json

def get_cinema_id_by_search(input):
    apiUrl = 'http://127.0.0.1:9090/v1/cinema/search?info={}'.format(
        input
    )
    result = requests.get(
        apiUrl
    )
    if result.status_code == 200:
        jsonResult = result.json()
        ans = []
        for temp in jsonResult:
            dict = {
                'id': temp['id'],
                'name': temp['name']
            }
            ans.append(dict)
    # print(reply)
    return ans
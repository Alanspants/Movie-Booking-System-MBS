import requests
import json

def get_movie_id_by_search(input):
    apiUrl = 'http://127.0.0.1:9090/v1/movie/search?info={}'.format(
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
                'title': temp['title']
            }
            ans.append(dict)
    return ans
    # print(reply)
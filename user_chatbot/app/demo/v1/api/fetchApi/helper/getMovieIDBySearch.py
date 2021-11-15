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
        # ans = []
        # for temp in jsonResult:
        #     dict = {
        #         'id': temp['id'],
        #         'name': temp['name']
        #     }
        #     ans.append(dict)
        if len(jsonResult) >= 1:
            available_cinema = "Available at:\n"
            movie_id = jsonResult[0]["movie_id"]
            movie_title = jsonResult[0]["movie_title"]
            for temp in jsonResult:
                available_cinema += "{}: {}\n".format(
                    temp['cinema_id'],
                    temp['cinema_name']
                )
            return {
                'id': movie_id,
                'title': movie_title,
                'available': available_cinema
            }
        else:
            return False
    # print(reply)
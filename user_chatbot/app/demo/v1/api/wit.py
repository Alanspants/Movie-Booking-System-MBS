import requests

from .fetchApi.booking.checkTimeslotAvailable import check_timeslot_available
from .fetchApi.booking.getAllTimetable import get_all_timetable
from .fetchApi.booking.getTimetableByCinemaID import get_timetable_by_cinema_id
from .fetchApi.booking.getTimetableByCinemaName import get_timetable_by_cinema_name
from .fetchApi.booking.getTimetableByMovieID import get_timetable_by_movie_id
from .fetchApi.booking.getTimetableByMovieName import get_timetable_by_movie_name
from .fetchApi.cinema.getAllCinemas import get_all_cinemas
from .fetchApi.cinema.getCinemaDetailByID import get_cinema_detail_by_id
from .fetchApi.cinema.getCinemaDetailByName import get_cinema_detail_by_name
from .fetchApi.cinema.getCinemaMovieByID import get_cinema_movie_by_id
from .fetchApi.cinema.getCinemaMovieByName import get_cinema_movie_by_name
from .fetchApi.cinema.getCinemaSnackByID import get_cinema_snack_by_id
from .fetchApi.cinema.getCinemaSnackByName import get_cinema_snack_by_name
from .fetchApi.cinema.searchCinema import search_cinema
from .fetchApi.movie.getAllMovies import get_all_movies
from .fetchApi.movie.getMovieCinemaByName import get_movie_cinema_by_name
from .fetchApi.movie.getMovieDetailByID import get_movie_detail_by_id
from .fetchApi.movie.getMovieDetailByName import get_movie_detail_by_name


def ask_wit(expression):
    result = requests.get('https://api.wit.ai/message?v=20211113&q={}'.format(expression),
                          headers={
                              'Authorization': "Bearer " + "PXDC56RDWEAS2TPPIS7ECXUIIGQW25GU",
                              'Accept': "application/json"
                          })
    jsonResult = result.json()
    intent = jsonResult['intents'][0]['name']
    try:
        if intent == "getAllCinemas":
            answer = get_all_cinemas()
            # answer = "hello"
        if intent == "getCinemaDetailByID":
            cinema_id = jsonResult['entities']['cinema_id:cinema_id'][0]['value']
            answer = get_cinema_detail_by_id(cinema_id)
        if intent == "searchCinema":
            search_input = jsonResult['entities']['search_input:search_input'][0]['value']
            answer = search_cinema(search_input)
        if intent == "getCinemaDetailByName":
            search_input = jsonResult['entities']['search_input:search_input'][0]['value']
            answer = get_cinema_detail_by_name(search_input)
        if intent == "getCinemaMovieByID":
            cinema_id = jsonResult['entities']['cinema_id:cinema_id'][0]['value']
            answer = get_cinema_movie_by_id(cinema_id)
        if intent == "getCinemaMovieByName":
            search_input = jsonResult['entities']['search_input:search_input'][0]['value']
            answer = get_cinema_movie_by_name(search_input)
        if intent == "getCinemaSnackByID":
            cinema_id = jsonResult['entities']['cinema_id:cinema_id'][0]['value']
            answer = get_cinema_snack_by_id(cinema_id)
        if intent == "getCinemaSnackByName":
            search_input = jsonResult['entities']['search_input:search_input'][0]['value']
            answer = get_cinema_snack_by_name(search_input)
        if intent == "getAllMovies":
            answer = get_all_movies()
        if intent == "getMovieDetailByID":
            movie_id = jsonResult['entities']['movie_id:movie_id'][0]['value']
            answer = get_movie_detail_by_id(movie_id)
        if intent == "getMovieDetailByName":
            search_input = jsonResult['entities']['search_input:search_input'][0]['value']
            answer = get_movie_detail_by_name(search_input)
        if intent == "getMovieCinemaByName":
            search_input = jsonResult['entities']['search_input:search_input'][0]['value']
            answer = get_movie_cinema_by_name(search_input)
        if intent == "getAllTimetable":
            answer = get_all_timetable()
        if intent == "getTimetableByMovieName":
            input = jsonResult['entities']['movie_name:movie_name'][0]['value']
            answer = get_timetable_by_movie_name(input)
        if intent == "getTimetableByMovieID":
            movie_id = jsonResult['entities']['movie_id:movie_id'][0]['value']
            answer = get_timetable_by_movie_id(movie_id)
        if intent == "getTimetableByCinemaID":
            cinema_id = jsonResult['entities']['cinema_id:cinema_id'][0]['value']
            answer = get_timetable_by_cinema_id(cinema_id)
        if intent == "getTimetableByCinemaName":
            input = jsonResult['entities']['cinema_name:cinema_name'][0]['value']
            answer = get_timetable_by_cinema_name(input)
        if intent == "checkTimeslotAvailable":
            ticket_num = jsonResult['entities']['ticket_num:ticket_num'][0]['value']
            time = jsonResult['entities']['time:time'][0]['value']
            date = jsonResult['entities']['date:date'][0]['value']
            cinema_name = jsonResult['entities']['cinema_name:cinema_name'][0]['value']
            movie_name = jsonResult['entities']['movie_name:movie_name'][0]['value']
            check_timeslot_available(cinema_name, movie_name, date, time, ticket_num)
    except KeyError as err:
        answer = "Sorry, I don't understand your request"
    return answer
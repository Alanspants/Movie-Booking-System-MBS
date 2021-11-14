# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import g
from rivescript import RiveScript
from pathlib import Path

from . import Resource
from .fetchApi.movie.getAllMovies import get_all_movies
from .wit import ask_wit

bot = RiveScript()
script_location = Path(__file__).absolute().parent
file_location = script_location / 'rules.rive'
print(file_location)
bot.load_file(str(file_location))
bot.sort_replies()

class ChatbotAsk(Resource):

    def get(self):
        # print(g.args)
        expression = g.args.get("expression")
        print("User says: " + expression)
        answer = bot.reply("localuser", expression)
        if "ERR" in answer:
            print("Bot cannot handle")
            # answer = ask_wit(expression)
            # answer = get_all_cinemas()
            # answer = get_cinema_detail_by_id(7)
            # answer = search_cinema("bondi")
            # answer = get_cinema_detail_by_name("Event")
            # answer = get_cinema_movie_by_id(0)
            # answer = get_cinema_movie_by_name("Event Cinemas George Street")
            # answer = get_cinema_snack_by_id(0)
            # answer = get_cinema_snack_by_name("hoyts")
            answer = get_all_movies()
            print("Wit Answer:\n" + answer)
        else:
            print("Bot Answer: " + answer)
        return answer, 200

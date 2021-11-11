# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, make_response

from . import Resource
from .. import schemas

from . import sql_link

class MovieSearch(Resource):

    def get(self):
        input = g.args['info']
        conn = sql_link.connect_sys_db()
        query = "select distinct cinemas.id as cinema_id, cinemas.name as cinema_name, movies.id as movie_id, movies.title as movie_title from movies\
                    join timeslots on movies.id = timeslots.movie_id\
                    join cinemas on cinemas.id = timeslots.cinema_id\
                    where title like \'%{input}%\' or description like \'%{input}%\'".format(
            input = input
        )
        print(query)
        with sql_link.mysql(conn) as cursor:
            cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        if len(result) == 0:
            return make_response({"status": "Cinema not found"}, 404)
        else:
            return result, 200
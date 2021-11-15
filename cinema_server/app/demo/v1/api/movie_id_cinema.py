# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, make_response

from . import Resource
from . import sql_link
from .. import schemas


class MovieIdCinema(Resource):

    def get(self, id):
        conn = sql_link.connect_sys_db()
        query = "select distinct cinemas.id as id, name from movies\
            join timeslots on movies.id = timeslots.movie_id\
            join cinemas on cinemas.id = timeslots.cinema_id\
            where movie_id = {id}".format(
            id = id
        )
        with sql_link.mysql(conn) as cursor:
            cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        if len(result) == 0:
            return make_response({"status": "Cinema not found"}, 404)
        else:
            return result, 200
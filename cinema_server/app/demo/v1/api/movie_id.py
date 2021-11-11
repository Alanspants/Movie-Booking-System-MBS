# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, make_response

from . import Resource
from .. import schemas

from . import sql_link

class MovieId(Resource):

    def get(self, id):
        conn = sql_link.connect_sys_db()
        query = "select * from movies where id = \'{id}\'".format(
            id = id
        )
        with sql_link.mysql(conn) as cursor:
            cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        if result == None:
            return make_response({"status": "Cinema not found"}, 404)
        else:
            return result, 200
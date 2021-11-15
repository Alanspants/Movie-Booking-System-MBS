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
        query = "select id, title from movies \
                    where title like \'%{input}%\' or description like \'%{input}%\'".format(
            input = input
        )
        print(query)
        with sql_link.mysql(conn) as cursor:
            cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result, 200
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas

from . import sql_link

class Movie(Resource):

    def get(self):
        conn = sql_link.connect_sys_db()
        query = "select * from movies"
        with sql_link.mysql(conn) as cursor:
            cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result, 200
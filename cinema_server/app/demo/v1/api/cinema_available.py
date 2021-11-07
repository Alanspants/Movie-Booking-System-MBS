# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from datetime import datetime

from flask import request, g, make_response

from . import Resource
from .. import schemas
from . import sql_link

from enum import IntEnum



class CinemaAvailable(Resource):

    def get(self):
        print(g.args)
        input = g.args
        date = input['date']
        try :
            datetimeobj = datetime.strptime(date, '%y/%m/%d')
            weekday = datetimeobj.weekday()
        except:
            return make_response({"status": "invalid input"}, 403)
        if weekday != 6:
            conn = sql_link.connect_sys_db()
            query = "select * from cinemas"
            with sql_link.mysql(conn) as cursor:
                cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result, 200
        else:
            return {}, 200
        # return make_response({"status": "Cinema not found"}, 404)
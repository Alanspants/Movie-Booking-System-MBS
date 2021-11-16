# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, make_response

from . import Resource
from .. import schemas

from . import sql_link
from datetime import datetime

class Available(Resource):

    def get(self):
        # print(g.args)
        cinema_id = g.args['cinema_id']
        movie_id = g.args['movie_id']
        date = g.args['date']
        timeslot = g.args['timeslot']
        ticket_num = g.args['ticket_num']

        # with sql_link.mysql(conn) as cursor:
        #     cursor.execute(query)
        # result = cursor.fetchall()

        try:
            conn = sql_link.connect_sys_db()
            query = "select * from timeslots\
                    where movie_id = \'{movie_id}\'\
                    and cinema_id = \'{cinema_id}\'\
                    and date = \'{date}\'\
                    and start_time = \'{timeslot}\'".format(
            movie_id = movie_id,
            cinema_id = cinema_id,
            date = datetime.strptime(date, '%Y-%m-%d'),
            timeslot = timeslot
        )
            with sql_link.mysql(conn) as cursor:
                cursor.execute(query)
            result = cursor.fetchall()
        except:
            return make_response({"status":"Invalid input"}, 400)

        if len(result) != 0:
            availableSeat = 0
            seatSet = ""
            for i in range(1, 16):
                seat = "seat" + str(i) + "_user_id"
                if result[0][seat] == None:
                    availableSeat += 1
                    if len(seatSet.split(" ")) <= ticket_num:
                        seatSet += str(i) + " "
            if availableSeat >= ticket_num:
                return {
                    "available": True,
                    "id": result[0]['id'],
                    "seat": seatSet
                       }, 200
            else:
                return {
                    "available": False
                }, 200
        return {
            "available": False
               }, 200
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
import copy

from . import Resource
from .. import schemas

from . import sql_link

class CinemaCinemaId(Resource):

    def get(self, cinema_id):
        conn = sql_link.connect_sys_db()
        query = "select * from movies\
                            join timeslots on movies.id = timeslots.movie_id\
                            join cinemas on cinemas.id = timeslots.cinema_id\
                            where cinemas.id = \'{cinema_id}\'\
                            order by movies.id, timeslots.id".format(
            cinema_id = cinema_id
        )
        with sql_link.mysql(conn) as cursor:
            cursor.execute(query)
        result = cursor.fetchall()
        output = []
        output_movie = {
            "movie_title": "",
            "movie_id": -1,
            "timetable": []
        }
        # print(result)
        for result_temp in result:
            # print(result)
            if result_temp['id'] != output_movie['movie_id']:
                output_movie['movie_title'] = result_temp['title']
                output_movie['movie_id'] = result_temp['id']
                output.append(copy.copy(output_movie))
        print(output)
        for result_temp in result:
            # print(result_temp)
            for output_temp in output:
                if result_temp['id'] == output_temp['movie_id']:
                    seats=""
                    for i in range(1, 16):
                        seat = "seat" + str(i) + "_user_id"
                        if result_temp[seat] == None:
                            seats = seats + str(i) + " "
                    temp = {
                        "timeslots_id": result_temp['timeslots.id'],
                        "cinema_id": result_temp['cinemas.id'],
                        "cinema_name": result_temp['name'],
                        "date": result_temp['date'].strftime("%Y-%m-%d"),
                        "start_time": str(result_temp['start_time']),
                        "seats": seats
                    }
                    test = copy.copy(output_temp['timetable'])
                    test.append(temp)
                    output_temp['timetable'] = test
            output_temp['timetable'].sort(key=lambda x:x['timeslots_id'])
        # print(output)
        return output, 200
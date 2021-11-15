# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
import copy

from . import Resource
from .. import schemas

from . import sql_link

class All(Resource):

    def get(self):
        conn = sql_link.connect_sys_db()
        query = "select * from movies\
                    join timeslots on movies.id = timeslots.movie_id\
                    join cinemas on cinemas.id = timeslots.cinema_id\
                    order by movies.id, cinemas.id, date, start_time"
        with sql_link.mysql(conn) as cursor:
            cursor.execute(query)
        result = cursor.fetchall()
        output = []
        output_movie = {
            "movie_title": "",
            "movie_id": -1,
            "timetable": []
        }
        # print(results)
        for result_temp in result:
            # print(result)
            if result_temp['id'] != output_movie['movie_id']:
                output_movie['movie_title'] = result_temp['title']
                output_movie['movie_id'] = result_temp['id']
                output.append(copy.copy(output_movie))
        print(output)
        for result_temp in result:
            print(result_temp)
            # for output_temp in output:
            for index in range(len(output)):
                # output_temp = output[index]
                if result_temp['id'] == output[index]['movie_id']:
                    seats=""
                    for i in range(1, 16):
                        seat = "seat" + str(i) + "_user_id"
                        if result_temp[seat] == None:
                            seats = seats + str(i) + " "
                    temp = {
                        "timeslots_id": int(result_temp['timeslots.id']),
                        "cinema_id": result_temp['cinemas.id'],
                        "cinema_name": result_temp['name'],
                        "date": result_temp['date'].strftime("%Y-%m-%d"),
                        "start_time": str(result_temp['start_time']),
                        "seats": seats
                    }
                    test = copy.copy(output[index]['timetable'])
                    test.append(temp)
                    # output[0]['timetable'].append(temp)
                    output[index]['timetable'] = test
            # output[index]['timetable'].sort(key=lambda x:x['timeslots_id'])
        # print(output)
        return output, 200
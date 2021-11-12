# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, make_response

from . import Resource
from .. import schemas

from . import sql_link
from . import helper

class Booking(Resource):

    def post(self):
        timeslot_id = g.args['timeslot_id']
        seat_number = g.args['seat_number']
        user_id = g.args['user_id']
        seat = 'seat' + str(seat_number) + '_user_id'

        if not helper.slot_empty_check(timeslot_id, seat_number):
            return make_response({"status": "This seat has already been booked"}, 403)

        if not helper.user_check(user_id):
            return make_response({"status": "User not found."}, 404)

        conn = sql_link.connect_sys_db()
        query = "update timeslots set {seat} = \'{user_id}\' where id = \'{timeslot_id}\'".format(
            seat = seat,
            timeslot_id = timeslot_id,
            user_id = user_id
        )
        with sql_link.mysql(conn) as cursor:
            cursor.execute(query)

        conn = sql_link.connect_sys_db()
        query = "select cinemas.name as cinema_name, movies.title as movie_title, timeslots.date as booking_date, timeslots.start_time as booking_start_time from movies\
                    join timeslots on movies.id = timeslots.movie_id\
                    join cinemas on cinemas.id = timeslots.cinema_id\
                    where timeslots.id = \'{timeslot_id}\'".format(
            timeslot_id = timeslot_id
        )
        with sql_link.mysql(conn) as cursor:
            cursor.execute(query)
        result = cursor.fetchone()
        print(result)
        cinema_name = result['cinema_name']
        movie_title = result['movie_title']
        booking_date = result['booking_date'].strftime("%Y-%m-%d")
        booking_start_time = str(result['booking_start_time'])
        ans = {
            "movie_title": movie_title,
            "cinema_name": cinema_name,
            "booking_date": booking_date,
            "booking_start_time": booking_start_time,
            "seat_number": seat_number
        }
        return ans, 200

    def delete(self):
        timeslot_id = g.args['timeslot_id']
        seat_number = g.args['seat_number']
        user_id = g.args['user_id']
        seat = 'seat' + str(seat_number) + '_user_id'

        if helper.slot_empty_check(timeslot_id, seat_number):
            return make_response({"status": "This seat has not been booked yet"}, 403)

        if not helper.user_check(user_id):
            return make_response({"status": "User not found."}, 404)

        conn = sql_link.connect_sys_db()
        query = "update timeslots set {seat} = null where id = \'{timeslot_id}\'".format(
            seat = seat,
            timeslot_id = timeslot_id,
            user_id = user_id
        )
        with sql_link.mysql(conn) as cursor:
            cursor.execute(query)

        conn = sql_link.connect_sys_db()
        query = "select cinemas.name as cinema_name, movies.title as movie_title, timeslots.date as booking_date, timeslots.start_time as booking_start_time from movies\
                    join timeslots on movies.id = timeslots.movie_id\
                    join cinemas on cinemas.id = timeslots.cinema_id\
                    where timeslots.id = \'{timeslot_id}\'".format(
            timeslot_id = timeslot_id
        )
        with sql_link.mysql(conn) as cursor:
            cursor.execute(query)
        result = cursor.fetchone()
        print(result)
        cinema_name = result['cinema_name']
        movie_title = result['movie_title']
        booking_date = result['booking_date'].strftime("%Y-%m-%d")
        booking_start_time = str(result['booking_start_time'])
        ans = {
            "movie_title": movie_title,
            "cinema_name": cinema_name,
            "booking_date": booking_date,
            "booking_start_time": booking_start_time,
            "seat_number": seat_number
        }
        return ans, 200
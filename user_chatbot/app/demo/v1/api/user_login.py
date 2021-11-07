# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, make_response
from pandas import read_sql

from . import sql_link
from . import Resource
from .. import schemas


class UserLogin(Resource):

    def post(self):
        input = g.json
        username = input['username']
        password = input['password']

        conn = sql_link.connect_sys_db()
        query = "select * from users where username = \'{username}\' and password = \'{password}\'".format(
            username = username,
            password = password
        )
        db_result = read_sql(sql=query, con=conn)
        if len(db_result) != 1:
            return make_response({
                       "status": "User not found",
                   }, 404)
        else:
            return make_response({
                "username": username,
                "password": password,
                "userID": int(db_result.iloc[0]['id'])
            }, 201)
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, make_response

from . import Resource
from .. import schemas

from . import sql_link
from pandas import read_sql


class UserRegister(Resource):

    def post(self):
        # print(g.json)
        input = g.json
        username = input['username']
        password = input['password']

        # Check username unique
        conn = sql_link.connect_sys_db()
        query = "select * from users where username = \'{username}\'".format(
            username = username
        )
        db_result = read_sql(sql=query, con=conn)
        if len(db_result) != 0:
            return make_response(
                {
                    "status": "username already in use",
                }, 403)

        # get new id
        conn = sql_link.connect_sys_db()
        query = "select * from users"
        db_result = read_sql(sql=query, con=conn)
        # print(db_result)
        new_id = len(db_result)
        # print(new_id[0])

        # register
        conn = sql_link.connect_sys_db()
        query = "insert into users values(\'{id}\', \'{username}\', \'{password}\')".format(
            id = new_id,
            username = username,
            password = password
        )
        with sql_link.mysql(conn) as cursor:
            cursor.execute(query)
        return make_response(
            {
                "username": username,
                "password": password,
                "userID": new_id
            }, 201)
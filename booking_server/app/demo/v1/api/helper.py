from . import sql_link

def user_check(user_id):
    conn = sql_link.connect_sys_db()
    query = "select * from users where id=\'{id}\'".format(
        id = user_id
    )
    with sql_link.mysql(conn) as cursor:
        cursor.execute(query)
    result = cursor.fetchall()
    if len(result) == 0:
        return False
    return True

def slot_empty_check(timeslot_id, seat_number):
    seat = 'seat' + str(seat_number) + '_user_id'
    conn = sql_link.connect_sys_db()
    query = "select {seat} from timeslots where id = \'{timeslot_id}\'".format(
        seat = seat,
        timeslot_id = timeslot_id
    )
    with sql_link.mysql(conn) as cursor:
        cursor.execute(query)
    result = cursor.fetchone()
    if result['seat1_user_id'] != None:
        return False
    return True
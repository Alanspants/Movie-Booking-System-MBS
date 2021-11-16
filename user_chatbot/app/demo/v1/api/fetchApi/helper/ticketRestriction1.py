from ... import sql_link

def ticket_restriction1(timeslot_id, date, time, user_id):
    conn = sql_link.connect_sys_db()
    query = "select * from timeslots\
            where date = \'{}\'\
            and start_time = \'{}\'".format(
        date,
        time
    )
    with sql_link.mysql(conn) as cursor:
        cursor.execute(query)
    result = cursor.fetchall()

    for temp in result:
        for i in range (1, 16):
            seat = "seat" + str(i) + "_user_id"
            if temp[seat] == user_id and temp['id'] != timeslot_id:
                return False
    return True
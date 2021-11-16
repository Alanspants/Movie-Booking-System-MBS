from ... import sql_link

def ticket_restriction2(ticket_num, timeslot_id, user_id):
    conn = sql_link.connect_sys_db()
    query = "select * from timeslots\
            where id = \'{}\'".format(
        timeslot_id,
    )
    with sql_link.mysql(conn) as cursor:
        cursor.execute(query)
    result = cursor.fetchall()

    for temp in result:
        ticket_sum = 0
        for i in range (1, 16):
            seat = "seat" + str(i) + "_user_id"
            if temp[seat] == user_id:
                ticket_sum += 1
        # print(ticket_sum, ticket_num)
        if (ticket_sum + ticket_num) == 15:
            return False
    return True
import contextlib
import pymysql
from . import config


def connect_sys_db():
    return pymysql.connect(host=config.SYS_DB_HOST, user=config.SYS_DB_USER, password=config.SYS_DB_PASSWORD, database=config.SYS_DB_DATABASE,
                           charset=config.SYS_DB_CHARSET)

@contextlib.contextmanager
def mysql(conn):
    cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)
    try:
        yield cursor
    finally:
        conn.commit()
        cursor.close()
        conn.close()
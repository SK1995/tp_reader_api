import psycopg2
import config


def connect():
    try:
        db_conn = psycopg2.connect(database=config.DATABASE_NAME, user=config.DATABASE_USER,
                                   password=config.DATABASE_PASSWORD, host=config.DATABASE_HOST)
        cursor = db_conn.cursor()
        print "Connected to DB successfully"
        return db_conn, cursor
    except:
        print "Can't connect to DB"
        return

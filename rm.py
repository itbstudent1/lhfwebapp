import sqlite3

def drop_table():
    try:
        conn=sqlite3.connect("lite.db")
        cur=conn.cursor()
        cur.execute("DROP TABLE scoreboard")
        conn.commit()
        print("table dropped")
        conn.close()
    except:
        print("no database exists")

drop_table()

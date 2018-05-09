import sqlite3

def create_table():
    # will create if doesn't exist
    conn=sqlite3.connect("lite.db")
    print("db created")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS scoreboard (name TEXT, score INT)")
    conn.commit()
    print ("table created")
    conn.close()

create_table()

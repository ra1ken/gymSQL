import os
import sqlite3




if not (os.path.exists("gym.db")):
    con = sqlite3.connect("gym.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE gymstats(exercise, weight, date, reps)")
    cur.execute("INSERT INTO gymstats VALUES('bench','100','12.2.2026',8)")
    con.commit()
    con.close()



# else:
   # print("db exists :)")
#table_list = [a for a in cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")]
#print(table_list)

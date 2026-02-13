import os
import sqlite3


con = sqlite3.connect("gym.db")
cur = con.cursor()


tablelist = cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='gymstats';").fetchall()

if len(tablelist) == 0:
    #initialize db
    cur.execute("CREATE TABLE gymstats(exercise, weight, date, reps)")
else:
    print(tablelist)

print("choose exercise:")
val1 = input()
print("weight (in kg):")
val2 = int(input())
print("date of lift:")
val3= input()
print("amount of reps:")
val4 = int(input())

# it werks :>
cur.execute(f"INSERT INTO gymstats VALUES('{val1}','{val2}','{val3}',{val4})")
con.commit()
con.close()


#print("db exists :)")
#table_list = [a for a in cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")]
# print(table_list)



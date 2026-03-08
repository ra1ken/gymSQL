import os
import sqlite3
import datetime as dt


con = sqlite3.connect("gym.db")
cur = con.cursor()


tablelist = cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='gymstats';").fetchall()

if len(tablelist) == 0:
    #initialize db
    cur.execute("CREATE TABLE gymstats(exercise, weight, date, reps)")
else:
    print(tablelist)



def ask():
    print("choose exercise:")
    print("1. Bench Press ")
    print("2. Squat")
    print("3. Deadlift")
    exercise = int(input())
    print(f"exercise {exercise}")
    if exercise == 1:
        val1 = "Bench Press"
    elif exercise == 2:
        val1 = "Squat"
    elif exercise == 3:
        val1 = "Deadlift"
    else:
        val1 = "notOk"    
    return(val1)

val1 = ask()
if val1 == "notOk":
    os.system('clear')
    print("invalid choice!")
    ask()

print("weight (in kg):")
val2 = int(input())
val3= dt.datetime.now()
print("amount of reps:")
val4 = int(input())

data = cur.execute("SELECT * FROM gymstats")
print(data)

# it werks :>
cur.execute(f"INSERT INTO gymstats VALUES('{val1}','{val2}','{val3}',{val4})")
con.commit()
con.close()


#print("db exists :)")
#table_list = [a for a in cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")]
# print(table_list)



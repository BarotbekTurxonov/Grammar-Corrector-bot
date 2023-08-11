import sqlite3

def send_ex(command):
    mydb = sqlite3.connect("telegram_bot.db")  # Connect to SQLite database file
    mycursor = mydb.cursor()

    mycursor.execute(command)
    res = mycursor.fetchall()
    mydb.commit()
    mycursor.close()
    mydb.close()
    return res

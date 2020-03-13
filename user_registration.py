import sqlite3 as sql
import json


db = "data.db"

with open("pkg.json") as req:
    json.dump(data, write_file)


def add_user(login, hash_password):
    con = sql.connect(db)
    cur = con.cursor()
    cur.execute("INSERT INTO Users (UserLogin , UserPass) VALUES (?,?)", (login, hash_password))
    con.commit()
    con.close()


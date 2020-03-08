import sqlite3

sql = sqlite3.connect("user_data.db")
sql.execute("insert into user values('12583','admin','12588');")
sql.execute("insert into user values('121212','adm','121212');")
sql.commit()
sql.close()
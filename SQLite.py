
import sqlite3
#建一个数据库
def create_sql():
	sql = sqlite3.connect("user_data.db")
	sql.execute("create table if not exists user("+
	     "id varchar(10) primary key,"+
	     "name varchar(128) not null,"+
	     "password varchar(128) not null);")
	sql.close()

def event_sql():
	sql = sqlite3.connect("user_data.db")
	sql.execute("create table if not exists event("+
	     "event_id integer,"+
	     "user_id varchar(10),"+
	     "name varchar(128) not null,"+
	     "st_time varchar(128) not null,"+
	     "en_time varchar(128),"+
	     "primary key(event_id,user_id),"+
	     "foreign key(user_id) references user(id));")
	sql.close()

def main():
	create_sql()
	event_sql()

main()
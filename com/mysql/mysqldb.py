# -*- coding: utf-8 -*-
# import MySQLdb
import pymysql

print(pymysql)

conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', passwd='inserthome', db='test', charset='utf8')
cursor = conn.cursor()

# ************************select**********************
# sql = 'select * from USER'
# cursor.execute(sql)
# print(cursor.rowcount

# rs = cursor.fetchone()
# print(rs
#
# rs = cursor.fetchmany(3)
# print(rs

# rs = cursor.fetchall()
# print(rs
# for row in rs:
#     print('userid=%s, username=%s' % row

# *************************update insert delete*****************
sql_insert = "insert into USER(userid, username) values(10, 'name10')"
sql_update = "update USER set username='name91' where userid=9"
sql_delete = "delete from USER where userid<3"

try:
    cursor.execute(sql_insert)
    print(cursor.rowcount)
    cursor.execute(sql_update)
    print(cursor.rowcount)
    cursor.execute(sql_delete)
    print(cursor.rowcount)

    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()

print(conn)
print(cursor)

cursor.close()
conn.close()

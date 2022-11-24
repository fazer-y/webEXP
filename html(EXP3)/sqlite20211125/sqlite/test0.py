# -*- coding: utf-8 -*-
import sqlite3


database = "./db/student_083.db"
conn = sqlite3.connect(database)

print ("-"*20)
def showall():
    cur = conn.cursor()
    sql="select * from student_info"
    cur.execute(sql)
    fields=[]
    for field in cur.description:
        fields.append(field[0])
    print(fields)
    result = cur.fetchall()
    print(type(result))
    for item in result:
        print(type(item))
        print(item)
    cur.close()

showall()
#
print ("-"*20)
if 1==1:
    sql="insert into  student_info (stu_id,stu_name,stu_sex,stu_age,stu_origin,stu_profession) values(?,?,?,?,?,?)"
    cur = conn.cursor()
    values=(1,"test","男",20,"威海","计算机")
    cur.execute(sql, values)
    conn.commit()
    cur.close()

showall()
#======================================

print ("-"*20)
sql="update student_info set stu_name='test1' where stu_id=1"
cur = conn.cursor()
cur.execute(sql)
conn.commit()
cur.close()
showall()

print ("-"*20)
sql="delete from student_info  where stu_id=1"
cur = conn.cursor()
cur.execute(sql)
conn.commit()
cur.close()
cur = conn.cursor()
showall()

conn.close()
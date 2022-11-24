# -*- coding: utf-8 -*-

# from .dbSqlite3 import *
from dbSqlite3 import *


result, _ = GetSql2("select * from users")
print(result)


datas, colNames = GetSql2("select * from student_info ")
print(colNames)
print(datas)

if 1 == 1:
    data = dict(
        stu_id=1,
        stu_name="test",
        stu_sex="男",
        stu_age=20,
        stu_origin="威海",
        stu_profession="计算机"
    )

    InsertData(data, "student_info")

    datas, _ = GetSql2("select * from student_info ")
    print(datas)

data = dict(
    stu_id=1,
    stu_name="test1",
    stu_sex="男",
    stu_age=20,
    stu_origin="威海",
    stu_profession="计算机"
)

UpdateData(data, "student_info")

datas, _ = GetSql2("select * from student_info ")
print(datas)

DelDataById("stu_id", 1, "student_info")

datas, _ = GetSql2("select * from student_info ")
print(type(datas))
print(type(datas[0]))
print(datas)

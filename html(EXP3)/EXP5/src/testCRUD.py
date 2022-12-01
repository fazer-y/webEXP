# -*- coding: utf-8 -*-
from src.sqlite3DB import sqlite3DB

# 创建一个数据库操作对象
dbPath = "../db/test.db"
db = sqlite3DB(dbPath)

"""
建立测试数据库：
sqlite3 test.db
sqlite> create table testTable(id int primary key, name text not null, age int);
"""

# 插入数据测试
insetSql = "insert into testTable(id, name, age) values(?,?,?)"
values1 = (1, '林鹏飞', 19)
db.InsertData(insetSql, values1)
insetSql = "insert into testTable(id, name, age) values(?,?,?)"
values2 = (2, '郭连帅', 21)
db.InsertData(insetSql, values2)

# 查询数据测试
readSql = "select * from testTable"
result, fields = db.GetSql(readSql)
print(result, fields)
# 结果：[(1, '林鹏飞', 19), (2, '郭连帅', 21)] ['id', 'name', 'age']

# 更新数据测试
updateSql = "update testTable set age=20 where id=1"
db.UpdateData(updateSql)
readSql = "select * from testTable"
result, fields = db.GetSql(readSql)
print(result, fields)
# 结果：[(1, '林鹏飞', 20), (2, '郭连帅', 21)]

# 删除数据测试
deleteID = "id"
idValue = "1"
tableName = "testTable"
db.DeleteDataById(deleteID, idValue, tableName)
readSql = "select * from testTable"
result, fields = db.GetSql(readSql)
print(result, fields)
# 结果：[(2, '郭连帅', 21)]


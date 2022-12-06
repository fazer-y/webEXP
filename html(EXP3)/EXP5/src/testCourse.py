# -*- coding: utf-8 -*-
from src.sqlite3DB import sqlite3DB

# 创建一个数据库操作对象
dbPath = "../db/courses.db"
db = sqlite3DB(dbPath)

# 按周次查询周二的课程
selectSql = "select weekDay, section, c.cName, t.tName, classroom " \
            "from courseTable ct, courses c, teachers t " \
            "where weekDay=2 and ct.cID=c.cID and ct.tID=t.tID"
result, fileds = db.GetSql(selectSql)
print(fileds)
for r in result:
    print(r)
"""
结果：
['weekDay', 'section', 'cName', 'tName', 'classroom']
(2, '1-2', '数字图像处理', '张亚涛', '商学院551')
(2, '3-4', '计算机图形学', '杨飞', '图东教学楼222')
"""

# 按教师名查询本周该教师的课程的课程
name = "'刘猛'"
selectSql = "select weekDay, section, c.cName, t.tName, classroom " \
            "from courseTable ct, courses c, teachers t " \
            "where ct.cID=c.cID and ct.tID=t.tID and t.tName=%s" % name
result, fileds = db.GetSql(selectSql)
print(fileds)
for r in result:
    print(r)
"""
结果：
['weekDay', 'section', 'cName', 'tName', 'classroom']
(5, '1-2', 'web技术', '刘猛', '海洋学院605')
"""
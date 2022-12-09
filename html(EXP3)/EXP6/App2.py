from flask import Flask, render_template, request, session, redirect, url_for, flash
from sqlite3DB import sqlite3DB

app = Flask(__name__)
app.secret_key = 'abcdefgh!@#$%'
dbPath = "./db/courses.db"
db = sqlite3DB(dbPath)
WeekDay = ['一', '二', '三', '四', '五', '六', '日']


@app.route('/', methods=['GET'])
def index():
    try:
        dayStr = request.args['day']
        day = int(dayStr)
    except KeyError:
        day = 0
    if day != 0:  # 星期查询
        selectSql = "select weekDay, section, c.cName, t.tName, classroom " \
                    "from courseTable ct, courses c, teachers t " \
                    "where weekDay=%s and ct.cID=c.cID and ct.tID=t.tID" % day
    else:  # 全周课表
        selectSql = "select weekDay, section, c.cName, t.tName, classroom " \
                    "from courseTable ct, courses c, teachers t " \
                    "where ct.cID=c.cID and ct.tID=t.tID"

    result, _ = db.GetSql(selectSql)

    courseTable = []
    # 格式化课程数据
    for c in result:
        temp = [c[2], c[4], '星期' + WeekDay[c[0] - 1] + " " + c[1], c[3]]
        courseTable.append(temp)

    return render_template('course.html', courseData=courseTable)


if __name__ == '__main__':
    app.run(debug=True)

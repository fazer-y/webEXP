from flask import Flask, render_template, request, session, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'abcdefgh!@#$%'


@app.route('/', methods=['GET'])
def index():  # put application's code here
    return render_template('index.html')


@app.route('/show1', methods=['GET', 'post'])
def get_multiplicationTable():
    SNumStr = request.form['startNum']
    ENumStr = request.form['endNum']
    try:
        SNum = int(SNumStr)
        ENum = int(ENumStr)

        # 数字范围有误
        if (SNum < 1) or (ENum > 9) or (SNum > ENum):
            flash("请输入1-9的数字，且起始数字小于等于终止数字！", category='error')
            return redirect(url_for('index'))
    except:  # 非数字
        flash("请输入数字！", category='error')
        return redirect(url_for('index'))

    # 绘制乘法表
    return render_template('show1.html', StartNum=SNum, EndNum=ENum)


@app.route('/show2', methods=['GET', 'POST'])
def show2():  # put application's code here
    if request.method == 'GET':
        SNum = 1
        ENum = 9
        return render_template('show2.html', StartNum=SNum, EndNum=ENum)

    SNumStr = request.form['startNum']
    ENumStr = request.form['endNum']
    try:
        SNum = int(SNumStr)
        ENum = int(ENumStr)

        # 数字范围有误
        if (SNum < 1) or (ENum > 9) or (SNum > ENum):
            flash("输入数字有误，请检查后重新输入！", category='error')
            return redirect(url_for('show2'))
    except ValueError:  # 非数字
        flash("请输入1-9的数字，且起始数字小于等于终止数字！", category='error')
        return redirect(url_for('show2'))

    # 绘制乘法表
    return render_template('show2.html', StartNum=SNum, EndNum=ENum)


if __name__ == '__main__':
    app.run(debug=True)

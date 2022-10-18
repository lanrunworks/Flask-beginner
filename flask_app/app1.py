# render_templateを導入
import datetime  # 1.
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    # index.htmlファイルを解析
    # return render_template('index.html')

    # 時間を扱うモジュールの追加

   # 第2引数にテンプレートで使用するオブジェクトを設定
    # 2.
    return render_template(
        'index.html',
        utc_dt=datetime.datetime.utcnow())


@app.route("/about/")
def about():
    return render_template('about.html')


@app.route("/comments/")
def comments():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.']
    return render_template('comments.html', comments=comments)

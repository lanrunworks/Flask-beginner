# flaskモジュールからFlaskをインポート
from flask import Flask, abort
from markupsafe import escape
# Flaskオブジェクトを生成
app = Flask(__name__)  # 1.

# トップページにアクセスしたときに実行される関数を定義


@app.route("/")  # 2.
@app.route("/index/")
def hello():  # 関数名は任意
    # ブラウザに表示される文字列
    return "<h1>こんにちは、世界!</h1><h2>今日がPythonの最後です。</h2>"  # 3.


@app.route("/about/")
def about():
    return '<h3>これはFlaskで作成したアプリケーションです。</h3>'

# <word>キーワードは変化します


@app.route("/capitalize/<word>/")  # 1.
def capitalize(word):
    # return '<h1>{}</h1>'.format(escape(word.capitalize())) # 2.
    return f'<h1>{ escape(word.capitalize()) }</h1>'

# 整数型の値を受け取り


@app.route("/add/<int:n1>/<int:n2>/")
def add(n1, n2):
    # 2つの値を加算した値を返却
    return f'<h1>{n1 + n2}</h1>'

# 整数型のuser_idで情報を取得


@app.route("/users/<int:user_id>/")
def greet_user(user_id):
    users = ['東京', '大阪', '名古屋']  # リスト
    try:
        # 指定された要素の情報を返却
        return f'<h2>{users[user_id]}</h2>'
    except IndexError:
        abort(404)

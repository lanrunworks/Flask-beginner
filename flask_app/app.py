from flask import Flask, render_template

app = Flask(__name__)

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Tow Content'}
            ]


@app.route("/")
def index():
    # リストを渡す
    return render_template('index.html', messages=messages)

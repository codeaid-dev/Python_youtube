from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'トップページ'

@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/projects/')
def projects():
    return 'プロジェクトページ'

@app.route('/user/<username>')
def show_user(username):
    return f'ユーザー名：{escape(username)}'

@app.route('/post/<float:post_id>')
def show_post(post_id):
    return f'投稿番号：{post_id+1}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
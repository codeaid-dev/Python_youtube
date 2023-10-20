from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'トップページ'

@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/redirect')
def tensou():
    return redirect(url_for('hello'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
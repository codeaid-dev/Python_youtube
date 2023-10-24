from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/menu/')
def menu():
    m = [
        {'item':'コーヒー','price':340},
        {'item':'パンケーキ','price':750},
        {'item':'クレープ','price':600},
        {'item':'<script>alert("XSS");</script>','price':100}
    ]
    return render_template('menu.html',menu=m)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
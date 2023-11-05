from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('getpost.html')

@app.route('/who', methods=['GET','POST'])
def who():
    if request.method == 'POST':
        name = request.form['name']
    else:
        name = request.args.get('name')
    return render_template('who.html', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
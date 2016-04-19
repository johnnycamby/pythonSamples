
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #return "<h1>Yo Men!</h1>"
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    #return '<h1>Hey, {0}!<h1>'.format(name)
    return render_template('user.html')

if __name__ == '__main__':
    app.run(debug=True)
import os
import psycopg2
from flask import Flask, render_template, g
import pickle

import scipy
import sklearn
from sklearn.cluster import KMeans


app = Flask(__name__)

# get data






@app.route('/')
@app.route('/<name>')
def index(name="defaultName"):
    return "hello from {}".format(name)


@app.route('/predict/<turd>')
@app.route('/predict/<float:one>/<float:two>/<float:three>/<float:four>')
def predict(one, two, three, four):

    file_path = os.path.join(app.root_path, 'static', 'my_saved_model.pkl')
    loaded_model = pickle.load(open(file_path, 'rb'))
    a_test = [one, two, three, four]
    result_a = loaded_model.predict([a_test])
    return "The result is {}".format(result_a)

# <int:num2> => extract num2 to as an int
@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return '{} + {} = {}'.format(num1, num2, num1+num2)


# /model/0.068661/-0.12495/0.7627/0.7905907
@app.route('/cats/<float:a>/<float:b>/<float:c>/<float:d>')
@app.route('/cats/<int:a>/<int:b>/<int:c>/<int:d>')
def cats(a, b, c, d):
    return '{} {} {} {}'.format(a,b,c,d)

#considering different combinations of clean style query params
@app.route('/count/<int:num>/<float:thing>')
@app.route('/count/<float:num>/<int:thing>')
@app.route('/count/<num>/<float:thing>')
@app.route('/count/<float:num>/<float:thing>')
@app.route('/count/<int:num>/<int:thing>')
def count(num, thing):
    return 'You have {} {}'.format(num, thing)
    # returns 404 if it gets






#
# @app.route('/')
# def index():
#     return "hello flask - this is a change"

# cur = g.db_conn.cursor()
# cur.execute("SELECT * FROM country;")
# return render_template('index.html', countries=cur.fetchall())

# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')

#
# def connect_db():
#     return psycopg2.connect(os.environ.get('DATABASE_URL'))

# @app.before_request
# def before_request():
#     g.db_conn = connect_db()

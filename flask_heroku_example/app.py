import os
import psycopg2
from flask import Flask, render_template, g
import pickle

import scipy
import sklearn
from sklearn.cluster import KMeans

import tensorflow as tf
sess = tf.InteractiveSession()

app = Flask(__name__)

# get data


@app.route('/')
@app.route('/<name>')
def index(name="defaultName"):
    return "hello from {}".format(name)
#tensorflow route

@app.route('/tensor/<string>')
def tensor(string="default_string"):

    file_path = os.path.join(app.root_path, 'static', './spikes/spikes.ckpt')
    
    spikes = tf.Variable([False]*8, name="spikes")
    # try
    
    print('\n')
    print('normal print', spikes)
    print('\n')
    print('wrapped in str()', str(spikes))
    print('\n')
    print('normal print', spikes)
    
    #simple test return
    return "default string: {}, spikes: {}".format(string, spikes)


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

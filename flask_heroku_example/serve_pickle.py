from flask import Flask
## to get access to request url and query params
from flask import request
## classes typically are uppercase
import pickle
import numpy as np

## namespace, "__name__" is 'simple_app' if imported to another file and
## 'main' if being run directly.
app = Flask(__name__)
## define routes
# simple request http://localhost:5000/?name=BeanBagMagoo
@app.route('/')
@app.route('/<name>')
def index(name="defaultName"):
    return "hello from {}".format(name)


@app.route('/predict/<turd>')
@app.route('/predict/<float:one>/<float:two>/<float:three>/<float:four>')
def predict(one, two, three, four):

    # filename = "finalized_model.sav"
    # loaded_model = pickle.load(open(filename, 'rb'))
    # a = [one, two, three, four]
    # result_a = loaded_model.predict(np.reshape(a, [1, 4]))
    return "You sent {} {} {} {}".format(one, two, three, four)

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


app.run(debug=True, port=5000, host='0.0.0.0')

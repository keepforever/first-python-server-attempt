import os
import psycopg2
from flask import Flask, render_template, g


app = Flask(__name__)


@app.route('/')
def index():
    return "hello flask - this is a change"

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

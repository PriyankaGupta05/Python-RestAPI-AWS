import flask
from flask import request, jsonify
from flask_restful import Resource, Api
import sqlite3
from flask import Flask, make_response

app = flask.Flask(__name__)
api = Api(app)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Customer REST API</h1>
<p>Current version of this API is v1.</p>'''

@app.route('/api/', methods=['GET'])
def home_api():
    return home()

# Dictionary for handlind customers data.. 
def dict_factory(cursor, row):

    d={}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]

    return d

# get all the data for GET method using API default url and database [table name = customers] ..
@app.route('/api/version/', methods=['GET'])
def get_version():
    conn = sqlite3.connect("customers-db-dummy.db")
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_data = cur.execute('SELECT * FROM customers').fetchall()

    return make_response('''<h1>Customer REST API</h1><p>Current version of this API is v1.</p>''', 200)
    #return make_response('''<h1>Customer REST API</h1><p>Current version of this API is v1.</p>''',jsonify(all_data), 200)
    
# Error handling response for the application api...
@app.errorhandler(404)
def page_not_found():
    return make_response(
        "<h1>404</h1><p>Resource Not Found.</p>",
        404
    )

@app.errorhandler(400)
def bad_request():
    return make_response(
        "<h1>400</h1><p>Bad request.</p>",
        400
    )
@app.errorhandler(500)
def server_error():
    return make_response(
        "<h1>500</h1><p>Internal server error..</p>",
        500
    )

##### Run the application.....
app.run(host='localhost', port=9880)

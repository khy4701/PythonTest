from flask import Flask
from flask_restful import Api

from ServiceClass import Departments_Meta


#Create a engine for connecting to SQLite3.
app = Flask(__name__)
api = Api(app)

api.add_resource(Departments_Meta, '/departments/<string:department_name>/<int:abc>')

if __name__ == '__main__':
    #app.run(threaded=True, host='0.0.0.0', port = 8500)
    app.run(threaded=True, host='0.0.0.0', port = 5555)

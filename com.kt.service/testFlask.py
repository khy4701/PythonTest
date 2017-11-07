import time

from flask import request
from flask.app import Flask
from flask.json import jsonify
from flask_restful import Resource, Api

class ttt(Resource):

    
    def post(self):

        # [WEB->RESTIF] RECEIVE PROCESS
        content = request.get_json(force=True)
        
        print request.remote_addr

        return "true"


if __name__== '__main__':
    app = Flask(__name__)
    api = Api(app)
    
    api.add_resource(ttt, '/ttt' )

    app.run(host='0.0.0.0')

import datetime
import time

from flask import request
from flask.json import jsonify
from flask_restful import Resource

class Departments_Meta(Resource):
    
    def get(self, department_name, abc):
        #Perform query and return JSON data
               
        start = datetime.datetime.now()
        time.sleep(3)
        return jsonify(start = start, end = datetime.datetime.now())


    # Json Example ( Parameter & Json Data )             
    def post(self, department_name, abc):

#        content = request.get_json(force=False)

        # Json Payload ( Don't input data with json decoding )
        content = request.get_json(force=True)
        
#        name = content[0]
#        age = content[1]
        name = content['name']
        age = content['age']

        return jsonify( d_name=department_name, abc=abc, name=name , age = age)
        
    # {
    #   "age": 123, 
    #   "name": "11"
    # }
    
    def patch(self,department_name,abc):
        # Query the result and get cursor.Dumping that data to a JSON is looked by extension
    
            content = request.get_json(force=True)
            
            name = content['name']
            age = content['age']
    
            return jsonify(name=name , age = age)


class Departments_Meta2(Resource):
    def post(self):
        return "hihi22"

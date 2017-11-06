from flask.json import jsonify
from flask_restful import Resource, reqparse



class Departmental_Salary(Resource):
    def get(self, department_name):
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
 
        return "True"
        #We can have PUT,DELETE,POST here. But in our API GET implementation is sufficient
   


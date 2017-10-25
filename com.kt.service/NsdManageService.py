import ApiDefine
import PLTEConnector
import datetime
import time

from flask import request
from flask.json import jsonify
from flask_restful import Resource
from ApiDefine import ApiDefine
from PLTEConnector import PLTEConnector

class NsdOnboarding:

    def post(self, department_name, abc):
     # Query the result and get cursor.Dumping that data to a JSON is looked by extension

        content = request.get_json(force=True)

        name = content['name']
        age = content['age']


        PLTEConnector.getInstance().sendMessage(ApiDefine.API_NUM1, abc)

        return jsonify( d_name=department_name, abc=abc, name=name , age = age)




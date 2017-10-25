from flask import request
from flask.json import jsonify
from flask_restful import Resource

from ConfigManager import ConfManager
from LogManager import LogManager
import ServiceManager.TransacManager


class NsdOnboarding(Resource, ServiceManager):

    logger = LogManager.getInstance().get_logger()
    
    def post(self):

        # force = True --> Need!
        content = request.get_json(force=True)

        if ConfManager.getInstance().getLogFlag():
                self.logger.info("===============================================");
                self.logger.info("[WEB] -> RESTIF")
                self.logger.info("===============================================");
                self.logger.info("REQUEST URL : " + request.url)
                self.logger.info("===============================================");
         
        print(content.keys())
                
        name = content['name']
        age = content['age']


        #PLTEConnector.getInstance().sendMessage(ApiDefine.API_NUM1, abc)

        return jsonify( name=name , age = age)
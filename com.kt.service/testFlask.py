import time

from flask import request
from flask.app import Flask
from flask.json import jsonify
from flask_restful import Resource, Api

from ApiDefine import ApiDefine
from ConfigManager import ConfManager
from LogManager import LogManager
from PLTEConnector import PLTEConnector
from PLTEManager import PLTEManager
from ProvMsg import HttpRes
from ServiceManager import ServiceManager


class ttt(Resource, ServiceManager):

    logger = LogManager.getInstance().get_logger()
    
    def post(self):

        # [WEB->RESTIF] RECEIVE PROCESS
        content = request.get_json(force=True)
        data = dict()
        
        for keys in content.keys():
            data[keys] = content[keys]

        # [WEB->RESTIF] RECEIVE LOGGING       
        if ConfManager.getInstance().getLogFlag():
                self.logger.info("===============================================");
                self.logger.info("[WEB] -> RESTIF")
                self.logger.info("===============================================");
                self.logger.info("REQUEST URL : " + request.url)
                self.logger.info("BODY : "  + str(content))
                self.logger.info("===============================================");
                        
        # [RESTIF->APP] MAKE SEND STRUCT
        resMsg = 'temp'
        #resMsg = self.setResMessage(data)
        
        # [RESTIF->APP] SEND QUEUE MESSAGE(RELAY)
        self.clientID = PLTEManager.getInstance().getClientReqId()
        
        self.logger.info("Client ID : " + str(self.clientID));
        
        PLTEManager.getInstance().sendCommand(ApiDefine.NSD_ON_BOARDING, self, self.clientId, resMsg)
                                        
        # WAIT                
        while self.clientID != self.receiveReqId:
            try:
                time.sleep(1)
            except Exception as e:
                self.logger.error(e)
        
        
        # [RESTIF->WEB] SEND LOGGING
        if ConfManager.getInstance().getLogFlag():
                self.logger.info("===============================================");
                self.logger.info("RESTIF -> [WEB]")
                self.logger.info("===============================================");
                self.logger.info("TID : " + str(self.receiveReqId))
                self.logger.info("RESCODE : " + int(self.rspCode))
                self.logger.info("BODY : "  + str(self.body))
                self.logger.info("===============================================");
        
        
        # [RESTIF->WEB] SEND RESPONSE
        name = content['name']
        age = content['age']

        return jsonify( name=name , age = age)

    
    # overide method
    def setComplete(self, rspCode, reqId, rcvMsg):
        self.msg = rcvMsg
        self.rspCode = rspCode
        self.receiveReqId = reqId
    
    # overide method    
    def setResMessage(self, data):
        resMsg  = HttpRes()
        
        return resMsg


if __name__== '__main__':
    app = Flask(__name__)
    api = Api(app)
    
    api.add_resource(ttt, '/ns_descriptors' )

    app.run(threaded=True, host='0.0.0.0')

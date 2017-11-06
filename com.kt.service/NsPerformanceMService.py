import time

from flask import request, json
import flask
from flask.json import jsonify
from flask_restful import Resource

from ApiDefine import ApiDefine
from ConfigManager import ConfManager
from LogManager import LogManager
from PLTEManager import PLTEManager
from ProvMsg import HttpRes, HttpReq, HttpHeader
from ServiceManager import ServiceManager


class CreatePmJobs(Resource, ServiceManager):

    logger = LogManager.getInstance().get_logger()
    
    def post(self):

        # 1. [WEB->RESTIF] RECEIVE PROCESS
        try:
            content = request.get_json(force=True)
            data = json.dumps(content)
        except Exception as e:
            data = ''        
   
        # 2. [WEB->RESTIF] RECEIVE LOGGING       
        ServiceManager.RecvLogging(self.logger, data, request)
                        
        # 3. [RESTIF->APP] MAKE SEND STRUCT
        self.clientId = PLTEManager.getInstance().getClientReqId()
        reqMsg = ServiceManager.setApiToStructMsg(data, self.clientId)
                
        # 4. [RESTIF->APP] SEND QUEUE MESSAGE(RELAY)
        PLTEManager.getInstance().sendCommand(ApiDefine.CREATE_PM_JOB, self, reqMsg)
                                        
        # 5. WAIT                
        self.receiveReqId = -1
        while self.clientId != self.receiveReqId:
            try:
                time.sleep(1)
            except Exception as e:
                self.logger.error(e)
        
        # 6. [RESTIF->WEB] SEND LOGGING
        ServiceManager.SendLogging(self.logger, self.resMsg)

        # 7. [RESTIF->WEB] SEND RESPONSE        
        return flask.Response(
            self.resMsg.jsonBody,
                       # mimetype=content_type,
            status=self.rspCode
        )
    
    # overide method
    def setComplete(self, rspCode, reqId, rcvMsg):
        self.resMsg = rcvMsg
        self.rspCode = rspCode
        self.receiveReqId = reqId
        
        
class QueryPmJob(Resource, ServiceManager):

    logger = LogManager.getInstance().get_logger()
    
    def post(self,pmJobId,reportId):

        # 1. [WEB->RESTIF] RECEIVE PROCESS
        try:
            content = request.get_json(force=True)
            data = json.dumps(content)
        except Exception as e:
            data = ''       
   
        # 2. [WEB->RESTIF] RECEIVE LOGGING       
        ServiceManager.RecvLogging(self.logger, data, request)
                        
        # 3. [RESTIF->APP] MAKE SEND STRUCT
        self.clientId = PLTEManager.getInstance().getClientReqId()
        reqMsg = ServiceManager.setApiToStructMsg(data, self.clientId)
                
        # 4. [RESTIF->APP] SEND QUEUE MESSAGE(RELAY)
        PLTEManager.getInstance().sendCommand(ApiDefine.QUERY_PM_JOB, self, reqMsg)
                                        
        # 5. WAIT                
        self.receiveReqId = -1
        while self.clientId != self.receiveReqId:
            try:
                time.sleep(1)
            except Exception as e:
                self.logger.error(e)
        
        # 6. [RESTIF->WEB] SEND LOGGING
        ServiceManager.SendLogging(self.logger, self.resMsg)

        # 7. [RESTIF->WEB] SEND RESPONSE        
        return flask.Response(
            self.resMsg.jsonBody,
                       # mimetype=content_type,
            status=self.rspCode
        )
    
    # overide method
    def setComplete(self, rspCode, reqId, rcvMsg):
        self.resMsg = rcvMsg
        self.rspCode = rspCode
        self.receiveReqId = reqId

    
import time

from flask import request
import flask
from flask.json import jsonify
from flask_restful import Resource

from ApiDefine import ApiDefine
from ConfigManager import ConfManager
from LogManager import LogManager
from PLTEManager import PLTEManager
from ProvMsg import HttpRes, HttpReq, HttpHeader
from ServiceManager import ServiceManager


class NsIdCreation(Resource, ServiceManager):

    logger = LogManager.getInstance().get_logger()
    
    def post(self):

        # [WEB->RESTIF] RECEIVE PROCESS
        content = request.get_json(force=True)
   
        # [WEB->RESTIF] RECEIVE LOGGING       
        if ConfManager.getInstance().getLogFlag():
                self.logger.info("===============================================");
                self.logger.info("[WEB] -> RESTIF")
                self.logger.info("===============================================");
                self.logger.info("REQUEST URL : " + request.url)
                self.logger.info("BODY : "  + str(content))
                self.logger.info("===============================================");
                        

        self.logger.info("MAKE SEND STRUCT");
        # [RESTIF->APP] MAKE SEND STRUCT
        self.clientId = PLTEManager.getInstance().getClientReqId()
        #resMsg = 'temp'
        self.logger.info("[RESTIF->APP] SEND QUEUE MESSAGE(RELAY)");
        reqMsg = self.setReqMessage( str(content), self.clientId)
        
        # [RESTIF->APP] SEND QUEUE MESSAGE(RELAY)
        self.logger.info("[RESTIF->APP] SEND QUEUE MESSAGE(RELAY)");
        PLTEManager.getInstance().sendCommand(ApiDefine.NS_ID_CREATE, self, reqMsg)
                                        
        # WAIT                
        self.receiveReqId = -1
        while self.clientId != self.receiveReqId:
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
                self.logger.info("RESCODE : " + str(self.rspCode))
                self.logger.info("BODY : "  + str(self.resMsg.jsonBody))
                self.logger.info("===============================================");
        
        
        # [RESTIF->WEB] SEND RESPONSE
        
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
    
    # overide method    
    def setReqMessage(self, receiveMsg, reqId):

        httpMsg =  HttpReq()
        header = HttpHeader()
         
        header.method = 1
        header.api_type = 2
        header.op_type = 3
        header.length = 4
        header.encoding = '5'        
                 
        httpMsg.msgId = reqId
        httpMsg.ehttpf_idx = 71
        httpMsg.srcQid = 300
        httpMsg.srcSysId = '1'
        httpMsg.http_hdr = header
        httpMsg.jsonBody = receiveMsg
        
        httpMsg.tot_len = 100

        
        return httpMsg

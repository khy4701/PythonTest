import time

from flask import request, json
import flask
from flask_restful import Resource

from ApiDefine import ApiDefine, MethodType, ApiType, OPType, ResourceType
from LogManager import LogManager
from PLTEManager import PLTEManager
from ServiceManager import ServiceManager


class NsIdCreation(Resource, ServiceManager):

    logger = LogManager.getInstance().get_logger()
    apiType = ApiType.NSLCM_API_TYPE
    resourceType = ResourceType.NSLCM_NS_INSTANCES
        
    def post(self):
        opType = OPType.Create_NS_Identifier_OP_TYPE
        methodType = ServiceManager.getMethodType(request.method)
        
        # 1. [WEB->RESTIF] RECEIVE PROCESS
        try:    
            content = request.get_json(force=True)
            data = json.dumps(content)
        except Exception as e:
            data = ''          

        # 2. [WEB->RESTIF] RECEIVE LOGGING       
        ServiceManager.RecvLogging(self.logger, data, request)
                        
        # 3. [RESTIF->APP] MAKE SEND STRUCT
        self.logger.info(type(MethodType.POST_METHOD_TYPE))
        self.clientId = PLTEManager.getInstance().getClientReqId()
        reqMsg = ServiceManager.setApiToStructMsg(request, data, self.clientId, methodType, self.apiType, self.resourceType, opType )
                
        # 4. [RESTIF->APP] SEND QUEUE MESSAGE(RELAY)
        PLTEManager.getInstance().sendCommand(ApiDefine.NS_ID_CREATE, self, reqMsg)
                                        
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
    

class NsInstantiation(Resource, ServiceManager):
    logger = LogManager.getInstance().get_logger()
    apiType = ApiType.NSLCM_API_TYPE
    resourceType = ResourceType.NSLCM_INSTANTIATE_NS_TASK

    def post(self,nsInstanceId ):
        opType = OPType.Instantiate_NS_OP_TYPE
        methodType = ServiceManager.getMethodType(request.method)

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
        reqMsg = ServiceManager.setApiToStructMsg(request, data, self.clientId, methodType, self.apiType, self.resourceType, opType )
                
        # 4. [RESTIF->APP] SEND QUEUE MESSAGE(RELAY)
        PLTEManager.getInstance().sendCommand(ApiDefine.NS_INSTANTIATION, self, reqMsg)
                                        
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
        
        
class NsIdTermination(Resource, ServiceManager):
    logger = LogManager.getInstance().get_logger()
    apiType = ApiType.NSLCM_API_TYPE
    resourceType = ResourceType.NSLCM_TERMINATE_NS_TASK

    def post(self,nsInstanceId):
        opType = OPType.Terminate_NS_OP_TYPE
        methodType = ServiceManager.getMethodType(request.method)

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
        reqMsg = ServiceManager.setApiToStructMsg(request, data, self.clientId, methodType, self.apiType, self.resourceType, opType )
                
        # 4. [RESTIF->APP] SEND QUEUE MESSAGE(RELAY)
        PLTEManager.getInstance().sendCommand(ApiDefine.NS_TERMINATION, self, reqMsg)
                                        
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
        
        
class NsScale(Resource, ServiceManager):
    logger = LogManager.getInstance().get_logger()
    apiType = ApiType.NSLCM_API_TYPE
    resourceType = ResourceType.NSLCM_SCALE_NS_TASK

    def post(self,nsInstanceId):
        opType = OPType.Scale_NS_OP_TYPE
        methodType = ServiceManager.getMethodType(request.method)

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
        reqMsg = ServiceManager.setApiToStructMsg(request, data, self.clientId, methodType, self.apiType, self.resourceType, opType )
                
        # 4. [RESTIF->APP] SEND QUEUE MESSAGE(RELAY)
        PLTEManager.getInstance().sendCommand(ApiDefine.NS_SCALE, self, reqMsg)
                                        
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

#api.add_resource(NsIdTermination, Service.NS_TERMINATION )
#api.add_resource(NsScale, Service.NS_SCALE )

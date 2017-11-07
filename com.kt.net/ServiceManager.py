from abc import abstractmethod
import ctypes

from ApiDefine import MethodType, ApiType, OPType, ContentEncoding, ResourceType
from ConfigManager import ConfManager
from ProvMsg import HttpReq, HttpHeader, HttpInfo


class ServiceManager:
        
    @abstractmethod    
    def setComplete(self, rspCode, reqId, rcvMsg):
        pass
        
    @staticmethod
    def setApiToStructMsg(reqAPI, receiveMsg, reqId):

        httpInfo = HttpInfo()
        httpMsg =  HttpReq()
        header = HttpHeader()

        httpInfo.nfvo_ip = "None"
        httpInfo.nfvo_port = 0

        header.method = MethodType.POST_METHOD_TYPE
        header.api_type = ApiType.NSLCM_API_TYPE
        header.op_type = OPType.Create_NS_Identifier_OP_TYPE
        header.resource_type = ResourceType.NSLCM_NS_INSTANCES
        header.length = len(receiveMsg)
        header.encoding = ContentEncoding.PLAIN
                 
        httpMsg.mtype = 123    # 
        httpMsg.msgId = 111
        httpMsg.tid   = reqId
        httpMsg.ehttpf_idx = 71
        httpMsg.srcQid = 111
        httpMsg.srcSysId = '1'
        httpMsg.info = httpInfo
        httpMsg.http_hdr = header
        httpMsg.jsonBody = receiveMsg
        
        httpMsg.tot_len = ctypes.sizeof(httpMsg) # need..
        
        return httpMsg

    
    @staticmethod
    def RecvLogging(logger, data, reqAPI):
        if ConfManager.getInstance().getLogFlag():
            logger.info("===============================================");
            logger.info("[WEB] -> RESTIF")
            logger.info("===============================================");
            logger.info("REQUEST URL : " + reqAPI.url)
            logger.info("BODY : "  + data)
            logger.info("===============================================");
            
    @staticmethod
    def SendLogging(logger, resMsg):
        if ConfManager.getInstance().getLogFlag():
            logger.info("===============================================");
            logger.info("RESTIF -> [WEB]")
            logger.info("===============================================");
            logger.info("TID : " + str(resMsg.tid))
            logger.info("RESCODE : " + str(resMsg.nResult))
            logger.info("BODY : "  + str(resMsg.jsonBody))
            logger.info("===============================================");



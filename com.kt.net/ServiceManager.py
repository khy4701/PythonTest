from abc import abstractmethod

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

        header.method = 1
        header.api_type = 2
        header.op_type = 3
        header.length = 4
        header.encoding = '5'        
                 
        httpMsg.mtype = 9
        httpMsg.msgId = 6
        httpMsg.tid   = reqId
        httpMsg.ehttpf_idx = 71
        httpMsg.srcQid = 300
        httpMsg.srcSysId = '1'
        httpMsg.http_hdr = header
        httpMsg.jsonBody = receiveMsg
        
        httpMsg.tot_len = 100
        
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



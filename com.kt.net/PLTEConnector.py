# -*- coding: utf-8 -*-
import Connector
import PLTEConnector
import ctypes
import sys

from ConfigManager import ConfManager
from Connector import *
from PLTEManager import PLTEManager
from ProvMsg import HttpReq, HttpRes, HttpHeader
import sysv_ipc, time, signal


class PLTEConnector(Connector):
    
    __instance = None
    
    logger = LogManager.getInstance().get_logger()

    @staticmethod
    def getInstance():
        """ Static access method. """
        if PLTEConnector.__instance == None:
            PLTEConnector.__instance = PLTEConnector()
        return PLTEConnector.__instance 

    def __init__(self):
        self.logger.debug('PLTEConnector Init')
        Connector.__init__(self, PLTEManager.getInstance())

        self.plteQueId = int(ConfManager.getInstance().getConfigData( ConfManager.MSGQUEUE_INFO , "PLTEIB" ))
        try :
                self.plteQueue = sysv_ipc.MessageQueue(self.plteQueId)
        except Exception as e:
                self.logger.error("msgQueue Connection Failed.. PLTE QUEUE_ID[%d]" % self.plteQueId)


    def sendMessage(self, apiName, reqId, receiveMsg):
        
        httpMsg =  HttpReq()
        header = HttpHeader()
         
        header.method = 1
        header.api_type = 2
        header.op_type = 3
        header.length = 4
        header.encoding = '5'        
                 
        httpMsg.tot_len = 100
        httpMsg.msgId = reqId
        httpMsg.ehttpf_idx = 71
        httpMsg.srcQid = 300
        httpMsg.srcSysId = '1'
        httpMsg.http_hdr = header
        httpMsg.jsonBody = receiveMsg

        pData = ctypes.cast(ctypes.byref(httpMsg), ctypes.POINTER(ctypes.c_char * ctypes.sizeof(httpMsg)))

        try:
            if self.plteQueue is not None :
                    self.plteQueue.send( pData.contents.raw, True, HttpReq.MTYPE_RESTIF_TO_APP_REQ )

        except Exception as e:
            self.logger.error("sendMessage Error! %s" % e)
            return False

        if ConfManager.getInstance().getLogFlag():
            self.logger.info("===============================================");
            self.logger.info("RESTIF -> PLTEIB")
            self.logger.info("===============================================");
            self.logger.info("API_NAME : " + str(apiName))
            self.logger.info("PID   : "+ str(reqId))
            self.logger.info("BODY   : " + str(receiveMsg))
            self.logger.info("===============================================");
            
        return True


    def sendResMessage(self, resMsg):
                
        pData = ctypes.cast(ctypes.byref(resMsg), ctypes.POINTER(ctypes.c_char * ctypes.sizeof(resMsg)))
        try:
            if self.plteQueue is not None :
                
                # MSG TYPE Check!
                self.plteQueue.send( pData.contents.raw, True, HttpRes.MTYPE_RESTIF_TO_APP_RES )
                
        except Exception as e:
            self.logger.error("sendMessage Error! %s" % e)
            return False

        if ConfManager.getInstance().getLogFlag():
            self.logger.info("===============================================");
            self.logger.info("RESTIF -> PLTEIB")
            self.logger.info("===============================================");
#             self.logger.info("API_NAME : " + str(apiName))
#             self.logger.info("PID   : "+ str(reqId))
#             self.logger.info("BODY   : " + str(receiveMsg))
            self.logger.info("===============================================");
            
        return True

    
# if __name__ == '__main__':
#       
#     if PLTEConnector.logger is None :
#         print 'None..'
#           
#     # PLTEConnector.logger = LogManager.getInstance()
#       
#     conn = PLTEConnector()    
#     conn.sendMessage()

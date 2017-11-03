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
                maxQSize = ConfManager.getInstance().getConfigData( ConfManager.MSGQUEUE_INFO , "MAX_QUEUE_SIZE" )
                self.plteQueue = sysv_ipc.MessageQueue(self.plteQueId)
                    
        except Exception as e:
                self.logger.error("msgQueue Connection Failed.. PLTE QUEUE_ID[%d] SIZE[%s]" % (self.plteQueId, maxQSize))


    def sendMessage(self, apiName, httpReqMsg):
        
        self.logger.info("Send Message..!")
        
        pData = ctypes.cast(ctypes.byref(httpReqMsg), ctypes.POINTER(ctypes.c_char * ctypes.sizeof(httpReqMsg)))

        try:
            if self.plteQueue is not None :
                    
                self.plteQueue.send( pData.contents.raw, True, HttpReq.MTYPE_RESTIF_TO_APP_REQ )

        except Exception as e:
            self.logger.error("sendMessage Error! %s" % e)
            return False

        if ConfManager.getInstance().getLogFlag():
            self.logger.info("===============================================")
            self.logger.info("RESTIF -> PLTEIB")
            self.logger.info("===============================================")
            self.logger.info("API_NAME : " + str(apiName))
            self.logger.info("PID   : "+ str(httpReqMsg.msgId))
            self.logger.info("BODY   : " + str(httpReqMsg.jsonBody))
            self.logger.info("===============================================")
            
        return True


    def sendResMessage(self, command, resMsg):
                
        pData = ctypes.cast(ctypes.byref(resMsg), ctypes.POINTER(ctypes.c_char * ctypes.sizeof(resMsg)))
        try:
            if self.plteQueue is not None :
                
                # MSG TYPE Check!
                self.plteQueue.send( pData.contents.raw, True, HttpRes.MTYPE_RESTIF_TO_APP_RES )
                
        except Exception as e:
            self.logger.error("sendMessage Error! %s" % e)
            return False

        if ConfManager.getInstance().getLogFlag():
            self.logger.info("===============================================")
            self.logger.info("RESTIF -> [APP]")
            self.logger.info("===============================================")
            self.logger.info("API_NAME : " + str(command))
            self.logger.info("PID   : "+ str(resMsg.msgId))
            self.logger.info("RESTCODE : " + str(resMsg.nResult) )
            self.logger.info("BODY   : " + resMsg.jsonBody)
            self.logger.info("===============================================")
            
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

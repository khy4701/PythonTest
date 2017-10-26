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
        self.myQueue = Connector.getMyQueue()
        try :
                self.plteQueue = sysv_ipc.MessageQueue(self.plteQueId)
        except Exception as e:
                self.logger.error("msgQueue Connection Failed.. PLTE QUEUE_ID[%d]" % self.plteQueId)


    def readMessage(self):
        try:
                resMsg = HttpRes()
                
                if self.myQueue is None:
                    self.myQueue = Connector.getMyQueue()
                    self.logger.error("tttttttttttttttttt..")

                    if self.myQueue is None:
                        self.logger.error("msgQueue[MYQUEUE] Get Failed...")
                        return 

                (message, msgType) = self.myQueue.receive(ctypes.sizeof(resMsg))
                
                mydata = ctypes.create_string_buffer( message )
                ctypes.memmove(ctypes.pointer(resMsg), mydata ,ctypes.sizeof(resMsg))

                time.sleep(1)

                headerMsg = resMsg.http_hdr

                # Receive Message Logging
                if ConfManager.getInstance().getLogFlag():
                    self.logger.info("===============================================");
                    self.logger.info("PLTEIB -> RESTIF")
                    self.logger.info("===============================================");
                    self.logger.info("msgType: %d" %msgType )
                    self.logger.info("tot_len : %s" %resMsg.tot_len )
                    self.logger.info("msgId : %d" %resMsg.msgId )
                    self.logger.info("ehttp_idx : %d" %resMsg.ehttpf_idx )
                    self.logger.info("srcQid : %d" %resMsg.srcQid )
                    self.logger.info("srcSysId : %c" %resMsg.srcSysId )
                    self.logger.info("nResult : %d" %resMsg.nResult )
                    self.logger.info("jsonBody: %s" %resMsg.jsonBody )
                    self.logger.info("===============================================");
                    self.logger.info("method: %d" %headerMsg.method )
                    self.logger.info("api_type: %d" %headerMsg.api_type )
                    self.logger.info("op_type: %d" %headerMsg.op_type )
                    self.logger.info("length: %d" %headerMsg.length )
                    self.logger.info("encoding: %c" %headerMsg.encoding )
                    
                self.manager.receiveHandling(resMsg.nResult, resMsg.msgId, resMsg.jsonBody )
                
        
        except Exception as e :
                self.logger.error("Msgrcv Failed..  %s" %e)
                time.sleep(1)
        

    def sendMessage(self, apiName, reqId, receiveMsg):
        
        self.logger.debug('Send Message')
        

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


    
# if __name__ == '__main__':
#       
#     if PLTEConnector.logger is None :
#         print 'None..'
#           
#     # PLTEConnector.logger = LogManager.getInstance()
#       
#     conn = PLTEConnector()    
#     conn.sendMessage()

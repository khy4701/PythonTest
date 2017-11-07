# -*- coding: utf-8 -*-
import ctypes

from ConfigManager import ConfManager
from Connector import Connector
from LogManager import LogManager
import PLTEConnector
from PLTEManager import PLTEManager
from ProvMsg import GeneralQResMsg, GeneralQReqMsg, MTYPE_NBRESTIF_TO_SLEE_REQ, \
    MTYPE_NBRESTIF_TO_SLEE_RES, MTYPE_SBRESTIF_TO_SLEE_RES
import sysv_ipc


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
                self.plteQueue = sysv_ipc.MessageQueue(self.plteQueId, max_message_size = int(maxQSize) )
                    
        except Exception as e:
                self.logger.error("msgQueue Connection Failed.. PLTE QUEUE_ID[%d] SIZE[%s]" % (self.plteQueId, maxQSize))


    def sendMessage(self, apiName, httpReqMsg):
        
        self.logger.info("Send Message..!")
        
        GenQMsg = GeneralQReqMsg()        
        GenQMsg.body = httpReqMsg
        
        pData = ctypes.cast(ctypes.byref(GenQMsg), ctypes.POINTER(ctypes.c_char * ctypes.sizeof(GenQMsg)))

        try:
            if self.plteQueue is not None :
                self.plteQueue.send( pData.contents.raw, True, MTYPE_NBRESTIF_TO_SLEE_REQ )

        except Exception as e:
            self.logger.error("sendMessage Error! %s" % e)
            return False

        if ConfManager.getInstance().getLogFlag():
            self.logger.info("===============================================")
            self.logger.info("NBRESTIF -> SLEE")
            self.logger.info("===============================================")
            self.logger.info("API_NAME : " + str(apiName))
            self.logger.info("PID   : "+ str(httpReqMsg.tid))
            self.logger.info("BODY   : " + str(httpReqMsg.jsonBody))
            self.logger.info("===============================================")
            
        return True


    def sendResMessage(self, command, resMsg):
                
        GenQMsg = GeneralQResMsg()        
        GenQMsg.body = resMsg
        
        pData = ctypes.cast(ctypes.byref(GenQMsg), ctypes.POINTER(ctypes.c_char * ctypes.sizeof(GenQMsg)))
        try:
            if self.plteQueue is not None :
                
                # MSG TYPE Check!
                self.plteQueue.send( pData.contents.raw, True, MTYPE_SBRESTIF_TO_SLEE_RES )
                
        except Exception as e:
            self.logger.error("sendMessage Error! %s" % e)
            return False

        if ConfManager.getInstance().getLogFlag():
            self.logger.info("===============================================")
            self.logger.info("SBRESTIF -> SLEE")
            self.logger.info("===============================================")
            self.logger.info("API_NAME : " + str(command))
            self.logger.info("PID   : "+ str(resMsg.tid))
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

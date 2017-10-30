import ctypes
import threading
import time

from ConfigManager import ConfManager
from Connector import Connector
from LogManager import LogManager
from PLTEManager import PLTEManager
from ProvMsg import HttpRes
import sysv_ipc

usleep = lambda x: time.sleep(x/1000000.0)

class Receiver(threading.Thread):
    
    myQueue = None   
    __instance = None
    
    logger = LogManager.getInstance().get_logger()

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Receiver.__instance == None:
            Receiver.__instance = Receiver()
        return Receiver.__instance 
        
    
    def __init__(self):
        super(Receiver,self).__init__()

        try :
            myQueId = 0
            if Receiver.myQueue is None:
                    #IPC_CREAT : create or return key if it is allocated.
                    #IPC_CREX  : IPC_CREAT | IPC_EXCL 
                    #IPC_EXCL  : return -1 if there is already allocated.
                    myQueId = int(ConfManager.getInstance().getConfigData( ConfManager.MSGQUEUE_INFO , "RESTIF" ))    
                    Receiver.myQueue = sysv_ipc.MessageQueue(myQueId, sysv_ipc.IPC_CREAT, mode=0777 )
                    
                    self.receiver = self
                    self.receiver.start()

            
        except Exception as e:
                Receiver.logger.error("msgQueue Connection Failed.. RESTIF QUEUE_ID[%d] %s" % (myQueId, e))

        return None

    
    @staticmethod
    def readMessage():
        try:
            resMsg = HttpRes()
            
            if Receiver.myQueue is None:
                Receiver.myQueue = Receiver.getMyQueue()
    
                if Receiver.myQueue is None:
                    Receiver.logger.error("msgQueue[MYQUEUE] Get Failed...")
                    return 
    
            (message, msgType) = Receiver.myQueue.receive(ctypes.sizeof(resMsg))
            
            mydata = ctypes.create_string_buffer( message )
            ctypes.memmove(ctypes.pointer(resMsg), mydata ,ctypes.sizeof(resMsg))
    
            time.sleep(1)
    
            headerMsg = resMsg.http_hdr
    
            # Receive Message Logging
            if ConfManager.getInstance().getLogFlag():
                Receiver.logger.info("===============================================");
                Receiver.logger.info("[APP] -> RESTIF")
                Receiver.logger.info("===============================================");
                Receiver.logger.info("msgType: %d" %msgType )
                Receiver.logger.info("tot_len : %s" %resMsg.tot_len )
                Receiver.logger.info("msgId : %d" %resMsg.msgId )
                Receiver.logger.info("ehttp_idx : %d" %resMsg.ehttpf_idx )
                Receiver.logger.info("srcQid : %d" %resMsg.srcQid )
                Receiver.logger.info("srcSysId : %c" %resMsg.srcSysId )
                Receiver.logger.info("nResult : %d" %resMsg.nResult )
                Receiver.logger.info("jsonBody: %s" %resMsg.jsonBody )
                Receiver.logger.info("===============================================");
                Receiver.logger.info("method: %d" %headerMsg.method )
                Receiver.logger.info("api_type: %d" %headerMsg.api_type )
                Receiver.logger.info("op_type: %d" %headerMsg.op_type )
                Receiver.logger.info("length: %d" %headerMsg.length )
                Receiver.logger.info("encoding: %c" %headerMsg.encoding )
                       
            
            PLTEManager.getInstance().receiveHandling(resMsg.nResult, resMsg.msgId, resMsg.jsonBody )
                
        
        except Exception as e :
            Receiver.logger.error("Msgrcv Failed..  %s" %e)
            time.sleep(1)
            
        
    def run(self):      
 
        try:                                
            while self.receiver == self:
                usleep(100)
                self.readMessage()
                 
        except Exception as e:
            self.logger.error(e)
#       self.readMessage()



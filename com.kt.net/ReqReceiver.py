import ctypes
import threading
import time

from ClientService import ClientService
from ConfigManager import ConfManager
from Connector import Connector
from LogManager import LogManager
from PLTEManager import PLTEManager
from ProvMsg import HttpRes, HttpReq, MTYPE_CLIENT_MODE
from Receiver import Receiver
import sysv_ipc


usleep = lambda x: time.sleep(x/1000000.0)

class ReqReceiver(Receiver):
    
    myQueue = None   
    __instance = None
    
    logger = LogManager.getInstance().get_logger()

    @staticmethod
    def getInstance():
        """ Static access method. """
        if ReqReceiver.__instance == None:
            ReqReceiver.__instance = ReqReceiver()
        return ReqReceiver.__instance 
        
    
    def __init__(self):
        Receiver.__init__(self)
        ReqReceiver.logger.error("ReqReceiver Init")

        try :
            myQueId = 0
            if ReqReceiver.myQueue is None:
                    #IPC_CREAT : create or return key if it is allocated.
                    #IPC_CREX  : IPC_CREAT | IPC_EXCL 
                    #IPC_EXCL  : return -1 if there is already allocated.
                    myQueId = int(ConfManager.getInstance().getConfigData( ConfManager.MSGQUEUE_INFO , "RESTIF_C" ))    
                    maxQSize = ConfManager.getInstance().getConfigData( ConfManager.MSGQUEUE_INFO , "MAX_QUEUE_SIZE" )

                    ReqReceiver.myQueue = sysv_ipc.MessageQueue(myQueId, sysv_ipc.IPC_CREAT, mode=0777 , max_message_size = int(maxQSize) )
                    
                    self.reqReceiver = self
                    self.reqReceiver.start()
            
        except Exception as e:
                ReqReceiver.logger.error("msgQueue Connection Failed.. RESTIF_C QUEUE_ID[%d] %s" % (myQueId, e))

        return None


    def readMessage(self):
        try:
            
            if ReqReceiver.myQueue is None:
                self.logger.error("msgQueue[RESTIF_RECV] Get Failed...")
                return
            
            reqMsg = HttpReq()
            (message, msgType) = ReqReceiver.myQueue.receive(ctypes.sizeof(reqMsg))
            mydata = ctypes.create_string_buffer( message )
            
            if msgType == MTYPE_CLIENT_MODE:    
                # Client Mode ( Handling Request Message )
                
                ctypes.memmove(ctypes.pointer(reqMsg), mydata ,ctypes.sizeof(reqMsg))
                            
                # Receive Message Logging
                if ConfManager.getInstance().getLogFlag():
                    headerMsg = reqMsg.http_hdr                    
                    self.logger.info("===============================================")
                    self.logger.info("[APP] -> RESTIF")
                    self.logger.info("===============================================")
                    self.logger.info("msgType: %d" %msgType )
                    self.logger.info("tot_len : %s" %reqMsg.tot_len )
                    self.logger.info("msgId : %d" %reqMsg.msgId )
                    self.logger.info("ehttp_idx : %d" %reqMsg.ehttpf_idx )
                    self.logger.info("srcQid : %d" %reqMsg.srcQid )
                    self.logger.info("srcSysId : %c" %reqMsg.srcSysId )
                    self.logger.info("jsonBody: %s" %reqMsg.jsonBody )
                    self.logger.info("===============================================")
                    self.logger.info("method: %d" %headerMsg.method )
                    self.logger.info("api_type: %d" %headerMsg.api_type )
                    self.logger.info("op_type: %d" %headerMsg.op_type )
                    self.logger.info("length: %d" %headerMsg.length )
                    self.logger.info("encoding: %c" %headerMsg.encoding )
                    self.logger.info("===============================================")

                clientReq = ClientService(reqMsg)
                clientReq.start()
                return 
        
        except Exception as e :
            self.logger.error("Msgrcv Failed..  %s" %e)
            time.sleep(1)
            
        
    def run(self):      
 
        try:                                
            while self.reqReceiver == self:
                usleep(100)
                self.readMessage()
                 
        except Exception as e:
            self.logger.error(e)
#       self.readMessage()



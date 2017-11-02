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
        
        try :
            myQueId = 0
            if ReqReceiver.myQueue is None:
                    #IPC_CREAT : create or return key if it is allocated.
                    #IPC_CREX  : IPC_CREAT | IPC_EXCL 
                    #IPC_EXCL  : return -1 if there is already allocated.
                    myQueId = int(ConfManager.getInstance().getConfigData( ConfManager.MSGQUEUE_INFO , "RESTIF_C" ))    
                    ReqReceiver.myQueue = sysv_ipc.MessageQueue(myQueId, sysv_ipc.IPC_CREAT, mode=0777 )
                    
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



# -*- coding: utf-8 -*-
from ConfigManager import ConfManager
from Connector import *
from PLTEManager import PLTEManager
from provMsg import provMsg
import sysv_ipc, time, signal
import ctypes

class PLTEConnector(Connector):
    
    __instance = None
    
    queueId = int(ConfManager.getInstance().getConfigData( ConfManager.MSGQUEUE_INFO , "PLTEIB" ))    
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
        
        #self.queue = sysv_ipc.MessageQueue(self.queueId , sysv_ipc.IPC_CREX, mode=0666 )
        try :
                self.queue = sysv_ipc.MessageQueue(self.queueId)
        except Exception as e:
                self.logger.error("msgQueue Connection Failed.. QUEUE_ID[%d]" % self.queueId)

    def readMessage(self):
        self.logger.debug('Read Message')

        try:
                receiveMsg =  provMsg()
                message = self.queue.receive(ctypes.sizeof(receiveMsg))

                mydata = ctypes.create_string_buffer( message[0] )
                
                ctypes.memmove(ctypes.pointer(receiveMsg), mydata ,ctypes.sizeof(receiveMsg))

                print (receiveMsg.id , receiveMsg.ce, receiveMsg.syms )
                time.sleep(1)

                self.logger.info("===============================================");
                self.logger.info("PLTEIB -> RESTIF")
                self.logger.info("===============================================");
                self.logger.info("ID : %d" %receiveMsg.id )
                self.logger.info("CE : %s" %receiveMsg.ce )
                self.logger.info("SYMS : %d" %receiveMsg.syms )
        
        except Exception as e :
                self.logger.error("Msgrcv Failed.. : %s" % e)
        

    def sendMessage(self, command, jobNo):
        
        self.logger.debug('Send Message')

        pMsg =  provMsg()
        pMsg.id = 555
        pMsg.ce = "Hello"
        pMsg.syms = 3

        pData = ctypes.cast(ctypes.byref(pMsg), ctypes.POINTER(ctypes.c_char * ctypes.sizeof(pMsg)))

        try:
            if self.queue is not None :
                    #self.queue.send( s.decode(), True)
                    self.queue.send( pData.contents.raw, True)

        except Exception as e:

            self.logger.info("===============================================");
            self.logger.info("[EXT_API] -> RESTIF")
            self.logger.info("===============================================");

                
            self.logger.info("===============================================");
            self.logger.info("COMMAND : " + command)
            self.logger.info("JOBNO   : " + jobNo)
            self.logger.info("===============================================");
        


    
# if __name__ == '__main__':
#       
#     if PLTEConnector.logger is None :
#         print 'None..'
#           
#     # PLTEConnector.logger = LogManager.getInstance()
#       
#     conn = PLTEConnector()    
#     conn.sendMessage()

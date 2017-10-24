# -*- coding: utf-8 -*-
from ConfigManager import ConfManager
from Connector import *
from PLTEManager import PLTEManager
import sysv_ipc

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
                self.queue = sysv_ipc.MessageQueue(self.queueId )
        except Exception as e:
                self.logger.error("msgQueue Connection Failed.. QUEUE_ID[%d]" % self.queueId)

    def readMessage(self):
        self.logger.debug('Read Message')

        try:
                s = "Hi Python To C"
                if self.queue is not None :
                        self.queue.send( s.decode(), True)

                print 'test'
                self.logger.info("===============================================");
                self.logger.info("[EXT_API] -> RESTIF")
#                self.logger.info("COMMAND : " + command)
#                self.logger.info("JOBNO   : " + jobNo)
                self.logger.info("===============================================");
        
        except sysv_ipc.ExistentialError:
                print "ERROR: message queue creation failed"
               
        print (self.queueId)

        
        
    def sendMessage(self, command, jobNo):
        self.logger.debug('Send Message')
                
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

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
        self.queue = sysv_ipc.MessageQueue(self.queueId )
                    
    def readMessage(self):
        self.logger.debug('Read Message')

        try:
                s = "Hi Python To C"
                self.queue.send( s.decode(), True)
        
                print 'Message Send Success'
        
        except sysv_ipc.ExistentialError:
                print "ERROR: message queue creation failed"
        
               
        print (self.queueId)

        
        
    def sendMessage(self, command, jobNo):
        self.logger.debug('Send Message')
                
        self.logger.info("===============================================");
        self.logger.info("COMMAND : " + command);
        self.logger.info("JOBNO   : " + jobNo);
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

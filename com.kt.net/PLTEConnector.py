# -*- coding: utf-8 -*-
from Connector import *
from PLTEManager import PLTEManager
from logManager import logManager


class PLTEConnector(Connector):
    
    __instance = None
    logger = logManager.getInstance().get_logger()

    @staticmethod
    def getInstance():
        """ Static access method. """
        if PLTEConnector.__instance == None:
            PLTEConnector.__instance = PLTEConnector()
        return PLTEConnector.__instance 

    def __init__(self):
        self.logger.debug('PLTEConnector Init')
        Connector.__init__(self, PLTEManager.getInstance())
        
        return 
        
    def sendMessage(self):
        self.logger.debug('Send Message')

    
# if __name__ == '__main__':
#       
#     if PLTEConnector.logger is None :
#         print 'None..'
#           
#     # PLTEConnector.logger = logManager.getInstance()
#       
#     conn = PLTEConnector()    
#     conn.sendMessage()

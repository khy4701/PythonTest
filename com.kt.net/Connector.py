# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import threading

from LogManager import LogManager


class Connector(threading.Thread):
    __metaclass__ = ABCMeta
    logger = LogManager.getInstance().get_logger()

    def __init__(self, receiver):
        super(Connector,self).__init__()
        self.logger.debug("Connector Init")
        self.receiver = receiver
        
        self.reader = self
        self.reader.start()
        
        return 
        
    @abstractmethod    
    def sendMessage(self):
        pass
    
    @abstractmethod    
    def readMessage(self):
        pass
        
    def run(self):      
        '''  
        while self.reader == self:
            try:                                
                self.readMessage()
            except Exception as e:
                self.logger.error(e)
        '''
        self.readMessage()
                           

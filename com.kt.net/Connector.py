# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import threading

from logManager import logManager


class Connector(threading.Thread):
    __metaclass__ = ABCMeta
    logger = logManager.getInstance().get_logger()

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
        
    def run(self):
        if ( self.reader == self ):
            self.logger.debug("Threading Start")
            
    
        
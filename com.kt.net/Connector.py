# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import sys, signal
import threading

from LogManager import LogManager


class Connector(threading.Thread):
    __metaclass__ = ABCMeta
    logger = LogManager.getInstance().get_logger()

#    def signal_handler(signal, frame):
#        self.logger.info('You pressed Ctrl+C!')
#        sys.exit(0)

    def __init__(self, receiver):
        super(Connector,self).__init__()
        self.logger.debug("Connector Init")
        self.receiver = receiver
        
#       signal.signal(signal.SIGINT, self.signal_handler)

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

        try:                                
            while self.reader == self:
                self.readMessage()
        except Exception as e:
            self.logger.error(e)
#       self.readMessage()
                           
                            

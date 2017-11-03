# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import sys, signal
import threading
import time

from ConfigManager import ConfManager
from LogManager import LogManager
import sysv_ipc


class Connector():
#class Connector(threading.Thread):
    __metaclass__ = ABCMeta
    logger = LogManager.getInstance().get_logger()

    myQueue = None 
#    def signal_handler(signal, frame):
#        self.logger.info('You pressed Ctrl+C!')
#        sys.exit(0)

    def __init__(self, manager):
        super(Connector,self).__init__()
        self.logger.debug("Connector Init")
        self.manager = manager
        
#       signal.signal(signal.SIGINT, self.signal_handler)

        return 
        
    @abstractmethod    
    def sendMessage(self):
        pass
    

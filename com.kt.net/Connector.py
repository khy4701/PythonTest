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
#        try :
#                #IPC_CREAT : create or return key if it is allocated.
#                #IPC_CREX  : IPC_CREAT | IPC_EXCL 
#                #IPC_EXCL  : return -1 if there is already allocated.
#                self.myQueue = sysv_ipc.MessageQueue(self.myQueId, sysv_ipc.IPC_CREAT, mode=0666 )
#        except Exception as e:
#                self.logger.error("msgQueue Connection Failed.. RESTIF QUEUE_ID[%d]" % self.myQueId)

#         self.reader = self
#         self.reader.start()
        
        return 
        
    @abstractmethod    
    def sendMessage(self):
        pass
    
#    @abstractmethod    
#    def readMessage(self):
#        pass
        
#     def run(self):      
# 
#         try:                                
#             while self.reader == self:
#                 usleep(100)
#                 #self.readMessage()
#                 
#         except Exception as e:
#             self.logger.error(e)
# #       self.readMessage()
                           
                            

from Receiver import Receiver
from logManager import logManager


class PLTEManager(Receiver):
    
    __instance = None
    logger = logManager.getInstance().get_logger()

    
    @staticmethod
    def getInstance():
        """ Static access method. """
        if PLTEManager.__instance == None:
            PLTEManager.__instance = PLTEManager()
        return PLTEManager.__instance 

    
    def __init__(self):
        self.logger.debug('PLTE Manager Init')

        pass
    
    def receiveMessage(self):
        
        print 'Receive Message'
        pass
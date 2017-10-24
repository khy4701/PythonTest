

from LogManager import LogManager
from Manager import Manager


class PLTEManager(Manager):
    
    __instance = None
    logger = LogManager.getInstance().get_logger()


    @staticmethod
    def getInstance():
        """ Static access method. """
        if PLTEManager.__instance == None:
            PLTEManager.__instance = PLTEManager()
        return PLTEManager.__instance 

    
    def __init__(self):
        self.logger.debug('PLTE Manager Init')

        pass
    
    def msgProcessing(self):        
        self.logger.debug('Message Processing')
        pass
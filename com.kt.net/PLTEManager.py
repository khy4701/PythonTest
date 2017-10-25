

from LogManager import LogManager
from Manager import Manager
from PLTEConnector import PLTEConnector
from SenderInfo import SenderInfo


class PLTEManager(Manager):
    
    __instance = None
    logger = LogManager.getInstance().get_logger()
    
    # SenderInfo Class Object List
    plteMembers = []

    @staticmethod
    def getInstance():
        """ Static access method. """
        if PLTEManager.__instance == None:
            PLTEManager.__instance = PLTEManager()
        return PLTEManager.__instance 

    
    def __init__(self):
        self.logger.debug('PLTE Manager Init')
        
        self.clientReqId = 0
        pass
    
    def receiveHandling(self, rspCode, reqId, rcvMsg):        
        self.logger.debug('receive Handling')
        
        for member in PLTEManager.plteMembers:
            
            if member.getClientReqId() == reqId:
                # Service Manager
                source = member.getSource()
                
                # Service setComplete 
                source.setComplete(rspCode, reqId, rcvMsg)
                PLTEManager.plteMembers.remove(member)
                    
    
    def getClientReqId(self):
        self.clientReqId += 1
        
        if self.clientReqId > 2000000000:
            self.clientReqId = 0
        
        return self.clientReqId
    
    @staticmethod
    def sendCommand(command, source, reqId, msg):
        
        senderInfo = SenderInfo(source, reqId)
        
        # Transcation List Add
        PLTEManager.plteMembers.append(senderInfo)
                
        if PLTEConnector.getInstance().sendMessage(command, reqId, msg):
            # Transcation List Remove
            PLTEManager.plteMembers.remove(senderInfo)
        
        
from abc import abstractmethod


class Manager:
     
    def __init_(self):
        pass
     
    @abstractmethod
    def receiveHandling(self, rspCode, reqId, msg):
        pass
    
    @abstractmethod
    def sendCommand(self, command, source, reqId, msg):
        pass

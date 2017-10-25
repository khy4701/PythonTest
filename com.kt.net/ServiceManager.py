from abc import abstractmethod


class ServiceManager:
    
    @abstractmethod    
    def setComplete(self, rspCode, reqId, rcvMsg):
        pass
    
    @abstractmethod    
    def setResMessage(self, data):
        pass
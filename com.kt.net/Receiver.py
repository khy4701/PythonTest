import threading
from abc import abstractmethod


class Receiver(threading.Thread):
        
    def __init__(self):
        super(Receiver,self).__init__()
    
    @abstractmethod
    def readMessage(self):
        pass
    
    @abstractmethod
    def run(self):
        pass
    
    
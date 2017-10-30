
class SenderInfo:
    
    # source ==> ServiceManager  
    
    def __init__(self, source, cliReqId ):
        self.source   = source
        self.cliReqId = cliReqId
        
    def getCliReqId(self):
        return self.cliReqId
    
    def getSource(self):
        return self.source


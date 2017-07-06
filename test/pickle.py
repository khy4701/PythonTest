import _pickle as cPickle

class Message():
    
    sendUser = ""
    destUser = ""    
    msgData  = ""
    
    def __init__(self, dest, msgData):
        self.destUser = dest
        self.msgData = msgData
        
    def setMessageData(self, text):
        self.msgData = text
        
    def getMessageData(self):
        return self.msgData
    
    def converByteToString(self, byteData):
        return byteData.decode("utf-8")
        
    def converStringToByte(self, strData):        
        return strData.encode(encoding='utf_8', errors='strict')   
    
    def isGetMessage(self):
        if self.msgData:
            return "true"            
                     
    def getUserInfo(self):
        userInfo = (self.sendUser, self.destUser)
        return userInfo




msg = Message("khy4701","1234")
data_string = cPickle.dump(msg.getMessageData(), )

print ('pickle :', data_string)

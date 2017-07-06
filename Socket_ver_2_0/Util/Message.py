from enum import Enum

class MSGTYPE(Enum):
    CONNECTION  = 0
    STRING_MSG  = 1
    DISCONNECT  = 2
    
    ROOM_CREATE    = 100
    ROOM_ENTER     = 101
    ROOM_EXIT      = 102
    SHOW_ROOM_LIST = 103    
    SHOW_MEMBER_LIST = 300
    SHOW_WAITING_LIST = 400
    
    

class msgClass():
    
    sendUser = ""
    destUser = ""    
    msgData  = ""
    msgType  = 0      # 0 : Connection , 1: Message , 2: DisConnection, 3:UserList
    userList = [] 
    roomList = []
    memberList = []
    waitingList = []
    
    def __init__(self, send, msgData ,msgType):
        self.sendUser = send
        self.msgData = msgData
        self.msgType = msgType
                
    def setMessageData(self, text, type):
        # configure[0], Message[1]
        self.msgType = type  
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
    
    def getsendUser(self):
        return self.sendUser

    def getMessageType(self):
        return self.msgType
    
    def setUserList(self, userList):
        self.userList = userList
                
    def getUserList(self):
        return self.userList
        
    def setRoomList(self, roomList):
        self.roomList = roomList
        
    def getRoomList(self):
        return self.roomList
    
    def setMemberList(self, memberList):
        self.memberList = memberList
        
    def getMemberList(self):
        return self.memberList
    
    def setWaitingMemberList(self, waitingList):
        self.waitingList = waitingList
        
    def getWaitingMemberList(self):
        return self.waitingList
        
        
        
class room():
    
    ROBY = "ROBY"
    
   
    def __init__(self, roomIdx, roomName, superUser, limitNum):        
        self.roomNum = roomIdx
        self.roomName = roomName
        self.roomSuperUser = superUser
        self.limitNum = limitNum
        self.userList = []
        self.userList.append(superUser)
        self.totalNum = 1
        
    def getRoomName(self):
        return self.roomName
    
    def changeSuperUser(self, superUser):
        self.roomSuperUser = superUser
        
    def getTotalNum(self):
        return self.totalNum
    
    def getUserList(self):
        return self.userList
    
    def addUserList(self, user):
        return self.userList.append(user)
    
    def delUser(self, user):
        self.userList.remove(user)
        
    def increaseTotalNum(self):
        self.totalNum += 1
        
    def decreaseTotalNum(self):
        self.totalNum -= 1
        
        
        
    
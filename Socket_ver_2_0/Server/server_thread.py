import sys
import threading
from time import ctime

from Util.Message import *
import _pickle as cPickle

BUFSIZE = 1024

class servThread(threading.Thread):
    
    userNum = 0
    isConnected = 0
    message = ''
    
    def __init__(self, socket, ADDR, connManager):
        super(servThread, self).__init__()
        self.socket = socket
        self.ip = ADDR[0]
        self.port = ADDR[1]
        self.userId = 'Default'
        self.connManager = connManager
        self.status = 'ALIVE'
        self.enterRoomNum = "ROBY"
        
        servThread.userNum += 1

    def run(self):
        try:
            print('Server Thread[%s] is started.' % self.ip)
            sys.stdout.flush()

            while True:
                self.readfile = self.socket.makefile('rb', 1024)
                self.readPicker = cPickle.Unpickler(self.readfile)
                
                msg = self.readPicker.load()
                self.readfile.close()
                                 
                strData = msg.getMessageData()
                msgType = msg.getMessageType()
                
                if msgType == MSGTYPE.CONNECTION:
                    print ('[RECEVIED] MSGTYPE[%s]' % MSGTYPE.CONNECTION)
                    self.userId = strData
                    print ('User[%s] Information Received..' % self.userId)
                    continue
                
                elif msgType == MSGTYPE.DISCONNECT: 
                    print ('[RECEVIED] MSGTYPE[%s]' % MSGTYPE.DISCONNECT)
                    self.status = 'DEAD'           
                    
                elif msgType == MSGTYPE.STRING_MSG:  
                    print ('MSG RECEVIED MSGTYPE[%s]' % MSGTYPE.STRING_MSG)
                    self.message = strData
                    print ('[%s] :  [%s] ' %( self.userId,strData))
                    sys.stdout.flush()
                                                
                elif msgType == MSGTYPE.ROOM_CREATE:
                    print ('[RECEVIED] MSGTYPE[%s]' % MSGTYPE.ROOM_CREATE)
                    self.connManager.addRoomList(strData)
                    self.connManager.sendRoomList()
                     
                elif msgType == MSGTYPE.ROOM_ENTER:
                    print ('[RECEVIED] MSGTYPE[%s]' % MSGTYPE.ROOM_ENTER)

                    enterMsg = strData.split("#")
                    roomName = enterMsg[0]
                    userId   = enterMsg[1]
                    self.connManager.roomEntered(userId, roomName )
                    
                elif msgType == MSGTYPE.ROOM_EXIT:
                    print ('[RECEVIED] MSGTYPE[%s]' % MSGTYPE.ROOM_EXIT)
                    
                    self.connManager.roomExit(strData)
                    
                elif msgType == MSGTYPE.SHOW_ROOM_LIST:
                    print ('[RECEVIED] MSGTYPE[%s]' % MSGTYPE.SHOW_ROOM_LIST)
                    self.connManager.sendRoomList()    
                    
                elif msgType == MSGTYPE.SHOW_MEMBER_LIST:
                    print ('[RECEVIED] MSGTYPE[%s]' % MSGTYPE.SHOW_MEMBER_LIST)
                    # Show Room Member
                    roomName = strData
                    self.connManager.sendMemberList(roomName, msg.getsendUser())
                                                   
                else:
                    print ('[RECEVIED] Unknown Message')

                if strData == 'exit':
                    break

        except Exception as e:
            self.sockClose()
            print (e)

    def printSoc(self):
        print('[INFO][%s] New Connection - %s' % (ctime(), self.userId))
        
    def sendToClient(self, strMsg , msgType):
     
        if isinstance(strMsg, str):
            msg = msgClass("Server", strMsg, MSGTYPE.STRING_MSG)
            print ('Send to client : %s' %strMsg)

        elif isinstance(strMsg, list):
            msg = msgClass("Server", '', msgType)
            
       #     if msgType == MSGTYPE.SHOW_MEMBER_LIST:
       #         msg.setUserList(strMsg)
                
            if msgType == msgType.SHOW_ROOM_LIST:
                msg.setRoomList(strMsg)
                
            if msgType == msgType.SHOW_MEMBER_LIST:
                msg.setMemberList(strMsg)
                
            if msgType == msgType.SHOW_WAITING_LIST:
                msg.setWaitingMemberList(strMsg)
                
        try:               
            self.writefile = self.socket.makefile('wb', 1024 )
            self.writePicker = cPickle.Pickler(self.writefile)         
            self.writePicker.dump(msg)         
            self.writefile.close()
 
            print ('Send Message To Client Success')
        except Exception as e:
            self.sockClose()
            print (e)
            
    def getUserId(self):
        return self.userId
    
    def getMessage(self):
        return self.message
    
    def setMessage(self):
        self.message = ''
    
    def sockClose(self):
        
        if self.isConnected == 1:
           
            self.socket.close()
            print ('[Disconnected] %s' % self.userId)
            
    def stopThread(self):
        self.run = False
        
    def getStatus(self):
        return self.status
        
    def setEnteredRoom(self, roomNum):
        self.enterRoomNum = roomNum
        
    def getEnteredRoom(self):
        return self.enterRoomNum
        
import sys
from _overlapped import NULL

sys.path.append("D:/Users/Ariel/workspace/Socket_ver_2_0")

import threading
import _pickle as cPickle
from Util.Message import *

BUFSIZE = 1024

class cliThread(threading.Thread):

    def __init__(self, cliSock, MainThread):
        self.clientSock = cliSock
        self.mainGui     = MainThread
        super(cliThread, self).__init__()
    def run(self):       
                               
        while True:
            sys.stdout.flush()
            try:                
                self.file = self.clientSock.makefile('rb', 1024)
                self.recvPicker = cPickle.Unpickler(self.file)
                msg = self.recvPicker.load()                
                self.file.close()

            except Exception as e:
                #print(e)
                sys.exit()   
           
            recvMsgType = msg.getMessageType().name
                                                         
            if msg.getMessageType() == MSGTYPE.SHOW_ROOM_LIST:
                print ('[RECEVIED] MSGTYPE[%s]' % recvMsgType )
                self.mainGui.updateRoomList( msg.getRoomList() )
                continue
            
            if msg.getMessageType() == MSGTYPE.SHOW_MEMBER_LIST:
                print ('[RECEVIED] MSGTYPE[%s]' % recvMsgType )
                
                roomGui = self.mainGui.getRoomGUI()
                if not roomGui:
                    self.mainGui.updateMemberList( msg.getMemberList() )
                    continue
                
                roomGui.updateList(msg.getmemberList())
                
                continue
            
            if msg.getMessageType() == MSGTYPE.SHOW_WAITING_LIST:
                print ('[RECEVIED] MSGTYPE[%s]' % recvMsgType )
                self.mainGui.updateWaitingMemberList(msg.getWaitingMemberList())

            if msg.isGetMessage() != "true":
                continue
            
            strMsg = msg.getMessageData()

            roomGUI = self.mainGui.getRoomGUI()
            if not roomGUI:
                print ('Room GUI Not Exist')
                continue
            
            roomGUI.printBoard(strMsg) 
            print(strMsg)
            
    def stop(self):       
        self.run = False

import sys

sys.path.append("D:/Users/Ariel/workspace/Socket_ver_2_0")

import threading
import time
import _pickle as cPickle
from select import *
from socket import *
from Util.Message import *
from Client.client_thread import *


class Socket():
    
    def __init__(self, host, port , userInfo):
    
        try:
            # 02. Try Connection
            self.userId = userInfo[0]
            self.host = host
            self.port = port
            self.ADDR = (self.host, self.port)
            
            self.clientSocket = socket(AF_INET, SOCK_STREAM)
            self.clientSocket.connect(self.ADDR)
        
        except Exception as e:
            print("Can't Connect to server(%s:%s)" % self.ADDR)
            
            sys.exit()
            
        print("Connect Success to Server(%s:%s)" % self.ADDR)

            
    def startThread(self, MainThread):
        self.client = cliThread(self.clientSocket, MainThread)
        
        self.sendToServer(self.userId, MSGTYPE.CONNECTION)        
        self.client.start()
        
    def sockClose(self):
        try:            
            self.sendToServer('', MSGTYPE.DISCONNECT)
            self.clientSocket.close()
            print ('Socket Closed..')
        except Exception as e:
            print (e)
                    
    def sendToServer(self, text, msgType):
                
        try:
            # Object Send -- using cPickle, Makefile 
            msg = msgClass(self.userId, text, msgType)        
            self.file = self.clientSocket.makefile('wb', 1024 )
            cPickle.dump(msg,self.file)
            
            self.file.close()      
                    
        except Exception as e:
            print(e)
            self.clientSocket.close()
            sys.exit()
            
    def stopThread(self):
        self.client.stop()
        print ('Thread Stopped..')
        
    def getUserId(self):
        return self.userId
    


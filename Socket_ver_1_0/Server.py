from select import *
from socket import *
import sys
import threading
from time import ctime
import time


# import server_thread
HOST = 'localhost'
PORT = 1234
ADDR = (HOST, PORT)
BUFSIZE = 1024
connectList = []

class servThread(threading.Thread):

    isConnected = 0
    message = ''
    def __init__(self, socket, ADDR, userId):
        super(servThread, self).__init__()
        self.socket = socket
        self.ip = ADDR[0]
        self.port = ADDR[1]
        self.userId = userId

    def run(self):
        try:
            print('Server Thread[%s] is started.' % self.ip)
            sys.stdout.flush()

            while True:
                byteData = self.socket.recv(BUFSIZE)                
                strData = byteData.decode("utf-8")
                
                self.message = strData
                print ('Received Data[%s] ' % strData)
                sys.stdout.flush()

                if strData == 'exit':
                    break

        except Exception as e:
            self.sockClose()
            print (e)

    def printSoc(self):
        print('[INFO][%s] New Connection - %s' % (ctime(), self.userId))
        
    def sendToClient(self, strMsg):
        byteData = strMsg.encode(encoding='utf_8', errors='strict')
        try:
            self.socket.send(byteData)
            
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
        

class connManager(threading.Thread):

    def __init__(self):
        super(connManager, self).__init__()

    def run(self):
        
        self.isConnected = 1
        while True:
            time.sleep(0.1)

            if not connectList:
                continue

            try:
                for conSock in connectList:
                    
                    userId = conSock.getUserId()
                    getMsg = conSock.getMessage()
                    
                    if getMsg:
                        for otherSock in connectList:
                            if userId == otherSock.getUserId():
                                continue
                            
                            strMsg = userId + "> " + getMsg
                            otherSock.sendToClient(strMsg)
                            conSock.setMessage()
                        

            except Exception as e:
                print (e)
                print ("Can't send to Client")

    def sendAllMessage(self, message):
        for conSock in connectList:
            conSock.sendToClient(message)
        

if __name__ == '__main__':
    serverSocket = []

    # 01. Create Socket Object
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # 02. Socket Binding
    serverSocket.bind(ADDR)

    print ('===================================================')
    print (' Starting Chatting Server .. Wait Port[%s] Conection ' % str(PORT))
    print ('===================================================')

    # 03. Listening
    serverSocket.listen(10)

    print ('Waiting..')
    sys.stdout.flush()
    
# 04. Send Thread Start
serv = connManager()
serv.start()

userNum = 0
while True:

    try:
        # 04. Accept Client
        clientSocket, addr_info = serverSocket.accept()

        userNum += 1
        userId = "Client" + str(userNum)
        newClient = servThread(clientSocket, addr_info, userId)

        newClient.printSoc()

        newClient.start()

        serv.sendAllMessage(newClient.getUserId() + " is Connected..")
        # 05. Add Connection List
        connectList.append(newClient)
        print ('Add connect List')
        sys.stdout.flush()

    except KeyboardInterrupt:
        serverSocket.close()
        sys.stdout.flush()

        sys.exit()

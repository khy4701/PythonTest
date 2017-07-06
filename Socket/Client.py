from select import *
from socket import *
import sys
import threading
import time


HOST = 'localhost'
PORT = 1234
BUFSIZE = 1024
ADDR = (HOST, PORT)  

clientSocket = []

class clientMain(threading.Thread):

    def __init__(self, cliSock):
        self.clientSock = cliSock
        super(clientMain, self).__init__()
        
    
    def run(self):       
                               
        while True:
            sys.stdout.flush()
            byteData = self.clientSock.recv(BUFSIZE)

            strMsg = byteData.decode("utf-8")

            if not strMsg:
                continue

            print (strMsg)
        
         
if __name__ == '__main__':
    
    try:
        # 02. Try Connection

        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect(ADDR)

    except Exception as e:
        print("Can't Connect to server(%s:%s)" % ADDR)
        sys.exit()
    
    print("Connect Success to Server(%s:%s)" % ADDR)

    client = clientMain(clientSocket)
    client.start()

    while True:

        try:
            data = input()
            print("<Me> " + data)
            sys.stdout.flush()
            
            byteData = data.encode(encoding='utf_8', errors='strict')
            clientSocket.send(byteData)

        except KeyboardInterrupt:
            clientSocket.close()
            print ('Socket Closed')
            sys.stdout.flush()
            sys.exit()
            

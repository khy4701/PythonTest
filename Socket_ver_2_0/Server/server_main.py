from select import *
from socket import *
import sys
import threading
import time

sys.path.append("D:/Users/Ariel/workspace/Socket_ver_2_0")

from Server.connManager import *
from Server.server_thread import *


# import server_thread
HOST = 'localhost'
PORT = 1234
ADDR = (HOST, PORT)

if __name__ == '__main__':
    serverSocket = []
    connectList = []
    roomList = []

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
    serv = connectManager(connectList, roomList)
    serv.start()

    while True:
        try:
            # 04. Accept Client
            clientSocket, addr_info = serverSocket.accept()
    
            newClient = servThread(clientSocket, addr_info, serv)
    
            newClient.printSoc()
            newClient.start()
    
            time.sleep(1)
            #serv.sendBroadCasting("[Connection]:"+newClient.getUserId(), 1)  
             
            # 05. Add Connection List
            connectList.append(newClient)
            
            print ('Add connect List')
            sys.stdout.flush()
    
        except KeyboardInterrupt:
            serverSocket.close()
            sys.stdout.flush()
    
            sys.exit()
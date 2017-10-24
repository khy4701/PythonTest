# -*- coding: utf-8 -*-
import ctypes

from ConfigManager import ConfManager
from Connector import *
from PLTEManager import PLTEManager
from provMsg import provMsg, HttpReq, HttpHeader
import sysv_ipc, time, signal


class PLTEConnector(Connector):
    
    __instance = None
    
    queueId = int(ConfManager.getInstance().getConfigData( ConfManager.MSGQUEUE_INFO , "PLTEIB" ))    
    logger = LogManager.getInstance().get_logger()

    @staticmethod
    def getInstance():
        """ Static access method. """
        if PLTEConnector.__instance == None:
            PLTEConnector.__instance = PLTEConnector()
        return PLTEConnector.__instance 

    def __init__(self):
        self.logger.debug('PLTEConnector Init')
        Connector.__init__(self, PLTEManager.getInstance())
        
        #self.queue = sysv_ipc.MessageQueue(self.queueId , sysv_ipc.IPC_CREX, mode=0666 )
        try :
                self.queue = sysv_ipc.MessageQueue(self.queueId)
        except Exception as e:
                self.logger.error("msgQueue Connection Failed.. QUEUE_ID[%d]" % self.queueId)

    def readMessage(self):
        self.logger.debug('Read Message')

        try:
                receiveMsg =  provMsg()
                message = self.queue.receive(ctypes.sizeof(receiveMsg))

                mydata = ctypes.create_string_buffer( message[0] )
                
                ctypes.memmove(ctypes.pointer(receiveMsg), mydata ,ctypes.sizeof(receiveMsg))

                print (receiveMsg.id , receiveMsg.ce, receiveMsg.syms )
                time.sleep(1)

                self.logger.info("===============================================");
                self.logger.info("PLTEIB -> RESTIF")
                self.logger.info("===============================================");
                self.logger.info("ID : %d" %receiveMsg.id )
                self.logger.info("CE : %s" %receiveMsg.ce )
                self.logger.info("SYMS : %d" %receiveMsg.syms )
        
        except Exception as e :
                self.logger.error("Msgrcv Failed.. : %s" % e)
        

    def sendMessage(self, command, jobNo):
        
        self.logger.debug('Send Message')

#         pMsg =  provMsg()
#         pMsg.id = jobNo
#         pMsg.ce = command
#         pMsg.syms = 3
# 
#         pData = ctypes.cast(ctypes.byref(pMsg), ctypes.POINTER(ctypes.c_char * ctypes.sizeof(pMsg)))
# 
#         try:
#             if self.queue is not None :
#                     #self.queue.send( s.decode(), True)
#                     self.queue.send( pData.contents.raw, True)

# class HttpHeader(Structure):
#     _fields = [("method", c_int),
#                ("api_type", c_int),
#                ("op_type", c_int),
#                ("length", c_int),
#                ("encoding", c_char ) ]
# 
# 
# class HttpReq(Structure):
#     _fields = [("tot_len", c_int),
#                ("msgId", c_int),
#                ("ehttpf_idx", c_short),
#                ("srcQid", c_int),
#                ("srcSysId", c_char ),
#                ("http_hdr", HttpHeader),
#                ("jsonBody", c_char * HTTPF_MSG_BUFSIZE ) ]


        httpMsg =  HttpReq()
        header = HttpHeader()
        
        header.method = 1
        header.api_type = 2
        header.op_type = 3
        header.length = 4
        header.encoding = '5'        
                
        httpMsg.tot_len = 100
        httpMsg.msgId = 200
        httpMsg.ehttpf_idx = 1
        httpMsg.srcQid = 300
        httpMsg.srcSysId = '1'
        httpMsg.http_hdr = header
        httpMsg.jsonBody = "Testing to.."
        
        pData = ctypes.cast(ctypes.byref(httpMsg), ctypes.POINTER(ctypes.c_char * ctypes.sizeof(httpMsg)))

        try:
            if self.queue is not None :
                    #self.queue.send( s.decode(), True)
                    self.queue.send( pData.contents.raw, True)

        except Exception as e:
            self.logger.error("sendMessage Error! %s" % e)

        self.logger.info("===============================================");
        self.logger.info("[EXT_API] -> RESTIF")
        self.logger.info("===============================================");
        self.logger.info("COMMAND : %s" % command)
        self.logger.info("JOBNO   : %d" % jobNo)
        self.logger.info("===============================================");
        


    
# if __name__ == '__main__':
#       
#     if PLTEConnector.logger is None :
#         print 'None..'
#           
#     # PLTEConnector.logger = LogManager.getInstance()
#       
#     conn = PLTEConnector()    
#     conn.sendMessage()

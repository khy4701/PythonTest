# -*- coding: utf-8 -*-
import ctypes
import sys

from ConfigManager import ConfManager
from Connector import *
from PLTEManager import PLTEManager
from provMsg import provMsg, HttpReq,HttpRes, HttpHeader
import sysv_ipc, time, signal


class PLTEConnector(Connector):
    
    __instance = None
    
    myQueId = int(ConfManager.getInstance().getConfigData( ConfManager.MSGQUEUE_INFO , "RESTIF" ))    
    plteQueId = int(ConfManager.getInstance().getConfigData( ConfManager.MSGQUEUE_INFO , "PLTEIB" ))    
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
        
        #self.myQueue = sysv_ipc.MessageQueue(self.plteQueId , sysv_ipc.IPC_CREX, mode=0666 )
        try :
                #IPC_CREAT : create or return key if it is allocated.
                #IPC_CREX  : IPC_CREAT | IPC_EXCL 
                #IPC_EXCL  : return -1 if there is already allocated.
                self.myQueue = sysv_ipc.MessageQueue(self.myQueId, sysv_ipc.IPC_CREAT, mode=0666 )
        except Exception as e:
                self.logger.error("msgQueue Connection Failed.. RESTIF QUEUE_ID[%d]" % self.myQueId)

        try :
                self.plteQueue = sysv_ipc.MessageQueue(self.plteQueId)
        except Exception as e:
                self.logger.error("msgQueue Connection Failed.. PLTE QUEUE_ID[%d]" % self.plteQueId)

    def readMessage(self):
        self.logger.debug('Read Message')

        try:
                resMsg = HttpRes()

                if self.myQueue is None:
                    try :
                            self.myQueue = sysv_ipc.MessageQueue(self.myQueId, sysv_ipc.IPC_CREAT, mode=0777 )
                    except Exception as e:
                            self.logger.error("msgQueue Connection Failed.. RESTIF QUEUE_ID[%d]" % self.myQueId)

                
                self.logger.info("read Start..");
                (message, msgType) = self.myQueue.receive(ctypes.sizeof(resMsg))

                mydata = ctypes.create_string_buffer( message )
                
                ctypes.memmove(ctypes.pointer(resMsg), mydata ,ctypes.sizeof(resMsg))

                time.sleep(1)

                headerMsg = resMsg.http_hdr

                self.logger.info("===============================================");
                self.logger.info("PLTEIB -> RESTIF")
                self.logger.info("===============================================");
                self.logger.info("msgType: %d" %msgType )
                self.logger.info("tot_len : %s" %resMsg.tot_len )
                self.logger.info("msgId : %d" %resMsg.msgId )
                self.logger.info("ehttp_idx : %d" %resMsg.ehttpf_idx )
                self.logger.info("srcQid : %d" %resMsg.srcQid )
                self.logger.info("srcSysId : %c" %resMsg.srcSysId )
                self.logger.info("nResult : %d" %resMsg.nResult )
                self.logger.info("jsonBody: %s" %resMsg.jsonBody )
                self.logger.info("===============================================");
                self.logger.info("method: %d" %headerMsg.method )
                self.logger.info("api_type: %d" %headerMsg.api_type )
                self.logger.info("op_type: %d" %headerMsg.op_type )
                self.logger.info("length: %d" %headerMsg.length )
                self.logger.info("encoding: %c" %headerMsg.encoding )
        
        except Exception as e :
                self.logger.error("Msgrcv Failed..  %s" %e)
                time.sleep(1)
        

    def sendMessage(self, command, jobNo):
        
        self.logger.debug('Send Message')

        p = provMsg()
        p.id = 1
        p.ce = '11'
        p.syms = 3


        httpMsg =  HttpReq()
        header = HttpHeader()
        
        header.method = 1
        header.api_type = 2
        header.op_type = 3
        header.length = 4
        header.encoding = '5'        
                
        #httpMsg.mtype = 2
        httpMsg.tot_len = 100
        httpMsg.msgId = 200
        httpMsg.ehttpf_idx = 71
        httpMsg.srcQid = 300
        httpMsg.srcSysId = '1'
        httpMsg.http_hdr = header
        httpMsg.jsonBody = "Testing to.."

        pData = ctypes.cast(ctypes.byref(httpMsg), ctypes.POINTER(ctypes.c_char * ctypes.sizeof(httpMsg)))

        try:
            if self.plteQueue is not None :
                    self.plteQueue.send( pData.contents.raw, True, HttpReq.MTYPE_RESTIF_TO_APP_REQ )

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

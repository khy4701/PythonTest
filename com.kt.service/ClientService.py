from ctypes.test.test_errno import threading
import json

import requests

from ConfigManager import ConfManager
from LogManager import LogManager
from PLTEManager import PLTEManager
from ProvMsg import HttpRes


class ClientService(threading.thread):
    
    __instance = None
    
    logger = LogManager.getInstance().get_logger()
    
    def __init__(self, httpMsg):
        super(ClientService, self).__init__()
        self.reqMsg = httpMsg
    
    
    def run(self):
        
        # payload = httpMsg.body....
        payload = {'name':'Hoyoung', 'age': 123 }
        url='http://localhost:5000/departments/abc/123'
        head = {'Content-type':'application/json', 'Accept':'application/json'}
        
        # 1. [RESTIF->EXT] INPUT REQUSET MESSAGE ( httpReq -> REST API )
        #payload = self.reqMsg.body
        
        # 2. [RESTIF->EXT] CLIENT SEND LOGGING        
        if ConfManager.getInstance().getLogFlag():
            self.logger.info("===============================================");
            self.logger.info("RESTIF -> [EXT]")
            self.logger.info("===============================================");
            self.logger.info("URL : " + url)
            self.logger.info("TID : " + "tid") # TID
            self.logger.info("HEADER : " + head)
            self.logger.info("BODY : "  + str(payload))
            self.logger.info("===============================================");
            
            
        # 3. [RESTIF->EXT] SEND DATA
        try:
            payld = json.dumps(payload)
            restAPI = requests.post(url,headers=head,data=payld)
        except Exception as e:
            self.logger.info(e);
           
        
        # 4. [EXT->RESTIF] RECEIVE LOGGING        
        if ConfManager.getInstance().getLogFlag():
            self.logger.info("===============================================");
            self.logger.info("[EXT] -> RESTIF")
            self.logger.info("===============================================");
            self.logger.info("URL : " + str(restAPI.url))
            self.logger.info("TID : " + "tid") # TID
            self.logger.info("RESULT : " + str(restAPI.status_code))
            self.logger.info("HEADER : "  + str(restAPI.headers))                   # resData.headers['Content-Length']
            self.logger.info("BODY : "  + str(restAPI.text))
            self.logger.info("===============================================");
            
        
        # 5. [RESTIF->APP] INPUT RESPONSE MESSAGE ( REST API -> httpRes )
        
        self.resMsg.jsonBody = restAPI.text
        
#         self.resMsg.tot_len = 1
#         self.resMsg.msgId = 1
#         self.resMsg.ehttpf_idx = 1
#         self.resMsg.srcQid = 1
#         self.resMsg.srcSysId = 1
#         self.resMsg.nResult = 2
#         #self.resMsg.http_hdr = 4
#         self.resMsg.jsonBody = "1231"
                
        # 6. [RESTIF->APP] SEND AND LOGGING
        PLTEManager.getInstance().sendResMessage(self.resMsg)
        
        
        
        
            
        
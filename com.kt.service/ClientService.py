import json
import threading
import requests

from ConfigManager import ConfManager
from LogManager import LogManager
from PLTEManager import PLTEManager
from ProvMsg import HttpRes


class ClientService(threading.Thread):
    
    __instance = None
    
    logger = LogManager.getInstance().get_logger()
    
    def __init__(self, httpMsg):
        super(ClientService, self).__init__()
        self.reqMsg = httpMsg
    
    def run(self):
        
        self.tid =  self.reqMsg.tid
        # payload = httpMsg.body....
        
        url='http://localhost:5555/departments/abc/123'
        #head = {'Content-type':'application/json', 'Accept':'application/json'} 
        #head = {'Content-type':'application/json'} 
        head = {'Content-type':'application/x-www-form-urlencoded', 'Accept':'application/json'} 

        # 1. [RESTIF->EXT] INPUT REQUSET MESSAGE ( httpReq -> REST API )
        
        payload = self.reqMsg.jsonBody
        
        # 2. [RESTIF->EXT] CLIENT SEND LOGGING        
        if ConfManager.getInstance().getLogFlag():
            self.logger.info("===============================================");
            self.logger.info("RESTIF -> [EXT]")
            self.logger.info("===============================================");
            self.logger.info("URL : " + url)
            self.logger.info("HEADER : " + str(head))
            self.logger.info("TID : " + str(self.tid)) # TID
            self.logger.info("BODY : "  + str(payload))
            self.logger.info("===============================================");
            
            
        # 3. [RESTIF->EXT] SEND DATA
        try:
            payld = json.dumps(payload)
            #restAPI = requests.post(url,headers=head,data=payld)
            restAPI = requests.post(url,headers=head,data=payload)
        except Exception as e:
            self.logger.info(e)
            
        try:
            # 4. [EXT->RESTIF] RECEIVE LOGGING        
            if ConfManager.getInstance().getLogFlag():
                self.logger.info("===============================================");
                self.logger.info("[EXT] -> RESTIF")
                self.logger.info("===============================================");
                self.logger.info("URL : " + str(restAPI.url))
                self.logger.info("TID : " + str(self.tid)) # TID
                self.logger.info("RESULT : " + str(restAPI.status_code))
                self.logger.info("HEADER : "  + str(restAPI.headers))                   # resData.headers['Content-Length']
                self.logger.info("BODY : "  + str(restAPI.text))
                self.logger.info("===============================================");
                
            
            # 5. [RESTIF->APP] INPUT RESPONSE MESSAGE ( REST API -> httpRes )
            resMsg = HttpRes()
            resMsg.tot_len = 1
            resMsg.msgId = 5
            resMsg.tid = self.tid
            resMsg.ehttpf_idx = 1
            resMsg.srcQid = 1
            resMsg.srcSysId = '1'
            resMsg.nResult = restAPI.status_code
            resMsg.jsonBody = restAPI.text
            
            resMsg.http_hdr = self.reqMsg.http_hdr
                    
        except Exception as e :
            # Error Exception -> if External Server is not connected..
            self.logger.info(e)
            resCode = 500
            #  make resMsg..[[]] 

            # 6. [RESTIF->APP] SEND AND LOGGING
        PLTEManager.getInstance().sendResCommand( "temp", resMsg )




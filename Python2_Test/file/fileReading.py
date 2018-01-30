class extConnfInfo():
    
    def __init__(self):
        self.extId = 0
        self.ipAddress_primary = ''
        self.ipAddress_secondary = ''
        self.port = 0
        self.nfvoName = ''  
        self.reqAuthMethod=''
        self.notiAuthMethod=''                  
        self.credentId = ''
        self.credentPw = ''
        self.tokenId = ''
        self.endpointUrl =''
        self.expiredTime =''
    
    def get_ext_id(self):
        return self.__extId

    def get_ip_address_primary(self):
        return self.__ipAddress_primary

    def get_ip_address_secondary(self):
        return self.__ipAddress_secondary

    def get_port(self):
        return self.__port

    def get_nfvo_name(self):
        return self.__nfvoName

    def get_auth_info(self):
        return self.__authInfo

    def get_req_credent_id(self):
        return self.__reqCredentId
    
    def get_req_credent_pw(self):
        return self.__reqCredentPw
    
    def get_noti_credent_id(self):
        return self.__NotiCredentId
    
    def get_noti_credent_pw(self):
        return self.__NotiCredentPw
    
    def get_token_id(self):
        return self.__tokenId

    def get_endpoint_url(self):
        return self.__endpointUrl
    
    def get_expired_time(self):
        return self.__expiredTime
    
    def get_req_auth_method(self):
        return self.__reqAuthMethod

    def get_noti_auth_method(self):
        return self.__notiAuthMethod


    def set_ext_id(self, value):
        self.__extId = value

    def set_ip_address_primary(self, value):
        self.__ipAddress_primary = value

    def set_ip_address_secondary(self, value):
        self.__ipAddress_secondary = value

    def set_port(self, value):
        self.__port = value

    def set_nfvo_name(self, value):
        self.__nfvoName = value

    def set_auth_info(self, value):
        self.__authInfo = value
  
    def set_req_credent_id(self, value):
        self.__reqCredentId = value
    
    def set_req_credent_pw(self, value):
        self.__reqCredentPw = value
    
    def set_noti_credent_id(self, value):
        self.__NotiCredentId = value
    
    def set_noti_credent_pw(self, value):
        self.__NotiCredentPw = value  

    def set_token_id(self, value):
        self.__tokenId = value

    def set_endpoint_url(self, value):
        self.__endpointUrl = value 
    
    def set_expired_time(self, value):
        self.__expiredTime = value
        
    def set_req_auth_method(self, value):
        self.__reqAuthMethod = value

    def set_noti_auth_method(self, value):
        self.__notiAuthMethod = value  
global extConnList   
global fileName
global wfileName
extConnList = []
fileName = "test.conf"
wfileName = "test2.conf"

def fileWriting():

    global wfileName
    global extConnList

    file = open(wfileName,'w')
    
    file.write("[NFVO_INFO]\n")
    file.write("#-----------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    file.write('%-5s%-20s%-20s%-10s%-15s%-15s%-10s%-10s%-10s%-10s%-10s%-20s%-30s%-10s' % ("#ID","IPADDR","IPADDR2","PORT","NAME","REQ_AUTH","NOTI_AUTH","REQ_ID","REQ_PW", 
                                                                                          "NOTI_ID","NOTI_PW","TOKEN_ID","ENDPOINT_URL","EXPIRED_TIME")
         )
    file.write("\n")
    file.write("#-----------------------------------------------------------------------------------------------------------------------------------------------------------\n")        
    for extConn in extConnList:
        
#         print(str(extConn.get_ext_id())+"\t"+ str(extConn.get_ip_address_primary())+"\t\t"+ str(extConn.get_ip_address_secondary())+"\t\t" +
#                     str(extConn.get_port()) + "\t\t"+ str(extConn.get_nfvo_name())         +"\t\t"+ str(extConn.get_req_auth_method())     +"\t\t" +
#                     str(extConn.get_noti_auth_method()) + "\t\t" + str(extConn.get_req_credent_id())+"\t\t"+ str(extConn.get_req_credent_pw()) + "\t\t"+ 
#                     str(extConn.get_noti_credent_id())  + "\t\t"  + str(extConn.get_noti_credent_pw()) +"\t\t"+ str(extConn.get_token_id()) + "\t\t" +
#                     str(extConn.get_endpoint_url())     +"\t\t" + str(extConn.get_expired_time()) + "\n")

        #strBuff = str(extConn.get_ext_id())+"\t"+ str(extConn.get_ip_address_primary())
        file.write( '%-5s%-20s%-20s%-10s%-15s%-15s%-10s%-10s%-10s%-10s%-10s%-20s%-30s%-10s' %( str(extConn.get_ext_id()), str(extConn.get_ip_address_primary()), str(extConn.get_ip_address_secondary()), #3
                                       str(extConn.get_port()), str(extConn.get_nfvo_name()),str(extConn.get_req_auth_method()), str(extConn.get_noti_auth_method()), # 4
                                       str(extConn.get_req_credent_id()), str(extConn.get_req_credent_pw()), str(extConn.get_noti_credent_id()),                    # 3
                                       str(extConn.get_noti_credent_pw()),  str(extConn.get_token_id()) ,  str(extConn.get_endpoint_url()), str(extConn.get_expired_time()) #4
                                       )
                   )
        
        file.write("\n")
        
        #file.write( fileStream )
        
    file.write("#-----------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    file.close()
    
    

def fileReading(sector):
    global extConnList
    global fileName
    file = open(fileName,'r')
    
    readFlag = 0
    
    for lines in file:

        lines = lines.rstrip('\n')
        if lines == sector:
            readFlag = 1
            continue
             
        if lines == '' or readFlag == 0 or lines[0] == '#':
            continue        
        
        data = []
        data = lines.split()
        
        extConn = extConnfInfo()
        
#         self.extId = 0
#         self.ipAddress_primary = ''
#         self.ipAddress_secondary = ''
#         self.port = 0
#         self.nfvoName = ''                    
#         self.credentId = ''
#         self.credentPw = ''
#         self.tokenId = ''
#         self.endpointUrl =''
#         self.expiredTime =''
        
        extConn.set_ext_id(int(data[0]))
        extConn.set_ip_address_primary(data[1])
        extConn.set_ip_address_secondary(data[2])
        extConn.set_port(int(data[3]))
        extConn.set_nfvo_name(data[4])
        extConn.set_req_auth_method(data[5])
        extConn.set_noti_auth_method(data[6])
        extConn.set_req_credent_id(data[7])
        extConn.set_req_credent_pw(data[8])
        extConn.set_noti_credent_id(data[9])
        extConn.set_noti_credent_pw(data[10])            
        extConn.set_token_id(data[11])
        extConn.set_endpoint_url(data[12])
        extConn.set_expired_time(data[13])       
        
        
        extConnList.append(extConn)
    #file.readline()

def getAuthInfo(ipAddress):
    
    for extConn in extConnList:
        if(extConn.get_ip_address_primary() == ipAddress):
            
            if( extConn.get_token_id() == "-"):
                extConn.set_token_id("12345")
                return 

fileReading("[NFVO_INFO]")
getAuthInfo("183.98.152.72")
fileWriting()

# for extConn in extConnList:
#     print extConn.get_ext_id(), extConn.get_ip_address_primary(), extConn.get_ip_address_secondary(), extConn.get_port(), extConn.get_nfvo_name(), extConn.get_auth_info()

        

    
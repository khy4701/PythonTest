"""
NOTIFICATION DATA MAKING SOURCE
[SAMPLE]

INPUT)

id pm_notification_id STRING
notificationType noti_type STRING
timeStamp time_stamp STRING
thresholdId threshold_id STRING
crossingDirection crossing_direction STRING
objectType objectType STRING
objectInstanceId obj_instance_id STRING
performanceMetric pm_type STRING
performanceValue pm_value STRING


RESULT)

[THRD_NOTI]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#INDEX    API_COL_NAME                  DB_COL_NAME                   TYPE(INTEGER(0), STRING(1))
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
0         id                            pm_notification_id            STRING
1         notificationType              noti_type                     STRING
2         timeStamp                     time_stamp                    STRING
3         thresholdId                   threshold_id                  STRING
4         crossingDirection             crossing_direction            STRING
5         objectType                    objectType                    STRING
6         objectInstanceId              obj_instance_id               STRING
7         performanceMetric             pm_type                       STRING
8         performanceValue              pm_value                      STRING
#-----------------------------------------------------------------------------------------------------------------------------------------------------------


"""



global apiList   
global fileName
global wfileName

fileName = "api.conf"
wfileName = "test2.conf"

apiList = []


class notiData:
  
    def __init__(self,idx, apiCol, dbCol, type):
        self.idx = idx
        self.apiCol = apiCol
        self.dbCol = dbCol
        self.type = type
        
    def getIdx(self):
        return self.idx
    
    def getApiCol(self):
        return self.apiCol
    
    def getDbCol(self):
        return self.dbCol
    
    def getType(self):
        return self.type
    

def fileReading():
    global apiList
    global fileName
    file = open(fileName,'r')
    
    idx = 0 
        
    for lines in file:

        lines = lines.rstrip('\n')
             
        if lines == '' or lines[0] == '#' or lines == ' ':
            continue        
        
        data = []
        data = lines.split()
        
        notiValue = notiData(idx, data[1], data[0], data[2] )        
        idx += 1
        
        apiList.append(notiValue)   
 
 
def fileWriting():
    global apiList
    global wfileName
    
    idx = 0
 
    file = open(wfileName,'w')
                                                    

    file.write("[THRD_NOTI]\n")
    file.write("#-----------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    file.write('%-10s%-30s%-30s%-10s' % ("#INDEX","API_COL_NAME","DB_COL_NAME","TYPE(INTEGER(0), STRING(1))")  )
    file.write("\n")
    file.write("#-----------------------------------------------------------------------------------------------------------------------------------------------------------\n")        
    
    for apiInfo in apiList:
        
        #strBuff = str(extConn.get_ext_id())+"\t"+ str(extConn.get_ip_address_primary())
        file.write( '%-10d%-30s%-30s%-10s' %( apiInfo.getIdx(), apiInfo.getApiCol(), apiInfo.getDbCol(), apiInfo.getType()   )  )
         
        file.write("\n")
                  
    file.write("#-----------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    file.close()
    

fileReading()
fileWriting()

# for extConn in extConnList:
#     print extConn.get_ext_id(), extConn.get_ip_address_primary(), extConn.get_ip_address_secondary(), extConn.get_port(), extConn.get_nfvo_name(), extConn.get_auth_info()

        

    
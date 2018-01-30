from collections import OrderedDict
import uuid

####  JSON SORTING --> important 
#using "import json"
#not using "from Flask import json"
##  
import json
    
data = OrderedDict()
    
data["id"]= str(uuid.uuid1())
data["nsdId"] = "1234"
data["nsdName"] = "1234"
data["nsdVersion"] = "1234"
data["nsdDesigner"] = "1234"
    
vnfPkgList = []
vnfPkgList.append(str(uuid.uuid1()))
data["onboardedVnfPkgInfoIds"] = vnfPkgList
data["nsdInfoState"] = "CREATED"
data["nsdUsageState"] = "IN_USE"
     
keyValuePairs = OrderedDict()
keyValuePairs["key1"] = "value1"
keyValuePairs["key2"] = "value2"
keyValuePairs["key3"] = "value3"
     
data["userDefinedData"] = keyValuePairs
      
# resultData = json.dumps(data)
resultData =  json.dumps(data, indent=4, separators=(',', ': '))
    
print resultData
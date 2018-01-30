from flask import json
from types import NoneType

'''
    "contestants": [{
        "sid": "53d88ec46fb1721307f3a185",
        "u": {
            "_id": {
                "$id": "53d88ec46fb1721307f3a185"
            },
            "g": "M",
            "id": "536lleepkyhnowfh67elpucsq",
            "n": "Asif Khairani",
            "st": "asif-khairani-53d88ec4b24d8"
        },
        "cl": {
            "_id": {
                "$id": "51ff5d1370b17224520002dc"
            },
            "st": "tirpude-institute-of-management-education",
            "ti": "Tirpude Institute of Management Education",
            "n": "Brands",
            "cst": "brands",
            "r": null,
            "c": null
        },
        "ct": "nagpur",
        "tv": 124,
        "cf": 20,
        "picture": "http:\/\/images.iimg.in\/u\/53d88ec46fb1721307f3a185-190-190\/asif-khairani-53d88ec4b24d8.img",
        "action": "+",
        "voteText": "Votes",
        "num1": 6,
        "num2": 5
    }]
}
'''
from operator import index

raw_json = '{"contestants":[{"sid":"53d88ec46fb1721307f3a185","u":{"_id":{"$id":"53d88ec46fb1721307f3a185"},"g":"M","id":"536lleepkyhnowfh67elpucsq", "n":"Asif Khairani","st":"asif-khairani-53d88ec4b24d8"},"cl":{"_id":{"$id":"51ff5d1370b17224520002dc"},"st":"tirpude-institute-of-management-education","ti":"Tirpude Institute of Management Education","n":"Brands","cst":"brands","r":null,"c":null},"ct":"nagpur","tv":124,"cf":20,"picture":"http:\/\/images.iimg.in\/u\/53d88ec46fb1721307f3a185-190-190\/asif-khairani-53d88ec4b24d8.img","action":"+","voteText":"Votes","num1":6,"num2":5}]}'
json_data = """
{
  "menu": {
    "id": "file",
    "value": "File",
    "popup": {
      "menuitem": [
        {"value": "New", "onclick": "CreateNewDoc()"},
        {"value": "Open", "onclick": "OpenDoc()"},
        {"value": "Close", "onclick": "CloseDoc()"}
      ]
    }
  }
}
"""

tt = """
{
    "entries": [
        {
            "objectInstanceId": "4e d544bd - 2504 - 4 d8d - baf9 - b5e971ca5dd4",
            "objectType": "ALL",
            "performanceMetric": "cpu.load",
            "performanceValue": [
                {
                    "performanceValue": "87",
                    "timeStamp": "2018-01-18 09:53:48"
                },
                {
                    "performanceValue": "44",
                    "timeStamp": "2018-01-18 09:53:48"
                },
                {
                    "performanceValue": "25",
                    "timeStamp": "2018-01-18 09:53:48"
                },
                {
                    "performanceValue": "12",
                    "timeStamp": "2018-01-18 09:53:48"
                }
            ]
        },
        {
            "objectInstanceId": "4e d544bd - 2504 - 4 d8d - baf9 - b5e971ca5dd4",
            "objectType": "ALL",
            "performanceMetric": "tps",
            "performanceValue": [
                {
                    "performanceValue": "15",
                    "timeStamp": "2018-01-18 09:53:48"
                },
                {
                    "performanceValue": "76",
                    "timeStamp": "2018-01-18 09:53:48"
                },
                {
                    "performanceValue": "47",
                    "timeStamp": "2018-01-18 09:53:48"
                },
                {
                    "performanceValue": "7",
                    "timeStamp": "2018-01-18 09:53:48"
                }
            ]
        },
        {
            "objectInstanceId": "4e d544bd - 2504 - 4 d8d - baf9 - b5e971ca5dd4",
            "objectType": "NS-5G-PYEONGCHANG",
            "performanceMetric": "memory.usage",
            "performanceValue": [
                {
                    "performanceValue": "1",
                    "timeStamp": "2018-01-18 09:53:48"
                },
                {
                    "performanceValue": "26",
                    "timeStamp": "2018-01-18 09:53:48"
                },
                {
                    "performanceValue": "84",
                    "timeStamp": "2018-01-18 09:53:48"
                },
                {
                    "performanceValue": "7",
                    "timeStamp": "2018-01-18 09:53:48"
                }
            ]
        }
    ]
}


"""

keyList = []

global num
global seperator

#origin_data = raw_json
origin_data = tt
#origin_data = tt

global pLevel

num = 0
pLevel = 0
obj = json.loads(origin_data)

def explore(data, parent, pListIndex, isList):

    global pLevel
    global num
    
    pLevel = pLevel + 1
    
    seperator = "."
    nParent = ''
    
    if isinstance(data,dict):
        
        for k,v in data.items():
            d = dict()
            
            if parent is "":
                
                if isinstance(v,dict):
                    d[k] = ">dict"                    
                    #print 'P|DICT|DICT' + str(jParser.pLevel)
                elif isinstance(v, list):
                    d[k] = ">list"
                    #print 'P|DICT|LIST'+ str(jParser.pLevel)
                else:
                    #print 'P|DICT|VALUE'+ str(jParser.pLevel)
                    d[k] = v
                
                keyList.append(d)
                nParent = str(k)
                
            else :                                
                if isList == 1:
                    nKey = parent +"["+str(pListIndex)+"]"+seperator+ str(k)
                else: 
                    nKey = parent +seperator+ str(k)
                
                if isinstance(v,dict):
                    #print 'DICT|DICT'+ str(jParser.pLevel)
                    d[nKey] = ">dict"
                elif isinstance(v, list):
                    #print 'DICT|LIST'+ str(jParser.pLevel)
                    d[nKey] = ">list"
                else :
                    #print 'DICT|VALUE'+ str(jParser.pLevel)
                    d[nKey] = v
                
                keyList.append(d)
                nParent = nKey
                                     
            num = num + 1
            explore(v, nParent, pListIndex,0)
                
    elif isinstance(data,list):
        listIndex = 0
        #print 'LIST'+ str(jParser.pLevel)
                
        valList = -1
        for v in data:
            d = dict()
            
            # LIST's Data --> dict or list
            if isinstance(v,dict):        
                d = dict()         
                nParent = parent+"["+str(listIndex)+"]" 
                d[nParent] = ">dict"     
                keyList.append(d)           
                explore(v, parent, listIndex, 1)
                listIndex = listIndex+1
            elif isinstance(v,list):  
                d = dict()
                nParent = parent+"["+str(listIndex)+"]"
                d[nParent] = ">list"
                keyList.append(d)
                explore(v, nParent, listIndex, 1)
                listIndex = listIndex+1            
                
            # LIST's data -> value 
            else :
                valList = valList + 1
                listIndex = listIndex+1
                keyList.append(v)
    else:
        return 
    
    keyList.append(">end")
    
    pLevel = pLevel - 1
   
   
num = 0
explore(obj,"", 0, 0)
# print (num)

retList = []

for k in keyList:
    
    if not isinstance(k, dict):
        continue
    
    for key,val in k.items():
        if val == '>dict':
            continue
        
        if isinstance(val, unicode):
            type = 'string'
        else:
            type = 'int'
            
        v = key +":" + str(val) +":" + str(type)
        retList.append( v.encode('utf-8') )
    
print retList
 
    





 
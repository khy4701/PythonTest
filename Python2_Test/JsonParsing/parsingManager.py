
import os
from flask import json

# D:\jsonsample file ..!

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

class jParser :
    
    keyList = []
    num = 0 
    seperator = "."
    pLevel = 0 
    index = -1
    level = 0

    def __init__(self):
        pass
    
    def search(self, dirr):
        files = os.listdir(dirr)
        
        for fName in files:
            fullFilename = os.path.join(dirr, fName)
            
            jParser.keyList = []
            
            jParser.num = 0 
            jParser.seperator = "."
            jParser.pLevel = 0 
            jParser.index = -1          
                          
            # read file 
            
            try :
                f = open(fullFilename, "r") 
                data = f.read()
                obj = json.loads(data.decode('cp949').encode('utf-8'))
                
                # json decoding
                jParser.explore(obj,"", 0, 0)
                #print jParser.keyList
                
                fNewName = os.path.join("D:/jsonsample/parsing", fName+".parsing.txt")
                fw= open(fNewName,"w") 
                fw.write(str(jParser.keyList)) 
                
                
                me = Object()
                jParser.jsonMaker(me, '', -1)
                #print me.toJSON()
                                
                #print(me.toJSON())
                # json encoding
                
                # write result
                fNewName = os.path.join("D:/jsonsample/result", fName+".json.txt")
                fw= open(fNewName,"w") 
                fw.write(me.toJSON()) 
                
                print "[SUCCESS] : " + fullFilename
            except Exception as e:
                print "[FAIL] : "+ fullFilename
                print e
             

    @staticmethod
    def explore(data, parent, pListIndex, isList):
    
        jParser.pLevel = jParser.pLevel + 1
        
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
                    
                    jParser.keyList.append(d)
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
                    
                    jParser.keyList.append(d)
                    nParent = nKey
                                         
                num = jParser.num + 1
                jParser.explore(v, nParent, pListIndex,0)
                    
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
                    jParser.keyList.append(d)           
                    jParser.explore(v, parent, listIndex, 1)
                    listIndex = listIndex+1
                elif isinstance(v,list):  
                    d = dict()
                    nParent = parent+"["+str(listIndex)+"]"
                    d[nParent] = ">list"
                    jParser.keyList.append(d)
                    jParser.explore(v, nParent, listIndex, 1)
                    listIndex = listIndex+1            
                    
                # LIST's data -> value 
                else :
                    valList = valList + 1
                    listIndex = listIndex+1
                    jParser.keyList.append(v)
        else:
            return 
        
        jParser.keyList.append(">end")
        
        jParser.pLevel = jParser.pLevel - 1

    
    @staticmethod
    def getKey(strr):
        
        data = strr.split(".")[-1]
      
        if "[" in data:
            data = data.split("[")[0]
             
        return data
    #     return strr
    
    @staticmethod
    def parentIsList(pObj, k , pKey, value , pIndex):
        
        idx = k.find(pKey)
        strLen = len(pKey)
        sp = idx+strLen
        data = k[sp:].split("[")[1].split("]")[0]
    
    #                print "k[%s], pKey[%s], pIndex[%d], data[%d]" %(k, pKey, pIndex, int(data))
    
        if int(data) == pIndex :
            #print "$k[%s], pKey[%s], pIndex[%d], data[%d]" %(k, pKey, pIndex, int(data))
            
            key = jParser.getKey(k)
            setattr(pObj[pIndex], key, value)                    
            #print('111111111111111111111111 %d' %pIndex)
        else:
            
            #print "^[%s], pKey[%s], Index[%d], data[%d]" %(k, pKey, idx, int(data))
            idx = len(pObj)
            
            if k[-1] == ']':
                #print('222222222222222222222222 %d' %idx )
    
                pObj.append(value)
            else:
                #print('333333333333333333333333 %d' %idx )
    
                pObj.append(Object())
                key = jParser.getKey(k)
                setattr(pObj[idx], key, value )
            
            pIndex = idx
            
        return pIndex
    
    @staticmethod
    def isChildKey(pKey, key):
        
        if pKey in key:
            return True
        
        return False    
    
    #pObj : Object or List([])
    @staticmethod
    def jsonMaker(pObj, pKey, pIndex):
        #print pKey, index
        
        jParser.level = jParser.level + 1
        
        while jParser.index < len(jParser.keyList):
            jParser.index = jParser.index + 1
            
            if jParser.index >= len(jParser.keyList): 
                return 
           
            i = jParser.keyList[jParser.index]
            
            # case Unicode 
            if (not isinstance(i, dict)) :
                        
                if i == '>end' and jParser.level != 1:
                    jParser.level = jParser.level - 1
                    
                    #print "DDDDDDDDDDDDDDDDDDDD1 , pKey : " + pKey
                    return 
                  
                if i != '>end':                     
                    pObj.append(i)
    
    #             pObj.append(i)
                          
                continue          
                   
            # case Dict Type                 
            for k in i.keys():
                
                # New key
                if not jParser.isChildKey(pKey, k):
                    
                    if jParser.level != 1 :
                        jParser.level = jParser.level - 1
                        jParser.index = jParser.index - 1
                        #print "DDDDDDDDDDDDDDDDDDDD2 , pKey : " + pKey
                        return 
                
                if i[k] == '>dict' :
                    n = Object()
                    
                    if not isinstance(pObj, list):
                        key = jParser.getKey(k)
                        setattr(pObj, key, n)
                        #print ">dict|NO|key(%s) pKey(%s), pIndex[%d] level[%d] :" %(k,pKey,pIndex, jParser.level)
    
                        jParser.jsonMaker(n, k, -1)
                        continue
    
                    #print ">dict|LI|key(%s) pKey(%s), pIndex[%d] level[%d]:" %(k,pKey,pIndex, jParser.level)
                    pIndex = jParser.parentIsList(pObj, k , pKey, n, pIndex)
    
                    jParser.jsonMaker(n, k, -1)
                
                elif i[k] == '>list':
                    vlist = [] 
                    if not isinstance(pObj, list):
                        key = jParser.getKey(k)
                        setattr(pObj, key, vlist)
                        #print ">list|NO|key(%s) pKey(%s), pIndex[%d] level[%d]:" %(k,pKey,pIndex, jParser.level)
                        jParser.jsonMaker(vlist, k, -1)
                        
                        continue
                    
                    #print ">list|LI|key(%s) pKey(%s), pIndex[%d] level[%d]:" %(k,pKey,pIndex, jParser.level)
                    pIndex = jParser.parentIsList(pObj, k , pKey, vlist, pIndex)
    
                    jParser.jsonMaker(vlist, k, -1)
                    
                else:
                    if not isinstance(pObj, list):
                        key = jParser.getKey(k)
                        setattr(pObj, key, i[k])
                        #print ">C|NO|key(%s) pKey(%s), pIndex[%d] level[%d]:" %(k,pKey,pIndex, jParser.level)
                        continue
                    
                    #print ">C|LI|key(%s) pKey(%s), pIndex[%d] level[%d]:" %(k,pKey,pIndex, jParser.level)                            
                    pIndex = jParser.parentIsList(pObj, k , pKey, i[k], pIndex)                


jparser =  jParser()
jparser.search("D:\jsonsample\origin")
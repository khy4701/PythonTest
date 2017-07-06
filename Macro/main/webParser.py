# -*- coding:utf-8 -*-

from datetime import datetime
from datetime import time
from bs4 import BeautifulSoup


class webParser():
    
    mainUrl =''
    initXml =''
    mainXml =''
    resMainXml =''
    endXml =''
    
    initFlag = 1
    endFlag = 0
    
    parseFileLoc = ''
    
    def __init__(self, mainUrl):
        
        print ('Web Parser Initialized..')
        self.mainUrl = mainUrl
        self.parseFileLoc = self.mainUrl + "/parsing.txt"
        
        f = open(self.parseFileLoc, 'r')
        
        while True:
            line = f.readline()
        
            if '<tr height="25">' in line:
                self.initFlag = 0
        
            if self.initFlag == 0 and '<tr height="30">' in line:
                self.endFlag = 1
            
            if not line:
                break
        
            if self.initFlag == 1:
                self.initXml += line
                continue
            
            if self.endFlag == 1:
                self.endXml += line
                continue
            
            self.mainXml += line
            
        f.close()

        
    def makeMainXml(self, col):
        f = open(self.mainUrl+"/Main.txt", 'w')

        writeStr = ''
        soup = BeautifulSoup(self.mainXml, "html.parser")
        trData = soup.findAll("tr")[0].findAll("td")
        
        for node in trData: 
            
            if node.text =="" or node.text =="/" or node.text ==":" or "\xa0" in node.string:
                node.string = '%s'
        
        writeStr += str((soup.findAll("tr")[0]))
        
        f.write(writeStr)
        print(col[0], col[1] , col[2], col[3], col[4], col[5] )
        
        #date
        
        excel_date = int(float(col[0]))
        dt = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + excel_date - 2)
        tt = dt.timetuple()
        dateStr = str(tt.tm_mon) +"/" +str(tt.tm_mday)
        
        x = float(col[4]) # a float
        x = int(x * 24 * 3600) # convert to number of seconds
        my_time = time(x//3600, (x%3600)//60, x%60) # hours, minutes, seconds

        timeFormat = "%.2d:%.2d" %(my_time.hour, my_time.minute)
        
        
        self.resMainXml += writeStr % (dateStr, col[1] , col[2], col[3], timeFormat, col[5])
        
        f.close()
        
        
    def makeEnd(self):

        f = open(self.mainUrl+"/End.txt", 'w')

        writeStr = ''
        soup = BeautifulSoup(self.endXml, "html.parser")
        
        changeStr = str('<td align="right" style="border: 1px solid #000; font-family : 맑은 고딕; padding-right : 2pt">&nbsp; ￦ %d</td>')
        trData = soup.findAll("tr")[0].findAll("td")[1].replaceWith(changeStr)
        
        writeStr += str((soup.findAll("tr")[0]))
        
        #print(writeStr)
        f.write(self.endXml)
        
        f.close()
        
        
    def makeResultFile(self):
        
        f = open(self.mainUrl+"/Result.txt", 'w')
                
        self.totalXml = self.initXml + self.resMainXml + self.endXml
        
        for i in self.totalXml:
            f.write(i)
        f.close()
    
        return self.totalXml
        
        

    
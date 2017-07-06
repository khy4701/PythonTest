import sys
from time import sleep
from xlrd import open_workbook
from main.webDriver import webDriver
from main.webParser import webParser

if __name__ == '__main__':
    
    mainUrl = 'D:/Users/Ariel/workspace/Macro/main'

    driver = webDriver(mainUrl)
    
    menu = driver.chooseMenu()    
    driver.getValue()
    
    sleep(5)
    parser = webParser(mainUrl)
        
    wb = open_workbook('sample.xlsx')
    for s in wb.sheets():
        #print 'Sheet:',s.name
        values = []
        for row in range(s.nrows):
            
            if row == 0 : continue
            
            col_value = []
            for col in range(s.ncols):
                value  = (s.cell(row,col).value)
                
                try : value = str(value)
                except : pass
                col_value.append(value)
                        
            parser.makeMainXml(col_value)    
        
        print ("Make Result Success")
        
    totalXml = parser.makeResultFile()
    
    #driver.sendValue(totalXml)
import sys

from xlrd import open_workbook

from MakeXml import XMLMaker


xmlMaker = XMLMaker()

wb = open_workbook('sample.xlsx')
for s in wb.sheets():
    #print 'Sheet:',s.name
    values = []
    for row in range(s.nrows):
        
        if row == 0 : continue
        
        col_value = []
        for col in range(s.ncols):
            value  = (s.cell(row,col).value)
            try : value = str(int(value))
            except : pass
            col_value.append(value)
                    
        xmlMaker.makeMainXml(col_value)      

xmlMaker.makeEndXml()
xmlMaker.makeResultFile()
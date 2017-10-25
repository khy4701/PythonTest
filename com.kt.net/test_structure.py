

pList = []

class SendInfo:
    
    def __init__(self, a,b):
        
        self.a = a
        self.b = b
        
    def getA(self):
        return self.a


sender1 = SendInfo(1,2)
pList.append(sender1)

sender2 = SendInfo(2,3)
pList.append(sender2)

sender3 = SendInfo(3,4)
pList.append(sender3)

sender4 = SendInfo(4,5)
pList.append(sender4)

for member in pList:
        
    if member.getA() == 2:
        pList.remove(member)
    

for member in pList:
    print member.getA()
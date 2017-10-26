

class stTest:
    
    lval = []
    
    def test(self):
        self.lval = [5,4,3]
        
    @classmethod
    def test2(self):
        stTest.lval.append(4)
        
    def tPrint(self):
        
        print (self.lval)
        print (stTest.lval)
        
c1 = stTest()
c3 = stTest()



c1.test()
c1.test2()


c2 = stTest()
c2.test()
c2.test2()


c1.tPrint()
print '----------'

c2.tPrint()

print '----------'

c3.tPrint()
 
        


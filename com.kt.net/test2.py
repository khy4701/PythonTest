from test import t1

class t2:
    
    def __init__(self):
        print 'init t2'
        return 
    
    def testFunc(self):
        t1.s_method()
    
    @staticmethod
    def testFunc2():
        print 'testFunc2'

if __name__=='__main__':
    test2 = t2()

    print '1111'
    test1 = t1(test2)


    test2.testFunc()
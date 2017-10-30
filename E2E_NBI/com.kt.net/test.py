
class t1:
    
    @staticmethod        
    def s_method():
        print 'testFunc1'
              
    def __init__(self, tes):
        from test2 import t2
        print 'init t1'

        self.test = tes
        t2.testFunc2()
        pass

# 
# 
# class test:
#     a = 1
#     
#     def __init__(self):
#         return
#     
#     @classmethod
#     def change(self, n):
#         self.a = n
#         
#         return self.a
# #     @staticmethod
# #     def change(n):
# #         a = n
# #         return a
# 
#     def test2(self):
#         print "c1 function : "+ str(self.a)
#         
#     def test3(self):
#         print "cl2 function : "+ str(self.a)
# 
#         
#     
# if __name__ == '__main__':
#     
#     cl = test()
#     cl2 = test()
#     
#     if (cl == cl2):
#         print 'true'
#         
#     if (cl is cl2):
#         print 'true'
#     
#     cl.test2()
#     cl2.test3()
#     
#     #cl.a = 2         #class member variable
#     
#     cl.a = 2
#     #cl.change(4)
#     
#     cl.test2()
#     cl2.test3()
#     
#     cl2.change(3)
# 
#     cl.test2()
#     cl2.test3()
#         
#     print(cl.a, test.a )
from flask import logging


class test:
    
    instance = None
    a = 2
    logger = None
    
    @staticmethod
    def getInstance():
        if test.instance == None:
            test()
        return test.instance     
    
    def __init__(self):
        if test.instance != None:
            raise Exception("This class is a singleton!")
        else:
            test.instance = self
            
        self.a= 3
        
        self.logger = logging.getLogger("crumbs")
        self.logger.setLevel(logging.DEBUG)
          
        #formatter
        self.formatter = logging.Formatter('[%(asctime)s|%(filename)s:%(lineno)s][%(levelname)s] > %(message)s') 
  
        # Console
        self.streamHandler = logging.StreamHandler() 
          
        # Setting Formatter
        self.streamHandler.setFormatter(self.formatter)
          
        # Handler logging 
        self.logger.addHandler(self.streamHandler)
        
        print(self.logger)

        return 
    
    @classmethod
    def getData(self):
        return self.a
    
    def getLogger(self):
        print (self.logger)
        return self.logger

t = test()
print(test.getInstance().a)      
print(test.getData())

logger = test.getInstance().getLogger()
logger.info("info") 
    

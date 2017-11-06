import logging
import logging.handlers

#from desginPattern import SingletonType
class LogManager:
          
    __instance = None
    logger = None
    #LOG_PATH = '/home/e2e/hykim/src/logs/my.log'
    LOG_PATH = '/home/e2e/PKG/T1.0.0/MP/src/RESTIF/logs/my.log'
    #LOG_PATH = 'D:/logs/python/my.log'
    
    @staticmethod
    def getInstance():
        """ Static access method. """
        if LogManager.__instance == None:
            LogManager.__instance = LogManager()
        return LogManager.__instance 
    
    
    def __init__(self):

        self.logger = logging.getLogger("crumbs")
        self.logger.setLevel(logging.DEBUG)
          
        #formatter
        self.formatter = logging.Formatter('[%(asctime)s|%(filename)s:%(lineno)s][%(levelname)s] > %(message)s') 
  
        # File
        self.fileHandler = logging.FileHandler(self.LOG_PATH) 
          
        # 10 MB ( Automation File Control )
        #file_max_bytes = 10 * 1024 * 1024
        #fileHandler = logging.handlers.RotatingFileHandler(filename='./log/test.log', maxBytes=file_max_bytes, backupCount=10)
          
        # Console
        self.streamHandler = logging.StreamHandler() 
          
        # Setting Formatter
        self.fileHandler.setFormatter(self.formatter) 
        self.streamHandler.setFormatter(self.formatter)
          
        # Handler logging 
        self.logger.addHandler(self.fileHandler) 
        self.logger.addHandler(self.streamHandler)
    
#         # logging logger.debug("debug")
#         self.logger.info("info") 
#         self.logger.warning("warning") 
#         self.logger.error("error") 
#         self.logger.critical("critical")

             
    def get_logger(self):        
        return self.logger
    
        
        

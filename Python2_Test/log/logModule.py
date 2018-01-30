import logging
import logging.handlers


logger = logging.getLogger("crumbs")
logger.setLevel(logging.DEBUG)

# formatter
formatter = logging.Formatter('[%(asctime)s|%(filename)s:%(lineno)s][%(levelname)s] > %(message)s') 

# File
fileHandler = logging.FileHandler('./log/my.log') 

# 10 MB ( Automation File Control )
#file_max_bytes = 10 * 1024 * 1024
#fileHandler = logging.handlers.RotatingFileHandler(filename='./log/test.log', maxBytes=file_max_bytes, backupCount=10)

# Console
streamHandler = logging.StreamHandler() 

# Setting Formatter
fileHandler.setFormatter(formatter) 
streamHandler.setFormatter(formatter)

# Handler logging 
logger.addHandler(fileHandler) 
logger.addHandler(streamHandler)
 
# logging logger.debug("debug")
logger.info("info") 
logger.warning("warning") 
logger.error("error") 
logger.critical("critical")



import ConfigParser
import sys

from LogManager import LogManager


class ConfManager:
    
    MSGQUEUE_INFO = "MSGQUEUE_INFO"
    LOG_INFO   = "LOG_INFO"
    
    __instance = None
    dictList = dict()
    logger = LogManager.getInstance().get_logger()
    
    @staticmethod
    def getInstance():
        """ Static access method. """
        if ConfManager.__instance == None:
            ConfManager.__instance = ConfManager()
        return ConfManager.__instance 
    
    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.config.read('../test.conf')
                
        for each_section in self.config.sections():
            dictionary = dict()
            for (each_key, each_val) in self.config.items(each_section):
                
                #add (key, value)
                #print( each_key, each_val )
                dictionary[each_key] = each_val            
            
            # append(index, value)
            self.dictList[each_section] = dictionary
        
        
        self.logFlag =  self.getConfigData("LOG_INFO", "LOG_FLAG")
        self.logFlag = self.logFlag.upper()

        '''
        for key in self.dictList.keys():
            print "[%s]" % key
            for instance in self.dictList[key].keys():
                print "%s\t%s" % (instance,  self.dictList[key][instance])
        '''

    def getConfigData(self, section, confKey):
        
        for key in self.dictList.keys():            
            if key.upper() != section.upper() :
                continue
            
            for instance in self.dictList[key].keys():
                if instance.upper() != confKey.upper():
                    continue
                
                return  self.dictList[key][instance]
        
        self.logger.error("Can't not found SECTION[%s] KEY[%s] " % (section, confKey))
        return None
        
    def getLogFlag(self):
        if self.logFlag == "ON":
            return True
        
        return False
    
if __name__== '__main__':

    # example 1
    print (ConfManager.getInstance().getConfigData("MSGQUEUE_INFO", "PLTEIB"))
    print (ConfManager.getInstance().getConfigData("MSGQUEUE_INFO", "proc2"))
    

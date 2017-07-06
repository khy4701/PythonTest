'''
import requests

class loginManager():
    
    def __init__(self):
        self.url = 'http://localhost/server.php?wsdl'
            
    def login(self, userId, userPw):
        
        self.id = userId
        self.pw = userPw
        
        result = requests.get(self.url)
        
        plain_text = result.text
        print(result.status_code)
        #print(plain_text)
        
        return result.status_code
        
'''
from suds.client import Client

class loginManager():
    
    def __init__(self):
        self.url = 'http://localhost/server_main.php?wsdl'
        self.client = Client(self.url)

            
    def login(self, userId, userPw):
        
        self.id = userId
        self.pw = userPw
        
        #print (client) ## shows the details of this service

        result = self.client.service.Login(self.id,self.pw) 
        #result = client.service.Register("khy4702","1234") 
        
        return result 
  
    def register(self, userId, userPw):
        
        self.id = userId
        self.pw = userPw
        
        #print (client) ## shows the details of this service

        result = self.client.service.Register(self.id,self.pw) 
        
        return result    
        
        
             
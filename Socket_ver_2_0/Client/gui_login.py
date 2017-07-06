import sys

sys.path.append("D:/Users/Ariel/workspace/Socket_ver_2_0")

from PyQt5.Qt import QVBoxLayout, QDialog
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog,
    QHBoxLayout, QFrame, QSplitter)

from Client.client_socket import *
from WebServer.manager import *


class guiLogin(QDialog):
    
    def __init__(self):
        super().__init__()
        self.initUI()
     
    def initUI(self):      

        hbox = QVBoxLayout(self)

        '''
        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)
 
        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        '''

        self.le_id = QLineEdit(self)
        self.le_id.move(130, 22)
        
        self.le_pw = QLineEdit(self)
        self.le_pw.move(130, 42)
        
        self.loginBtn = QPushButton('Login', self)
        self.loginBtn.move(220, 220)
        self.loginBtn.clicked.connect(self.tryLogin)

        self.regisBtn = QPushButton('Register', self)
        self.regisBtn.move(250, 220)
        self.regisBtn.clicked.connect(self.tryRegister)


        hbox.addWidget(self.loginBtn)
        hbox.addWidget(self.regisBtn)
        hbox.addWidget(self.le_id)
        hbox.addWidget(self.le_pw)

        #hbox.addWidget(splitter2)
        self.setLayout(hbox)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Server Login Page')
        self.show()
               
    def tryLogin(self):
        
        self.id = self.le_id.text()
        self.pw = self.le_pw.text()
        
        print( "ID[%s] ,PW[%s] try to connect" %(self.id ,self.pw) )
        
        #web authentication
        webManager = loginManager()
        result = webManager.login(self.id, self.pw)
        
        if(result == "Success"):
            self.accept()            
                                
    def tryRegister(self):
                   
        # TEMP
        self.id = self.le_id.text()
        self.pw = self.le_pw.text()
                                           
        #web authentication
        webManager = loginManager()
        result = webManager.register(self.id, self.pw)
        
        print (result)
            
    def onChanged(self, text):        
        self.lbl.setText(text)
        self.lbl.adjustSize()    
        
    def keyPressEvent(self, e):        
        if e.key() == Qt.Key_Escape:
            self.close()    
            
    def getUserInfo(self):
        
        return (self.id, self.pw)

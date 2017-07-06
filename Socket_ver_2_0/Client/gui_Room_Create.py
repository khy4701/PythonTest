import sys

sys.path.append("D:/Users/Ariel/workspace/Socket_ver_2_0")

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QAction

from Client.client_socket import *
from Util.Message import MSGTYPE
from Util.Room import room
from WebServer.manager import *      


class guiRoomCreate(QDialog):
    
    def __init__(self , socketTh, mainWindow):
        super().__init__()
        self.initUI() 
        self.socketTh = socketTh      
        self.mainWindow = mainWindow
                             
    def initUI(self):      

        self.setObjectName("RoomCreate")
        self.resize(573, 212)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(40, 50, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 101, 16))
        self.label_2.setObjectName("label_2")
        self.edRoomName = QtWidgets.QLineEdit(self)
        self.edRoomName.setGeometry(QtCore.QRect(140, 50, 361, 20))
        self.edRoomName.setObjectName("edRoomName")
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 491, 16))
        self.groupBox.setObjectName("groupBox")
        self.edLimitMember = QtWidgets.QLineEdit(self)
        self.edLimitMember.setGeometry(QtCore.QRect(140, 90, 361, 20))
        self.edLimitMember.setObjectName("edLimitMember")
        self.CreateBtn = QtWidgets.QPushButton(self)
        self.CreateBtn.setGeometry(QtCore.QRect(110, 130, 131, 51))
        self.CreateBtn.setObjectName("CreateBtn")
        self.CancelBtn = QtWidgets.QPushButton(self)
        self.CancelBtn.setGeometry(QtCore.QRect(320, 130, 131, 51))
        self.CancelBtn.setObjectName("CancelBtn")

        self.CreateBtn.clicked.connect(self.createBtnClicked)
        self.CancelBtn.clicked.connect(self.cancelBtnClicked)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("RoomCreate", "RoomCreate"))
        self.label.setText(_translate("RoomCreate", "Room Name"))
        self.label_2.setText(_translate("RoomCreate", "Limit Member"))
        self.groupBox.setTitle(_translate("RoomCreate", "RoomCreate"))
        self.CreateBtn.setText(_translate("RoomCreate", "Create"))
        self.CancelBtn.setText(_translate("RoomCreate", "Cancel"))
   
                            
    def closeEvent(self, event):
        close = QMessageBox()
        close.setText("Are You sure exit?")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()
                
        if close == QMessageBox.Yes:
            self.mainWindow.show()
        else:
            event.ignore()
            
    def createBtnClicked(self):
        
        sndMsg = self.edRoomName.text()+"#"+ self.socketTh.getUserId()+"#"+ self.edLimitMember.text()
                       
        print ("SendRoomCreate : "+sndMsg)
        self.socketTh.sendToServer(sndMsg, MSGTYPE.ROOM_CREATE)
        self.newRoomName = self.edRoomName.text()
        self.accept()
        
        
    def cancelBtnClicked(self):
        print('Clicked')
        
    def getNewRoomInfo(self):
        return self.newRoomName
    

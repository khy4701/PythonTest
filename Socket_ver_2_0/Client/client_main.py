import sys, os

sys.path.append("D:/Users/Ariel/workspace/Socket_ver_2_0")

from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication)
from PyQt5.Qt import QDialog

from Client.gui_login import *
from Client.gui_main import *



if __name__ == '__main__':

    app = QApplication(sys.argv)
    loginProgram = guiLogin()
    
    if loginProgram.exec_() == QDialog.Accepted:
        
        userInfo = loginProgram.getUserInfo()
        mainProgram = guiMain(userInfo)
        mainProgram.show()
        
        status = app.exec_()
        #sys.exit(app.exec_())

        sys.exit(1)
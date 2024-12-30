import os,random
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import QSizePolicy
import Ui_MainDemo

class MainDemo(QtWidgets.QMainWindow,Ui_MainDemo.Ui_MainDemo):
    def __init__(self,parent=None):
        super(MainDemo,self).__init__(parent)
        self.setupUi(self)

    def on_pbClose_released(self):
        print("Close Button released.")
        self.close()


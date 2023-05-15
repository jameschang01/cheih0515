from PyQt5.QtWidgets import * #星星代表要輸入全部的資料
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from mainwindow import Ui_Dialog
import sys

def clicked_press_me():
    print("hi")

app = QApplication(sys.argv)
widge = QWidget()
ui = Ui_Dialog() 
ui.setupUi(widge)

ui.PressMeBotton.clicked.connect(clicked_press_me) # 連接BUTTON

widge.show()
sys.exit(app.exec_())
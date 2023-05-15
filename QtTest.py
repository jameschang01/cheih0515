from PyQt5.QtWidgets import * #星星代表要輸入qt全部小部件和函數的資料，來構建用戶介面
from PyQt5.QtCore import *  #輸入Qt的核心模塊<包含基本功能(信號和槽機制)
from PyQt5.QtGui import *  #導入Qt 的圖形用戶介面模塊，包含與圖形相關的函數

from mainwindow import Ui_Dialog #定義用戶介面的布局和組件
import sys

def clicked_press_me():
    x = ui.lineEdit.text()            #從lineEdit 給資料
    message = QMessageBox()           #為了使結果不要出現在terminal,而是出現在
    message.setWindowTitle("surprise")
    message.setInformativeText(x)
    message.exec_()                   #執行啟動

def clicked_show_string():
    ui.label_3.setText("hello")
    print("hello")


app = QApplication(sys.argv)  #創建QApplication對象<為核心，用於處理應用程序的事件循環和管理資源
widge = QWidget()  #主窗口
ui = Ui_Dialog()  #創建Ui_Dialog的對象，並調用setupUi()方法，將widge設置為Ui_Dialog的用戶介面
ui.setupUi(widge)

ui.PressMeButton.clicked.connect(clicked_press_me) # 連接BUTTON
ui.ShowStringButton.clicked.connect(clicked_show_string)

widge.show() #顯示主窗口
sys.exit(app.exec_()) #進入事件循環
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1068, 776)
        Dialog.setStyleSheet("font: 9pt \"微軟正黑體\";")
        self.PressMeBotton = QtWidgets.QPushButton(Dialog)
        self.PressMeBotton.setGeometry(QtCore.QRect(370, 450, 111, 31))
        self.PressMeBotton.setStyleSheet("background-color: rgb(130,135,139);\n"
"color: rgb(255, 255, 255);")
        self.PressMeBotton.setObjectName("PressMeBotton")
        self.ShowStringBotton = QtWidgets.QPushButton(Dialog)
        self.ShowStringBotton.setGeometry(QtCore.QRect(720, 450, 111, 31))
        self.ShowStringBotton.setStyleSheet("background-color: rgb(130, 135, 139);\n"
"color: rgb(255, 255, 255);")
        self.ShowStringBotton.setObjectName("ShowStringBotton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 311, 341))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("test.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(450, 100, 291, 171))
        self.label_3.setStyleSheet("font: 18pt \"Adobe Devanagari\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(410, 310, 371, 61))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.PressMeBotton.setText(_translate("Dialog", "show string"))
        self.ShowStringBotton.setText(_translate("Dialog", "press me"))
        self.label_3.setText(_translate("Dialog", "Please enter value"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
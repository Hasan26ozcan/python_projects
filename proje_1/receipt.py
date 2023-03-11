# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'receipt.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from pizza_full_database import Customer_Database
customer_db = Customer_Database()
_translate = QtCore.QCoreApplication.translate

class Ui_Receiptwindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 539))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.title_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title_lineEdit.setFont(font)
        self.title_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.title_lineEdit.setObjectName("title_lineEdit")
        self.gridLayout_2.addWidget(self.title_lineEdit, 0, 0, 1, 1)
        self.receipt_textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.receipt_textEdit.setObjectName("receipt_textEdit")
        self.gridLayout_2.addWidget(self.receipt_textEdit, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_lineEdit.setText(_translate("MainWindow", "your receipt"))
        self.receipt_write()
        
    def receipt_write(self):
        now_time_line = datetime.now()
        with open("currentcustomer.txt","r") as file:
            personal_numb = file.readline()

            purchase_details=file.readlines()
        print(personal_numb)
        customer_name = customer_db.get_name_by_id(personal_numb[:-1])[0].title()

        details = ""
        for detail in purchase_details[:-1]:
            details += detail + "\n"
        
        print(details.split("$"))
        receip_text = ""
        for paragb in details.split("$")[:-1]:
            a=paragb+"$"+"\n"
            receip_text += f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Purchase detail: {a} </p>\n"
        total = details.split("$")[-1]+"$"
        self.receipt_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
f"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Customer: {customer_name}</p>\n"
f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Purchase Date: {now_time_line} </p>\n"
f"{receip_text}"
f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Purchase total: {total} </p>\n"
f"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Receiptwindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

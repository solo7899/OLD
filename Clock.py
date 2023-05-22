# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Clock.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import time
import os


class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(297, 94)
        window.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 271, 61))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(window)
        self.statusbar.setObjectName("statusbar")
        window.setStatusBar(self.statusbar)

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)
        

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "Clock"))
        
    def time_set(self):
        while True:
            now = datetime.now()
            now = now.strftime('%H:%M:%S')
            self.lineEdit.setText(now)
            time.sleep(1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_window()
    ui.time_set()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())

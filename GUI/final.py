import matplotlib.pyplot as plt
from matplotlib import dates
from datetime import datetime
import pyowm
import pytz
from PyQt5 import QtWidgets,QtGui,QtCore
import sys
import numpy as np
from min_max_temp import find_min_max
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


class Ui_MainWindow(object):
    
    def pressed(self):
        self.place=self.lineEdit.text() 
        self.unit_t=None
        print(self.place)
        if self.radioButton.isChecked()==True and self.radioButton_2.isChecked()==False:
            self.unit_t = 'fahrenheit'
            find_min_max(self.place,self.unit_t)            
        elif self.radioButton_2.isChecked()==True and self.radioButton.isChecked()==False:
            self.unit_t = 'Celsius'
            find_min_max(self.place,self.unit_t)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1013, 851)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../App/GUI/iconn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(390, 170, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(540, 170, 109, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 310, 871, 511))
        self.label_3.setText("")
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setPixmap(QtGui.QPixmap("../../Final Project/white.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(730, 200, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setAcceptDrops(False)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 80, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 170, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 260, 100, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(520, 260, 107, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(290, 80, 531, 41))
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton.clicked.connect(self.pressed) 
        self.pushButton_2.clicked.connect(self.show_bar)
        self.pushButton_3.clicked.connect(self.show_line)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WeatherApp"))
        self.radioButton.setText(_translate("MainWindow", "Fahrenheit"))
        self.radioButton_2.setText(_translate("MainWindow", "Celsius"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.pushButton.setShortcut(_translate("MainWindow", "Return"))
        self.label.setText(_translate("MainWindow", "Location :"))
        self.label_2.setText(_translate("MainWindow", "Temperature Unit :"))
        self.pushButton_2.setText(_translate("MainWindow", "Bar Graph"))
        self.pushButton_3.setText(_translate("MainWindow", "Line Graph"))

    def show_bar(self):
        self.label_3.setPixmap(QtGui.QPixmap("figure.png"))
        print("Bar Graph Done")  
    def show_line(self):
        self.label_3.setPixmap(QtGui.QPixmap("figure_line.png"))
        print("Line Graph Done") 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

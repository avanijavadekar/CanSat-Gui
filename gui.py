import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLCDNumber, QMainWindow
from PyQt5.QtCore import QTime, QTimer
from datetime import datetime
import random

from PyQt5 import QtCore, QtGui, QtWidgets

class LivePlotCanvas(FigureCanvas):
    def __init__(self, parent=None, title="", ylabel=""):
        self.fig = Figure(figsize=(5, 3), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title(title)
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel(ylabel)
        super().__init__(self.fig)

        self.x_data = []
        self.y_data = []

    def update_plot(self, new_y, time_step):
        self.x_data.append(time_step)
        self.y_data.append(new_y)

        # keep only last 50 points for readability
        if len(self.x_data) > 50:
            self.x_data.pop(0)
            self.y_data.pop(0)

        self.ax.clear()
        self.ax.plot(self.x_data, self.y_data, color="cyan")
        self.ax.set_title(self.ax.get_title())
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel(self.ax.get_ylabel())
        self.ax.grid(True)
        self.draw()




class Ui_MainWindow(object):

    def on_clicked(self, button1,button2):
        print("pressed")
        button1.setStyleSheet("background-color: gray")
        button2.setStyleSheet("background-color: black")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1424, 890)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setTabletTracking(False)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setStyleSheet("color: rgb(37, 160, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, -10, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(1120, -30, 20, 1051))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(1150, 0, 261, 141))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(20, 30, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setStyleSheet("color: rgb(37, 160, 255);\n"
"")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 80, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton.clicked.connect(lambda: self.on_clicked(self.pushButton,self.pushButton_2))
        self.pushButton_2.clicked.connect(lambda: self.on_clicked(self.pushButton_2,self.pushButton))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(1150, 140, 261, 341))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(130, 30, 113, 20))
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit.setInputMask("")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 60, 113, 21))
        self.lineEdit_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 90, 113, 20))
        self.lineEdit_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_3.setInputMask("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 130, 113, 20))
        self.lineEdit_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_4.setInputMask("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 160, 113, 21))
        self.lineEdit_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_5.setInputMask("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(130, 190, 113, 20))
        self.lineEdit_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_6.setInputMask("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 220, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(130, 240, 113, 20))
        self.lineEdit_7.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_7.setInputMask("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(130, 270, 113, 20))
        self.lineEdit_8.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_8.setInputMask("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(130, 300, 113, 20))
        self.lineEdit_9.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_9.setInputMask("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(1150, 490, 261, 151))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_10.setGeometry(QtCore.QRect(120, 30, 113, 20))
        self.lineEdit_10.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_10.setInputMask("")
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 70, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_11.setGeometry(QtCore.QRect(120, 70, 113, 20))
        self.lineEdit_11.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_11.setInputMask("")
        self.lineEdit_11.setText("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(10, 110, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_12.setGeometry(QtCore.QRect(120, 110, 113, 20))
        self.lineEdit_12.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_12.setInputMask("")
        self.lineEdit_12.setText("")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(1150, 640, 261, 181))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(10, 30, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(10, 60, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(10, 90, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(10, 120, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        self.label_13.setGeometry(QtCore.QRect(10, 150, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setGeometry(QtCore.QRect(10, 180, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_13.setGeometry(QtCore.QRect(110, 30, 113, 20))
        self.lineEdit_13.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_13.setInputMask("")
        self.lineEdit_13.setText("")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_14.setGeometry(QtCore.QRect(110, 60, 113, 20))
        self.lineEdit_14.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_14.setInputMask("")
        self.lineEdit_14.setText("")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_15.setGeometry(QtCore.QRect(110, 90, 113, 20))
        self.lineEdit_15.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_15.setInputMask("")
        self.lineEdit_15.setText("")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_16.setGeometry(QtCore.QRect(110, 120, 113, 20))
        self.lineEdit_16.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_16.setInputMask("")
        self.lineEdit_16.setText("")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_17.setGeometry(QtCore.QRect(110, 150, 113, 20))
        self.lineEdit_17.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_17.setInputMask("")
        self.lineEdit_17.setText("")
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_18.setGeometry(QtCore.QRect(110, 180, 113, 20))
        self.lineEdit_18.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_18.setInputMask("")
        self.lineEdit_18.setText("")
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(850, 630, 271, 191))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setCheckable(False)
        self.groupBox_5.setObjectName("groupBox_5")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 95, 20))
        self.radioButton.setCheckable(False)
        self.radioButton.setChecked(False)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_2.setGeometry(QtCore.QRect(130, 40, 121, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 80, 101, 20))
        self.radioButton_3.setCheckable(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 120, 141, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_5.setGeometry(QtCore.QRect(130, 80, 121, 20))
        self.radioButton_5.setObjectName("radioButton_5")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(470, 630, 371, 201))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_14 = QtWidgets.QLabel(self.groupBox_6)
        self.label_14.setGeometry(QtCore.QRect(20, 30, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setAutoFillBackground(False)
        self.label_14.setStyleSheet("background-color: grey;\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_6)
        self.label_15.setGeometry(QtCore.QRect(180, 30, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: grey;\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_6)
        self.label_16.setGeometry(QtCore.QRect(20, 70, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color: grey;\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox_6)
        self.label_17.setGeometry(QtCore.QRect(170, 70, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("Background-color: grey;\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_6)
        self.label_18.setGeometry(QtCore.QRect(270, 30, 55, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background-color: grey;\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.groupBox_6)
        self.label_19.setGeometry(QtCore.QRect(170, 110, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("Background-color: grey;\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.groupBox_6)
        self.label_20.setGeometry(QtCore.QRect(20, 110, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("Background-color: grey;\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.groupBox_6)
        self.label_21.setGeometry(QtCore.QRect(270, 70, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("Background-color: grey;\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.groupBox_6)
        self.label_22.setGeometry(QtCore.QRect(20, 150, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("Background-color: grey;\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.groupBox_6)
        self.label_23.setGeometry(QtCore.QRect(270, 110, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("Background-color: grey;\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"")
        self.label_23.setObjectName("label_23")
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(350, 630, 120, 201))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_24 = QtWidgets.QLabel(self.groupBox_7)
        self.label_24.setGeometry(QtCore.QRect(10, 30, 101, 16))
        self.label_24.setObjectName("label_24")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_19.setGeometry(QtCore.QRect(10, 50, 91, 22))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.label_25 = QtWidgets.QLabel(self.groupBox_7)
        self.label_25.setGeometry(QtCore.QRect(10, 90, 81, 21))
        self.label_25.setObjectName("label_25")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_20.setGeometry(QtCore.QRect(10, 110, 91, 22))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.groupBox_8 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_8.setGeometry(QtCore.QRect(810, 529, 161, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setObjectName("groupBox_8")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_8)
        self.progressBar.setGeometry(QtCore.QRect(10, 40, 131, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.groupBox_9 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_9.setGeometry(QtCore.QRect(980, 529, 141, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setObjectName("groupBox_9")
        self.label_27 = QtWidgets.QLabel(self.groupBox_9)
        self.label_27.setGeometry(QtCore.QRect(10, 30, 101, 16))
        self.label_27.setObjectName("label_27")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_21.setGeometry(QtCore.QRect(10, 50, 113, 22))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(970, 10, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        #
        self.plot_layout = QtWidgets.QVBoxLayout()
        self.centralwidget.setLayout(self.plot_layout)
        self.altitude_plot = LivePlotCanvas(title="Altitude", ylabel="Altitude (m)")
        self.altitude_plot.setGeometry(QtCore.QRect(50, 100, 100, 50))
        self.angular_plot = LivePlotCanvas(title="Angular Velocity", ylabel="ω (deg/s)")
        self.angular_plot.setGeometry(QtCore.QRect(50, 200, 100, 50))
        self.plot_layout.addWidget(self.altitude_plot)
        self.plot_layout.addWidget(self.angular_plot)  #
        #
        # Timer to update plots
        self.plot_timer = QTimer()
        self.plot_timer.timeout.connect(self.update_plots)
        self.plot_timer.start(1000)
        self.time_step = 0
        #

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1424, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #def __init__(self):
        #super(Ui_MainWindow, self).__init__()
        #uic.loadui("GUIfinal.ui", self)
        #self.lcd=self.findChild(QLCDNumber, "lcdNumber") #defining widget
        #self.timer=QTimer()  #creating timer
        #self.timer.timeout.connect(self.lcd_number)
        #self.timer.start(1000) #starting the timer and updating every second
        #self.lcd_number()
        


    #def lcd_number(self):
        #time=datetime.now()
        #formatted_time=time.strftime("%H:%M:%S")
        #set number of digits 
        #self.lcd.setDigitCount(12)
        #self.lcd.display(formatted_time)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TEAM VYOMGATI"))
        self.groupBox.setTitle(_translate("MainWindow", "MODE:"))
        self.pushButton.setText(_translate("MainWindow", "Real-Time telemetry mode"))
        self.pushButton_2.setText(_translate("MainWindow", "Simulation Mode"))
        self.groupBox_2.setTitle(_translate("MainWindow", "IMU(BNO055):"))
        self.label_2.setText(_translate("MainWindow", "Accelerometer:"))
        self.lineEdit.setText(_translate("MainWindow", "x -"))
        self.lineEdit_2.setText(_translate("MainWindow", "y -"))
        self.lineEdit_3.setText(_translate("MainWindow", "z -"))
        self.label_3.setText(_translate("MainWindow", "Gyroscope:"))
        self.lineEdit_4.setText(_translate("MainWindow", "x -"))
        self.lineEdit_5.setText(_translate("MainWindow", "y -"))
        self.lineEdit_6.setText(_translate("MainWindow", "z -"))
        self.label_4.setText(_translate("MainWindow", "Magnetometer:"))
        self.lineEdit_7.setText(_translate("MainWindow", "x -"))
        self.lineEdit_8.setText(_translate("MainWindow", "y -"))
        self.lineEdit_9.setText(_translate("MainWindow", "z -"))
        self.groupBox_3.setTitle(_translate("MainWindow", "BMP280:"))
        self.label_5.setText(_translate("MainWindow", "Temperature:"))
        self.label_6.setText(_translate("MainWindow", "Altitude:"))
        self.label_7.setText(_translate("MainWindow", "Pressure:"))
        self.groupBox_4.setTitle(_translate("MainWindow", "GNSS:"))
        self.label_8.setText(_translate("MainWindow", "Altitude:"))
        self.label_10.setText(_translate("MainWindow", "Satellites:"))
        self.label_9.setText(_translate("MainWindow", "Latitude:"))
        self.label_11.setText(_translate("MainWindow", "Longitudes:"))
        self.label_13.setText(_translate("MainWindow", "Time:"))
        self.label_12.setText(_translate("MainWindow", "Velocity:"))
        self.groupBox_5.setTitle(_translate("MainWindow", "STATE:"))
        self.radioButton.setText(_translate("MainWindow", "BOOT"))
        self.radioButton_2.setText(_translate("MainWindow", "STANDBY"))
        self.radioButton_3.setText(_translate("MainWindow", "ASCENT"))
        self.radioButton_4.setText(_translate("MainWindow", "RECOVERY"))
        self.radioButton_5.setText(_translate("MainWindow", "DESCENT"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Error Flags:"))
        self.label_14.setText(_translate("MainWindow", "E_COMM_LOSS"))
        self.label_15.setText(_translate("MainWindow", "E_IMU"))
        self.label_16.setText(_translate("MainWindow", "E_COMM_DEL"))
        self.label_17.setText(_translate("MainWindow", "E_PRE"))
        self.label_18.setText(_translate("MainWindow", "E_SD"))
        self.label_19.setText(_translate("MainWindow", "E_PARA"))
        self.label_20.setText(_translate("MainWindow", "E_MEM"))
        self.label_21.setText(_translate("MainWindow", "E_BATT"))
        self.label_22.setText(_translate("MainWindow", "E_NONE"))
        self.label_23.setText(_translate("MainWindow", "E_GNSS"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Metadata:"))
        self.label_24.setText(_translate("MainWindow", "TimeStamp:"))
        self.label_25.setText(_translate("MainWindow", "Packet count:"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Battery Power:"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Health data:"))
        self.label_27.setText(_translate("MainWindow", "RSSI LoRa:"))

    def update_plots(self): 
         self.time_step += 1
         # Simulated data (later replace with CSV/LoRa)
         altitude_value = random.uniform(100, 500)
         angular_velocity_value = random.uniform(-50, 50)

         # Update both plots
         self.altitude_plot.update_plot(altitude_value, self.time_step)
         self.angular_plot.update_plot(angular_velocity_value, self.time_step)

class TelemetryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Instantiate the UI and set it up
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialize the counter for elapsed seconds (mission time)
        self.elapsed_seconds = 0 

        # 1. Initialize QTimer for the clock
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_mission_timer)
        # Update the timer every 1000 ms (1 second)
        self.timer.start(1000) 

        # 2. Configure QLCDNumber
        # Set the number of digits to accommodate HH:MM:SS
        self.ui.lcdNumber.setDigitCount(8) 
        
        # 3. Initialize display to 00:00:00
        self.update_mission_timer()

    def update_mission_timer(self):
        """
        Increments the elapsed time and updates the QLCDNumber with 
        the formatted mission time (HH:MM:SS).
        """
        
        # Increment the counter
        self.elapsed_seconds += 1
        
        # Convert total seconds to hours, minutes, and seconds
        total_seconds = self.elapsed_seconds
        
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        
        # Format the time as a string with leading zeros (e.g., 01:05:09)
        formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        
        # Display the formatted time on the QLCDNumber
        self.ui.lcdNumber.display(formatted_time)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    # Use the new TelemetryWindow class as the main window
    main_window = TelemetryWindow()
    main_window.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
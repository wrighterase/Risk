#!/usr/bin/python
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 441, 251))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("risk.jpg")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(450, 0, 341, 451))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.scrollArea.setFont(font)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 339, 429))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(250, 260, 111, 81))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(120, 260, 144, 80))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.spinBox = QtGui.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.horizontalLayout.addWidget(self.spinBox)
        self.spinBox_2 = QtGui.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.horizontalLayout.addWidget(self.spinBox_2)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 260, 116, 80))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.radioButton = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.verticalLayout_2.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.verticalLayout_2.addWidget(self.radioButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_2.setText(_translate("MainWindow", "Roll", None))
        self.pushButton.setText(_translate("MainWindow", "Exit", None))
        self.radioButton.setText(_translate("MainWindow", "Single Attack", None))
        self.radioButton_2.setText(_translate("MainWindow", "Auto Attack", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


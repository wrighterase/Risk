# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'risk_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

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
        MainWindow.resize(800, 450)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.logo = QtGui.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(0, 0, 381, 211))
        self.logo.setText(_fromUtf8(""))
        self.logo.setPixmap(QtGui.QPixmap(_fromUtf8("risk.jpg")))
        self.logo.setScaledContents(True)
        self.logo.setObjectName(_fromUtf8("logo"))
        self.console_window = QtGui.QTextEdit(self.centralwidget)
        self.console_window.setGeometry(QtCore.QRect(400, 10, 381, 411))
        self.console_window.setReadOnly(True)
        self.console_window.setObjectName(_fromUtf8("console_window"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(1, 303, 381, 114))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.fouroneseven = QtGui.QVBoxLayout()
        self.fouroneseven.setObjectName(_fromUtf8("fouroneseven"))
        self.one_button = QtGui.QPushButton(self.widget)
        self.one_button.setObjectName(_fromUtf8("one_button"))
        self.fouroneseven.addWidget(self.one_button)
        self.four_button = QtGui.QPushButton(self.widget)
        self.four_button.setObjectName(_fromUtf8("four_button"))
        self.fouroneseven.addWidget(self.four_button)
        self.seven_button = QtGui.QPushButton(self.widget)
        self.seven_button.setObjectName(_fromUtf8("seven_button"))
        self.fouroneseven.addWidget(self.seven_button)
        self.horizontalLayout_3.addLayout(self.fouroneseven)
        self.eightfivetwo = QtGui.QVBoxLayout()
        self.eightfivetwo.setObjectName(_fromUtf8("eightfivetwo"))
        self.two_button = QtGui.QPushButton(self.widget)
        self.two_button.setObjectName(_fromUtf8("two_button"))
        self.eightfivetwo.addWidget(self.two_button)
        self.five_button = QtGui.QPushButton(self.widget)
        self.five_button.setObjectName(_fromUtf8("five_button"))
        self.eightfivetwo.addWidget(self.five_button)
        self.eight_button = QtGui.QPushButton(self.widget)
        self.eight_button.setObjectName(_fromUtf8("eight_button"))
        self.eightfivetwo.addWidget(self.eight_button)
        self.horizontalLayout_3.addLayout(self.eightfivetwo)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.ninesixthree = QtGui.QVBoxLayout()
        self.ninesixthree.setObjectName(_fromUtf8("ninesixthree"))
        self.three_button = QtGui.QPushButton(self.widget)
        self.three_button.setObjectName(_fromUtf8("three_button"))
        self.ninesixthree.addWidget(self.three_button)
        self.six_button = QtGui.QPushButton(self.widget)
        self.six_button.setObjectName(_fromUtf8("six_button"))
        self.ninesixthree.addWidget(self.six_button)
        self.nine_button = QtGui.QPushButton(self.widget)
        self.nine_button.setObjectName(_fromUtf8("nine_button"))
        self.ninesixthree.addWidget(self.nine_button)
        self.horizontalLayout_4.addLayout(self.ninesixthree)
        self.zeroclear = QtGui.QVBoxLayout()
        self.zeroclear.setObjectName(_fromUtf8("zeroclear"))
        self.clear_button = QtGui.QPushButton(self.widget)
        self.clear_button.setObjectName(_fromUtf8("clear_button"))
        self.zeroclear.addWidget(self.clear_button)
        self.zero = QtGui.QPushButton(self.widget)
        self.zero.setObjectName(_fromUtf8("zero"))
        self.zeroclear.addWidget(self.zero)
        self.horizontalLayout_4.addLayout(self.zeroclear)
        self.widget1 = QtGui.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.widget2 = QtGui.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.widget2)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.widget3 = QtGui.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.widget3.setObjectName(_fromUtf8("widget3"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.widget3)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.widget4 = QtGui.QWidget(self.centralwidget)
        self.widget4.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.widget4.setObjectName(_fromUtf8("widget4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget4)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.widget5 = QtGui.QWidget(self.centralwidget)
        self.widget5.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.widget5.setObjectName(_fromUtf8("widget5"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.widget5)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.widget6 = QtGui.QWidget(self.centralwidget)
        self.widget6.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.widget6.setObjectName(_fromUtf8("widget6"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.widget6)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.widget7 = QtGui.QWidget(self.centralwidget)
        self.widget7.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.widget7.setObjectName(_fromUtf8("widget7"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.widget7)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.widget8 = QtGui.QWidget(self.centralwidget)
        self.widget8.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.widget8.setObjectName(_fromUtf8("widget8"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.widget8)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.widget9 = QtGui.QWidget(self.centralwidget)
        self.widget9.setGeometry(QtCore.QRect(280, 220, 101, 72))
        self.widget9.setObjectName(_fromUtf8("widget9"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget9)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.roll_button = QtGui.QPushButton(self.widget9)
        self.roll_button.setObjectName(_fromUtf8("roll_button"))
        self.verticalLayout.addWidget(self.roll_button)
        self.exit_button = QtGui.QPushButton(self.widget9)
        self.exit_button.setObjectName(_fromUtf8("exit_button"))
        self.verticalLayout.addWidget(self.exit_button)
        self.widget10 = QtGui.QWidget(self.centralwidget)
        self.widget10.setGeometry(QtCore.QRect(90, 220, 181, 73))
        self.widget10.setObjectName(_fromUtf8("widget10"))
        self.verticalLayout_31 = QtGui.QVBoxLayout(self.widget10)
        self.verticalLayout_31.setObjectName(_fromUtf8("verticalLayout_31"))
        self.groupBox = QtGui.QGroupBox(self.widget10)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.attacker_radio = QtGui.QRadioButton(self.groupBox)
        self.attacker_radio.setGeometry(QtCore.QRect(0, 0, 81, 25))
        font = QtGui.QFont()
        font.setPointSize(10.5)
        self.attacker_radio.setFont(font)
        self.attacker_radio.setObjectName(_fromUtf8("attacker_radio"))
        self.defender_radio = QtGui.QRadioButton(self.groupBox)
        self.defender_radio.setGeometry(QtCore.QRect(80, 0, 101, 25))
        font = QtGui.QFont()
        font.setPointSize(10.5)
        self.defender_radio.setFont(font)
        self.defender_radio.setObjectName(_fromUtf8("defender_radio"))
        self.verticalLayout_31.addWidget(self.groupBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.acount_spinbox = QtGui.QSpinBox(self.widget10)
        self.acount_spinbox.setMinimum(1)
        self.acount_spinbox.setObjectName(_fromUtf8("acount_spinbox"))
        self.horizontalLayout.addWidget(self.acount_spinbox)
        self.dcount_spinbox = QtGui.QSpinBox(self.widget10)
        self.dcount_spinbox.setMinimum(1)
        self.dcount_spinbox.setObjectName(_fromUtf8("dcount_spinbox"))
        self.horizontalLayout.addWidget(self.dcount_spinbox)
        self.verticalLayout_31.addLayout(self.horizontalLayout)
        self.widget11 = QtGui.QWidget(self.centralwidget)
        self.widget11.setGeometry(QtCore.QRect(0, 230, 81, 58))
        self.widget11.setObjectName(_fromUtf8("widget11"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget11)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.single_radio = QtGui.QRadioButton(self.widget11)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.single_radio.setFont(font)
        self.single_radio.setObjectName(_fromUtf8("single_radio"))
        self.verticalLayout_2.addWidget(self.single_radio)
        self.auto_radio = QtGui.QRadioButton(self.widget11)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.auto_radio.setFont(font)
        self.auto_radio.setObjectName(_fromUtf8("auto_radio"))
        self.verticalLayout_2.addWidget(self.auto_radio)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.one_button.setText(_translate("MainWindow", "1", None))
        self.four_button.setText(_translate("MainWindow", "4", None))
        self.seven_button.setText(_translate("MainWindow", "7", None))
        self.two_button.setText(_translate("MainWindow", "2", None))
        self.five_button.setText(_translate("MainWindow", "5", None))
        self.eight_button.setText(_translate("MainWindow", "8", None))
        self.three_button.setText(_translate("MainWindow", "3", None))
        self.six_button.setText(_translate("MainWindow", "6", None))
        self.nine_button.setText(_translate("MainWindow", "9", None))
        self.clear_button.setText(_translate("MainWindow", "Clear", None))
        self.zero.setText(_translate("MainWindow", "0", None))
        self.roll_button.setText(_translate("MainWindow", "Roll", None))
        self.exit_button.setText(_translate("MainWindow", "Exit", None))
        self.attacker_radio.setText(_translate("MainWindow", "Attacker", None))
        self.defender_radio.setText(_translate("MainWindow", "Defender", None))
        self.single_radio.setText(_translate("MainWindow", "Single", None))
        self.auto_radio.setText(_translate("MainWindow", "Auto", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
#!/usr/bin/python
from PyQt4 import QtGui
from PyQt4 import QtCore
import sys
import risk_dice
import gui


class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)
    def write(self, text):
        self.textWritten.emit(str(text))
        
        
class RiskApp(QtGui.QMainWindow, gui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(RiskApp, self).__init__(parent)
        self.setupUi(self)
        self.exit_button.clicked.connect(sys.exit)
        self.clear_button.clicked.connect(self.clear_gui)
        self.one_button.clicked.connect(self.numpad)
        self.two_button.clicked.connect(self.numpad)
        self.two_button.clicked.connect(self.numpad)
        self.three_button.clicked.connect(self.numpad)
        self.four_button.clicked.connect(self.numpad)
        self.five_button.clicked.connect(self.numpad)
        self.six_button.clicked.connect(self.numpad)
        self.seven_button.clicked.connect(self.numpad)
        self.eight_button.clicked.connect(self.numpad)
        self.nine_button.clicked.connect(self.numpad)
        self.zero.clicked.connect(self.numpad)
        self.roll_button.clicked.connect(self.war)
        self.single_radio.toggled.connect(self.reset_dice)
        #self.auto_radio.toggled.connect(self.attack_mode)
        sys.stdout = EmittingStream(textWritten=self.console_output)

    
    def reset_dice(self):
        if self.single_radio.isChecked() == True:
            #self.aedit.setText(str(3))
            #self.dedit.setText(str(2))
            self.acount_spinbox.setValue(3)
            self.dcount_spinbox.setValue(2)    

    def war(self):
        self.console_window.clear()
        if self.single_radio.isChecked() == True:
            attack = self.acount_spinbox.value()
            defend = self.dcount_spinbox.value()
            risk_dice.single(attack, defend)
            
        if self.auto_radio.isChecked() == True:
            attack = self.acount_spinbox.value()
            defend = self.dcount_spinbox.value()
            risk_dice.auto(attack,defend)

    
    def __del__(self):
        # Restore sys.stdout
        sys.stdout = sys.__stdout__
        
    def console_output(self, text):
    #redirect stdout to a readonly lineedit widget
        cursor = self.console_window.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.console_window.setTextCursor(cursor)
        self.console_window.ensureCursorVisible()

        
    def numpad(self):
    #sets both spinboxes to equal value until focusInEvent can be solved
        if self.attacker_radio.isChecked() == True:
            self.acount_spinbox.setValue(int(self.sender().text()))
        if self.defender_radio.isChecked() == True:
            self.dcount_spinbox.setValue(int(self.sender().text()))
                    
    def clear_gui(self):
    #clear spinbox values
        self.acount_spinbox.setValue(0)
        self.dcount_spinbox.setValue(0)
        

def main():
    app = QtGui.QApplication(sys.argv)
    form = RiskApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
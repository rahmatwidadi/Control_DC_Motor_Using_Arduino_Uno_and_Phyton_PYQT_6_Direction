import sys, os, glob
from PyQt5 import QtCore, QtWidgets, uic
import serial, time

qtCreatorFile = "gui_tugas_pyqt_arduino.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
        def __init__(self):
                QtWidgets.QMainWindow.__init__(self)
                Ui_MainWindow.__init__(self)
                self.setupUi(self)
                self.button_serial.clicked.connect(self.OpenSerial)
                self.button_exit.clicked.connect(self.AppExit)
                self.button_forward.pressed.connect(self.forward)
                self.button_forward.released.connect(self.stay)
                self.button_reverse.pressed.connect(self.reverse)
                self.button_reverse.released.connect(self.stay)
                self.button_turn_forward_right.pressed.connect(self.turn_forward_right)
                self.button_turn_forward_right.released.connect(self.stay)
                self.button_turn_forward_left.pressed.connect(self.turn_forward_left)
                self.button_turn_forward_left.released.connect(self.stay)
                self.button_turn_reverse_right.pressed.connect(self.turn_reverse_right)
                self.button_turn_reverse_right.released.connect(self.stay)
                self.button_turn_reverse_left.pressed.connect(self.turn_reverse_left)                              
                self.button_turn_reverse_left.released.connect(self.stay)
                self.button_stay.clicked.connect(self.stay)
                self.button_stay.setEnabled(False)
                self.button_forward.setEnabled(False)
                self.button_turn_forward_right.setEnabled(False)
                self.button_turn_reverse_right.setEnabled(False)
                self.button_reverse.setEnabled(False)
                self.button_turn_reverse_left.setEnabled(False)
                self.button_turn_forward_left.setEnabled(False)

        def OpenSerial(self):
                if self.button_serial.text()=='Serial':
                        self.ser = serial.Serial("COM4", "9600", timeout=0.1)
                        if self.ser.isOpen():
                         self.button_serial.setText('Close Serial')
                         self.textEdit_LogMessage.append("Opening serial port... OK")
                         self.button_stay.setEnabled(True)
                         self.button_forward.setEnabled(True)
                         self.button_turn_forward_right.setEnabled(True)
                         self.button_turn_reverse_right.setEnabled(True)
                         self.button_reverse.setEnabled(True)
                         self.button_turn_reverse_left.setEnabled(True)
                         self.button_turn_forward_left.setEnabled(True)
                        else:
                                self.textEdit_LogMessage.append("can not open serial port")
                else:
                        if self.ser.isOpen():
                                self.ser.close()
                                self.button_serial.setText('Serial')
                                self.textEdit_LogMessage.append("Closing serial port... OK")
                                self.button_stay.setEnabled(False)
                                self.button_forward.setEnabled(False)
                                self.button_turn_forward_right.setEnabled(False)
                                self.button_turn_reverse_right.setEnabled(False)
                                self.button_reverse.setEnabled(False)
                                self.button_turn_reverse_left.setEnabled(False)
                                self.button_turn_forward_left.setEnabled(False)
        def stay(self):
                self.TXdata=1
                self.ser.write(self.TXdata)
                self.textEdit_LogMessage.append("Stop")
        
        def forward(self):
                self.TXdata=2
                self.ser.write(self.TXdata)
                self.textEdit_LogMessage.append("Constan Forward")
                time.sleep(2)
                
        def turn_forward_right(self):
                self.TXdata=3
                self.ser.write(self.TXdata)
                self.textEdit_LogMessage.append("Turn Forward Right" )
                time.sleep(2)
                
        def turn_reverse_right(self):
                self.TXdata=4
                self.ser.write(self.TXdata)
                self.textEdit_LogMessage.append("Turn Forward Right" )
                time.sleep(2)
                
        def reverse(self):
                self.TXdata=5
                self.ser.write(self.TXdata)
                self.textEdit_LogMessage.append("Constan Reverse" )
                time.sleep(2)
                
        def turn_reverse_left(self):
                self.TXdata=6
                self.ser.write(self.TXdata)
                self.textEdit_LogMessage.append("Turn Reverse Left" )
                time.sleep(2)
                
        def turn_forward_left(self):
                self.TXdata=7
                self.ser.write(self.TXdata)
                self.textEdit_LogMessage.append("Turn Forward Left" )
                time.sleep(2)
                
        def AppExit(self):
                self.textEdit_LogMessage.setText("Exit application")
                sys.exit()
        
if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        window = MyApp()
        window.show()
        sys.exit(app.exec_())

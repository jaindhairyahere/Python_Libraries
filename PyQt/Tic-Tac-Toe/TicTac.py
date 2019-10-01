# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TicTacToeGui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
try:
    def _fromUtf8(s):
        return s
except:
    pass

try:
    # _encoding =QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class Ui_TicTacToe(object):
    def setupUi(self, TicTacToe):
        TicTacToe.setObjectName("TicTacToe")
        TicTacToe.resize(466, 452)
        self.centralwidget = QWidget(TicTacToe)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 20, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 20, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.line = QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(160, 120, 21, 261))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(280, 120, 21, 261))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(30, 200, 401, 20))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(30, 280, 401, 20))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 130, 121, 81))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 130, 121, 81))
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(290, 130, 121, 81))
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 210, 121, 81))
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(170, 210, 121, 81))
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(290, 210, 121, 81))
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(50, 290, 121, 81))
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(170, 290, 121, 81))
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(290, 290, 121, 81))
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.player1 = QLineEdit(self.centralwidget)
        self.player1.setGeometry(QtCore.QRect(10, 60, 211, 41))
        self.player1.setObjectName("player1")
        self.player2 = QLineEdit(self.centralwidget)
        self.player2.setGeometry(QtCore.QRect(240, 60, 211, 41))
        self.player2.setObjectName("player2")
        self.pushButton_12 = QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(310, 380, 101, 41))
        self.pushButton_12.setObjectName("pushButton_12")
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 390, 231, 21))
        self.label.setObjectName("label")
        TicTacToe.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(TicTacToe)
        self.statusbar.setObjectName("statusbar")
        TicTacToe.setStatusBar(self.statusbar)

        self.retranslateUi(TicTacToe)
        QtCore.QMetaObject.connectSlotsByName(TicTacToe)

    def retranslateUi(self, TicTacToe):
        TicTacToe.setWindowTitle(_translate("TicTacToe", "TicTacToe", None))
        self.pushButton.setText(_translate("TicTacToe", "Player X", None))
        self.pushButton_2.setText(_translate("TicTacToe", "Player O", None))
        self.pushButton_12.setText(_translate("TicTacToe", "New Game", None))
        self.label.setText(_translate("TicTacToe", "The Winner is Player X", None))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    TicTacToe = QMainWindow()
    ui = Ui_TicTacToe()
    ui.setupUi(TicTacToe)
    TicTacToe.show()
    sys.exit(app.exec_())


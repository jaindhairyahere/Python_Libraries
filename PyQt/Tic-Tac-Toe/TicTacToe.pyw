import sys
import TicTac
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#tkinter
class TicTacToeBoard(TicTac.Ui_TicTacToe, QMainWindow):
	def __init__(self,start='X'):
		super(TicTacToeBoard,self).__init__()
		self.setupUi(self)
		self._start=start
		self._board=[[None]*3 for i in range(3)]
		self._Mark=[None,'O','X']
		dic={'O':1,'X':-1}
		self._i=dic[self._start]

		self.connect(self.pushButton_3,SIGNAL("clicked()"), lambda: self.pushButton_3.setText("%s" %self._Mark[self._i]) )
		self.connect(self.pushButton_3,SIGNAL("clicked()"), lambda: self.mark(0,0))
		self.connect(self.pushButton_3,SIGNAL("clicked()"), lambda: self.pushButton_3.setEnabled(False))

		self.connect(self.pushButton_4,SIGNAL("clicked()"), lambda: self.pushButton_4.setText("%s" %self._Mark[self._i]) )
		self.connect(self.pushButton_4,SIGNAL("clicked()"), lambda: self.mark(0,1))
		self.connect(self.pushButton_4,SIGNAL("clicked()"), lambda: self.pushButton_4.setEnabled(False))

		self.connect(self.pushButton_5,SIGNAL("clicked()"), lambda: self.pushButton_5.setText("%s" %self._Mark[self._i]) )
		self.connect(self.pushButton_5,SIGNAL("clicked()"), lambda: self.mark(0,2))
		self.connect(self.pushButton_5,SIGNAL("clicked()"), lambda: self.pushButton_5.setEnabled(False))

		self.connect(self.pushButton_6,SIGNAL("clicked()"), lambda: self.pushButton_6.setText("%s" %self._Mark[self._i]) )
		self.connect(self.pushButton_6,SIGNAL("clicked()"), lambda: self.mark(1,0))
		self.connect(self.pushButton_6,SIGNAL("clicked()"), lambda: self.pushButton_6.setEnabled(False))
		self.connect(self.pushButton_7,SIGNAL("clicked()"), lambda: self.pushButton_7.setText("%s" %self._Mark[self._i]) )
		self.connect(self.pushButton_7,SIGNAL("clicked()"), lambda: self.mark(1,1))
		self.connect(self.pushButton_7,SIGNAL("clicked()"), lambda: self.pushButton_7.setEnabled(False))

		self.connect(self.pushButton_8,SIGNAL("clicked()"), lambda: self.pushButton_8.setText("%s" %self._Mark[self._i]) )
		self.connect(self.pushButton_8,SIGNAL("clicked()"), lambda: self.mark(1,2))
		self.connect(self.pushButton_8,SIGNAL("clicked()"), lambda: self.pushButton_8.setEnabled(False))

		self.connect(self.pushButton_9,SIGNAL("clicked()"), lambda: self.pushButton_9.setText("%s" %self._Mark[self._i]) )
		self.connect(self.pushButton_9,SIGNAL("clicked()"), lambda: self.mark(2,0))
		self.connect(self.pushButton_9,SIGNAL("clicked()"), lambda: self.pushButton_9.setEnabled(False))

		self.connect(self.pushButton_10,SIGNAL("clicked()"), lambda: self.pushButton_10.setText("%s" %self._Mark[self._i]) )
		self.connect(self.pushButton_10,SIGNAL("clicked()"), lambda: self.mark(2,1))
		self.connect(self.pushButton_10,SIGNAL("clicked()"), lambda: self.pushButton_10.setEnabled(False))

		self.connect(self.pushButton_11,SIGNAL("clicked()"), lambda: self.pushButton_11.setText("%s" %self._Mark[self._i]) )
		self.connect(self.pushButton_11,SIGNAL("clicked()"), lambda: self.mark(2,2))
		self.connect(self.pushButton_11,SIGNAL("clicked()"), lambda: self.pushButton_11.setEnabled(False))

		self.connect(self.pushButton_12,SIGNAL("clicked()"), lambda: self.newgame())


	def mark(self,x,y):
		self._board[x][y]=self._Mark[self._i]
		self._i*=-1
		flag=bool(1)
		for entry in self._board:
			if entry is  None:
				flag=0
				break
		if flag:
			self.label.setText("%s" %self.winner())
		if self.winner() != "Match Draw":
			self.label.setText("%s" %self.winner())

	def newgame(self):
		self._board=[[' ']*3 for i in range(3)]
		dic={'O':1,'X':-1}
		self._i=dic[self._start]*-1
		self.pushButton_3.setText("")
		self.pushButton_3.setEnabled(True)
		self.pushButton_4.setText('')
		self.pushButton_4.setEnabled(True)
		self.pushButton_5.setText('')
		self.pushButton_5.setEnabled(True)
		self.pushButton_6.setText('')
		self.pushButton_6.setEnabled(True)
		self.pushButton_7.setText('')
		self.pushButton_7.setEnabled(True)
		self.pushButton_8.setText('')
		self.pushButton_8.setEnabled(True)
		self.pushButton_9.setText('')
		self.pushButton_9.setEnabled(True)
		self.pushButton_10.setText('')
		self.pushButton_10.setEnabled(True)
		self.pushButton_11.setText('')
		self.pushButton_11.setEnabled(True)
			
	def _iswin(self,mark):
		board=self._board
		return (mark == board[0][0] == board[0][1] == board[0][2] or 
		mark == board[1][0] == board[1][1] == board[1][2] or # row 1
		mark == board[2][0] == board[2][1] == board[2][2] or # row 2
		mark == board[0][0] == board[1][0] == board[2][0] or # column 0
		mark == board[0][1] == board[1][1] == board[2][1] or # column 1
		mark == board[0][2] == board[1][2] == board[2][2] or # column 2
		mark == board[0][0] == board[1][1] == board[2][2] or # diagonal
		mark == board[0][2] == board[1][1] == board[2][0]) 
	

	def winner(self):
		dic={'X':self.player1.text(),'O':self.player2.text()}
		for mark in dic:
			if self._iswin(mark):
				string='The winner is :'+ dic[mark]
				return string
		return "Match Draw"
	

	def __str__(self):
		rows=['|'.join(self._board[r]) for r in range(3)]
		return '\n------\n'.join(rows)

if __name__=="__main__":
	app=QApplication(sys.argv)
	Game=TicTacToeBoard()
	Game.show()
	app.exec_()

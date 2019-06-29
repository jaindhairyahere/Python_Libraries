'''This application uses two widgets: A QTextBrowser which is a read-only multiline text box that can display both plain text and HTML;and a QLineEdit, which
is a single-line text box that displays plain text. '''
from __future__ import division
import sys
from math import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Calci(QDialog):						# Inheriting it gives an empty grey box with 3 functional buttons(close, minimize and all)
	def __init__(self,parent=None):
		super(Calci,self).__init__(parent)
		#Creating Layout
		self._textbox=QTextBrowser()
		self._lineedit=QLineEdit("Type the expression and press Enter")
		self._lineedit.selectAll()			#This will ensure that as soon as the user starts typing, the text we gave will be overwritten

		Layout=QVBoxLayout()
		Layout.addWidget(self._textbox)
		Layout.addWidget(self._lineedit)
		
		self.setLayout(Layout)
		self.setWindowTitle('Calculate')
		self._lineedit.setFocus()

		self.connect(self._lineedit, SIGNAL("returnPressed()"), self.Calculate)

	def Calculate(self):
		try:
			text=self._lineedit.text()
			insert_text="=" + str(eval(text))
			self._textbox.append(insert_text)
		except:
			self._textbox.append("<font color=red>%s is invalid!</font>" % text)

if __name__=='__main__':
	app=QApplication(sys.argv)
	Calc=Calci()
	Calc.show()
	app.exec_()


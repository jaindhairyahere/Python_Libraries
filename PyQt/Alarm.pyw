import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
app=QApplication(sys.argv)			# Makes an QApplication Instance at the path sys.argv

# Writing Code to get time
due=QTime.currentTime()
t=QTime(18,40)
print(t)
msg='Alert'
hours, mins = sys.argv[1].split(':')
due=QTime(int(hours),int(mins))
if len(sys.argv)>2:
	message=" ".join(sys.argv[2:])

#Printing the Message
label=QLabel("<font color=red size=72><b>"+message+"<\b><\font>")
label.setWindowFlags(Qt.SplashScreen) #We don’t want a title bar for this application, so we set the label’s window flags to those used for splash screens since they have no title bar. 
label.show()
QTimer.singleShot(60000, app.exit) #how long until it should time out (one minute in this case), and a function or method for it to call when it times out.
app.exec_()


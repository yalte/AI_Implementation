from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
  def __init__(self):
    super(MyWindow, self).__init__()
    self.setGeometry(200,200,300,300)
    self.setWindowTitle('DAVE')
    self.initUI()
  
  def initUI(self):
    self.label = QtWidgets.QLabel(self)
    self.label.setText('Hello Sir!')
    self.label.move(10,0)

    self.b1 = QtWidgets.QPushButton(self)
    self.b1.setText('Click')
    self.b1.move(0,25)
    self.b1.clicked.connect(self.clicked)

  def clicked(self):
    self.label.setText('You Pressed the button!')
    self.update()

  def update(self):
    self.label.adjustSize()

def window():
  app = QApplication(sys.argv)
  win = MyWindow()

  win.show()
  sys.exit(app.exec_())

window()
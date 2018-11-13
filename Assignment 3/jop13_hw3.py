
import sys
from PyQt5 import QtWidgets, QtCore, QtGui

class Homework3(QtWidgets.QMainWindow):
   def __init__(self):
      QtWidgets.QMainWindow.__init__(self)
      self.setup()

   def setup(self):
      self.setWindowTitle('Homework 3')
      
      self.draw = Droid(self)
      self.setCentralWidget(self.draw)

      self.show()

class Droid(QtWidgets.QWidget):
   def __init__(self, parent):
      QtWidgets.QWidget.__init__(self, parent)
      self.setup()
   
   def setup(self):
      self.droid = DrawImage(self)
      self.up = UpBtn(self)
      self.right = RightBtn(self)
      self.down = DownBtn(self)
      self.left = LeftBtn(self)

      # setup grid
      self.grid = QtWidgets.QGridLayout()
      self.setLayout(self.grid)

      # setup grid widgets
      self.grid.addWidget(self.droid, 2, 2, 1, 1)
      self.grid.addWidget(self.up, 1, 1, 1, 3)
      self.grid.addWidget(self.right, 2, 3, 1, 1)
      self.grid.addWidget(self.down, 3, 1, 1, 3)
      self.grid.addWidget(self.left, 2, 1, 1, 1)

class DrawImage(QtWidgets.QWidget):
   def __init__(self, parent):
      QtWidgets.QWidget.__init__(self, parent)
      self.setup()

   def setup(self):
      self.setFixedSize(300,300)
      p = self.palette()
      p.setColor(self.backgroundRole(), QtGui.QColor(255, 255, 255, 255)) 
      self.setPalette(p)
      self.setAutoFillBackground(True)
   
   def paintEvent(self, event):
      qp = QtGui.QPainter()
      qp.begin(self)
      pen = qp.pen()

      # outer circle
      pen.setColor(QtCore.Qt.black)
      qp.setPen(pen)
      qp.drawEllipse(75,75,150,150)

      # inner circle
      pen.setColor(QtGui.QColor(255,140,0,255))
      pen.setWidth(23)
      qp.setPen(pen)
      qp.drawEllipse(120,120,60,60)

      qp.end()

class UpBtn(QtWidgets.QPushButton):
   def __init__(self, parent):
      QtWidgets.QPushButton.__init__(self,parent)
      self.setText("Up")

class RightBtn(QtWidgets.QPushButton):
   def __init__(self, parent):
      QtWidgets.QPushButton.__init__(self,parent)
      self.setText("Right")

class DownBtn(QtWidgets.QPushButton):
   def __init__(self, parent):
      QtWidgets.QPushButton.__init__(self,parent)
      self.setText("Down")

class LeftBtn(QtWidgets.QPushButton):
   def __init__(self, parent):
      QtWidgets.QPushButton.__init__(self,parent)
      self.setText("Left")

if __name__ == "__main__":
   app = QtWidgets.QApplication(sys.argv)
   main_window = Homework3()
   app.exec_()
import sys
from PyQt5 import QtWidgets, QtCore, QtGui

class Homework3(QtWidgets.QMainWindow):
   def __init__(self):
      QtWidgets.QMainWindow.__init__(self)
      self.setup()

   def setup(self):
      # create window
      self.setWindowTitle('Homework 3')
      self.droid = Droid(self)
      self.setCentralWidget(self.droid)
      self.show()

class Droid(QtWidgets.QWidget):
   def __init__(self, parent):
      QtWidgets.QWidget.__init__(self, parent)
      self.setup()
   
   def setup(self):
      # setup buttons
      self.image = DrawImage(self)
      self.up = UpBtn(self)
      self.right = RightBtn(self)
      self.down = DownBtn(self)
      self.left = LeftBtn(self)

      # setup event listeners for buttons
      self.up.clicked.connect(self.image.up)
      self.right.clicked.connect(self.image.right)
      self.down.clicked.connect(self.image.down)
      self.left.clicked.connect(self.image.left)

      # setup grid
      self.grid = QtWidgets.QGridLayout()
      self.setLayout(self.grid)

      # setup grid widgets
      self.grid.addWidget(self.image, 2, 2, 1, 1)
      self.grid.addWidget(self.up, 1, 1, 1, 3)
      self.grid.addWidget(self.right, 2, 3, 1, 1)
      self.grid.addWidget(self.down, 3, 1, 1, 3)
      self.grid.addWidget(self.left, 2, 1, 1, 1)

class DrawImage(QtWidgets.QWidget):
   def __init__(self, parent):
      QtWidgets.QWidget.__init__(self, parent)
      self.position = "Up"
      self.setup()

   def setup(self):
      # setup canvas
      p = self.palette()
      p.setColor(self.backgroundRole(), QtGui.QColor(255, 255, 255, 255)) 
      self.setPalette(p)
      self.setAutoFillBackground(True)
      self.setFixedSize(300,300)

   def up(self):
      # up button event
      self.position = "Up"
      self.update()

   def down(self):
      # down button event
      self.position = "Down"
      self.update()
      
   def left(self):
      # left button event
      self.position = "Left"
      self.update()
      
   def right(self):
      # right button event
      self.position = "Right"
      self.update()
   
   def paintEvent(self, event):
      # create pen
      qp = QtGui.QPainter()
      qp.begin(self)
      pen = qp.pen()

      # outer circle
      pen.setColor(QtCore.Qt.black)
      qp.setPen(pen)
      qp.drawEllipse(75,75,150,150)

      # head position
      if(self.position == "Up"):
         qp.drawChord(100, 34, 100, 100, 10*16, 160*16)
      elif(self.position == "Left"):
         qp.drawChord(34, 100, 100, 100, 100*16, 160*16)
      elif(self.position == "Right"):
         qp.drawChord(167, 100, 100, 100, 1000*16, 160*16)
      elif(self.position == "Down"):
         qp.drawChord(100, 167, 100, 100, -10*16, -160*16)

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
      self.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
      self.setText("Right")

class DownBtn(QtWidgets.QPushButton):
   def __init__(self, parent):
      QtWidgets.QPushButton.__init__(self,parent)
      self.setText("Down")

class LeftBtn(QtWidgets.QPushButton):
   def __init__(self, parent):
      QtWidgets.QPushButton.__init__(self,parent)
      self.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
      self.setText("Left")

if __name__ == "__main__":
   app = QtWidgets.QApplication(sys.argv)
   main_window = Homework3()
   app.exec_()
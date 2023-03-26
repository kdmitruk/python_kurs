from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 800)
        self.playerPos = QPoint(self.width()/2,self.height()/2)


    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        brush = QBrush()
        brush.setColor(QColor(231, 236, 163))
        brush.setStyle(Qt.SolidPattern)
        painter.fillRect(self.rect(), brush)
        brush.setColor(QColor(131, 36, 163))
        painter.fillRect(QRect(self.playerPos.x()-10,self.playerPos.y()-10,20,20),brush)

        painter.end()

    def keyPressEvent(self, event):
        step=5
        if event.key() == Qt.Key_Left:
            self.playerPos.setX(self.playerPos.x()-step)
        if event.key() == Qt.Key_Right:
            self.playerPos.setX(self.playerPos.x()+step)
        if event.key() == Qt.Key_Up:
            self.playerPos.setY(self.playerPos.y()-step)
        if event.key() == Qt.Key_Down:
            self.playerPos.setY(self.playerPos.y()+step)

        if self.playerPos.x() <= 0:
            self.playerPos.setX(self.width()-1)
        if self.playerPos.x() >= self.width():
            self.playerPos.setX(0)
        if self.playerPos.y() <= 0:
            self.playerPos.setY(self.height()-1)
        if self.playerPos.y() >= self.height():
            self.playerPos.setY(0)
        self.update()

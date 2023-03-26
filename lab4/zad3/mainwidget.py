from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 800)
        self.playerPos = QPointF(self.width()/2,self.height()/2)
        self.enemyPos = QPointF(0,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateGameState)
        self.timer.start(5)

    def updateGameState(self):
        step = 1
        if self.enemyPos.x()<self.playerPos.x():
            self.enemyPos.setX(self.enemyPos.x()+step*1.5)
        else:
            self.enemyPos.setX(self.enemyPos.x()-step*1.5)
        if self.enemyPos.y()<self.playerPos.y():
            self.enemyPos.setY(self.enemyPos.y()+step*1.5)
        else:
            self.enemyPos.setY(self.enemyPos.y()-step*1.5)
        self.update()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        brush = QBrush()
        brush.setColor(QColor(231, 236, 163))
        brush.setStyle(Qt.SolidPattern)
        painter.fillRect(self.rect(), brush)
        brush.setColor(QColor(131, 36, 163))
        painter.fillRect(QRect(self.playerPos.x()-10,self.playerPos.y()-10,20,20),brush)
        brush.setColor("blue")
        painter.fillRect(QRect(self.enemyPos.x()-10,self.enemyPos.y()-10,20,20),brush)
        painter.end()

    def keyPressEvent(self, event):
        step=6
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

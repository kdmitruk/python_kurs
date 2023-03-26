from PySide2.QtWidgets import *
from PySide2.QtGui import *

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 500)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        brush = QBrush()
        brush.setColor("white")
        brush.setStyle(Qt.SolidPattern)
        print(self.rect())
        painter.fillRect(self.rect(), brush)
        painter.end()

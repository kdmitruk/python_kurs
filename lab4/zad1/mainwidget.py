from PySide2.QtWidgets import QWidget, QPushButton, QLineEdit,\
    QLabel, QVBoxLayout


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main widget")

        button = QPushButton("Press me!", self)
        button.clicked.connect(self.onButtonClicked)

        self.edit = QLineEdit(self)
        self.label = QLabel("tekst" ,self)

        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.label)
        layout.addWidget(button)


    def onButtonClicked(self):
        editText = self.edit.text()
        self.label.setText(editText)
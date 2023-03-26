from PySide2.QtWidgets import QApplication, QWidget, QPushButton
from mainwidget import MainWidget

def main():
    app = QApplication([])

    window = MainWidget()
    window.show()

    # button = QPushButton("Press me!", window)
    # button.show()

    app.exec_()


if __name__ == "__main__":
    main()
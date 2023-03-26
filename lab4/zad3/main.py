from PySide2.QtWidgets import QApplication
from mainwidget import MainWidget

def main():
    app = QApplication([])

    window = MainWidget()
    window.show()


    app.exec_()


if __name__ == "__main__":
    main()
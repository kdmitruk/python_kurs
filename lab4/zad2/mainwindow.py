from PySide2.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main widget")
        self.initializeMenu()

        self.edit = QTextEdit(self)
        self.setCentralWidget(self.edit)
        self.path = ""

    def initializeMenu(self):
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("File")
        newAction = fileMenu.addAction("New")
        openAction = fileMenu.addAction("Open")
        saveAction = fileMenu.addAction("Save")
        saveAsAction = fileMenu.addAction("Save as")
        newAction.triggered.connect(self.onNewAction)
        openAction.triggered.connect(self.onOpenAction)
        saveAction.triggered.connect(self.onSaveAction)
        saveAsAction.triggered.connect(self.onSaveAsAction)

    def onNewAction(self):
        self.edit.clear()
        self.path = ""

    def onOpenAction(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "")
        if len(path) > 0:
            file = open(path, 'r')
            data = file.read()
            self.edit.setText(data)
            self.path = path
            file.close()

    def onSaveAsAction(self):
        path,_ = QFileDialog.getSaveFileName(self, "Save file")
        if len(path) > 0:
            self.__save(path)

    def onSaveAction(self):
        if self.path == "":
            self.onSaveAsAction()
        else:
            self.__save(self.path)

    def __save(self,path):
        file = open(path, "w")
        data = self.edit.toPlainText()
        file.write(data)
        file.close()
        self.path = path


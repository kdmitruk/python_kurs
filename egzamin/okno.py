from PySide2.QtWidgets import *
from produkt import Produkt

class Okno(QWidget):
    def __init__(self):
        super().__init__()

        self.__pole_wejsciowe = QLineEdit(self)
        self.__pole_wyjsciowe = QTextEdit(self)

        self.__pole_wyjsciowe.setReadOnly(True)

        przycisk = QPushButton("Szukaj", self)
        przycisk.clicked.connect(self.szukaj_podciagu)

        uklad = QVBoxLayout(self)
        uklad.addWidget(self.__pole_wejsciowe)
        uklad.addWidget(przycisk)
        uklad.addWidget(self.__pole_wyjsciowe)

    def szukaj_podciagu(self):
        podciag = self.__pole_wejsciowe.text()
        wynik = ""
        for nazwa_produktu in Produkt.produkty.keys():
            if podciag.lower() in nazwa_produktu.lower():
                wynik += nazwa_produktu + "\n"
        self.__pole_wyjsciowe.setText(wynik)

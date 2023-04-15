from PySide2.QtWidgets import *
from uczen import Uczen

class Okno(QWidget):
    def __init__(self):
        super().__init__()
        self.__uczniowie = []

        self.__lista_przedmiotow = QComboBox(self)
        self.__lista_przedmiotow.currentTextChanged.connect(self.wybierz_przedmiot)

        self.__pole_wynikow = QTextEdit(self)

        self.__pole_wynikow.setReadOnly(True)

        przycisk_do_ustawiania_katalogu = QPushButton("Wybierz katalog", self)
        przycisk_do_ustawiania_katalogu.clicked.connect(self.wybierz_katalog)

        uklad = QVBoxLayout(self)
        uklad.addWidget(przycisk_do_ustawiania_katalogu)
        uklad.addWidget(self.__lista_przedmiotow)
        uklad.addWidget(self.__pole_wynikow)

    def wybierz_katalog(self):
        sciezka = QFileDialog.getExistingDirectory(self, "Wybierz katalog", "")
        if len(sciezka) > 0:
            self.__uczniowie = Uczen.uczniowie_z_katalogu(sciezka)

            przedmioty = set()
            for uczen in self.__uczniowie:
                przedmioty_ucznia = uczen.get_oceny().keys()
                przedmioty.update(przedmioty_ucznia)

            self.__lista_przedmiotow.clear()
            for przedmiot in przedmioty:
                self.__lista_przedmiotow.addItem(przedmiot)

    def wybierz_przedmiot(self, przedmiot):
        posortowani_uczniowie = Uczen.lista_rankingowa(self.__uczniowie, przedmiot)

        wynik = ""
        for uczen in posortowani_uczniowie:
            wynik += str(uczen) + " " + str(uczen.srednia_wazona(przedmiot)) + "\n"
        self.__pole_wynikow.setText(wynik)
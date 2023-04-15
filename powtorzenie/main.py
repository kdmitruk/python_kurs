from uczen import Uczen
from PySide2.QtWidgets import QApplication
from okno import Okno
from ocena import Ocena


def main():
    ocena1 = Ocena(3.5, 2)
    ocena2 = Ocena.utworz("4+", 1)

    pass
    #
    # uczen = Uczen("Jan", "Kowalski")
    #
    # uczen.dodaj_ocene("matematyka", ocena1)
    # uczen.dodaj_ocene("matematyka", ocena2)
    #
    # print(uczen.srednia_wazona("matematyka"))

    #uczniowie = []
    #Uczen.dodaj_przedmiot_z_pliku(uczniowie, "uczniowie/matematyka.csv")
    #Uczen.dodaj_przedmiot_z_pliku(uczniowie, "uczniowie/polski.csv")

    # uczniowie = Uczen.uczniowie_z_katalogu("uczniowie")
    # #
    # uczniowie = Uczen.lista_rankingowa(uczniowie, "matematyka")
    # #
    # for uczen in uczniowie:
    #     #uczen.zapisz_oceny_ucznia_do_pliku(uczen.get_imie()+"_"+uczen.get_nazwisko()+".csv")
    #     print(uczen, uczen.srednia_wazona("matematyka"))

    app = QApplication([])

    window = Okno()
    window.show()


    app.exec_()

if __name__ == '__main__':
    main()
from produkt import Produkt
from koszyk import Koszyk
from PySide2.QtWidgets import QApplication


def main():
    # Produkt.wczytaj_produkty("ceny.csv")
    # #print(Produkt.produkt("Cebula - za 1 kg").cena(3,2023))
    # koszyk = Koszyk()
    # koszyk.dodaj(Produkt.produkt("Cebula - za 1 kg"))
    # koszyk.dodaj(Produkt.produkt("Cebula - za 1 kg"))
    #
    # print(koszyk.roczna_stopa_inflacji(3,2015))

    app = QApplication([])

    window = Okno()
    window.show()


    app.exec_()


if __name__ == "__main__":
    main()

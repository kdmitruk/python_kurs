class Produkt:
    produkty = set()

    def __init__(self, linia):
        dane = linia.split(";")
        self.__nazwa=dane[0]
        self.__ceny=[float(cena) for cena in dane[1:]]

    def get_nazwa(self):
        return self.__nazwa

    def get_cena(self):
        return self.__cena

    @staticmethod
    def wczytaj_produkty(sciezka):
        plik = open(sciezka, "r")
        plik.readline()
        for wiersz in plik:
            Produkt.produkty.add(Produkt(wiersz))

    @staticmethod
    def produkt(nazwa):
        for produkt in Produkt.produkty:
            if produkt.__nazwa == nazwa:
                return produkt
        return None


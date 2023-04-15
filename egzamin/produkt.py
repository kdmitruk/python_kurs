class Produkt:
    def __init__(self, linia):
        dane = linia.split(";")
        self.__nazwa=dane[0]
        self.__ceny=[float(cena) for cena in dane[1:]]

    def get_nazwa(self):
        return self.__nazwa

    def get_cena(self):
        return self.__cena

class Ocena:
    mapa_ocen = {'1': 1.0, '1+': 1.5, '2': 2.0, '2+': 2.5, '3': 3.0, '3+': 3.5, '4': 4.0, '4+': 4.5, '5': 5.0,
                 '5+': 5.5, '6': 6.0}

    def __init__(self, ocena, waga):
        self.__ocena = ocena
        self.__waga = waga

    def get_ocena(self):
        return self.__ocena

    def get_waga(self):
        return self.__waga

    @staticmethod
    def utworz(napis, waga):
        if napis in Ocena.mapa_ocen:
            ocena = Ocena.mapa_ocen[napis]
            ocena = float(ocena)
            if 0.0 < waga <= 1.0:
                return Ocena(ocena, waga)
        return None
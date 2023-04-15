from ocena import Ocena
import os

class Uczen:
    def __init__(self, imie, nazwisko):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__oceny = {}

    def __str__(self):
        return self.__imie + " " + self.__nazwisko

    def get_imie(self):
        return self.__imie

    def get_nazwisko(self):
        return self.__nazwisko

    def get_oceny(self):
        return self.__oceny

    def dodaj_ocene(self, przedmiot: str, ocena: Ocena) -> None:
        if przedmiot not in self.__oceny:
            self.__oceny[przedmiot] = []
        self.__oceny[przedmiot].append(ocena)

    def srednia_arytmetyczna(self, przedmiot: str) -> float:
        if przedmiot not in self.__oceny:
            return None
        if len(self.__oceny[przedmiot]) == 0:
            return None
        suma_ocen = sum([ocena.get_ocena() for ocena in self.__oceny[przedmiot]])
        return suma_ocen / len(self.__oceny[przedmiot])

    def srednia_wazona(self, przedmiot: str) -> float:
        if przedmiot not in self.__oceny:
            return None
        if len(self.__oceny[przedmiot]) == 0:
            return None
        suma_ocen = sum([ocena.get_ocena() * ocena.get_waga() for ocena in self.__oceny[przedmiot]])
        suma_wag = sum([ocena.get_waga() for ocena in self.__oceny[przedmiot]])
        return suma_ocen / suma_wag

    @staticmethod
    def dodaj_przedmiot_z_pliku(uczniowie, sciezka):
        plik = open(sciezka, 'r')
        przedmiot = plik.readline().strip()
        for linia in plik:
            dane = linia.strip().split(',')
            imie, nazwisko = dane[:2]

            wybrany_uczen = None
            for uczen in uczniowie:
                if (uczen.__imie, uczen.__nazwisko) == (imie, nazwisko):
                    wybrany_uczen = uczen
            if wybrany_uczen == None:
                wybrany_uczen = Uczen(imie, nazwisko)
                uczniowie.append(wybrany_uczen)

            if przedmiot not in wybrany_uczen.__oceny:
                wybrany_uczen.__oceny[przedmiot] = []

            oceny = dane[2:]
            for i in range(0, len(oceny), 2):
                wybrany_uczen.__oceny[przedmiot].append(Ocena.utworz(oceny[i], float(oceny[i+1])))
        plik.close()

    def zapisz_oceny_ucznia_do_pliku(self, sciezka):
        plik = open(sciezka, 'w')
        plik.write(self.__imie + " " + self.__nazwisko + "\n")
        for przedmiot in self.__oceny.keys():
            linia = []
            linia.append(przedmiot)
            for ocena in self.__oceny[przedmiot]:
                linia.append(str(ocena.get_ocena()))
                linia.append(str(ocena.get_waga()))
            plik.write(",".join(linia) + "\n")
        plik.close()

    @staticmethod
    def lista_rankingowa(uczniowie, przedmiot):
        posortowani_uczniowie = uczniowie.copy()
        posortowani_uczniowie.sort(reverse = True, key = lambda uczen : uczen.srednia_wazona(przedmiot))
        return posortowani_uczniowie

    @staticmethod
    def uczniowie_z_katalogu(sciezka):
        uczniowie = []
        for plik in os.listdir(sciezka):
            Uczen.dodaj_przedmiot_z_pliku(uczniowie, os.path.join(sciezka, plik))
        return uczniowie




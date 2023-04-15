from produkt import Produkt
from koszyk import Koszyk

def main():
    Produkt.wczytaj_produkty("ceny.csv")
    #print(Produkt.produkt("Cebula - za 1 kg").cena(3,2023))
    koszyk = Koszyk()
    koszyk.dodaj(Produkt.produkt("Cebula - za 1 kg"))
    koszyk.dodaj(Produkt.produkt("Cebula - za 1 kg"))
    pass

if __name__ == "__main__":
    main()

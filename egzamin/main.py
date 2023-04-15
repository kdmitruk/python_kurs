from produkt import Produkt

def main():
    Produkt.wczytaj_produkty("ceny.csv")
    print(Produkt.produkt("Chleb pszenno-żytni - za 0.5 kg").get_nazwa())

if __name__ == "__main__":
    main()

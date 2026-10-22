import random

# krok 1
class Produkt:
    def __init__(self, nazwa, cena=0, liczba_sztuk=0):
        self.nazwa = nazwa
        self.cena = cena
        self.liczba_sztuk = liczba_sztuk
        self.wartosc = 0.0

    # krok 6 part 1
    def oblicz_wartosc(self):
        self.wartosc = round(self.cena * self.liczba_sztuk, 2)

# krok 2
produkty = [
    Produkt("Chleb"),
    Produkt("Masło"),
    Produkt("Kawa"),
    Produkt("Czekolada"),
    Produkt("Ręcznik"),
    Produkt("Zeszyt"),
    Produkt("Długopis"),
    Produkt("Szampon"),
]

# krok 3
for produkt in produkty:
    produkt.cena = round(random.uniform(5.00,500.00),2)
    produkt.liczba_sztuk = random.randint(1,100)

# krok 4
print("Wszystkie produkty:")
for produkt in produkty:
    print(f"{produkt.nazwa}: {produkt.cena} zł, ilość: {produkt.liczba_sztuk}")

# krok 5
n = len(produkty)
for i in range(n):
    for j in range(0,n - i - 1):
        if produkty[j].cena > produkty[j+1].cena:
            produkty[j], produkty[j+1] = produkty[j+1], produkty[j]

# krok 6 part 2
for produkt in produkty:
    produkt.oblicz_wartosc()

# krok 7
with open("magazyn.txt", "w", encoding="utf-8") as plik:
    for produkt in produkty:
        plik.write(f"{produkt.nazwa}: {produkt.cena} zł, ilość: {produkt.liczba_sztuk}, wartość {produkt.wartosc} zł\n")

# krok 8
print("\nProdukty o wartości zapasu powyżej 1000 zł:")
with open("magazyn.txt", "r", encoding="utf-8") as plik:
    for linia in plik:
        slowa = linia.split()
        wartosc = float(slowa[-2])
        if wartosc > 1000:
            print(linia.strip())

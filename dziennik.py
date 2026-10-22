import random

# krok 1
class Uczen:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.lista_ocen = []
        self.srednia = 0.0

# krok 2
uczniowie = [
    Uczen("Adam", "Nowak"),
    Uczen("Jan", "Kowalski"),
    Uczen("Piotr", "Wiśniewski"),
    Uczen("Tomasz", "Wójcik"),
    Uczen("Anna", "Kamińska")
]

# krok 3
for uczen in uczniowie:
    for _ in range(5):
        uczen.lista_ocen.append(random.randint(1,6))

# krok 4
def oblicz_srednia(uczen):
    uczen.srednia = sum(uczen.lista_ocen) / len(uczen.lista_ocen)

for uczen in uczniowie:
    oblicz_srednia(uczen)

# krok 5
print("Ranking uczniów:")
for uczen in uczniowie:
    print(f"{uczen.imie} {uczen.nazwisko}, oceny: {uczen.lista_ocen}, średnia: {uczen.srednia}")

# krok 6
n = len(uczniowie)
for i in range(n):
    for j in range(0, n - i - 1):
        if uczniowie[j].srednia < uczniowie[j+1].srednia:
            uczniowie[j], uczniowie[j+1] = uczniowie[j+1], uczniowie[j]

# krok 7
with open("uczniowie.txt", "w", encoding="utf-8") as plik:
    for i in range(len(uczniowie)):
        u = uczniowie[i]
        plik.write(f"{u.imie}, {u.nazwisko}, {u.lista_ocen}, {u.srednia}\n")

# krok 8
print("\nDane z pliku:")
with open("uczniowie.txt", "r", encoding="utf-8") as plik:
    linie = plik.readlines()
    for linia in linie:
        print(linia.strip())

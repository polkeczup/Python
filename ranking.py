import random

# krok 1
class Zawodnik:
    def __init__(self, imie, nazwisko, wynik=0):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynik = wynik

# krok 2
z1 = Zawodnik("Adam", "Nowak")
z2 = Zawodnik("Anna", "Kamińska")
z3 = Zawodnik("Piotr", "Wiśniewski")
z4 = Zawodnik("Marek", "Kowalczyk")
z5 = Zawodnik("Ewa", "Dąbrowska")
z6 = Zawodnik("Paweł", "Kaczmarek")
z7 = Zawodnik("Jan", "Kowalski")
z8 = Zawodnik("Ola", "Lewandowska")
z9 = Zawodnik("Tomasz", "Wójcik")
z10 = Zawodnik("Kamil", "Mazur")

# krok 3
z1.wynik = random.randint(0,100)
z2.wynik = random.randint(0,100)
z3.wynik = random.randint(0,100)
z4.wynik = random.randint(0,100)
z5.wynik = random.randint(0,100)
z6.wynik = random.randint(0,100)
z7.wynik = random.randint(0,100)
z8.wynik = random.randint(0,100)
z9.wynik = random.randint(0,100)
z10.wynik = random.randint(0,100)

# krok 4
zawodnicy = [z1,z2,z3,z4,z5,z6,z7,z8,z9,z10]
for zawodnik in zawodnicy:
    print(zawodnik.imie, zawodnik.nazwisko, zawodnik.wynik)

# krok 5
n = len(zawodnicy)
for i in range(n):
    for j in range(0,n - i - 1):
        if zawodnicy[j].wynik < zawodnicy[j+1].wynik:
            zawodnicy[j], zawodnicy[j+1] = zawodnicy[j+1], zawodnicy[j]

# krok 6
print(f"\nPOSORTOWANE")
for i in range(len(zawodnicy)):
    z = zawodnicy[i]
    print(f"{i+1}. {z.imie} {z.nazwisko}: {z.wynik} pkt")

# krok 7
with open("ranking.txt", "w", encoding="utf-8") as plik:
    for i in range(len(zawodnicy)):
        z = zawodnicy[i]
        plik.write(f"{i+1}. {z.imie} {z.nazwisko}: {z.wynik} pkt\n")

# krok 8
print(f"\nTRZECH NAJLEPSZYCH")
with open("ranking.txt", "r", encoding="utf-8") as plik:
    linie = plik.readlines()
    for linia in linie[:3]:
        print(linia.strip())

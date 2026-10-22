# krok 1
tekst = input("Podaj tekst do zaszyfrowania: ")

# krok 2
klucz = int(input("Podaj klucz (liczbę przesunięcia): "))

# krok 3 i krok 4
def szyfruj(tekst_wejsciowy, klucz_przesuniecia):
    zaszyfrowany = ""
    for znak in tekst_wejsciowy:
        if znak.isupper():
            nowy_znak = chr((ord(znak) - 65 + klucz_przesuniecia) % 26 + 65)
            zaszyfrowany += nowy_znak
        elif znak.islower():
            nowy_znak = chr((ord(znak) - 97 + klucz_przesuniecia) % 26 + 97)
            zaszyfrowany += nowy_znak
        else:
            zaszyfrowany += znak
    return zaszyfrowany

tekst_zaszyfrowany = szyfruj(tekst, klucz)

# krok 5
print("Tekst zaszyfrowany:", tekst_zaszyfrowany)

# krok 6
with open("cezar.txt", "w", encoding="utf-8") as plik:
    plik.write(str(klucz) + "\n")
    plik.write(tekst_zaszyfrowany)

# krok 7
with open("cezar.txt", "r", encoding="utf-8") as plik:
    odczytany_klucz = int(plik.readline())
    odczytany_tekst = plik.read()

def odszyfruj(tekst_wejsciowy, klucz_przesuniecia):
    return szyfruj(tekst_wejsciowy, -klucz_przesuniecia)

tekst_odszyfrowany = odszyfruj(odczytany_tekst, odczytany_klucz)

# krok 8
print("Tekst odszyfrowany:", tekst_odszyfrowany)

if tekst_odszyfrowany == tekst:
    print("Weryfikacja poprawna.")
else:
    print("Błąd weryfikacji.")

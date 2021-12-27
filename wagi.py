podaj="Podaj wagi elementow w kg, min 1 max 10. Zero konczy zaladunek."
error_waga="Podano zla wage elementu. Min 1kg, max 10kg. KONIEC PROGRAMU."

print(podaj)

waga_paczka= 0              # waga paczki
nr_paczka = 1               # nr paczki wyslane
puste_kg_paczka = 0         # ile pustych kg w danej paczce

suma_puste_kg_paczka = 0    # suma pustych we wszystkich paczkach

max_puste_kg_paczka = 0     # najwiecej pustych kg w paczce
nr_max_puste_kg_paczka = 1  # numer paczki z najwieksza ilosc pustych kg

waga_element = 0            # waga elementu pobrana z inta
suma_waga_element = 0       # suma kg pobranych z inta
nr_element = 0              # nr kolejnego elementu

krok=0
error=False
while True:
    krok += 1
    print("Element nr ", krok, "waga:")
    waga_element = float(input())
    if waga_element == 0:
        error = False
# print(error_waga)
        break
    if waga_element > 10:
        error=True
        print(error_waga)
        break
    if waga_element < 1:
        error = True
        print(error_waga)
        break

    suma_waga_element = round(suma_waga_element + waga_element,2)  # sumujemy wyslane kilogramy
    waga_paczka = waga_paczka + waga_element    # dodajemy wagi elementow do paczki


    if waga_paczka > 20:
        print('---------------------------------------------------------------')
        print ('Przekroczono 20kg/paczka! Jest w sumie:', waga_paczka, "do wyslania")
        print ('Aktualny nr paczki to:',  nr_paczka)

        waga_paczka = round (waga_paczka - waga_element,2)

        print('Zamykam paczke:', nr_paczka, 'zostaje w niej elementow:', waga_paczka)

        puste_kg_paczka = round( 20 - (waga_paczka),2)  # puste w danej paczce
        suma_puste_kg_paczka = round(suma_puste_kg_paczka + puste_kg_paczka,2)

        print('Puste kg w tej paczce: ', puste_kg_paczka)

        if puste_kg_paczka > max_puste_kg_paczka:
            max_puste_kg_paczka = puste_kg_paczka
            nr_max_puste_kg_paczka = nr_paczka

        nr_paczka += 1
        print('Rozpoczynam paczke:', nr_paczka)
        print('---------------------------------------------------------------')
        waga_paczka = waga_element    # te kg zostaja do next parcel
        puste_kg_paczka = 0
#   break
    if waga_paczka < 20:
        print('Aktualna waga paczki to', waga_paczka)
        print('Aktualny nr paczki to:', nr_paczka)
        puste_kg_paczka = 0
    if waga_paczka == 20:
        print('Aktualna waga paczki to', waga_paczka, "rozpoczynam next paczke")
        print('Zamykam paczke nr:', nr_paczka)
        nr_paczka += 1
        waga_paczka = 0
        puste_kg_paczka = 0
        continue

    continue

if not error:
    nr_paczka=nr_paczka-1
    print("*** Podsumowanie ***")
    print("Liczba paczek wysłanych:", nr_paczka)
    print("Liczba kilogramów wysłanych:", suma_waga_element)
    # suma_pustych = liczba paczek * 20 - liczba kilogramów wysłanych
    print("Suma pustych kilogramów: ", suma_puste_kg_paczka)
    print("Najwięcej pustych kg miała paczka nr:", nr_max_puste_kg_paczka , "a było to:", max_puste_kg_paczka)

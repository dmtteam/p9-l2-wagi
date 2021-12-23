waga_min_element=1
waga_max_element=10

waga_paczka_max=20

ile_paczek_wyslane=0
ile_element_wyslane=0

podaj="Podaj wagi elementow w kg, min 1 max 10. Zero konczy zaladunek."
error_waga="Podano zla wage elementu. Min 1kg, max 10kg. KONIEC PROGRAMU."

print(podaj)

waga_paczka=0
waga_element=0
nr_element=0
krok=0
while krok <20:
    krok +=1
    waga_element=float(input())
    if waga_element == 0:
        print(error_waga)
        print('Bye')
        break
    if waga_element > 10:
        print(error_waga)
        print('Bye')
        break
    if waga_element < 1:
        print(error_waga)
        print('Bye')
        break
    nr_element=krok
    waga_paczka=waga_element


# waga_paczka=(waga element)+
# for nr_element in range (1, nr_element+1, 1):
# waga_paczka=waga_element+

else:
    print("*** Podsumowanie ***")
    print("Liczba paczek wysłanych:")
# round dodać
    print("Liczba kilogramów wysłanych:")
# suma_pustych = liczba paczek * 20 - liczba kilogramów wysłanych
    print(("Suma pustych kilogramów: "), " ")
#
    print(("Najwięcej pustych kg miała paczka nr: "), " ", ("to było:"), " ")


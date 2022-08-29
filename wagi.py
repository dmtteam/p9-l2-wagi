enter = "Enter the weight of the elements in kg, min 1kg max 10kg. Zero completes loading."
enter_error = "The item was considered to be wrong. Min 1 kg, max 10 kg. END OF THE PROGRAM!"

print(enter)

waga_paczka = 0              # waga paczki
nr_paczka = 1               # nr paczki wyslane
puste_kg_paczka = 0         # ile pustych kg w danej paczce

suma_puste_kg_paczka = 0    # suma pustych we wszystkich paczkach

max_puste_kg_paczka = 0     # najwiecej pustych kg w paczce
nr_max_puste_kg_paczka = 1  # numer paczki z najwieksza ilosc pustych kg

waga_element = 0            # waga elementu pobrana z inta
suma_waga_element = 0       # suma kg pobranych z inta
nr_element = 0              # nr kolejnego elementu

step = 0
error = False
while True:
    step += 1
    print("Element nr ", step, "waga:")
    waga_element = float(input())
    if waga_element == 0:
        error = False
# print(enter_error)
        break
    if waga_element > 10:
        error = True
        print(enter_error)
        break
    if waga_element < 1:
        error = True
        print(enter_error)
        break
    suma_waga_element = round(suma_waga_element + waga_element, 2)  # sumujemy wyslane kilogramy
    waga_paczka = waga_paczka + waga_element    # dodajemy wagi elementow do paczki
    if waga_paczka > 20:
        print('---------------------------------------------------------------')
        print('Przekroczono 20kg/paczka! Jest w sumie:', waga_paczka, "do wyslania")
        print('Aktualny nr paczki to:',  nr_paczka)
        waga_paczka = round(waga_paczka - waga_element, 2)
        print('Zamykam paczke:', nr_paczka, 'zostaje w niej elementow:', waga_paczka)
        puste_kg_paczka = round(20 - waga_paczka, 2)  # puste w danej paczce
        suma_puste_kg_paczka = round(suma_puste_kg_paczka + puste_kg_paczka, 2)
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
    nr_paczka = nr_paczka-1
    print("*** Summary ***")
    print("Number of packages shipped:", nr_paczka)
    print("Number of kilos shipped:", suma_waga_element)
    # suma_pustych = liczba paczek * 20 - liczba kilogramów wysłanych
    print("Total empty kilos: ", suma_puste_kg_paczka)
    print("Most empty kilos was in the package number:", nr_max_puste_kg_paczka, "this was:", max_puste_kg_paczka)

enter = "Enter the weight of the elements in kg, min 1kg max 10kg. Zero completes loading."
enter_error = "The item was considered to be wrong. Min 1 kg, max 10 kg. END OF THE PROGRAM!"

print(enter)

parcel_weight = 0           # total weight of the package
parcel_number = 1           # the number of the parcel sent
parcel_empty_kilograms = 0  # how many empty kilos are left in the parcel

parcel_amount_empty_kilograms = 0       # how many empty kilos are in all parcels
max_parcel_empty_kilograms = 0          # most empty kilograms in the parcel
nr_max_parcel_empty_kilograms = 1       # parcel number with the most empty kilograms

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
    parcel_weight = parcel_weight + waga_element    # dodajemy wagi elementow do paczki
    if parcel_weight > 20:
        print('---------------------------------------------------------------')
        print('Przekroczono 20kg/paczka! Jest w sumie:', parcel_weight, "do wyslania")
        print('Aktualny nr paczki to:',  parcel_number)
        parcel_weight = round(parcel_weight - waga_element, 2)
        print('Zamykam paczke:', parcel_number, 'zostaje w niej elementow:', parcel_weight)
        parcel_empty_kilograms = round(20 - parcel_weight, 2)  # puste w danej paczce
        parcel_amount_empty_kilograms = round(parcel_amount_empty_kilograms + parcel_empty_kilograms, 2)
        print('Puste kg w tej paczce: ', parcel_empty_kilograms)
        if parcel_empty_kilograms > max_parcel_empty_kilograms:
            max_parcel_empty_kilograms = parcel_empty_kilograms
            nr_max_parcel_empty_kilograms = parcel_number
        parcel_number += 1
        print('Starting parcel no:', parcel_number)
        print('---------------------------------------------------------------')
        parcel_weight = waga_element    # te kg zostaja do next parcel
        parcel_empty_kilograms = 0
#   break
    if parcel_weight < 20:
        print('Current parcel weight is:', parcel_weight)
        print('Current parcel no is:', parcel_number)
        parcel_empty_kilograms = 0
    if parcel_weight == 20:
        print('Current parcel weight is:', parcel_weight, "Starting next parcel")
        print('I am closing the parcel no', parcel_number)
        parcel_number += 1
        parcel_weight = 0
        parcel_empty_kilograms = 0
        continue
    continue
if not error:
    parcel_number = parcel_number-1
    print("*** Summary ***")
    print("Number of packages shipped:", parcel_number)
    print("Number of kilos shipped:", suma_waga_element)
    # suma_pustych = liczba paczek * 20 - liczba kilogramów wysłanych
    print("Total empty kilos: ", parcel_amount_empty_kilograms)
    print("Most empty kilos was in the package number:", nr_max_parcel_empty_kilograms, "this was:", max_parcel_empty_kilograms)

enter = "Enter the weight of the elements in kg, min 1kg max 10kg. Zero completes loading."
enter_error = "The item was considered to be wrong. Min 1 kg, max 10 kg. END OF THE PROGRAM!"

print(enter)

parcel_weight = 0           # total weight of the package
parcel_number = 1           # the number of the parcel sent
parcel_empty_kilograms = 0  # how many empty kilos are left in the parcel

parcel_amount_empty_kilograms = 0       # how many empty kilos are in all parcels
max_parcel_empty_kilograms = 0          # most empty kilograms in the parcel
nr_max_parcel_empty_kilograms = 1       # parcel number with the most empty kilograms

element_weight = 0            # element weight taken from the int
sum_element_weight = 0       # sum of kilos taken from the int
nr_element = 0              # nr kolejnego elementu

step = 0
error = False
while True:
    step += 1
    print("Element nr ", step, "waga:")
    element_weight = float(input())
    if element_weight == 0:
        error = False
# print(enter_error)
        break
    if element_weight > 10:
        error = True
        print(enter_error)
        break
    if element_weight < 1:
        error = True
        print(enter_error)
        break
    suma_element_weight = round(sum_element_weight + element_weight, 2)  # sum od the sent items
    parcel_weight = parcel_weight + element_weight    # added weight of items to the parcel
    if parcel_weight > 20:
        print('---------------------------------------------------------------')
        print('Exceeded 20 kg in parcels! It is in total:', parcel_weight, "to be shipped")
        print('The current parcel number is:',  parcel_number)
        parcel_weight = round(parcel_weight - element_weight, 2)
        print('I close the parcel number:', parcel_number, 'there are elements in it:', parcel_weight)
        parcel_empty_kilograms = round(20 - parcel_weight, 2)  # empty kilograms in parcel
        parcel_amount_empty_kilograms = round(parcel_amount_empty_kilograms + parcel_empty_kilograms, 2)
        print('Empty kg in this parcel: ', parcel_empty_kilograms)
        if parcel_empty_kilograms > max_parcel_empty_kilograms:
            max_parcel_empty_kilograms = parcel_empty_kilograms
            nr_max_parcel_empty_kilograms = parcel_number
        parcel_number += 1
        print('Starting parcel no:', parcel_number)
        print('---------------------------------------------------------------')
        parcel_weight = element_weight    # kilograms to the next parcel
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
    print("Number of kilos shipped:", suma_element_weight)
    # sum of empty kilos = parcel number * 20 - sent kilos
    print("Total empty kilos: ", parcel_amount_empty_kilograms)
    print("Most empty kilos was in the package number:", nr_max_parcel_empty_kilograms,
          "this was:", max_parcel_empty_kilograms)

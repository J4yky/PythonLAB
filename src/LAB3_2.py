"""
Napisz skrypt, który będzie pobierał od użytkownika w pętli (np. 10 razy) imię i dopisywał
je do listy imion. Sprawdź czy użytkownik wpisuje tylko litery (imiona zwykle składają się
wyłącznie z liter :) ), a przed zapisem imienia do listy odpowiednio je sformatuj (imiona
piszemy wielką literą!). Ponadto, skrypt powinien sprawdzać, czy wprowadzone imię nie
znajduje się już na liście. Jeśli jest na liście, to powiadom o tym użytkownika. Na koniec,
niech zostanie wyświetlona cała lista zapisanych imion.
"""
listOfNames = []

for i in range(10):
    name = input("Name: ").strip()

    if name.isalpha():
        name = name.capitalize()

        if name in listOfNames:
            print(f"Name '{name}' is already on the list.")
        else:
            listOfNames.append(name)
    else:
        print("Name must be alphanumeric. Try again.")

print("\nList of Names:")
print(listOfNames)
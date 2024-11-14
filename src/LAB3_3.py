"""
Zmodyfikuj skrypt z pkt. 2 tak, żeby lista imion była uzupełniana aż do momentu, gdy
użytkownik zamiast imienia wpisze hasło np. 'koniec' (niezależnie od wielkości liter).
Wówczas lista imion zostanie posortowana rosnąco, a następnie zostanie wyświetlona na
ekranie i zapisana do pliku tekstowego (np. imiona.txt) w taki sposób, żeby każde imię z
listy było w osobnej linii pliku.
"""
listOfNames = []

print("Type 'stop' to exit")

while True:
    name = input("Name: ").strip()

    if name.lower() == 'stop':
        break
    if name.isalpha():
        name = name.capitalize()

        if name in listOfNames:
            print(f"Name '{name}' is already on the list.")
        else:
            listOfNames.append(name)
    else:
        print("Name must be alphanumeric. Try again.")

listOfNames.sort()

print("\nList of Names:")
print(listOfNames)

with open("names.txt", "w") as file:
    for name in listOfNames:
        file.write(name + "\n")
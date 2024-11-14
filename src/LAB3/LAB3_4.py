"""
Zmodyfikuj skrypt z pkt. 3 tak, żeby lista imion była inicjalizowana poprzez wczytywanie
jej z pliku tekstowego (np. imiona.txt).
"""
listOfNames = []

try:
    with open("names.txt", "r") as file:
        for line in file:
            name = line.strip().capitalize()
            if name and name.isalpha():
                listOfNames.append(name)
except FileNotFoundError:
    print("File 'names.txt' not found. List of names will start empty.")

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
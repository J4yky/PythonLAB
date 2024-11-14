"""
Uzupełnij powyższy skrypt o rozpoznawanie polskich imion żeńskich i męskich (w języku
polskim, wszystkie imiona żeńskie kończą się na literę 'a', a wśród imion męskich tylko:
Kosma, Barnaba, Bonawentura, Jarema i Kuba). W zależności od tego, czy imię jest męskie,
czy żeńskie, będzie zapisywane do odpowiedniej listy imion. Obie listy powinny zostać
posortowane i wyświetlone, a następnie zapisane do pliku binarnego (wykorzystaj
serializację – czyli moduł pickle).
"""
import pickle

listOfFemaleNames = []
listOfMaleNames = []
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

for name in listOfNames:
    if name[-1] == 'a' and name not in ['Kosmo', 'Barnaba', 'Bonawentura', 'Jarema', 'Kuba']:
        listOfFemaleNames.append(name)
    else:
        listOfMaleNames.append(name)

listOfFemaleNames.sort()
listOfMaleNames.sort()

print("\nList of female names:")
print(listOfFemaleNames)
print("\nList of male names:")
print(listOfMaleNames)

try:
    with open("names.pkl", "wb") as file:
        pickle.dump(listOfFemaleNames, file)
        pickle.dump(listOfMaleNames, file)
except Exception as e:
    print("ERROR while saving lists: ", e)
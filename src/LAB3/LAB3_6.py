"""
Ostatnia modyfikacja... czyli inicjalizacja obu list imion (imiona męskie i żeńskie) poprzez
odczyt z pliku binarnego (deserializacja!).
"""
import pickle

listOfFemaleNames = []
listOfMaleNames = []
listOfNames = []

try:
    with open("names.pkl", "rb") as file:
        female_names = pickle.load(file)
        male_names = pickle.load(file)
        for line in female_names + male_names:
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
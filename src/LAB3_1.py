"""
Napisz skrypt, który będzie pobierał od użytkownika cyfrę i wyświetlał ją słownie, np. 1 →
jeden, 2 → dwa itd. (wykorzystaj w tym celu słownik!).
"""
dictionary = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five",
              6:"six", 7:"seven", 8:"eight", 9:"nine", 0:"zero"}
question = int(input("Enter a number: "))
print(dictionary[question])
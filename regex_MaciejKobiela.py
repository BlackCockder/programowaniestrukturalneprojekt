import re
with open(input("Podaj nazwe pliku tekstowego: "), "r") as opened_file:
    print(re.findall(r'\b\w{'+input("Podaj minimalna liczbe znakow slowa: ")+r',}\b', opened_file.read()))
    
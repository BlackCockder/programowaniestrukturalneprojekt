import pickle
import re

GLOBAL_ERROR_LINE_ARRAY = []
GLOBAL_WORKERS_ARRAY = []


class Pracownik:

    def __init__(self, imie: str, nazwisko: str, miejsce_pracy: str):
        self.imie = imie
        self.nazwisko = nazwisko
        self.miejsce_pracy = miejsce_pracy

    def przedstaw_sie(self):

        print(f"Nazywam się {self.imie} {self.nazwisko}. Pracuję w {self.miejsce_pracy}")


class Policjant(Pracownik):
    def __init__(self, imie: str, nazwisko: str):
        super().__init__(imie, nazwisko, "komisariat")

    def przedstaw_sie(self):
        # Nadpisuje metode przedstw_sie w celu zmodyfikowania printa
        print(f"Nazywam się {self.imie} {self.nazwisko}. Pracuję {"na komisariacie" if self.miejsce_pracy == "komisariat" else "brak danych"}.")


class Lekarz(Pracownik):
    def __init__(self, imie: str, nazwisko: str):
        super().__init__(imie, nazwisko, "szpital")

    def przedstaw_sie(self):
        # Nadpisuje metode tak samo jak dla klasy Policjant
        print(f"Nazywam się {self.imie} {self.nazwisko}. Pracuję {"w szpitalu" if self.miejsce_pracy == "szpital" else "brak danych"}.")


def worker_file_manage(filename):
    try:
        with open(filename, 'r') as f:
            for i, line in enumerate(f, start=1):

                line = line.strip()

                if not line:
                    continue

                columns = line.split(' ')

                # Tutaj mialbyc elemet funkcji ktory by laczyl dwuczlonowe elementy kolumny polaczone znakiem '"'.
                # Niestety nie podolalem wyzwaniu.
                # Zeby to zrobic, algorytm wygladalby tak:
                # 1. Sprawdzic dla kazdej kolumny czy pierwszym jej charem jest ".
                # 2. Jesli tak, to od tej kolumny sprawdzac czy reszta kolumn zawiera char " na swoim koncu.
                # 3. Jesli tak, skleic te kolumny w postaci kolumna inicjujaca algrotym +
                #   kolumny pomiedzy + kolumna konczonca algorytm.
                # 4. metoda .pop() wyrzucic z tablicy kolumn wykorzystane kolumny, zostawic inicjujaca sklejona.
                # Wtedy ostatnia pozycja w pracownicy.txt pliku poluczylaby sie jako poprawny pracownik.
                # A no i poniewaz bylby to substring to ten checker ponizej by go jeszcze usuwal.
                # Zostawiam ten checker bo w sumie dziala, ale nie zastepuje algorytmu:
                substingchecker = r'"'
                for column in columns:
                    if re.search(substingchecker, columns[columns.index(column)]) is not None:
                        columns[columns.index(column)].translate({ord('"'): None}).translate({ord(' '): None})

                if len(columns) == 3:
                    tempworker = Pracownik(columns[0], columns[1], columns[2])
                    GLOBAL_WORKERS_ARRAY.append(tempworker)
                elif len(columns) > 3:
                    GLOBAL_ERROR_LINE_ARRAY.append(f"linia nr {i} ma wiecej niz 3 kolumny")
                else:
                    GLOBAL_ERROR_LINE_ARRAY.append(f"linia nr {i} ma mniej niz 3 kolumny")

        return True

    except FileNotFoundError:

        print("Nie ma takiego pliku, podaj poprawną nazwę pliku")

        return None


if __name__ == "__main__":

    # Czesc obowiazkowa zadania
    policjant = Policjant("Jan", "Kowalski")
    lekarz = Lekarz("Jan", "Kowalski")
    policjant.przedstaw_sie()
    lekarz.przedstaw_sie()

    workerFilePath = input("Podaj plik do otworzenia: ")

    # Czesc nieobowiazkowa
    while True:
        workerFile = worker_file_manage(workerFilePath)

        if workerFile:
            pickle_file = 'pracownicy.pkl'

            for n in GLOBAL_WORKERS_ARRAY:
                GLOBAL_WORKERS_ARRAY[GLOBAL_WORKERS_ARRAY.index(n)].przedstaw_sie()

            try:

                with open(pickle_file, 'xb') as return_file:
                    pickle.dump(GLOBAL_WORKERS_ARRAY, return_file)

            except FileExistsError:

                while True:

                    decision = input("Plik juz istnieje, czy chcesz go nadpisac? (podaj Y jesli tak, N jesli nie)")

                    if decision == "Y" or decision == "N":

                        if decision == "Y":

                            with open(pickle_file, 'wb') as return_file:
                                pickle.dump(GLOBAL_WORKERS_ARRAY, return_file)

                            break
                        else:

                            break
                    else:

                        print("Niepoprawny wybor, wprowadz jeszcze raz")

            for n in GLOBAL_ERROR_LINE_ARRAY:
                print(GLOBAL_ERROR_LINE_ARRAY[GLOBAL_ERROR_LINE_ARRAY.index(n)])

            break
        else:

            workerFilePath = input("Podaj poprawny plik: ")

            if not workerFilePath:

                break
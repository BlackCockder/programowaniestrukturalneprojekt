import random
import math


class Calculations:
    def __init__(self):
        self.needleLength = float(input("Podaj dlugosc igly: "))
        self.wrapLength = float(input("Podaj dlugosc paska: "))
        self.repetitionTimes = float(input("Podaj ilosc powtorzen: "))
        self.results = "Error, calculations did not change results variable"

    def calculate(self):
        angle = random.uniform(0, math.pi / 2)
        instance = random.uniform(0, self.wrapLength)
        right = instance + (self.needleLength / 2) * math.cos(angle)
        left = instance - (self.needleLength / 2) * math.cos(angle)
        return left < 0 or right > self.wrapLength

    def calculate_alternative(self):
        t = self.wrapLength
        length = self.needleLength
        fst = (2 * length) / (t * math.pi)
        scnd = 2 / (t * math.pi)
        rd3 = (math.sqrt(math.pow(length, 2) - math.pow(t, 2)) + t * math.asin(t / length))
        return str(fst - scnd * rd3 + 1)


def main():
    calculations = Calculations()
    if calculations.needleLength > calculations.wrapLength:
        print("Igla jest dluzsza niż pasek, prawdopodobienstwo z drugiego wzrou: " + calculations.calculate_alternative())
    else:
        successes = 0.0
        for i in range(int(calculations.repetitionTimes)):
            if calculations.calculate():
                successes = successes + 1
        print("Wynik z wyliczen powtorzeniowych dla n'tych operacji: " + str(successes / calculations.repetitionTimes))
        print("Wynik ze wzoru: " + str((2 * calculations.needleLength) / (calculations.wrapLength * math.pi)))


main()

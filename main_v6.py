# Projekt rovnica na výpočet koreňa lineárnej rovnice
# Objektové riešenie zakladna verzia bez overenia vstupu
from math import isinf
from math import isnan


class Rovnica:

    inf, nan = float("inf"), float("nan")

    def __init__(self, koefA: float = 1.0, koefB: float = 1.0):
        self.a: float = koefA
        self.b: float = koefB

    def __str__(self) -> str:
        return f"{self.a}x + {self.b} = 0"

    def dajRiesenie1(self) -> float | None:
        if self.a != 0.0:
            return -self.b / self.a
        else:
            return None

    def vypisRiesenie1(self) -> None:
        vyries = self.dajRiesenie1()
        if vyries is not None:
            print(f"Rovnica má koreň:{vyries:.2f}")
        elif self.b == 0:
            print("Rovnica má veľa riešení")
        else:
            print("Rovnica nemá žiadne riešenie")

    def dajRiesenie(self) -> float:
        if self.a != 0:
            riesenie: float = -self.b / self.a
        else:
            if self.b == 0.0:
                riesenie = Rovnica.inf
            else:
                riesenie = Rovnica.nan
        return riesenie

    def vypisRiesenie(self) -> None:
        vyries = self.dajRiesenie()
        if isinf(vyries):
            print("Rovnica má veľa riešení")
        elif isnan(vyries):
            print("Rovnica nemá žiadne riešenie")
        else:
            print(f"Rovnica má koreň:{vyries:.2f}")


Prva = Rovnica(0, 0)
Prva.vypisRiesenie()
Prva.vypisRiesenie1()


# def getNumber(koeficient: str) -> float:
#    while True:
#        try:
#            cislo: float = float(input("Zadaj koeficient " + f"{koeficient}" + ":"))
#            return cislo
#        except ValueError:  # ak prevod zlyhal, zachyt vynimku a spracuj ju
#            print("Zadana hodnota koeficientu nie je cislom!")


# print("Zadaj koeficienty lineárnej rovnice: ax + b = 0")
# a: float = getNumber("a")
# b: float = getNumber("b")
# print(f"Rovnica {a}x + {b} = 0",end=' ')

# pokúsime sa vypočítať koreň a testujeme, či sa nebude deliť nulou
# try:
#    koren: float = -b / a + 0.0  # pripočítame 0.0 aby sa neukazovalo znamienko -0
# except ZeroDivisionError:  # ak bolo zachytené delenie nulou, vyriešime...
#   if b == 0.0:
#        print("má veľa riešení.")
#    else:
#        print("nemá riešenie")
# else:  # výnimka nebola vyhodená, existuje koreň
#    print(f"má koreň:{koren:.2f}")

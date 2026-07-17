# Projekt rovnica na výpočet koreňa lineárnej rovnice
# Ošetrenie číselného vstupu nekonečným cyklom vo vnutri funkcie s parametrami min a max cislo a nula (ano/nie)
def getNumber(popis: str = "Zadaj číslo:",najmenej: float = -100.0,najviac: float = 100.0, nulaPovolena: bool = True) -> float:
    while True:
        try:
            cislo: float = float(input(f"{popis} ∊ <{najmenej};{najviac}> nula je {'povolená' if nulaPovolena==True else 'zakázaná'}"+ ":"))
            if najmenej < cislo < najviac:
                if not nulaPovolena and cislo == 0.0:
                    raise ZeroDivisionError("Nula nie je povolena")
            else:
                raise ArithmeticError("Mimo intervalu")
        except ValueError:  # ak prevod zlyhal, zachyt vynimku a spracuj ju
            print("Zadana hodnota koeficientu nie je cislom!")
        except ArithmeticError:
            print("Zadana hodnota nie je z intervalu!")
        except ZeroDivisionError:
            print("Nula nie je povolená!")
        else:
            return cislo


print("Zadaj koeficienty lineárnej rovnice: ax + b = 0")
a: float = getNumber("Zadaj koeficient a")
b: float = getNumber("Zadaj koeficient b")
print(f"Rovnica {a}x + {b} = 0", end=" ")

# pokúsime sa vypočítať koreň a testujeme, či sa nebude deliť nulou
try:
    koren: float = -b / a + 0.0  # pripočítame 0.0 aby sa neukazovalo znamienko -0
except ZeroDivisionError:  # ak bolo zachytené delenie nulou, vyriešime...
    if b == 0.0:
        print("má veľa riešení.")
    else:
        print("nemá riešenie")
else:  # výnimka nebola vyhodená, existuje koreň
    print(f"má koreň:{koren:.2f}")

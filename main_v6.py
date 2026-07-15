# Projekt rovnica na výpočet koreňa lineárnej rovnice
# Ošetrenie číselného vstupu nekonečným cyklom vo vnutri funkcie s parametrami
def getNumber(koeficient: str) -> float:
    while True:
        try:
            cislo: float = float(input("Zadaj koeficient " + f"{koeficient}" + ":"))
            return cislo
        except ValueError:  # ak prevod zlyhal, zachyt vynimku a spracuj ju
            print("Zadana hodnota koeficientu nie je cislom!")


print("Zadaj koeficienty lineárnej rovnice: ax + b = 0")
a: float = getNumber("a")
b: float = getNumber("b")
print(f"Rovnica {a}x + {b} = 0",end=' ')

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

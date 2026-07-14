# Projekt rovnica na výpočet koreňa lineárnej rovnice
# Ošetrenie číselného vstupu nekonečným cyklom vo vnutri funkcie bez parametrov
def getNumber() -> int:
    while True:
        try:
            cislo: float = float(input("Zadaj koeficient = "))
            return cislo
        except ValueError:  # ak prevod zlyhal, zachyt vynimku a spracuj ju
            print("Nebolo zadane cislo!")


print("Zadaj koeficienty lineárnej rovnice: ax + b=0")
a = getNumber()
b = getNumber()
print(f"Rovnica ma tvar: {a}x + {b} = 0")

# pokúsime sa vypočítať koreň a testujeme, či sa nebude deliť nulou
try:
    koren: float = -b / a + 0.0  # pripočítame 0.0 aby sa neukazovalo znamienko -0
except ZeroDivisionError:  # ak bolo zachytené delenie nulou, vyriešime...
    if b == 0.0:
        print("Rovnica má veľa riešení.")
    else:
        print(f"Rovnica nemá riešenie")
else:  # výnimka nebola vyhodená, existuje koreň
    print(f"Rovnica má koreň:{koren:.2f}")

# Projekt rovnica na výpočet koreňa lineárnej rovnice
# Ošetrenie delenia nulou výninkou
print("Zadaj koeficienkty lineárnej rovnice: ax + b=0")
try:
    # pokus sa previest vstup na realne cislo
    a: float = float(input("Koeficient a = "))
except ValueError:  # ak prevod zlyhal, zachyt vynimku a spracuj ju
    print("Nebolo zadane cislo!")
    exit()  # skonci program

try:
    b: float = float(input("Koeficient b = "))
except ValueError:
    print("Nebolo zadane cislo!")
    exit()  # skonci program

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

# Projekt rovnica na výpočet koreňa lineárnej rovnice
# Ošetrenie kontroly vstupu výnimkou
print("Zadaj koeficienkty lineárnej rovnice: ax + b=0")
try:
    a: float = float(input("Koeficient a = "))  # pokus sa previest vstup na realne cislo
except ValueError:  # ak prevod zlyhal, zachyt vynimku a spracuj ju
    print("Nebolo zadane cislo!")
    exit()  # skonci program

try:
    b: float = float(input("Koeficient b = "))  # pokus sa previest vstup na realne cislo
except ValueError:  # ak prevod zlyhal, zachyt vynimku a spracuj ju
    print("Nebolo zadane cislo!")
    exit()  # skonci program

print(f"Rovnica ma tvar: {a}x + {b} = 0")
if a == 0.0:
    if b == 0.0:
        print("Rovnica má veľa riešení.")
    else:
        print(f"Rovnica nemá riešenie")
else:
    koren: float = -b / a + 0.0  # pripočítame 0.0 aby sa neukazovalo znamienko -0
    print(f"Rovnica má koreň:{koren:.2f}")

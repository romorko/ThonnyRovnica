# Projekt rovnica na výpočet koreňa lineárnej rovnice
print("Zadaj koeficienkty lineárnej rovnice: ax + b=0")
a: float = float(input("Koeficient a = "))
b: float = float(input("Koeficient b = "))
print(f"Rovnica ma tvar: {a}x + {b} = 0")
koren:float = -b/a
print(f'Koren rovnice x={koren:.2f}')

# Projekt rovnica na výpočet koreňa lineárnej rovnice
# Objektové riešenie zakladna verzia bez overenia vstupu pridaný docstring a statická metóda nan získanie vstupu
# Upravený konštruktor

import random


def get_number(
    popis: str = "Zadaj číslo:",
    najmenej: float = -100.0,
    najviac: float = 100.0,
    nulaPovolena: bool = True,
) -> float:
    """Získava od uživateľa vstupnú hodnotu - reálne číslo zo zadaného intervalu aobmedzením nuly

    Parametre:
        popis(str): textový reťazec, ktorý sa zobrazí uživateľovi
        najmenej(float): najmenšia možná zadaná hodnota
        najviac(float): najväčšia možná zadaná hodnota
        nulaPovolena(bool): či je možné zadať nulu (True/False)
    Návratová hodnota:
        cislo(float): uživateľom zadané číslo spĺňajúce podmienky
    Výnimky:
        ValueError: ak sa zadaný vstup nedá previesť na číslo
        ArithmeticError: ak zadaná hodnota nie je z požadovaného intervalu
        ZeroDivisionError: ak bola zadaná nula, ale nebola povolená

    """
    while True:
        try:
            cislo: float = float(
                input(
                    f"{popis} ∊ <{najmenej};{najviac}> nula je {'povolená' if nulaPovolena==True else 'zakázaná'}"
                    + ":"
                )
            )
        except ValueError:
            print("Zadaná hodnota nie je číslo!")
            continue

        if not najmenej <= cislo <= najviac:
            print("Zadaná hodnota nie je z intervalu!")
            continue

        if not nulaPovolena and cislo == 0.0:
            print("Nula nie je povolená!")
            continue
        return cislo


class Rovnica:

    def __init__(self, koef_A: float, koef_B: float):
        """Ak boli koeficienty zadané použije ich, v opačnom prípade si ich vypýta alebo vygeneruje
        Parametre:
            koefA(float): koeficient a
            koefB(float): koeficient b
        """
        self.a: float = koef_A
        self.b: float = koef_B

    def __str__(self) -> str:
        """Vypíše tvar lineárnej rovnice

        Parametre:
        Návratová hodnota:

            reťazec popisujúci lineárnu rovnicu
        """
        znamienko = "+" if self.b >= 0 else "-"
        return f"{self.a:>6.2f}x {znamienko} {abs(self.b):>5.2f} = 0"

    @staticmethod
    def generuj_koeficient(najmensi: int = -10, najvacsi: int = 10) -> float:
        """Vygeneruje nahodné číslo z daného rozsahu
        Parametre:
            najmensi(int): minimalna generovana hodnota
            najvacsi(int): maximalna generovana hodnota
        Návratová hodnota:
            vygenerované float číslo z daného intervalu
        """
        return round(random.uniform(najmensi, najvacsi), 2)

    def daj_riesenie(self) -> tuple[str, float | None]:
        """Vracia nticu s informáciou o počte koreňov a samotný koreň
        Parametre:
        Návratová hodnota:
            tuple(str,float|None):prvá položka obsahuje text a druhá koreň alebo None
        """
        if self.a != 0:
            return ("koren", -self.b / self.a)
        else:
            if self.b == 0.0:
                return ("vela", None)
            else:
                return ("ziadne", None)

    def vypis_riesenie(self) -> None:
        """Vypíše informáciu o počte koreňov a hodnotu koreňa"""
        match self.daj_riesenie():
            case ("koren", x):
                print(f"Rovnica {self} má koreň:{x:5.2f}")
            case ("vela", _):
                print(f"Rovnica {self} má veľa riešení")
            case ("ziadne", _):
                print(f"Rovnica {self} nemá žiadne riešenie")


def zadaj_rovnicu() -> Rovnica:
    k1 = get_number("Zadaj koeficient a:", -10, 10, False)
    k2 = get_number("Zadaj koeficient b:", -10, 10, False)
    return Rovnica(k1, k2)


def generuj_rovnicu() -> Rovnica:
    k1 = Rovnica.generuj_koeficient()
    k2 = Rovnica.generuj_koeficient()
    return Rovnica(k1, k2)


def generuj_rovnice(pocet: int) -> list[Rovnica]:
    """Vygeneruje zadany pocet linearnych rovnic
    Parametre:
        pocet(int):kolko rovnic sa vygeneruje
    Navratova hodnota:
        list:zoznam vygenerovanych rovnic
    """
    rovnice = []
    for _ in range(pocet):
        rovnice.append(generuj_rovnicu())
    return rovnice


def main():
    R1 = Rovnica(2, 10)
    R2 = zadaj_rovnicu()
    R3 = generuj_rovnicu()
    R1.vypis_riesenie()()
    R2.vypis_riesenie()()
    R3.vypis_riesenie()()
    for index, rovnica in enumerate(generuj_rovnice(5)):
        print(index + 1, end=". ")
        rovnica.vypis_riesenie()()


if (
    __name__ == "__main__"
):  # aby sa nespustilo pri importe, ale len pri priamom spustení
    main()

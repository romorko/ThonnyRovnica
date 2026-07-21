# Projekt rovnica na výpočet koreňa lineárnej rovnice
# Objektové riešenie zakladna verzia bez overenia vstupu pridaný docstring a statická metóda nan získanie vstupu
# Upravený konštruktor
from math import isinf, isnan
from random import randint


class Rovnica:

    inf, nan = float("inf"), float("nan")

    @staticmethod
    def getNumber(
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
                if najmenej <= cislo <= najviac:
                    if not nulaPovolena and cislo == 0.0:
                        raise ZeroDivisionError("Nula nie je povolena")
                else:
                    raise ArithmeticError("Mimo intervalu")
            except ValueError:
                print("Zadana hodnota koeficientu nie je cislom!")
            except ZeroDivisionError:
                print("Nula nie je povolená!")
            except ArithmeticError:
                print("Zadana hodnota nie je z intervalu!")
            else:
                return cislo

    @staticmethod
    def generujKoeficient(najmensi: int = -10, najvacsi: int = 10) -> float:
        """Vygeneruje nahodné číslo z daného rozsahu
        Parametre:
            najmensi(int): minimalna generovana hodnota
            najvacsi(int): maximalna generovana hodnota
        Návratová hodnota:
            vygenerované float číslo z daného intervalu
        """
        return float(randint(najmensi, najvacsi))

    @classmethod
    def generujRovnice(cls, pocet: int) -> list:
        """Vygeneruje zadany pocet linearnych rovnic
        Parametre:
            pocet(int):kolko rovnic sa vygeneruje
        Navratova hodnota:
            list:zoznam vygenerovanych rovnic
        """
        rovnice = []
        for _ in range(pocet):
            rovnice.append(cls(generuj=True))
        return rovnice
    
    def __init__(
        self,
        koefA: float | None = None,
        koefB: float | None = None,
        *,
        generuj: bool = False,
    ):
        """Ak boli koeficienty zadané použije ich, v opačnom prípade si ich vypýta alebo vygeneruje
        Parametre:
            koefA(float): koeficient a
            koefB(float): koeficient b
            generuj(bool): určuje, či sa majú nezadané hodnoty generovať

        """
        if not generuj:
            self.a = (
                self.getNumber("Zadaj koeficient a:", -10, 10, False)
                if koefA is None
                else koefA
            )
            self.b = (
                self.getNumber("Zadaj koeficient b:", -10, 10, True)
                if koefB is None
                else koefB
            )
        else:
            self.a = self.generujKoeficient() if koefA is None else koefA
            self.b = self.generujKoeficient() if koefB is None else koefB

    def __str__(self) -> str:
        """Vypíše tvar lineárnej rovnice

        Parametre:
        Návratová hodnota:

            reťazec popisujúci lineárnu rovnicu
        """
        znamienko = "+" if self.b >= 0 else "-"
        return f"{self.a:>6}x {znamienko} {abs(self.b):>5} = 0"

        #     def dajRiesenie1(self) -> float | None:
        #         """Vypočíta riešenie lineárnej rovnice
        #
        #         Parametre:
        #         Návratová hodnota:
        #             float: koreň lineárnej rovnice
        #             None: ak funkcia nemá riešenie alebo ich má veľa
        #
        #         """
        #         if self.a != 0.0:
        #             return -self.b / self.a
        #         else:
        #             return None
        #
        #     def vypisRiesenie1(self) -> None:
        #         """Vypiše riešenie lineárnej rovnice na obrazovku
        #
        #         Parametre:
        #         Návratová hodnota:
        #
        #         """
        #         vyries = self.dajRiesenie1()
        #         if vyries is not None:
        #             print(f"Rovnica {self} má koreň:{vyries:.2f}")
        #         elif self.b == 0:
        #             print(f"Rovnica {self} má veľa riešení")
        #         else:
        #             print(f"Rovnica {self} nemá žiadne riešenie")

        #     def dajRiesenie(self) -> float:
        #         if self.a != 0:
        #             riesenie: float = -self.b / self.a
        #         else:
        #             if self.b == 0.0:
        #                 riesenie = Rovnica.inf
        #             else:
        #                 riesenie = Rovnica.nan
        #         return riesenie
        #
        #     def vypisRiesenie(self) -> None:
        #         vyries = self.dajRiesenie()
        #         if isinf(vyries):
        #             print(f"Rovnica {self} má veľa riešení")
        #         elif isnan(vyries):
        #             print(f"Rovnica {self} nemá žiadne riešenie")
        #         else:
        #             print(f"Rovnica {self} má koreň:{vyries:.2f}")

    def dajRiesenie(self) -> tuple[str, float | None]:
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

    def vypisRiesenie(self) -> None:
        """Vypíše informáciu o počte koreňov a hodnotu koreňa"""
        match self.dajRiesenie():
            case ("koren", x):
                print(f"Rovnica {self} má koreň:{x:5.2f}")
            case ("vela", _):
                print(f"Rovnica {self} má veľa riešení")
            case ("ziadne", _):
                print(f"Rovnica {self} nemá žiadne riešenie")


if (
    __name__ == "__main__"
):  # aby sa nespustilo pri importe, ale len pri priamom spustení
    #     Prva = Rovnica(10, 27)
    #     Druha = Rovnica(10)
    #     Tretia = Rovnica()
    #     Stvrta = Rovnica(generuj=True)
    #     Piata = Rovnica(4, generuj=True)
    #     Prva.vypisRiesenie()
    #     Druha.vypisRiesenie()
    #     Tretia.vypisRiesenie()
    #     Stvrta.vypisRiesenie()
    #     Piata.vypisRiesenie()
    for i in Rovnica.generujRovnice(10):
        i.vypisRiesenie()

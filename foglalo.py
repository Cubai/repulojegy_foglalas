from abc import ABC, abstractmethod

# Szülőosztály mindenféle járathoz
class Jarat(ABC):
    def __init__(self, szam, cel, ar):
        self.szam = szam
        self.cel = cel
        self.ar = ar

    @abstractmethod
    def info(self):
        pass

# Belföldi járat osztály
class BelfoldiJarat(Jarat):
    def __init__(self, szam, cel, ar):
        super().__init__(szam, cel, ar)

    def info(self):
        return f"Belföldi | {self.szam} - {self.cel} | Ár: {self.ar} Ft"

# Nemzetközi járat osztály
class NemzetkoziJarat(Jarat):
    def __init__(self, szam, cel, ar):
        super().__init__(szam, cel, ar)

    def info(self):
        return f"Nemzetközi | {self.szam} - {self.cel} | Ár: {self.ar} Ft"

# Jegy foglalás osztály
class JegyFoglalas:
    def __init__(self, azonosito, jarat, nev):
        self.azonosito = azonosito
        self.jarat = jarat
        self.nev = nev

    def info(self):
        return f"{self.azonosito}: {self.nev} - {self.jarat.info()}"

# Légitársaság, ami tárolja a járatokat és foglalásokat
class Legitarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []
        self.foglalasok = []

    def hozzaad_jarat(self, j):
        self.jaratok.append(j)

    def uj_foglalas(self, szam, nev):
        for j in self.jaratok:
            if j.szam == szam:
                uj_id = len(self.foglalasok) + 1
                f = JegyFoglalas(uj_id, j, nev)
                self.foglalasok.append(f)
                return f"Foglalás sikeres! Ár: {j.ar} Ft"
        else:
            return "Nem létező járatszám :("

    def lemond_foglalas(self, azonosito):
        for f in self.foglalasok:
            if f.azonosito == azonosito:
                self.foglalasok.remove(f)
                return "Foglalás törölve."
        return "Nem található ilyen azonosító."

    def mutat_foglalasok(self):
        if len(self.foglalasok) == 0:
            return "Jelenleg nincs egyetlen foglalás sem."
        else:
            szoveg = ""
            for f in self.foglalasok:
                szoveg += f.info() + "\n"
            return szoveg.strip()

# Főmenü és programindítás
def main():
    legitars = Legitarsasag("Pelda Légitársaság")
    legitars.hozzaad_jarat(BelfoldiJarat("J200J", "Debrecen", 9000))
    legitars.hozzaad_jarat(BelfoldiJarat("F300F", "Pecs", 10000))
    legitars.hozzaad_jarat(NemzetkoziJarat("N400N", "Helsinki", 35000))

    # Kezdő foglalások
    legitars.uj_foglalas("J200J", "Nap Pali")
    legitars.uj_foglalas("J200J", "Pum Pál")
    legitars.uj_foglalas("F300F", "Kukor Ica")
    legitars.uj_foglalas("N400N", "Toth Jozsef")
    legitars.uj_foglalas("N400N", "Szabó Anna")
    legitars.uj_foglalas("N400N", "Szabó Pál")

    while True:
        print("\n=== Repülőjegy foglaló rendszer ===")
        print("1. Új jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások megtekintése")
        print("0. Kilépés")
        valasz = input("Add meg a választott művelet számát: ")

        if valasz == "1":
            print("\nElérhető járatok:")
            for j in legitars.jaratok:
                print(j.info())
            szam = input("Melyik járatszámra foglalsz?: ").strip()
            nev = input("Utas neve: ").strip()

            if szam == "" or nev == "":
                print("Nem adtál meg minden adatot!")
            else:
                eredmeny = legitars.uj_foglalas(szam, nev)
                print(eredmeny)

        elif valasz == "2":
            try:
                az = int(input("Add meg a foglalás azonosítóját (szám): "))
                print(legitars.lemond_foglalas(az))
            except:
                print("Hiba: csak számot adj meg!")

        elif valasz == "3":
            print("\nFoglalások listája:")
            print(legitars.mutat_foglalasok())

        elif valasz == "0":
            print("Viszlát!")
            break
        else:
            print("Nem jó választás, próbáld újra.")

if __name__ == "__main__":
    main()

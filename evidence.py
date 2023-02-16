from vstupni_funkce import vstup_cisel, vstup_string


class Pojisteni:

    def __init__(self, jmeno=None, prijmeni=None, vek=None, telefon=None):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return "{} {} {} {}".format(self.jmeno.capitalize(), self.prijmeni.capitalize(), self.vek, self.telefon)

    def novy_pojistenec(self):
        pojisteni = []
        while True:
            print("\n1. Přidat nového pojištěného")
            print("2. Vypsat všechny pojištěné")
            print("3. Vyhledat pojistného podle jména a příjmení")
            print("4. Konec\n")
            volba = input("Vyberte si akci: ")
            if volba == "1":
                pojisteni.append(self.vytvor_pojisteneho())
            elif volba == "2":
                self.vypis_pojistenych(pojisteni)
            elif volba == "3":
                self.vyhledej_pojisteneho(pojisteni)
            elif volba == "4":
                print("Děkujeme za použití našeho programu.")
                break
            else:
                print("\nNeplatná volba\n")

    @staticmethod
    def vytvor_pojisteneho():
        jmeno = vstup_string("\nZadejte prosím vaše jméno: ").lower()
        prijmeni = vstup_string("Zadejte prosím vaše příjmení: ").lower()
        vek = vstup_cisel("Zadejte prosím vaš věk: ")
        telefon = vstup_cisel("Zadejte prosím vaše číslo: ")
        return Pojisteni(jmeno, prijmeni, vek, telefon)

    @staticmethod
    def vypis_pojistenych(pojisteni):
        for pojisteny in pojisteni:
            print(pojisteny)

    @staticmethod
    def vyhledej_pojisteneho(pojisteni):
        jmeno = vstup_string("Zadej jméno: ").lower()
        prijmeni = vstup_string("Zadej příjmení: ").lower()
        for pojisteny in pojisteni:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                print(pojisteny)
            else:
                print("Uživatel neexistuje")

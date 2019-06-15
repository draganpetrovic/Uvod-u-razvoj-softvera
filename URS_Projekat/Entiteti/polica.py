from Entiteti.identifikacija import Identifikacija

class Polica(Identifikacija):
    
    def __init__(self, oznaka, red, kolona, pozicija, duzina, sirina, visina, sekcija):
        super().__init__(oznaka)
        self.red = red
        self.kolona = kolona
        self.pozicija = pozicija
        self.duzina = duzina
        self.sirina = sirina
        self.visina = visina
        self.sekcija = sekcija
        # if self.red < 0:
        #     raise ValueError("Vrijednost mora biti veca od 0!")
        # if self.kolona < 0:
        #     raise ValueError("Vrijednost mora biti veca od 0!")
        # if self.duzina < 0:  
        #     raise ValueError("Vrijednost mora biti veca od 0!")
        # if self.sirina < 0:
        #     raise ValueError("Vrijednost mora biti veca od 0!")
        # if self.visina < 0:
        #     raise ValueError("Vrijednost mora biti veca od 0!")

    def __str__(self):
        return f"{self.oznaka};{self.red};{self.kolona};{self.pozicija};{self.duzina};{self.sirina};{self.visina};{self.sekcija}\n"
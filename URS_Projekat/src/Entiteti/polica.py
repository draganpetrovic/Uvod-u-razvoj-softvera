from Entiteti.identifikacija import Identifikacija

class Polica(Identifikacija):
    """Klasa Polica, nasledjuje klasu Identifikacija"""

    def __init__(self, oznaka, red, kolona, pozicija, duzina, sirina, visina, sekcija):
        super().__init__(oznaka)
        self.red = red
        self.kolona = kolona
        self.pozicija = pozicija
        self.duzina = duzina
        self.sirina = sirina
        self.visina = visina
        self.sekcija = sekcija

    def __str__(self):
        """Metoda __str__ prilagodjena na format koji nam odgovara za klasu"""
        return f"{self.oznaka};{self.red};{self.kolona};{self.pozicija};{self.duzina};{self.sirina};{self.visina};{self.sekcija}\n"
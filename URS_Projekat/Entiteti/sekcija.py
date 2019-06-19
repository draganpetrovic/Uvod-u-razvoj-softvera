from Entiteti.identifikacija import Identifikacija

class Sekcija(Identifikacija):
    """Klasa Sekcija, nasledjuje klasu Identifikacija"""

    def __init__(self, oznaka, naziv, opis, pozicija):
        super().__init__(oznaka)
        self.naziv = naziv
        self.opis = opis
        self.pozicija = pozicija

    
    def __str__(self):
        """Metoda __str__ prilagodjena na format koji nam odgovara za klasu"""
        return f"{self.oznaka};{self.naziv};{self.opis};{self.pozicija}\n"
        
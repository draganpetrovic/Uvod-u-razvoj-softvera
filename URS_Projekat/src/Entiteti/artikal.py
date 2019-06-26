from Entiteti.identifikacija import Identifikacija

class Artikal(Identifikacija):
    """Klasa artikal, nasledjuje klasu Identifikacija"""
    
    def __init__(self, oznaka, naziv, opis, cijena, rok_trajanja, polica):
        super().__init__(oznaka)
        self.naziv = naziv
        self.opis = opis
        self.cijena = float(cijena)
        self.rok_trajanja = rok_trajanja
        self.polica = polica

    
    def __str__(self):
        """Metoda __str__ prilagodjena na format koji nam odgovara za klasu"""
        return f"{self.oznaka};{self.naziv};{self.opis};{self.cijena};{self.rok_trajanja};{self.polica}\n"
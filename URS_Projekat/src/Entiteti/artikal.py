from Entiteti.identifikacija import Identifikacija

class Artikal(Identifikacija):
    """Klasa artikal, nasledjuje klasu Identifikacija"""
    
    def __init__(self, oznaka, naziv, opis, rok_trajanja, polica, cijena):
        super().__init__(oznaka)
        self.naziv = naziv
        self.opis = opis
        self.rok_trajanja = rok_trajanja
        self.polica = polica
        self.cijena = float(cijena)

    
    def __str__(self):
        """Metoda __str__ prilagodjena na format koji nam odgovara za klasu"""
        return f"{self.oznaka};{self.naziv};{self.opis};{self.cijena};{self.rok_trajanja};{self.polica}\n"
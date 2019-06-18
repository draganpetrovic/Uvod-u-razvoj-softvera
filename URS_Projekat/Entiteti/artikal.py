from Entiteti.identifikacija import Identifikacija

class Artikal(Identifikacija):
    
    def __init__(self, oznaka, naziv, opis, cijena, rok_trajanja, polica):
        super().__init__(oznaka)
        self.naziv = naziv
        self.opis = opis
        self.cijena = int(cijena)
        self.rok_trajanja = rok_trajanja
        self.polica = polica

        # if self.cijena < 0:
        #     raise ValueError("Vrijednost mora biti veca od 0!")

    
    def __str__(self):
        return f"{self.oznaka};{self.naziv};{self.opis};{self.cijena};{self.rok_trajanja};{self.polica}\n"
        # return "{:^11}{:^11}{:^11}{:^11}{:^11}{:^11}\n".format(self.oznaka, self.naziv, self.opis, self.cijena, self.rok_trajanja, self.polica)
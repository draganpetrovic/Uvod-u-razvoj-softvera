from Entiteti.identifikacija import Identifikacija

class Stavka(Identifikacija):
    
    def __init__(self, oznaka, kolicina, ukupna_cijena, artikal, racun):
        super().__init__(oznaka)
        self.kolicina = float(kolicina)
        self.ukupna_cijena = float(ukupna_cijena)
        self.artikal = artikal
        self.racun = racun
    
    
    @property
    def ukupna_cijena(self):
        return self.__ukupna_cijena
        
    @ukupna_cijena.setter
    def ukupna_cijena(self,vrednost):
        if vrednost <= 0:
            raise ValueError("Ukupna cena mora biti veca od 0.")
        self.__ukupna_cijena = vrednost
    
    
    @property
    def kolicina(self):
        return self.__kolicina
        
    @kolicina.setter
    def kolicina(self,vrednost):
        if vrednost <= 0:
            raise ValueError("Kolicina mora biti veca od 0.")
        self.__kolicina = vrednost
        
        
    def __str__(self):
        return f"{self.oznaka};{self.kolicina};{self.ukupna_cijena};{self.artikal};{self.racun}\n"
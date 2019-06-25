from Entiteti.identifikacija import Identifikacija

class Racun(Identifikacija):

    def __init__(self, oznaka, prodavac, ukupna_cijena, datum):
        super().__init__(oznaka)
        self.prodavac = prodavac
        self.ukupna_cijena = float(ukupna_cijena)
        self.datum = datum
        
    @property
    def ukupna_cijena(self):
        return self.__ukupna_cijena
    
        
    @ukupna_cijena.setter
    def ukupna_cijena(self,vrednost):
        if vrednost <= 0:
            raise ValueError("Ukupna cena mora biti veca od 0.")
        self.__ukupna_cijena = vrednost
        
        

    def __str__(self):
        return f"{self.oznaka};{self.prodavac};{self.ukupna_cijena};{self.datum}\n"
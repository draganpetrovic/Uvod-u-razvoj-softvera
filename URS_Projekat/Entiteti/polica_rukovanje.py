from Logika.entiteti_rukovanje import EntitetiRukovanje
from Entiteti.polica import Polica


class Polica_rukovanje(EntitetiRukovanje):
    def __init__(self,putanja):
        super().__init__(putanja)

    def citanje_svih(self):
        with open(self.putanja, "r") as file:
            podaci = []
            for linija in file.readlines():
                podaci.append(self.napravi_entitet(linija))
            return podaci
                
            
    def napravi_entitet(self, linija):
        polje = linija.strip().split(";")
        return Polica(polje[0], polje[1], polje[2], polje[3], polje[4], polje [5], polje[6], polje[7])

    def upis_jednog(self, entitet):
        with open(self.putanja, "a") as file:
            file.write(str(entitet))
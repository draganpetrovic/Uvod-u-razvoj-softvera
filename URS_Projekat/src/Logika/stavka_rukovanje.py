from Entiteti.stavka import Stavka
from Logika.entiteti_rukovanje import EntitetiRukovanje

class Stavka_rukovanje(EntitetiRukovanje):
    def __init__(self, putanja):
        super().__init__(putanja)
    

    def citanje_svih(self):
        with open(self.putanja, "r") as file:
            podaci = []
            for linija in file.readlines():
                podaci.append(self.napravi_entitet(linija))
            return podaci
                

    def napravi_entitet(self, linija):
        polje = linija.strip().split(";")
        return Stavka(polje[0], polje[1], polje[2], polje[3], polje[4])

    def upis_jednog(self, entitet):
        with open(self.putanja, "a") as file:
            file.write(str(entitet))
    
    def izmjena_jednog(self, entitet):
        entiteti = self.citanje_svih()
        pronasao = False
        for i in range(len(entiteti)):
            if entiteti[i].oznaka == entitet.oznaka:
                entiteti.pop(i)
                if i >= len(entiteti):
                    entiteti.append(entitet)
                else:
                    entiteti.insert(i, entitet)
                pronasao = True
                break
        with open(self.putanja, "w") as file:
            for entitet in entiteti:
                file.write(str(entitet))
            return pronasao
    
    def pretraga_po_oznaci(self, lst, rijec):
        pretrazeno = []
        for i in lst:
            if i.oznaka.lower().find(rijec.lower()) != -1:
                pretrazeno.append(i)
        return pretrazeno

    def pretraga_po_kolicini(self, lst, broj):
        pretrazeno = []
        for i in lst:
            if i.kolicina == broj:
                pretrazeno.append(i)
        return pretrazeno
    
    def pretraga_po_ukupnoj_cijeni(self, lst, broj):
        pretrazeno = []
        for i in lst:
            if i.ukupna_cijena == broj:
                pretrazeno.append(i)
        return pretrazeno
    
    def kljuc(self):
        return self.kolicina
    
    
    def sortiranje_po_kolicini(self, lst, smjer):
        if smjer == "+":
            lst.sort(key=Stavka_rukovanje.kljuc, reverse=True)
            return lst
        elif smjer == "-":
            lst.sort(key=Stavka_rukovanje.kljuc)
            return lst
        else:
            print("Pogresan unos!")
from Entiteti.artikal import Artikal
from Logika.entiteti_rukovanje import EntitetiRukovanje
from datetime import date

class Artikal_rukovanje(EntitetiRukovanje):

    def __init__(self,putanja):
        super().__init__(putanja)


    def citanje_svih(self):
        with open(self.putanja, "r") as file:
            podaci = []
            for linija in file.readlines():
                podaci.append(self.napravi_entitet(linija))
            return podaci

    def napravi_entitet(self,linija):
        polje = linija.strip().split(";")
        return Artikal(polje[0], polje[1], polje[2], polje[3], polje[4], polje[5])



    def upis_jednog(self,entitet):

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

    def pretraga_po_nazivu(self, lst,rijec):
        pretrazeno = []
        for i in lst:
            if i.naziv.lower().find(rijec.lower()) != -1:
                pretrazeno.append(i)
        return pretrazeno

    def pretraga_po_opisu(self, lst, rijec):
        pretrazeno = []
        for i in lst:
            if i.opis.lower().find(rijec.lower()) != -1:
                pretrazeno.append(i)
        return pretrazeno

    def pretraga_po_cijeni(self, lst, broj):
        pretrazeno = []
        for i in lst:
            if i.cijena == broj:
                pretrazeno.append(i)
        return pretrazeno

    def pretraga_po_roku_trajanja(self, lst, datum):
        pretrazeno = []
        for i in lst:
            if i.rok_trajanja == datum:
                pretrazeno.append(i)
        return pretrazeno
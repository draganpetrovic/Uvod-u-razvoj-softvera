from Entiteti.artikal import Artikal
from Logika.entiteti_rukovanje import EntitetiRukovanje
from datetime import date

class Artikal_rukovanje(EntitetiRukovanje):
    """Klasa za rukovanje policama prosledjujemo putanju do fajla"""

    def __init__(self,putanja):
        super().__init__(putanja)


    def citanje_svih(self):
        """Citanje svih entiteta iz fajla"""
        with open(self.putanja, "r") as file:
            podaci = []
            for linija in file.readlines():
                podaci.append(self.napravi_entitet(linija))
            return podaci

    def napravi_entitet(self,linija):
        "Metoda za pravljenje novog entiteta u formatu sa ; delimiterom iz __str__ funkcije"
        polje = linija.strip().split(";")
        return Artikal(polje[0], polje[1], polje[2], polje[3], polje[4], polje[5])



    def upis_jednog(self,entitet):
        """Metoda za upis novog entiteta"""
        with open(self.putanja, "a") as file:
           file.write(str(entitet))


    def izmjena_jednog(self, entitet):
        """Metoda za izmjenu odredjenog entiteta sa podacima novog entiteta"""
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
        """Pretraga entiteta po oznaci"""
        pretrazeno = []
        for i in lst:
            if i.oznaka.lower().find(rijec.lower()) != -1:
                pretrazeno.append(i)
        return pretrazeno

    def pretraga_po_nazivu(self, lst,rijec):
        """Pretraga entiteta po nazivu"""
        pretrazeno = []
        for i in lst:
            if i.naziv.lower().find(rijec.lower()) != -1:
                pretrazeno.append(i)
        return pretrazeno

    def pretraga_po_opisu(self, lst, rijec):
        """Pretraga entiteta po opisu"""
        pretrazeno = []
        for i in lst:
            if i.opis.lower().find(rijec.lower()) != -1:
                pretrazeno.append(i)
        return pretrazeno

    def pretraga_po_cijeni(self, lst, broj):
        """Pretraga entiteta po cijeni"""
        pretrazeno = []
        for i in lst:
            if i.cijena == broj:
                pretrazeno.append(i)
        return pretrazeno

    def pretraga_po_roku_trajanja(self, lst, datum):
        """Pretraga entiteta po roku trajanja"""
        pretrazeno = []
        for i in lst:
            if i.rok_trajanja == datum:
                pretrazeno.append(i)
        return pretrazeno

    def sortiranje_po_cijeni(self, lst, smjer):
        """Sortiranje entiteta po cijeni, prosledjujemo listu za sortiranje i smjer"""
        for i in range(len(lst)-1):
            najmanji = i
            for j in range(i+1, len(lst)):
                if smjer == "+":
                    if lst[najmanji].cijena > lst[j].cijena:
                        najmanji = j
                elif smjer == "-":
                    if lst[najmanji].cijena < lst[j].cijena:
                        najmanji = j
            skladiste = lst[i]
            lst[i] = lst[najmanji]
            lst[najmanji] = skladiste
        return lst

    def sortiranje_po_roku_trajanja(self, lst, smjer):
        """Sortiranje entiteta po roku trajanja, prosledjujemo listu za sortiranje i smjer"""
        for i in range(len(lst)-1):
            najmanji = i
            for j in range(i+1, len(lst)):
                if smjer == "+":
                    if self.konvertuj_datum(lst[najmanji].rok_trajanja) > self.konvertuj_datum(lst[j].rok_trajanja):
                        najmanji = j
                elif smjer == "-":
                    if self.konvertuj_datum(lst[najmanji].rok_trajanja) < self.konvertuj_datum(lst[j].rok_trajanja):
                        najmanji = j
            skladiste = lst[i]
            lst[i] = lst[najmanji]
            lst[najmanji] = skladiste
        return lst


    def konvertuj_datum(self, datum):
        """Metoda za konvertovanje datuma u format za sortiranje"""
        brojevi = datum.split(".")
        konvertovani = date(int(brojevi[2]), int(brojevi[1]), int(brojevi[0]))
        return konvertovani

    
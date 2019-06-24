from Entiteti.sekcija import Sekcija
from Logika.entiteti_rukovanje import EntitetiRukovanje

class Sekcija_rukovanje(EntitetiRukovanje):
    """Klasa za rukovanje policama prosledjujemo putanju do fajla"""
    def __init__(self, putanja):
        super().__init__(putanja)

    def citanje_svih(self):
        """Citanje svih entiteta iz fajla"""
        with open(self.putanja, "r") as file:
            podaci = []
            for linija in file.readlines():
                podaci.append(self.napravi_entitet(linija))
            return podaci

    def napravi_entitet(self, linija):
        "Metoda za pravljenje novog entiteta u formatu sa ; delimiterom iz __str__ funkcije"
        polje = linija.strip().split(";")
        return Sekcija(polje[0], polje[1], polje[2], polje[3])

    def upis_jednog(self, entitet):
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

    def pretraga_po_nazivu(self, lst, rijec):
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
    
    def pretraga_po_poziciji(self, lst, rijec):
        """Pretraga entiteta po poziciji"""
        pretrazeno = []
        for i in lst:
            if  i.pozicija.lower().find(rijec.lower()) != -1:
                pretrazeno.append(i)
        return pretrazeno

    def izlistaj_police(self, sekcija, lista_polica):
        """Prikazivanje svih polica u odredjenoj sekciji"""
        police_sa_sekcijama = []
        for i in lista_polica:
            if i.sekcija == sekcija:
                police_sa_sekcijama.append(i)
        return police_sa_sekcijama

    def izlistaj_artikle(self, polica, lista_artikala):
        """Prikazivanje svih artikala koji se nalaze na polici"""
        artikli_na_polici = []
        for i in lista_artikala:
            if i.polica == polica:
                artikli_na_polici.append(i)
        return artikli_na_polici

    def izlistaj_police_i_artikle(self, sekcija, lista_polica, lista_artikala):
        """Prikazivanje svih polica u odredjenoj sekciji, i artikala koje se nalaze na tim policama"""
        police_i_artikli = []
        for i in lista_polica:
            if i.sekcija == sekcija:
                for j in lista_artikala:
                    if i.artikal == j.oznaka:
                        police_i_artikli.append({'polica' : i, 'artikal' : j})
        return police_i_artikli
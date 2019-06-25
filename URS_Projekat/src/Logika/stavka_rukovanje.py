from Entiteti.stavka import Stavka
from Logika.entiteti_rukovanje import EntitetiRukovanje

class Stavka_rukovanje(EntitetiRukovanje):
    
    """ Klasa Stavka_rukovanje sadrzi sve metode vezane za objekte Stavka."""
    
    def __init__(self, putanja):
        super().__init__(putanja)
    

    def citanje_svih(self):
        
        """Vrsi se citanje stavki iz fajla stavke.txt
        podaci=[] skladisti objekte u listu"""
                
        with open(self.putanja, "r") as file:
            podaci = []
            for linija in file.readlines():
                podaci.append(self.napravi_entitet(linija))
            return podaci
                

    def napravi_entitet(self, linija):
        
        '''Metoda za pravljenje novog entiteta u formatu sa ; delimiterom iz __str__ funkcije'''
        
        polje = linija.strip().split(";")
        return Stavka(polje[0], polje[1], polje[2], polje[3], polje[4])

    def upis_jednog(self, entitet):
        
        """ Dodavanje novog entiteta u fajl stavka.txt."""
        
        with open(self.putanja, "a") as file:
            file.write(str(entitet))
    
    def izmjena_jednog(self, entitet):
        
        """Metoda za izmenu odredjenog entiteta .
        Unos novih podataka"""
        
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
        
        """ Svaka stavka ima svoju oznaku, koja je jedinstvena i uvek
        lako mozemo pronaci stavku po toj oznaci"""
        
        pretrazeno = []
        for i in lst:
            if i.oznaka.lower().find(rijec.lower()) != -1:
                pretrazeno.append(i)
        return pretrazeno

    def pretraga_po_kolicini(self, lst, broj):
        
        """Pretraga stavki po kolicini. Uporedjuju se kolicine
        iz liste stavki sa unetom kolicinom za pretragu."""
        
        pretrazeno = []
        for i in lst:
            if i.kolicina == broj:
                pretrazeno.append(i)
        return pretrazeno
    
    def pretraga_po_ukupnoj_cijeni(self, lst, broj):
        
        """ Pretraga stavki po ceni. Dobijamo listu stavki i cenu 
        po kojoj trazimo stavku u listi."""
        
        pretrazeno = []
        for i in lst:
            if i.ukupna_cijena == broj:
                pretrazeno.append(i)
        return pretrazeno
    
    def kljuc(self):
        '''Koristi se kao pomocna funkcija u metodi: sortiranje_po_kolicini;
         kao <key_function> za sortiranje'''
        return self.kolicina
    
    
    def sortiranje_po_kolicini(self, lst, smjer):
        
        """Sortira stavki po kolicini.
        Ponudjen izbor prilikom sortiranja, za rastuce ili opadajuce vrednosti.
        Koristi kljuc() metodu kao key function za sortiranje i vraca sortiranu listu nazad 
        u metodu koja pozove ovu metodu. Kolicina atribut mora biti float vrednost da bi sort
        mogao da je gleda kao broj, a ne kao string, kada gleda samo prvu cifru."""
        
        
        if smjer == "+":
            lst.sort(key=Stavka_rukovanje.kljuc, reverse=True)
            return lst
        elif smjer == "-":
            lst.sort(key=Stavka_rukovanje.kljuc)
            return lst
        else:
            print("Pogresan unos!")
from Logika.entiteti_rukovanje import EntitetiRukovanje
from Entiteti.racun import Racun


class Racun_rukovanje(EntitetiRukovanje):
    
    """ Klasa Racuni_rukovanje sadrzi sve metode vezane za objekte Racun."""
    
    def __init__(self, putanja):
        super().__init__(putanja)

    def citanje_svih(self):
        
        """Vrsi se citanje racuna iz fajla racuni.txt
        podaci=[] skladisti objekte u listu"""
        
        with open(self.putanja, "r") as file:
            podaci = []
            for linija in file.readlines():
                podaci.append(self.napravi_entitet(linija))
            return podaci  


    def napravi_entitet(self, linija):
        
        '''Metoda za pravljenje novog entiteta u formatu sa ; delimiterom iz __str__ funkcije'''
        
        polje = linija.strip().split(";")
        return Racun(polje[0], polje[1], polje[2], polje[3])

    def upis_jednog(self, entitet):
        
        """ Dodavanje novog entiteta u fajl racuni.txt."""
        
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
        with open(self.putanja, "w") as file:
            for entitet in entiteti:
                file.write(str(entitet))
        return pronasao


    def pretraga_po_oznaci(self, lst, rijec):
        
        """ Svaki racun ima svoju oznaku, koja je jedinstvena i uvek
        lako mozemo pronaci racun po toj oznaci"""
        
        pretrazeno = []
        for i in lst:
            if i.oznaka.lower().find(rijec.lower()) != -1:
                pretrazeno.append(i)
        return pretrazeno
    
    def pretraga_po_prodavcu(self, lst, rijec):
        """ Pretraga racuna po imenu Prodavca koji je izdao racun."""
        pretrazeno = []
        for i in lst:
            if i.prodavac.lower().find(rijec.lower()) != -1:
                pretrazeno.append(i)
        return pretrazeno

    def pretraga_po_ukupnoj_cijeni(self, lst, broj):
        
        """ Pretraga racuna po ceni. Dobijamo listu racuna i cenu 
        po kojoj trazimo racun u listi."""
        
        pretrazeno = []
        for i in lst:
            if i.ukupna_cijena == broj:
                pretrazeno.append(i)
        return pretrazeno

    def pretraga_po_datumu(self, lst, broj):
        
        """ Pretraga racuna po datumu kada su izdati.
        Dobijamo listu racuna i zeljeni datum za koji trazimo racun."""
        
        pretrazeno = []
        for i in lst:
            if i.datum.lower().find(broj.lower()) != -1:
                pretrazeno.append(i)
        return pretrazeno





    def kljuc(self):
        '''Koristi se kao pomocna funkcija u metodi: sortiranje_po_ukupnoj_cijeni;
         kao <key_function> za sortiranje'''
        return self.ukupna_cijena
   
   
    def sortiranje_po_ukupnoj_cijeni(self, lst, smjer):
        
        """Sortira racune po ukupnoj ceni.
        Ponudjen izbor prilikom sortiranja, za rastuce ili opadajuce vrednosti.
        Koristi kljuc() metodu kao key function za sortiranje i vraca sortiranu listu nazad 
        u metodu koja pozove ovu metodu. Ukupna_cijena atribut mora biti float vrednost da bi sort
        mogao da je gleda kao broj, a ne kao string kada gleda samo prvu cifru."""
        
        if smjer == "+":
            lst.sort(key=Racun_rukovanje.kljuc, reverse=True)
            return lst
        elif smjer == "-":
            lst.sort(key=Racun_rukovanje.kljuc)
            return lst
        else:
            print("Pogresan unos!")
            
            
        
    def kljuc2(self):
        
        '''Koristi se kao pomocna funkcija u metodi: sortiranje_po_datumu;
         kao <key_function> za sortiranje'''
        
        return self.datum

    def sortiranje_po_datumu(self, lst, smjer):
        
        """ U slucaju kada sortiramo datum kao string, najlakse je da datum bude formata
        %Y.%m.%d """
        
        if smjer == "+":
            lst.sort(key=Racun_rukovanje.kljuc2, reverse=True)
            return lst
        elif smjer == "-":
            lst.sort(key=Racun_rukovanje.kljuc2)
        else:
            print("Pogresan unos!")

    def stavke_i_artikli_u_racunu(self, racun, lista_stavki, lista_artikala):
        
        """ Metoda dobija kao argumente liste stavki i artikala od metode koja je poziva.
        Za izabrani racun nam ispisuje stavke i artikle koji se nalaze na njemu."""
        
        stavke_i_artikli = []
        for i in lista_stavki:
            if i.racun == racun:
                for j in lista_artikala:
                    if i.artikal == j.oznaka:
                        stavke_i_artikli.append({'stavka' : i, 'artikal' : j})
        return stavke_i_artikli
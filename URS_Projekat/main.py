from Logika.entiteti_rukovanje import EntitetiRukovanje
from Entiteti.artikal import Artikal
from Logika.artikal_rukovanje import Artikal_rukovanje
from Entiteti.polica import Polica
from Logika.polica_rukovanje import Polica_rukovanje
from Entiteti.sekcija import Sekcija
from Logika.sekcija_rukovanje import Sekcija_rukovanje

if __name__ == "__main__":
    print("*************** EVIDENCIJA ARTIKALA I RACUNA ZA PRODAVCE ***************\n\n")
    opcija = 0
    while opcija != 6:
        print("1 -> Police")
        print("2 -> Sekcije")
        print("3 -> Artikli")
        print("4 -> Stavke")
        print("5 -> Racuni")
        print("6 -> Izlaz iz aplikacije")
        print("-------------------------")
        opcija = int(input("Izaberite opciju: "))
        while opcija > 6 or opcija < 1:
            opcija = int(input("Unesite postojecu opciju: "))
        if opcija == 1:
            opt = 0
            while opt != 7:
                print("1 -> Prikaz polica")
                print("2 -> Dodavanje polica")
                print("3 -> Izmjena polica")
                print("4 -> Pretraga polica")
                print("5 -> Sortiranje polica")
                print("6 -> Prikaz artikala na polici")
                print("7 -> Nazad")
                print("---------------------------------")
                opt = int(input("Izaberite neku od opcija"))

                if opt == 1:
                    police = Polica_rukovanje("police.txt")
                    lista_polica = police.citanje_svih()
                    for i in lista_polica:
                        print(i)

                elif opt == 2:
                    p = Polica_rukovanje("police.txt")
                    oznaka = input("Unesite oznaku: ")
                    oznaka = str(oznaka)
                    red = int(input("Unesite red: "))
                    if red <= 0:
                        raise Exception
                    kolona = int(input("Unesite kolonu: "))
                    if kolona <= 0:
                        raise Exception
                    pozicija = str(input("Unesite poziciju: "))
                    duzina = float(input("Unesite duzinu: "))
                    if duzina <= 0:
                        raise Exception
                    sirina = float(input("Unesite sirinu: "))
                    if sirina <= 0:
                        raise Exception
                    visina = float(input("Unesite visinu: "))
                    if visina <= 0:
                        raise Exception
                    sekcija = str(input("Unesite sekciju: "))

                    polica = Polica(oznaka, red, kolona, pozicija, duzina, sirina, visina, sekcija)
                    p.upis_jednog(polica)

                elif opt == 3:
                    p = Polica_rukovanje("police.txt")
                    oznaka = input("Unesite oznaku police koji zelite da zamjenite: ")
                    oznaka = str(oznaka)
                    red = input("Unesite red nove police: ")
                    red = int(red)
                    kolona = input("Unesite kolonu nove police: ")
                    kolona = int(kolona)
                    pozicija = input("Unesite poziciju nove police: ")
                    pozicija = str(pozicija)
                    duzina = input("Unesite duzinu nove police: ")
                    duzina = float(duzina)
                    sirina = input("Unesite sirinu nove police: ")
                    sirina = float(sirina)
                    visina = input("Unesite visinu nove police: ")
                    visina = float(visina)
                    sekcija = input("Unesite sekciju nove police: ")
                    sekcija = str(sekcija)
                    polica = Polica(oznaka, red, kolona, pozicija, duzina, sirina, visina, sekcija)
                    p.izmjena_jednog(polica)
                
                elif opt == 4:
                    print("Meni pretrage")
                    opt_pretraga = 0
                    print("1 -> Pretraga po oznaci")
                    print("2 -> Pretraga po redu")
                    print("3 -> Pretraga po po koloni")
                    print("4 -> Pretraga po poziciji")
                    print("5 -> Pretraga po duzini")
                    print("6 -> Pretraga po sirini")
                    print("7 -> Pretraga po visini")
                    opt_pretraga = int(input("Unesite pretragu: "))
            
                    if opt_pretraga == 1:
                        p = Polica_rukovanje("police.txt")
                        lista_polica = p.citanje_svih()
                        oznaka_za_pretragu = input("Unesite oznaku police za pretragu: ")
                        pretrazeno = p.pretraga_po_oznaci(lista_polica, oznaka_za_pretragu)
                        for i in pretrazeno:
                            print(i)
                    elif opt_pretraga == 2:
                        p = Polica_rukovanje("police.txt")
                        lista_polica = p.citanje_svih()
                        red_za_pretragu = input("Unesite red police za pretragu: ")
                        pretrazeno = p.pretraga_po_redu(lista_polica, red_za_pretragu)
                        for i in pretrazeno:
                            print(i)
                    elif opt_pretraga == 3:
                        p = Polica_rukovanje("police.txt")
                        lista_polica = p.citanje_svih()
                        kolona_za_pretragu = input("Unesite kolonu police za pretragu: ")
                        pretrazeno = p.pretraga_po_koloni(lista_polica, kolona_za_pretragu)
                        for i in pretrazeno:
                            print(i)
                    elif opt_pretraga == 4:
                        p = Polica_rukovanje("police.txt")
                        lista_polica = p.citanje_svih()
                        pozicija_za_pretragu = input("Unesite pziciju police za pretragu: ")
                        pretrazeno = p.pretraga_po_poziciji(lista_polica, pozicija_za_pretragu)
                        for i in pretrazeno:
                            print(i)
                    elif opt_pretraga == 5:
                        p = Polica_rukovanje("police.txt")
                        lista_polica = p.citanje_svih()
                        duzina_za_pretragu = float(input("Unesite duzinu police za pretragu: "))
                        pretrazeno = p.pretraga_po_duzini(lista_polica, duzina_za_pretragu)
                        for i in pretrazeno:
                            print(i)
                    elif opt_pretraga == 6:
                        p = Polica_rukovanje("police.txt")
                        lista_polica = p.citanje_svih()
                        sirina_za_pretragu = float(input("Unesite sirinu police za pretragu: "))
                        pretrazeno = p.pretraga_po_sirini(lista_polica, sirina_za_pretragu)
                        for i in pretrazeno:
                            print(i)
                    elif opt_pretraga == 7:
                        p = Polica_rukovanje("police.txt")
                        lista_polica = p.citanje_svih()
                        visina_za_pretragu = float(input("Unesite visinu police za pretragu: "))
                        pretrazeno = p.pretraga_po_visini(lista_polica, visina_za_pretragu)
                        for i in pretrazeno:
                            print(i)

                elif opt == 5:

                    
                        print("Meni Sortiranje")
                        opt_sortiranje = 0
                        print("1 -> Srotiranje po poziciji")
                        opt_sortiranje = int(input("Izaberite jednu od opcija za sortiranje: "))
                    
                        if opt_sortiranje == 1:
                            p = Polica_rukovanje("police.txt")
                            lista_polica = p.citanje_svih()
                            smjer = input("Napisite '+' za opadajuci redoslijed, '-' za rastuci redoslijed: ")
                            sortirano = p.sortiranje_po_poziciji(lista_polica, smjer)
                            for i in sortirano:
                                print(i)
                elif opt == 6:
                    print("Prikazi artikle na polici")
                
                    a = Artikal_rukovanje("artikli.txt")
                    lista_artikala = a.citanje_svih()
                    p = Polica_rukovanje("police.txt")
                    lista_polica = p.citanje_svih()
                    for i in lista_polica:
                        print(i)

                    id_police = input("Unesite ID police: ")
                    artikli_u_polici = p.izlistaj_artikle(id_police, lista_artikala)
                    for i in artikli_u_polici:
                        print(i)
                
                while opt < 1 or opt > 7:
                    opt = int(input("Iaberite neku od postojecih opcija!: "))
            
        elif opcija == 2:
            print("Rad sa sekcijama!")
            opt = 0
            while opt != 6:
                print("1 -> Prikaz sekcija")
                print("2 -> Dodavanje sekcija")
                print("3 -> Izmjena sekcija")
                print("4 -> Pretraga sekcija")
                print("5 -> Vidi sve police i artikle u sekciji")
                print("6 -> Nazad")
                opt = int(input("Izaberi neku od opcija"))

                if opt == 1:
                    s = Sekcija_rukovanje("sekcije.txt")
                    lista_sekcija = s.citanje_svih()
                    for i in lista_sekcija:
                        print(i)

                elif opt == 2:
                    s = Sekcija_rukovanje("sekcije.txt")
                    oznaka = str(input("Unesite oznaku sekcije koju mijenjate: "))
                    naziv = str(input("Unesite naziv sekcije"))
                    opis = str(input("Unesite opis sekcije"))
                    pozicija = str(input("Unesite poziciju usekcije"))
                    sekcija = Sekcija(oznaka, naziv, opis, pozicija)
                    s.upis_jednog(sekcija)
                
                elif opt == 3:
                    s = Sekcija_rukovanje("sekcije.txt")
                    oznaka = input("Unesite oznaku sekcije koju zelite da zamjenite: ")
                    oznaka = str(oznaka)
                    naziv = input("Unesite naziv nove sekcije: ")
                    naziv = str(naziv)
                    opis = input("Unesite opis nove sekcije: ")
                    opis = str(opis) 
                    pozicija = input("Unesite poziciju nove sekcije: ")
                    pozicija = str(pozicija)
                    sekcija = Sekcija(oznaka, naziv, opis, pozicija)
                    s.izmjena_jednog(sekcija)

                elif opt == 4:
                    print("Meni pretrage")
                    opt_pretraga = 0
                    print("1 -> Pretraga po oznaci")
                    print("2 -> Pretraga po nazivu")
                    print("3 -> Pretraga po po opisu")
                    print("4 -> Pretraga po poziciji")
                    opt_pretraga = int(input("Unesite pretragu: "))

                    if opt_pretraga == 1:
                        s = Sekcija_rukovanje("sekcije.txt")
                        lista_sekcija = s.citanje_svih()
                        oznaka_za_pretragu = input("Unesite oznaku sekcije za pretragu: ")
                        pretrazeno = s.pretraga_po_oznaci(lista_sekcija, oznaka_za_pretragu)
                        for i in pretrazeno:
                            print(i)
                    
                    elif opt_pretraga == 2:
                        s = Sekcija_rukovanje("sekcije.txt")
                        lista_sekcija = s.citanje_svih()
                        naziv_za_pretragu = input("Unesite naziv sekcije za pretragu: ")
                        pretrazeno = s.pretraga_po_nazivu(lista_sekcija, naziv_za_pretragu)
                        for i in pretrazeno:
                            print(i)

                    elif opt_pretraga == 3:
                        s = Sekcija_rukovanje("sekcije.txt")
                        lista_sekcija = s.citanje_svih()
                        opis_za_pretragu = input("Unesite opis sekcije za pretragu: ")
                        pretrazeno = s.pretraga_po_opisu(lista_sekcija, opis_za_pretragu)
                        for i in pretrazeno:
                            print(i)

                    elif opt_pretraga == 4:
                        s = Sekcija_rukovanje("sekcije.txt")
                        lista_sekcija = s.citanje_svih()
                        pozicija_za_pretragu = input("Unesite poziciju sekcije za pretragu: ")
                        pretrazeno = s.pretraga_po_poziciji(lista_sekcija, pozicija_za_pretragu)
                        for i in pretrazeno:
                            print(i)
                    
                elif opt == 5:
                    print("Izlistaj police i artikle na policama")
                    opt_izlistaj = 0
                    print("1 -> Izlistaj police u sekciji")
                    print("2 -> Izlistaj artikle na polici")
                    opt_izlistaj = int(input("Unesite zeljenu opciju: "))

                    s = Sekcija_rukovanje("sekcije.txt")

                    if opt_izlistaj == 1:
                        
                        s = Sekcija_rukovanje("sekcije.txt")
                        lista_sekcija = s.citanje_svih()

                        p = Polica_rukovanje("police.txt")
                        lista_polica = p.citanje_svih()

                        for l in lista_sekcija:
                            print(l)

                        id_sekcije = input("Unesite ID sekcije: ")
                        police = s.izlistaj_police(id_sekcije, lista_polica)
                        for i in police:
                            print(i)
                    
                    elif opt_izlistaj == 2:
                        
                        p = Polica_rukovanje("police.txt")
                        lista_polica = p.citanje_svih()
                        
                        a = Artikal_rukovanje("artikli.txt")
                        lista_aritkala = a.citanje_svih()

                        for l in lista_polica:
                            print(l)

                        id_police = input("Unesite ID police: ")
                        artikli = s.izlistaj_artikle(id_police, lista_aritkala)
                        for i in artikli:
                            print(i)





                while opt < 1 or opt > 6:
                  opt = int(input("Izaberite neku od postojecih opcija"))
        elif opcija == 3:
            print("Rad sa artiklima")
            opt = 0
            while opt != 6:
                print("1 -> Prikaz artikala")
                print("2 -> Dodavanje artikala")
                print("3 -> Izmjena artikala")
                print("4 -> Pretraga artikala")
                print("5 -> Sortiranje artikala")
                print("6 -> Nazad")
                opt = int(input("Izaberi neku od opcija"))

                if opt == 1:
                    print("Meni ucitaj artikle")
                    artikli = Artikal_rukovanje("artikli.txt")
                    lista_artikala = artikli.citanje_svih()
                    for l in lista_artikala:
                        print(l)

                elif opt == 2:
                    print("Meni Dodaj Artikal")
                    a = Artikal_rukovanje("artikli.txt")
                    oznaka = str(input("Unesite oznaku artikla: "))
                    naziv =  str(input("unesite naziv artikla: "))
                    opis  = str(input("Unesite opis artikla: "))
                    cijena = int(input("Unesite cijenu: "))
                    if cijena <= 0:
                        raise Exception
                    rok_trajanja = str(input("Unesite rok trajanja: "))
                    polica = str(input("Unesite policu za artikal: "))
                    artikal = Artikal(oznaka, naziv, opis, cijena, rok_trajanja, polica)
                    a.upis_jednog(artikal)

                elif opt == 3:
                    a = Artikal_rukovanje("artikli.txt")
                    oznaka = input("Unesite oznaku artikla koji zelite da izmjenite: ")
                    oznaka = str(oznaka)
                    naziv =  input("unesite naziv novog artikla: ")
                    naziv = str(naziv)
                    opis  = input("Unesite opis novog artikla: ")
                    opis = str(opis)
                    cijena = input("Unesite cijenu novog artikla: ")
                    cijena = int(cijena)
                    rok_trajanja = input("Unesite rok trajanja novog artikla: ")
                    rok_trajanja = str(rok_trajanja)
                    polica = input("Inesite policu za novi artikal: ")
                    polica = str(polica)
                    artikal = Artikal(oznaka, naziv, opis, cijena, rok_trajanja, polica)
                    a.izmjena_jednog(artikal)
                
                elif opt == 4:
                    print("Meni pretrage")
                    opt_pretraga = 0
                    print("1 -> Pretraga po oznaci")
                    print("2 -> Pretraga po nazivu")
                    print("3 -> Pretraga po opisu")
                    print("4 -> Pretraga po cijeni")
                    print("5 -> Pretraga po roku trajanja")
                    opt_pretraga = int(input("Unesite pretragu: "))

                    if opt_pretraga == 1:
                        a = Artikal_rukovanje("artikli.txt")
                        lista_artikala= a.citanje_svih()
                        oznaka_za_pretragu = input("Unesite oznaku artikla za pretragu: ")
                        pretrazeno = a.pretraga_po_oznaci(lista_artikala, oznaka_za_pretragu)
                        for i in pretrazeno:
                            print(i)
                    
                    if opt_pretraga == 1:
                        a = Artikal_rukovanje("artikli.txt")
                        lista_artikala= a.citanje_svih()
                        oznaka_za_pretragu = input("Unesite oznaku artikla za pretragu: ")
                        pretrazeno = a.pretraga_po_oznaci(lista_artikala, oznaka_za_pretragu)
                        for i in pretrazeno:
                            print(i)

                    elif opt_pretraga == 2:
                        a = Artikal_rukovanje("artikli.txt")
                        lista_artikala= a.citanje_svih()
                        naziv_za_pretragu = input("Unesite naziv artikla za pretragu: ")
                        pretrazeno = a.pretraga_po_nazivu(lista_artikala, naziv_za_pretragu)
                        for i in pretrazeno:
                            print(i)
                            
                    elif opt_pretraga == 3:
                        a = Artikal_rukovanje("artikli.txt")
                        lista_artikala= a.citanje_svih()
                        opis_za_pretragu = input("Unesite opis artikla za pretragu: ")
                        pretrazeno = a.pretraga_po_opisu(lista_artikala, opis_za_pretragu)
                        for i in pretrazeno:
                            print(i)

                    elif opt_pretraga == 4:
                        a = Artikal_rukovanje("artikli.txt")
                        lista_artikala= a.citanje_svih()
                        cijena_za_pretragu = input("Unesite cijenu artikla za pretragu: ")
                        pretrazeno = a.pretraga_po_cijeni(lista_artikala, cijena_za_pretragu)
                        for i in pretrazeno:
                            print(i)
                    
                    elif opt_pretraga == 5:
                        a = Artikal_rukovanje("artikli.txt")
                        lista_artikala= a.citanje_svih()
                        rok_trajanja_za_pretragu = input("Unesite rok trajanja artikla za pretragu: ")
                        pretrazeno = a.pretraga_po_roku_trajanja(lista_artikala, rok_trajanja_za_pretragu)
                        for i in pretrazeno:
                            print(i)
                
                elif opt == 5:
                    opt_soritranje = 0
                    print("Meni za sortiranje")
                    print("1 -> Soritranje po cijeni")
                    print("2 -> Sortiranje po roku trajanja")
                    opt_sortiranje = int(input("Izaberite jednu od opcija za sortiranje: "))

                    if opt_sortiranje == 1:
                        a = Artikal_rukovanje("artikli.txt")
                        lista_artikala = a.citanje_svih()
                        smjer = input("Napisite '+' za opadajuci redoslijed, '-' za rastuci redoslijed: ")
                        sortirano = a.sortiranje_po_cijeni(lista_artikala, "+")
                        for i in sortirano:
                            print(i)
                    elif opt_sortiranje == 2:
                        a = Artikal_rukovanje("artikli.txt")
                        lista_artikala = a.citanje_svih()
                        smjer = input("Napisite '+' za opadajuci redoslijed, '-' za rastuci redoslijed: ")
                        sortirano = a.sortiranje_po_roku_trajanja(lista_artikala, "+")
                        for i in sortirano:
                            print(i)

                while opt < 1 or opt > 6:
                    opt = int(input("Izaberite neku od postojecih opcija"))
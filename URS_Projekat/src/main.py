from Entiteti.artikal import Artikal
from Logika.artikal_rukovanje import Artikal_rukovanje
from Entiteti.polica import Polica
from Logika.polica_rukovanje import Polica_rukovanje
from Entiteti.sekcija import Sekcija
from Logika.sekcija_rukovanje import Sekcija_rukovanje
from Logika.racun_rukovanje import Racun_rukovanje
from Logika.stavka_rukovanje import Stavka_rukovanje
from Entiteti.racun import Racun
from Entiteti.stavka import Stavka

""" Main metoda sadrzi petlju koja nam daje meni prilikom pokretanja programa
Omogucava rad sa entitetima i njihovim metodama."""

if __name__ == "__main__":
    print("*************** EVIDENCIJA ARTIKALA I RACUNA ZA PRODAVCE ***************\n\n")
    opcija = ""
    while opcija not in ['1', '2', '3', '4', '5', '6']:
        print("1 -> Police")
        print("2 -> Sekcije")
        print("3 -> Artikli")
        print("4 -> Stavke")
        print("5 -> Racuni")
        print("6 -> Izlaz iz aplikacije")
        print("-------------------------")
        opcija = input("Izaberite opciju: ")
        if opcija == '1':
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
                opt = int(input("Izaberite neku od opcija: "))

                if opt == 1:
                    police = Polica_rukovanje("Upisi/police.txt")
                    lista_polica = police.citanje_svih()
                    for i in lista_polica:
                        print(i)

                elif opt == 2:
                    p = Polica_rukovanje("Upisi/police.txt")
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
                    p = Polica_rukovanje("Upisi/police.txt")
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
                        p = Polica_rukovanje("Upisi/police.txt")
                        lista_polica = p.citanje_svih()
                        oznaka_za_pretragu = input("Unesite oznaku police za pretragu: ")
                        pretrazeno = p.pretraga_po_oznaci(lista_polica, oznaka_za_pretragu)
                        for i in pretrazeno:
                            print(i)
                    elif opt_pretraga == 2:
                        p = Polica_rukovanje("Upisi/police.txt")
                        lista_polica = p.citanje_svih()
                        red_za_pretragu = input("Unesite red police za pretragu: ")
                        pretrazeno = p.pretraga_po_redu(lista_polica, red_za_pretragu)
                        for i in pretrazeno:
                            print(i)
                    elif opt_pretraga == 3:
                        p = Polica_rukovanje("Upisi/police.txt")
                        lista_polica = p.citanje_svih()
                        kolona_za_pretragu = input("Unesite kolonu police za pretragu: ")
                        pretrazeno = p.pretraga_po_koloni(lista_polica, kolona_za_pretragu)
                        for i in pretrazeno:
                            print(i)
                    elif opt_pretraga == 4:
                        p = Polica_rukovanje("Upisi/police.txt")
                        lista_polica = p.citanje_svih()
                        pozicija_za_pretragu = input("Unesite pziciju police za pretragu: ")
                        pretrazeno = p.pretraga_po_poziciji(lista_polica, pozicija_za_pretragu)
                        for i in pretrazeno:
                            print(i)
                    elif opt_pretraga == 5:
                        p = Polica_rukovanje("Upisi/police.txt")
                        lista_polica = p.citanje_svih()
                        duzina_za_pretragu = float(input("Unesite duzinu police za pretragu: "))
                        pretrazeno = p.pretraga_po_duzini(lista_polica, duzina_za_pretragu)
                        for i in pretrazeno:
                            print(i)
                    elif opt_pretraga == 6:
                        p = Polica_rukovanje("Upisi/police.txt")
                        lista_polica = p.citanje_svih()
                        sirina_za_pretragu = float(input("Unesite sirinu police za pretragu: "))
                        pretrazeno = p.pretraga_po_sirini(lista_polica, sirina_za_pretragu)
                        for i in pretrazeno:
                            print(i)
                    elif opt_pretraga == 7:
                        p = Polica_rukovanje("Upisi/police.txt")
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
                            p = Polica_rukovanje("Upisi/police.txt")
                            lista_polica = p.citanje_svih()
                            smjer = input("Napisite '+' za opadajuci redoslijed, '-' za rastuci redoslijed: ")
                            sortirano = p.sortiranje_po_poziciji(lista_polica, smjer)
                            for i in sortirano:
                                print(i)
                elif opt == 6:
                    print("Prikazi artikle na polici")
                
                    a = Artikal_rukovanje("Upisi/artikli.txt")
                    lista_artikala = a.citanje_svih()
                    p = Polica_rukovanje("Upisi/police.txt")
                    lista_polica = p.citanje_svih()
                    for i in lista_polica:
                        print(i)

                    id_police = input("Unesite ID police: ")
                    artikli_u_polici = p.izlistaj_artikle(id_police, lista_artikala)
                    for i in artikli_u_polici:
                        print(i)
                
                while opt < 1 or opt > 7:
                    opt = int(input("Iaberite neku od postojecih opcija!: "))
            
        elif opcija == '2':
            print("Rad sa sekcijama!")
            opt = 0
            while opt != 6:
                print("1 -> Prikaz sekcija")
                print("2 -> Dodavanje sekcija")
                print("3 -> Izmjena sekcija")
                print("4 -> Pretraga sekcija")
                print("5 -> Vidi sve police i artikle u sekciji")
                print("6 -> Nazad")
                opt = int(input("Izaberi neku od opcija: "))

                if opt == 1:
                    s = Sekcija_rukovanje("Upisi/sekcije.txt")
                    lista_sekcija = s.citanje_svih()
                    for i in lista_sekcija:
                        print(i)

                elif opt == 2:
                    s = Sekcija_rukovanje("Upisi/sekcije.txt")
                    oznaka = str(input("Unesite oznaku sekcije koju dodajete: "))
                    naziv = str(input("Unesite naziv sekcije: "))
                    opis = str(input("Unesite opis sekcije: "))
                    pozicija = str(input("Unesite poziciju usekcije: "))
                    sekcija = Sekcija(oznaka, naziv, opis, pozicija)
                    s.upis_jednog(sekcija)
                
                elif opt == 3:
                    s = Sekcija_rukovanje("Upisi/sekcije.txt")
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
                        s = Sekcija_rukovanje("Upisi/sekcije.txt")
                        lista_sekcija = s.citanje_svih()
                        oznaka_za_pretragu = input("Unesite oznaku sekcije za pretragu: ")
                        pretrazeno = s.pretraga_po_oznaci(lista_sekcija, oznaka_za_pretragu)
                        for i in pretrazeno:
                            print(i)
                    
                    elif opt_pretraga == 2:
                        s = Sekcija_rukovanje("Upisi/sekcije.txt")
                        lista_sekcija = s.citanje_svih()
                        naziv_za_pretragu = input("Unesite naziv sekcije za pretragu: ")
                        pretrazeno = s.pretraga_po_nazivu(lista_sekcija, naziv_za_pretragu)
                        for i in pretrazeno:
                            print(i)

                    elif opt_pretraga == 3:
                        s = Sekcija_rukovanje("Upisi/sekcije.txt")
                        lista_sekcija = s.citanje_svih()
                        opis_za_pretragu = input("Unesite opis sekcije za pretragu: ")
                        pretrazeno = s.pretraga_po_opisu(lista_sekcija, opis_za_pretragu)
                        for i in pretrazeno:
                            print(i)

                    elif opt_pretraga == 4:
                        s = Sekcija_rukovanje("Upisi/sekcije.txt")
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

                    s = Sekcija_rukovanje("Upisi/sekcije.txt")

                    if opt_izlistaj == 1:
                        
                        s = Sekcija_rukovanje("Upisi/sekcije.txt")
                        lista_sekcija = s.citanje_svih()

                        p = Polica_rukovanje("Upisi/police.txt")
                        lista_polica = p.citanje_svih()

                        for l in lista_sekcija:
                            print(l)

                        id_sekcije = input("Unesite ID sekcije: ")
                        police = s.izlistaj_police(id_sekcije, lista_polica)
                        for i in police:
                            print(i)
                    
                    elif opt_izlistaj == 2:
                        
                        p = Polica_rukovanje("Upisi/police.txt")
                        lista_polica = p.citanje_svih()
                        
                        a = Artikal_rukovanje("Upisi/artikli.txt")
                        lista_aritkala = a.citanje_svih()

                        for l in lista_polica:
                            print(l)

                        id_police = input("Unesite ID police: ")
                        artikli = s.izlistaj_artikle(id_police, lista_aritkala)
                        for i in artikli:
                            print(i)





                while opt < 1 or opt > 6:
                    opt = int(input("Izaberite neku od postojecih opcija"))
        elif opcija == '3':
            print("Rad sa artiklima")
            opt = 0
            while opt != 6:
                print("1 -> Prikaz artikala")
                print("2 -> Dodavanje artikala")
                print("3 -> Izmjena artikala")
                print("4 -> Pretraga artikala")
                print("5 -> Sortiranje artikala")
                print("6 -> Nazad")
                opt = int(input("Izaberi neku od opcija: "))

                if opt == 1:
                    print("Meni ucitaj artikle")
                    artikli = Artikal_rukovanje("Upisi/artikli.txt")
                    lista_artikala = artikli.citanje_svih()
                    for l in lista_artikala:
                        print(l)

                elif opt == 2:
                    print("Meni Dodaj Artikal")
                    a = Artikal_rukovanje("Upisi/artikli.txt")
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
                    a = Artikal_rukovanje("Upisi/artikli.txt")
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
                        a = Artikal_rukovanje("Upisi/artikli.txt")
                        lista_artikala= a.citanje_svih()
                        oznaka_za_pretragu = input("Unesite oznaku artikla za pretragu: ")
                        pretrazeno = a.pretraga_po_oznaci(lista_artikala, oznaka_za_pretragu)
                        for i in pretrazeno:
                            print(i)

                    elif opt_pretraga == 2:
                        a = Artikal_rukovanje("Upisi/artikli.txt")
                        lista_artikala= a.citanje_svih()
                        naziv_za_pretragu = input("Unesite naziv artikla za pretragu: ")
                        pretrazeno = a.pretraga_po_nazivu(lista_artikala, naziv_za_pretragu)
                        for i in pretrazeno:
                            print(i)
                            
                    elif opt_pretraga == 3:
                        a = Artikal_rukovanje("Upisi/artikli.txt")
                        lista_artikala= a.citanje_svih()
                        opis_za_pretragu = input("Unesite opis artikla za pretragu: ")
                        pretrazeno = a.pretraga_po_opisu(lista_artikala, opis_za_pretragu)
                        for i in pretrazeno:
                            print(i)

                    elif opt_pretraga == 4:
                        a = Artikal_rukovanje("Upisi/artikli.txt")
                        lista_artikala= a.citanje_svih()
                        cijena_za_pretragu = input("Unesite cijenu artikla za pretragu: ")
                        pretrazeno = a.pretraga_po_cijeni(lista_artikala, cijena_za_pretragu)
                        for i in pretrazeno:
                            print(i)
                    
                    elif opt_pretraga == 5:
                        a = Artikal_rukovanje("Upisi/artikli.txt")
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
                        a = Artikal_rukovanje("Upisi/artikli.txt")
                        lista_artikala = a.citanje_svih()
                        smjer = input("Napisite '+' za opadajuci redoslijed, '-' za rastuci redoslijed: ")
                        sortirano = a.sortiranje_po_cijeni(lista_artikala, smjer)
                        for i in sortirano:
                            print(i)
                    elif opt_sortiranje == 2:
                        a = Artikal_rukovanje("Upisi/artikli.txt")
                        lista_artikala = a.citanje_svih()
                        smjer = input("Napisite '+' za opadajuci redoslijed, '-' za rastuci redoslijed: ")
                        sortirano = a.sortiranje_po_roku_trajanja(lista_artikala, smjer)
                        for i in sortirano:
                            print(i)

                while opt < 1 or opt > 6:
                    opt = int(input("Izaberite neku od postojecih opcija"))
                    
                    
                    
                    
        elif opcija == '4':
            print("")
            opt = ''
            while opt not in ['1', '2', '3', '4', '5', '6']:
                print("1 -> Prikaz stavki")
                print("2 -> Dodavanje stavki")
                print("3 -> Izmena stavki")
                print("4 -> Pretraga stavki")
                print("5 -> Sortiranje stvaki")
                print("6 -> Nazad")
                print("")
                opt = input("Izaberi neku od opcija")
        
                if opt == '1':
                    s = Stavka_rukovanje("Upisi/stavke.txt")
                    lista_stavki = s.citanje_svih()
                    for i in lista_stavki:
                        print(i)
                        print("")
                
                elif opt == '2':
                    s = Stavka_rukovanje("Upisi/stavke.txt")
                    try:
                        oznaka = str(input("Unesite oznaku: "))
                        kolicina = float(input("Unesite kolicinu: "))
                        ukupna_cijena = float(input("Unesite ukupnu cenu: "))
                        artikal = str(input("Unesite artikal: "))
                        racun = str(input("Unesite racun: "))
                        stavka = Stavka(oznaka, kolicina, ukupna_cijena, artikal, racun)
                        s.upis_jednog(stavka)
                    except ValueError:
                        print("Neispravni unosi!")

                elif opt == '3':
                    s = Stavka_rukovanje("Upisi/stavke.txt")
                    try:
                        oznaka = str(input("Unesite oznaku stavke koju zelite da zamjenite: "))
                        kolicina = float(input("Unesite kolicinu nove stavke: "))
                        ukupna_cijena = float(input("Unesite ukupnu cenu nove stavke: "))
                        artikal = str(input("Unesite novi artikal: "))
                        racun = str(input("Unesite novi racun: "))
                        stavka = Stavka(oznaka, kolicina, ukupna_cijena, artikal, racun)
                        s.izmjena_jednog(stavka)
                    except ValueError:
                        print("Neispravni unosi!")

                elif opt == '4':
                    print("")
                    opt_pretraga = ''
                    print("1 -> Pretraga po oznaci")
                    print("2 -> Pretraga po kolicini")
                    print("3 -> Pretraga po ukupnoj ceni")
                    print("")
                    opt_pretraga = input("Unesite pretragu: ")
                    print("")

                    if opt_pretraga == '1':
                        s = Stavka_rukovanje("Upisi/stavke.txt")
                        lista_stavki= s.citanje_svih()
                        oznaka_za_pretragu = input("Unesite oznaku stavke za pretragu: ")
                        print("")
                        pretrazeno = s.pretraga_po_oznaci(lista_stavki, oznaka_za_pretragu)
                        if not pretrazeno:
                            print("Ne postoji stavka sa trazenom oznakom.")
                        else:
                            for i in pretrazeno:
                                print(i)
                                print("")
                    elif opt_pretraga == '2':
                        s = Stavka_rukovanje("Upisi/stavke.txt")
                        lista_stavki= s.citanje_svih()
                        kolicina_za_pretragu = input("Unesite kolicinu stavke za pretragu: ")
                        print("")
                        pretrazeno = s.pretraga_po_kolicini(lista_stavki, kolicina_za_pretragu)
                        if not pretrazeno:
                            print("Ne postoji stavka za unetu kolicinu.")
                        else:
                            for i in pretrazeno:
                                print(i)
                                print("")
                    elif opt_pretraga == '3':
                        s = Stavka_rukovanje("Upisi/stavke.txt")
                        lista_stavki= s.citanje_svih()
                        ukupna_cijena_za_pretragu = input("Unesite ukupnu cenu stavke za pretragu: ")
                        print("")
                        pretrazeno = s.pretraga_po_ukupnoj_cijeni(lista_stavki, ukupna_cijena_za_pretragu)
                        if not pretrazeno:
                            print("Ne postoji stavka sa unetom cenom.")
                        else:
                            for i in pretrazeno:
                                print(i)
                                print("")
                    else:
                        print("Pogresan unos.")
                    

                elif opt == '5': 
                    print("Soritranje po kolicini")
                    print("")
                    s = Stavka_rukovanje("Upisi/stavke.txt")
                    lista_stavki = s.citanje_svih()
                    smjer = input("Unesite '+' za opadajuci redosled, '-' za rastuci redosled: ")
                    print("")
                    sortirano = s.sortiranje_po_kolicini(lista_stavki, smjer)
                    try:
                        for i in sortirano:
                            print(i)
                    except TypeError:
                        print('')

                        
                        
                        
                

        elif opcija == '5':
            print("")
            opt = ''
            while opt not in ['1', '2', '3', '4', '5', '6','7']:
                print("1 -> Prikaz racuna")
                print("2 -> Dodavanje racuna")
                print("3 -> Izmena racuna")
                print("4 -> Pretraga Racuna")
                print("5 -> Sortiranje racuna")
                print("6 -> Prikazi stavke i artikle na racunu")
                print("7 -> Nazad")
                print("")

                opt = input("Izaberi neku od opcija")
                print("")

                if opt == '1':
                    r = Racun_rukovanje("Upisi/racuni.txt")
                    lista_racuna = r.citanje_svih()
                    for l in lista_racuna:
                        print(l)
                        print("")
                
                elif opt == '2':
                    r = Racun_rukovanje("Upisi/racuni.txt")
                    try:
                        oznaka = str(input("Unesite oznaku: "))
                        prodavac = str(input("Unesite prodavca: "))
                        ukupna_cijena = float(input("Unesite ukupnu cenu: "))
                        datum = str(input("Unesite datum: "))
                        racun = Racun(oznaka, prodavac, ukupna_cijena, datum)
                        r.upis_jednog(racun)
                    except ValueError:
                        print("Neispravni unosi, pokusajte ponovo!")

                elif opt == '3':
                    r = Racun_rukovanje("Upisi/racuni.txt")
                    try:
                        oznaka = input("Unesite oznaku racuna koji zelite da zamenite: ")
                        oznaka = str(oznaka)
                        prodavac = input("Unesite prodavca novog racuna: ")
                        prodavac = str(prodavac)
                        ukupna_cijena = input("Unesite ukupnu cenu novog racuna: ")
                        ukupna_cijena = float(ukupna_cijena)
                        datum = input("Unesite datum novog racuna: ")
                        datum = str(datum)
                        racun = Racun(oznaka, prodavac, ukupna_cijena, datum)
                        r.izmjena_jednog(racun)
                    except ValueError:
                        print("Neispravni unosi, pokusajte ponovo!")
                
                elif opt == '4':
                    print("")
                    opt_pretraga = ''
                    print("1 -> Pretraga po oznaci")
                    print("2 -> Pretraga po prodavcu")
                    print("3 -> Pretraga po ukupnoj ceni")
                    print("4 -> Pretraga po datumu")
                    print("")
                    opt_pretraga = input("Unesite pretragu: ")
                    print("")

                    if opt_pretraga == '1':
                        r = Racun_rukovanje("Upisi/racuni.txt")
                        lista_racuna= r.citanje_svih()
                        oznaka_za_pretragu = input("Unesite oznaku racuna za pretragu: ")
                        print("")
                        pretrazeno = r.pretraga_po_oznaci(lista_racuna, oznaka_za_pretragu)
                        if not pretrazeno:
                            print("Ne postoji trazena oznaka")
                        else:
                            for i in pretrazeno:
                                print(i)
                                print("")
                            
                    elif opt_pretraga == '2':
                        r = Racun_rukovanje("Upisi/racuni.txt")
                        lista_racuna= r.citanje_svih()
                        prodavac_za_pretragu = input("Unesite prodavca racuna za pretragu: ")
                        print("")
                        pretrazeno = r.pretraga_po_prodavcu(lista_racuna, prodavac_za_pretragu)
                        if not pretrazeno:
                            print("Ne postoji trazeni prodavac")
                        else:
                            for i in pretrazeno:
                                print(i)
                                print("")
                            
                    elif opt_pretraga == '3':
                        r = Racun_rukovanje("Upisi/racuni.txt")
                        lista_racuna= r.citanje_svih()
                        ukupna_cijena_za_pretragu = input("Unesite ukupnu cenu racuna za pretragu: ")
                        print("")
                        pretrazeno = r.pretraga_po_ukupnoj_cijeni(lista_racuna, ukupna_cijena_za_pretragu)
                        if not pretrazeno:
                            print("Ne postoji racun sa trazenom cenom.")
                        else:
                            for i in pretrazeno:
                                print(i)
                                print("")
                            
                    elif opt_pretraga == '4':
                        r = Racun_rukovanje("Upisi/racuni.txt")
                        lista_racuna= r.citanje_svih()
                        datum_za_pretragu = input("Unesite datum racuna za pretragu: ")
                        print("")
                        pretrazeno = r.pretraga_po_datumu(lista_racuna, datum_za_pretragu)
                        if not pretrazeno:
                            print("Ne postoji racun za trazeni datum.")
                        else:
                            for i in pretrazeno:
                                print(i)
                                print("")
                    else:
                        print("Pogresan unos!")
                    
                elif opt == '5':
                    print("")
                    opt_soritranje = ""
                    print("1 -> Soritranje po ukupnoj ceni")
                    print("2 -> Sortiranje po datumu")
                    print("")
                    opt_sortiranje = input("Izaberite jednu od opcija za sortiranje: ")
                    print("")

                    if opt_sortiranje == '1':
                        r = Racun_rukovanje("Upisi/racuni.txt")
                        lista_racuna = r.citanje_svih()
                        smjer = input("Unesite '+' za opadajuci redosled, '-' za rastuci redosled: ")
                        print("")
                        sortirano = r.sortiranje_po_ukupnoj_cijeni(lista_racuna, smjer)
                        try:
                            for i in sortirano:
                                print(i)
                        except TypeError:
                            print('')

                    elif opt_sortiranje == '2':
                        r = Racun_rukovanje("Upisi/racuni.txt")
                        lista_racuna = r.citanje_svih()
                        smjer = input("Unesite '+' za opadajuci redosled, '-' za rastuci redosled: ")
                        print("")
                        sortirano = r.sortiranje_po_datumu(lista_racuna, smjer)
                        try:
                            for i in sortirano:
                                print(i)
                        except TypeError:
                            print('')
                    else:
                        print("Pogresan unos.")
                            
                
                elif opt == '6':
                    print("Izlistaj stavke i artikle")
                    print("")
                    
                    r = Racun_rukovanje("Upisi/racuni.txt")
                    lista_racuna = r.citanje_svih()

                    a = Artikal_rukovanje("Upisi/artikli.txt")
                    lista_aritkala = a.citanje_svih()
                    
                    st = Stavka_rukovanje("Upisi/stavke.txt")
                    lista_stavki = st.citanje_svih()
                    
                    for i in lista_racuna:
                        print(i)
                        print("")
                    id_racuna = input("Unesite ID racuna: ")
                    print("")
                    stavke_i_artikli = r.stavke_i_artikli_u_racunu(id_racuna, lista_stavki, lista_aritkala)
                    for i in stavke_i_artikli:
                        print("stavka" + str(i["stavka"]) + ", artikal" + str(i["artikal"]))
                        print("")
                    
                    
        elif opcija == "6":               
            print("Dovidjenja!")
            exit()

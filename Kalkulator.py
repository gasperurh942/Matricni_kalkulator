import tkinter as tk
from Funkcije import *

glavno_okno = tk.Tk()

def zacni_program():
    
    def nalozi_matriko():
        if preberi('shranjena_matrika.txt') != '':
            matrika_z_nizi = preberi('shranjena_matrika.txt')
            stevilo_vrstic.insert(0, str(len(matrika_z_nizi)))
            stevilo_stolpcev.insert(0, str(len(matrika_z_nizi[0])))
            odpri_polje_za_matriko()
            st_vrstic = len(matrika_z_nizi)
            st_stolpcev = len(matrika_z_nizi[0])
            mreza_nicel = []
            for i in range(st_vrstic):
                mreza_nicel.append([])
                vrstica = tk.Frame(zgoraj)
                vrstica.grid(row = i, column = 0)
                for j in range(st_stolpcev):
                    mreza_nicel[i].append(Ulomek(0, 1))
                    mreza[(i, j)] = tk.Entry(vrstica, width = 4)
                    mreza[(i, j)].grid(row = i, column = j)
                    mreza[(i, j)].insert(0, matrika_z_nizi[i][j])
        else:
            obvestilo = tk.Tk()
            napis = tk.Label(obvestilo, text='Ni shranjene matrike.', width=20)
            napis.pack()
    
    def odpri_polje_za_matriko():
        global mreza_nicel
        global mreza

        if stevilo_vrstic.get() != '' and stevilo_stolpcev.get() != '':            
            st_vrstic = int(stevilo_vrstic.get())
            st_stolpcev = int(stevilo_stolpcev.get())
            gumb_nalozi_matriko.destroy()
            stevilo_vrstic.destroy()
            krat.destroy()
            stevilo_stolpcev.destroy()
            OK.destroy()
            mreza = {}
            mreza_nicel = []
            for i in range(st_vrstic):
                mreza_nicel.append([])
                vrstica = tk.Frame(zgoraj)
                vrstica.grid(row = i, column = 0)
                for j in range(st_stolpcev):
                    mreza_nicel[i].append(Ulomek(0, 1))
                    mreza[(i, j)] = tk.Entry(vrstica, width = 4)
                    mreza[(i, j)].grid(row = i, column = j)
                    
            def ponastavi():
                okno1.destroy()
                zacni_program()

            def pobrisi_matriko():
                mreza_nicel = []
                for i in range(st_vrstic):
                    mreza_nicel.append([])
                    for j in range(st_stolpcev):
                        mreza[(i, j)].delete(0, tk.END)

            def shrani_matriko():
                '''Spremeni vnešena števila iz tabele v seznam seznamov z ulomki in v
                prazna polja vpiše ničle.'''
                for i in range(st_vrstic):
                    for j in range(st_stolpcev):
                        niz = mreza[(i, j)].get()
                        if niz != '':
                            if '/' in niz:
                                par = niz.split('/')
                                mreza_nicel[i][j] = Ulomek(int(par[0]), int(par[1]))
                            else:
                                mreza_nicel[i][j] = Ulomek(int(niz), 1)
                return mreza_nicel

            def izracunaj_determinanto():
                '''Izračuna determinanto še ne pretvorjene matrike (uporabi funkcijo
                'shrani_matriko' in jo izračuna iz oblike seznama seznamov) ter jo
                izpiše v novem oknu. V obliki seznama predpostavi,da gre za kvadratno
                matriko, drugače javi, da ni ustreznih dimenzij.'''
                matrika_objekt = shrani_matriko()
                if st_vrstic == st_stolpcev:
                    determinanta_niz = str(determinanta(matrika_objekt))
                else:
                    determinanta_niz = 'Matrika ni ustreznih dimenzij.'

                koncno_okno = tk.Tk()
                izpis = tk.Label(koncno_okno, text=determinanta_niz)
                izpis.pack()

            def izracunaj_inverz():
                '''Izračuna inverz še ne pretvorjene matrike (uporabi funkcijo
                'shrani_matriko' in ga izračuna iz oblike seznama seznamov) ter ga
                izpiše v novem oknu (v obliki matrike, ne seznama).'''
                matrika_objekt = shrani_matriko()

                koncno_okno = tk.Tk()

                def shrani_v_knjiznico():
                    with open('shranjena_matrika.txt', 'w') as knjiznica:
                        for i in inv:
                            vrstica = ''
                            for clen in i:
                                vrstica = vrstica + str(clen) + '|'
                            print(vrstica, file=knjiznica)
                        koncno_okno_spodaj.destroy()

                if st_stolpcev != st_vrstic:
                    izpis = tk.Label(koncno_okno, text='Matrika ni ustreznih dimenzij\nza računanje inverza.')
                    izpis.pack()
                elif determinanta(matrika_objekt) == Ulomek(0, 1):
                    izpis = tk.Label(koncno_okno, text=inverz(matrika_objekt))
                    izpis.pack()
                else:
                    inv = inverz(matrika_objekt)
                    for i in range(st_vrstic):
                        vrstica = tk.Frame(koncno_okno)
                        vrstica.grid(row = i, column = 0)
                        for j in range(st_stolpcev):
                            clen = tk.Label(vrstica, text=str(inv[i][j]),
                                            height=2, width=5)
                            clen.grid(row = 0, column = j)
                            
                    koncno_okno_spodaj = tk.Frame(koncno_okno)
                    gumb_shrani = tk.Button(koncno_okno_spodaj, text='Shrani matriko',
                                            command = shrani_v_knjiznico)
                    
                    koncno_okno_spodaj.grid(row = st_vrstic, column = 0)
                    gumb_shrani.pack()

            def izracunaj_transponiranko():
                '''Izračuna transponiranko še ne pretvorjene matrike (uporabi funkcijo
                'shrani_matriko' in jo izračuna iz oblike seznama seznamov) ter jo
                izpiše v novem oknu (v obliki matrike, ne seznama).'''
                matrika_objekt = shrani_matriko()

                koncno_okno = tk.Tk()

                def shrani_v_knjiznico():
                    with open('shranjena_matrika.txt', 'w') as knjiznica:
                        for i in tra:
                            vrstica = ''
                            for clen in i:
                                vrstica = vrstica + str(clen) + '|'
                            print(vrstica, file=knjiznica)
                        koncno_okno_spodaj.destroy()
                        
                tra = transponiranka(matrika_objekt)
                for i in range(st_stolpcev):
                    vrstica = tk.Frame(koncno_okno)
                    vrstica.grid(row = i, column = 0)
                    for j in range(st_vrstic):
                        clen = tk.Label(vrstica, text=str(tra[i][j]),
                                        height=2, width=5)
                        clen.grid(row = 0, column = j)

                koncno_okno_spodaj = tk.Frame(koncno_okno)
                gumb_shrani = tk.Button(koncno_okno_spodaj, text='Shrani matriko',
                                        command = shrani_v_knjiznico)
                
                koncno_okno_spodaj.grid(row = st_stolpcev, column = 0)
                gumb_shrani.pack()

            def zmnozi_s_skalarjem():
                matrika_objekt = shrani_matriko()
                #faktor
                niz = zapisi_faktor.get()
                sez = niz.split('/')
                stevec = int(sez[0])
                imenovalec = int(sez[1])
                faktor = Ulomek(stevec, imenovalec)

                produkt = mnozenje_s_skalarjem(matrika_objekt, faktor)
                koncno_okno = tk.Tk()

                def shrani_v_knjiznico():
                    with open('shranjena_matrika.txt', 'w') as knjiznica:
                        for i in produkt:
                            vrstica = ''
                            for clen in i:
                                vrstica = vrstica + str(clen) + '|'
                            print(vrstica, file=knjiznica)
                        koncno_okno_spodaj.destroy()

                for i in range(st_vrstic):
                    vrstica = tk.Frame(koncno_okno)
                    vrstica.grid(row = i, column = 0)
                    for j in range(st_stolpcev):
                        clen = tk.Label(vrstica, text=str(produkt[i][j]),
                                        height=2, width=5)
                        clen.grid(row = 0, column = j)

                koncno_okno_spodaj = tk.Frame(koncno_okno)
                gumb_shrani = tk.Button(koncno_okno_spodaj, text='Shrani matriko',
                                        command = shrani_v_knjiznico)
                
                koncno_okno_spodaj.grid(row = st_vrstic, column = 0)
                gumb_shrani.pack()
                        
            def potenciraj():
                matrika_objekt = shrani_matriko()
                eksponent = int(zapisi_eksponent.get())

                rezultat = potenca(matrika_objekt, eksponent)
                koncno_okno = tk.Tk()

                def shrani_v_knjiznico():
                    with open('shranjena_matrika.txt', 'w') as knjiznica:
                        for i in rezultat:
                            vrstica = ''
                            for clen in i:
                                vrstica = vrstica + str(clen) + '|'
                            print(vrstica, file=knjiznica)
                        koncno_okno_spodaj.destroy()

                if st_stolpcev != st_vrstic:
                    napis = tk.Label(koncno_okno, text='Matrika ni ustreznih dimenzij')
                    napis.pack()
                elif determinanta(matrika_objekt) == Ulomek(0, 1) and eksponent < 0:
                    return None
                else:
                    for i in range(st_vrstic):
                        vrstica = tk.Frame(koncno_okno)
                        vrstica.grid(row = i, column = 0)
                        for j in range(st_stolpcev):
                            clen = tk.Label(vrstica, text=str(rezultat[i][j]),
                                            height=2, width=5)
                            clen.grid(row = 0, column = j)

                    koncno_okno_spodaj = tk.Frame(koncno_okno)
                    gumb_shrani = tk.Button(koncno_okno_spodaj, text='Shrani matriko',
                                            command = shrani_v_knjiznico)
                    
                    koncno_okno_spodaj.grid(row = st_vrstic, column = 0)
                    gumb_shrani.pack()
                
            gumb_ponastavi = tk.Button(prva_vrsta, text='Ponastavi', width=15,
                                       command=ponastavi)
            gumb_pobrisi = tk.Button(prva_vrsta, text='Pobriši', width=15,
                                     command=pobrisi_matriko)
            gumb0 = tk.Button(spodaj, text='Determinanta', width=20,
                              command=izracunaj_determinanto)
            gumb1 = tk.Button(spodaj, text='Inverz', width=20,
                              command=izracunaj_inverz)
            gumb2 = tk.Button(spodaj, text='Transponiranka', width=20,
                              command=izracunaj_transponiranko)
            gumb4 = tk.Frame(spodaj, width=20)
            zapisi_faktor = tk.Entry(gumb4, width=6)
            gumb41 = tk.Button(gumb4, text='Zmnoži s skalarjem:', width=14,
                               command=zmnozi_s_skalarjem)
            gumb5 = tk.Frame(spodaj, width=20)
            zapisi_eksponent = tk.Entry(gumb5, width=6)
            gumb51 = tk.Button(gumb5, text='Potenciraj na:', width=14,
                               command=potenciraj)
            
            gumb_ponastavi.grid(row = 0, column = 0)
            gumb_pobrisi.grid(row = 0, column = 1)
            gumb0.pack()
            gumb1.pack()
            gumb2.pack()
            gumb4.pack()
            zapisi_faktor.grid(row = 0, column = 1)
            zapisi_faktor.insert(0, '0')
            gumb41.grid(row = 0, column = 0)
            gumb5.pack()
            zapisi_eksponent.grid(row = 0, column = 1)
            zapisi_eksponent.insert(0, '0')
            gumb51.grid(row = 0, column = 0)                      

            def dodaj_matriko():
                gumb3.destroy()
                zgoraj2 = tk.Frame(okno1)
                spodaj2 = tk.Frame(okno1)
                prva_vrsta2 = tk.Frame(okno1)
                prva_vrsta2.pack()
                zgoraj2.pack()
                spodaj2.pack()
                
                def odpri_novo_polje_za_matriko():
                    st_vrstic2 = int(stevilo_vrstic2.get())
                    st_stolpcev2 = int(stevilo_stolpcev2.get())
                    stevilo_vrstic2.destroy()
                    krat2.destroy()
                    stevilo_stolpcev2.destroy()
                    OK2.destroy()
                    mreza2 = {}
                    mreza_nicel2 = []
                    for i in range(st_vrstic2):
                        mreza_nicel2.append([])
                        vrstica = tk.Frame(zgoraj2)
                        vrstica.grid(row = i, column = 0)
                        for j in range(st_stolpcev2):
                            mreza_nicel2[i].append(Ulomek(0, 1))
                            mreza2[(i, j)] = tk.Entry(vrstica, width = 4)
                            mreza2[(i, j)].grid(row = i, column = j)

                    def shrani_matriko2():
                        '''Spremeni vnešena števila iz tabele 2 v seznam seznamov z ulomki
                        in v prazna polja vpiše ničle.'''
                        for i in range(st_vrstic2):
                            for j in range(st_stolpcev2):
                                niz = mreza2[(i, j)].get()
                                if niz != '':
                                    if '/' in niz:
                                        par = niz.split('/')
                                        mreza_nicel2[i][j] = Ulomek(int(par[0]), int(par[1]))
                                    else:
                                        mreza_nicel2[i][j] = Ulomek(int(niz), 1)
                        return mreza_nicel2
                    
                    def sestej():
                        matrika1 = shrani_matriko()
                        matrika2 = shrani_matriko2()
                        
                        koncno_okno = tk.Tk()
                        vsota = sestevanje(matrika1, matrika2)

                        def shrani_v_knjiznico():
                            with open('shranjena_matrika.txt', 'w') as knjiznica:
                                for i in vsota:
                                    vrstica = ''
                                    for clen in i:
                                        vrstica = vrstica + str(clen) + '|'
                                    print(vrstica, file=knjiznica)
                                koncno_okno_spodaj.destroy()

                        if (vsota == 'Matriki nimata enako dolgih stolpcev.' or
                            vsota == 'Matriki nimata enakega števila vrstic.'):
                            napis = tk.Label(koncno_okno, text=vsota)
                            napis.pack()
                        else:
                            for i in range(st_vrstic2):
                                vrstica = tk.Frame(koncno_okno)
                                vrstica.grid(row = i, column = 0)
                                for j in range(st_stolpcev2):
                                    clen = tk.Label(vrstica, text=str(vsota[i][j]),
                                                    height=2, width=5)
                                    clen.grid(row = 0, column = j)

                            koncno_okno_spodaj = tk.Frame(koncno_okno)
                            gumb_shrani = tk.Button(koncno_okno_spodaj, text='Shrani matriko',
                                                    command = shrani_v_knjiznico)
                            
                            koncno_okno_spodaj.grid(row = st_vrstic, column = 0)
                            gumb_shrani.pack()

                    def zmnozi():
                        matrika1 = shrani_matriko()
                        matrika2 = shrani_matriko2()

                        koncno_okno = tk.Tk()
                        produkt = mnozenje(matrika1, matrika2)

                        def shrani_v_knjiznico():
                            with open('shranjena_matrika.txt', 'w') as knjiznica:
                                for i in produkt:
                                    vrstica = ''
                                    for clen in i:
                                        vrstica = vrstica + str(clen) + '|'
                                    print(vrstica, file=knjiznica)
                                koncno_okno_spodaj.destroy()
                        
                        if produkt == 'Množenje ni mogoče.':
                            napis = tk.Label(koncno_okno, text=produkt)
                            napis.pack()
                        else:
                            for i in range(len(matrika1)):
                                vrstica = tk.Frame(koncno_okno)
                                vrstica.grid(row = i, column = 0)
                                for j in range(len(matrika2[0])):
                                    clen = tk.Label(vrstica, text=str(produkt[i][j]),
                                                    height=2, width=5)
                                    clen.grid(row = 0, column = j)

                            koncno_okno_spodaj = tk.Frame(koncno_okno)
                            gumb_shrani = tk.Button(koncno_okno_spodaj, text='Shrani matriko',
                                                    command = shrani_v_knjiznico)
                            
                            koncno_okno_spodaj.grid(row = st_vrstic, column = 0)
                            gumb_shrani.pack()

                    gumb30 = tk.Button(spodaj2, text='Seštej', width=20,
                                       command=sestej)
                    gumb31 = tk.Button(spodaj2, text='Zmnoži', width=20,
                                       command=zmnozi)

                    gumb30.pack()
                    gumb31.pack()

                stevilo_vrstic2 = tk.Entry(zgoraj2, width = 4)
                krat2 = tk.Label(zgoraj2, text=' X ', width = 4)
                stevilo_stolpcev2 = tk.Entry(zgoraj2, width = 4)
                OK2 = tk.Button(spodaj2, text='Nastavi velikost matrike', width=20,
                                command=odpri_novo_polje_za_matriko)

                stevilo_vrstic2.grid(row = 0, column = 0)
                krat2.grid(row = 0, column = 1)
                stevilo_stolpcev2.grid(row = 0, column = 2)
                OK2.pack()
                
            gumb3 = tk.Button(spodaj, text='Dodaj matriko', width=20,
                              command=dodaj_matriko)

            gumb3.pack()
        
    okno1 = tk.Frame(glavno_okno)

    okno1.grid(row = 0, column = 0)

    prva_vrsta = tk.Frame(okno1)
    zgoraj = tk.Frame(okno1)
    spodaj = tk.Frame(okno1)

    prva_vrsta.pack()
    zgoraj.pack()
    spodaj.pack()
    
    gumb_nalozi_matriko = tk.Button(prva_vrsta, text='Naloži shranjeno matriko',
                                    width=20,
                                    command=nalozi_matriko)
    stevilo_vrstic = tk.Entry(zgoraj, width = 4)
    krat = tk.Label(zgoraj, text=' X ', width = 4)
    stevilo_stolpcev = tk.Entry(zgoraj, width = 4)
    OK = tk.Button(spodaj, text='Nastavi velikost matrike', width=20,
                   command=odpri_polje_za_matriko)
    
    gumb_nalozi_matriko.pack()
    stevilo_vrstic.grid(row = 0, column = 0)
    krat.grid(row = 0, column = 1)
    stevilo_stolpcev.grid(row = 0, column = 2)
    OK.pack()

    okno1.mainloop()

zacni_program()

glavno_okno.mainloop()


import vislice

def izpis_igre(igra):
    return f"""{igra.pravilni_del_gesla()}
    
Nepravilni ugibi: {igra.nepravilni_ugibi()}
Preostalo število ugibanj : {vislice.STEVILO_DOVOLJENIH_NAPAK - igra.št_napak() +1}"""

def izpis_zmage(igra):
    return f"""ČESTITAM USPELO TI JE!   
    Geslo je bilo; {igra.geslo}"""

def izpis_poraza(igra):
    return f"Žal ni šlo, geslo je bilo; {igra.geslo}. Več sreče prihodnjič."

def zahtevaj_vnos():
    return(input("Ugibaj črko: "))

def poženi_vmesnik():
    igra = vislice.nova_igra()

    while True:
        print(izpis_igre(igra))
        crka = zahtevaj_vnos()
        stanje = igra.ugibaj(crka)

        if stanje == vislice.ZMAGA:
            print(izpis_zmage(igra))
            break
        elif stanje == vislice.PORAZ:
            print(izpis_poraza(igra))
            break

poženi_vmesnik()


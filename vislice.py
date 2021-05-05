STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA, PONOVLJENA_CRKA, NAPACNA_CRKA = "+", "o", "-"
ZAČETEK = "S"
ZMAGA, PORAZ = "W", "L"

class Vislice:
    def __init__(self):
        self.igre = {}
        self.max_id = 0

    def prost_id_igre(self):
        self.max_id += 1
        return self.max_id

    def nova_igra(self):
        nov_id = self.prost_id_igre()
        sveza_igra = nova_igra(bazen_besed)

        self.igre[nov_id] = (sveza_igra, ZAČETEK)
        return nov_id

    def ugibaj(self, id_igre, crka):
        #Najdi
        igra, _ = self.igre[id_igre]

        #Posodobi z delegiranjem
        novo_stanje = igra.ugibaj(crka)
        
        #Pospravi v slovarju
        self.igre[id_igre] = (igra, novo_stanje)

class Igra:
    def __init__(self, geslo, črke=[]):
        self.geslo = geslo
        self.črke = črke 
    
    def napačne_črke(self):
        seznam = []
        for črka in self.črke:
            if črka.upper() not in self.geslo.upper():
                seznam.append(črka)
        return seznam

    def pravilne_črke(self):
        seznam = []
        for črka in self.črke:
            if črka in self.geslo:
                seznam.append(črka)
        return seznam

    def št_napak(self):
        return len(self.napačne_črke())

    def zmaga(self):
        return not self.poraz() and len(set(self.pravilne_črke())) == len(set(self.geslo)) 

    def poraz(self):
        return self.št_napak() > STEVILO_DOVOLJENIH_NAPAK
            

    def pravilni_del_gesla(self):
        niz = ""
        for crka in self.geslo.upper():
            if crka.upper() in self.črke:
                niz += crka
            else:
                niz += "_"
        return niz

    def nepravilni_ugibi(self):
        niz = ""
        for znak in self.napačne_črke():
            niz += f"{znak} "
        return niz
    
    def ugibaj(self, črka):
        črka = črka.upper()
        if črka in self.črke:
            return PONOVLJENA_CRKA 
        
        self.črke.append(črka)

        if self.poraz() == True:
            return PORAZ
        elif self.zmaga() == True:
            return ZMAGA
        elif črka in self.geslo:
            return PRAVILNA_CRKA
        elif črka not in self.geslo:
            return NAPACNA_CRKA
        
with open("besede.txt", encoding="utf8") as f:
    bazen_besed = f.read().split()


import random

def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo)
    



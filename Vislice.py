import bottle
import Modul

vislice = Modul.Vislice()

@bottle.get("/")
def index():
    return bottle.template("index.tpl")

@bottle.post("/igra/")
def nova_igra():

    vislice = Modul.Vislice.preberi_iz_datoteke(
        Modul.DATOTEKA_ZA_SHRANJEVANJE
    )
    id_igre = vislice.nova_igra()
    novi_url = f"/igra/{id_igre}/"

    vislice.zapisi_v_datoteko(Modul.DATOTEKA_ZA_SHRANJEVANJE)

    bottle.redirect(novi_url)

@bottle.get("/igra/<id_igre:int>/")
def pokazi_igro(id_igre):
    vislice = Modul.Vislice.preberi_iz_datoteke(
        Modul.DATOTEKA_ZA_SHRANJEVANJE
    )
    trenutna_igra, trenutno_stanje = vislice.igre[id_igre]
    vislice.zapisi_v_datoteko(Modul.DATOTEKA_ZA_SHRANJEVANJE)
    return bottle.template("igra.tpl", igra=trenutna_igra, stanje=trenutno_stanje)

@bottle.post("/igra/<id_igre:int>/")
def ugibaj_na_igri(id_igre):
    vislice = Modul.Vislice.preberi_iz_datoteke(
        Modul.DATOTEKA_ZA_SHRANJEVANJE
    )
    ugibana = bottle.request.forms["crka"]
    vislice.ugibaj(id_igre, ugibana) 
    vislice.zapisi_v_datoteko(Modul.DATOTEKA_ZA_SHRANJEVANJE)
    bottle.redirect(f"/igra/{id_igre}/")
    
@bottle.route("/img/<file_path:path>")
def img_static(file_path):
    return bottle.static_file(file_path, "img")


bottle.run(reloader=True, debug=True)
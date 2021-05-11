import bottle
import Modul

COOKIE_SECRET = "KJNFOR90OKEIJ03POJR02JRO3'oif3j20k'2e3e20"

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

    bottle.response.set_cookie("ID_IGRE", str(id_igre), path="/", secret=COOKIE_SECRET)

    bottle.redirect("/igraj/")


@bottle.get("/igraj/")
def pokazi_igro():

    id_igre = int(bottle.request.get_cookie("ID_IGRE", secret=COOKIE_SECRET))

    vislice = Modul.Vislice.preberi_iz_datoteke(
        Modul.DATOTEKA_ZA_SHRANJEVANJE
    )
    trenutna_igra, trenutno_stanje = vislice.igre[id_igre]
    vislice.zapisi_v_datoteko(Modul.DATOTEKA_ZA_SHRANJEVANJE)
    return bottle.template("igra.tpl", igra=trenutna_igra, stanje=trenutno_stanje)


@bottle.post("/igraj/")
def ugibaj_na_igri():
    id_igre = int(bottle.request.get_cookie("ID_IGRE", secret=COOKIE_SECRET))

    vislice = Modul.Vislice.preberi_iz_datoteke(
        Modul.DATOTEKA_ZA_SHRANJEVANJE
    )
    ugibana = bottle.request.forms["crka"]
    vislice.ugibaj(id_igre, ugibana) 
    vislice.zapisi_v_datoteko(Modul.DATOTEKA_ZA_SHRANJEVANJE)
    bottle.redirect(f"/igraj/")
    
@bottle.route("/img/<file_path:path>")
def img_static(file_path):
    return bottle.static_file(file_path, "img")


bottle.run(reloader=True, debug=True)
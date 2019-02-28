# Recipebook

### Documentation in Finnish

## Kuvaus

Recipebook on websovellus, johon käyttäjät voivat jakaa omia reseptejään ja lukea muiden reseptejä.
Reseptejä voidaan kommentoida ja äänestää. Jokainen resepti sisältää yhden tai useamman tagin esim.
"jälkiruoka", "juoma" tai "välipala". Yksittäinen resepti sisältää raaka-ainekentän, valmistusohjeen
sekä vapaan "vinkit" kentän.

## Toimintoja

- Kirjautuminen ja rekisteröityminen
- Reseptien lisäys, poisto ja muokkaus
- Reseptien kommentointi ja äänestys
- Ylläpitäjällä käyttäjien lisäys muokkaus ja poisto ominaisuudet

Sovellus on toteutettu Python Flaskilla, Helsingin Yliopiston Tietokantasovellus harjoitustyötä
varten.

Sovellus on toiminnassa osoitteessa

## Testitunnukset

käyttäjä: testuser

salasana: testpassword

(huom. älä rekisteröidy palveluun käyttämällä salasanaa, jota et halua jakaa koko maailmalle, suojaus on puutteellinen)

## Linkkejä

[Heroku](https://recipebook-pro.herokuapp.com/)

[käyttäjätarinat](https://github.com/jonitaajamo/recipebook/blob/master/documentation/user_stories.md)

[tietokantakaavio](https://github.com/jonitaajamo/recipebook/blob/master/documentation/database_info/uml_chart.jpg)

[CREATE TABLE -lauseet](https://github.com/jonitaajamo/recipebook/blob/master/documentation/database_info/create_table.md)

[loppudokumentti](https://github.com/jonitaajamo/recipebook/blob/master/documentation/conclusion.md)

## Asennus paikallisesti

- Lataa Git-repositorio koneellesi zip-pakettina tai komennolla `git clone https://github.com/jonitaajamo/recipebook.git`
- Navigoi projektin juureen ja luo virtuaaliympäristö komennolla `python3 -m venv venv`
- Käynnistä virtuaaliympäristö komennolla `source venv/bin/activate`
- Sovelluksen ajamiseksi tarvitset ohjelmat pip, python3 ja sqlite3
- Asenna riippuvuudet komennolla `pip install -r requirements`
- Aja `python3 run.py`

## Käyttöohjeet

- Tallettaaksesi uusia reseptejä tulee sinun luoda tunnus
- Tallenna uusi resepti navigoimalla välilehdelle "Post a recipe"
- Kaikki reseptit ovat listattuna sivulla "All recipes"
- Reseptit löytyvät kategorioittain sivulta "Categories"
- Tarkastellaksesi yksittäistä reseptiä, klikkaa listalta löytyvää linkkiä
- Reseptejä voidaan kommentoida reseptin sivulta

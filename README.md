# Recipebook

## Kuvaus

Recipebook on websovellus, johon käyttäjät voivat jakaa omia reseptejään ja lukea muiden reseptejä.
Reseptejä voidaan kommentoida ja äänestää. Jokainen resepti sisältää yhden tai useamman tagin esim.
"jälkiruoka", "juoma" tai "välipala". Yksittäinen resepti sisältää raaka-ainekentän, valmistusohjeen
sekä vapaan "vinkit" kentän.

Järjestelmän ylläpitäjä voi lisätä, muokata ja poistaa reseptejä ja kommentteja.

## Toimintoja

- Kirjautuminen ja rekisteröityminen
- Reseptien lisäys, poisto ja muokkaus
- Reseptien kommentointi ja äänestys
- Ylläpitäjällä käyttäjien lisäys muokkaus ja poisto ominaisuudet

Sovellus totetutetaan Python Flaskilla Helsingin Yliopiston Tietokantasovellus harjoitustyökurssia
varten.

Sovellus on toiminnassa osoitteessa

## Testitunnukset

käyttäjä: testuser

salasana: testpassword

(huom. älä rekisteröidy palveluun käyttämällä salasanaa, jota et halua jakaa koko maailmalle, suojaus on toistaiseksi puutteellinen)

## Linkkejä

[Heroku](https://recipebook-pro.herokuapp.com/)

[käyttäjätarinat](https://github.com/jonitaajamo/recipebook/blob/master/documentation/user_stories.md)

[tietokantakaavio](https://github.com/jonitaajamo/recipebook/blob/master/documentation/database_info/uml_diagram.jpg)
(WIP)

## Asennus paikallisesti

- Lataa Git-repositorio koneellesi esim. zip-pakettina
- Navigoi projektin juureen ja luo virtuaaliympäristö komennolla `python3 -m venv venv`
- Käynnistä virtuaaliympäristö komennolla `source venv/bin/activate`
- Asenna riippuvuudet komennolla `pip install -r requirements`
- Aja `python3 run.py`

## Käyttöohjeet

- Tallettaaksesi uusia reseptejä tulee sinun luoda tunnus
- Tallenna uusi resepti navigoimalla välilehdelle "Post a recipe"
- Kaikki reseptit ovat listattuna sivulla "All recipes"
- Tarkastellaksesi yksittäistä reseptiä, klikkaa listalta löytyvää linkkiä
- Reseptejä voidaan kommentoida reseptin sivulta

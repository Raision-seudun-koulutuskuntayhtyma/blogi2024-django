# Blogi2024/Django

Blogiesimerkki Djangolla koodattuna

## Django-projektin aloittaminen

1. Tee repository GitHubiin

    1. Valitse sopiva nimi ja omistaja (oma vai organisaatio)
    2. Kirjoita kuvaus
    3. Valitse julkinen vai yksityinen (public/private)
    4. Valitse .gitignore-templateksi Python
    5. Klikkaa "Create repository"

2. Kloonaa repository omalle koneelle

    1. Klikkaa "Code"-nappia
    2. Valitse "Open with GitHub Desktop", jos haluat käyttää sitä tai
       kopioi repon URL leikepöydälle
    3. Jos menet GitHub-desktopin kautta, niin cloonaa sillä johonkin
       kansioon ja valitse Open with VSCode
    4. Jos menet URLin kautta, niin valitse VSCodessa Clone Git
       Repository ja syötä URL leikepöydältä

3. Luo virtuaaliympäristö (virtualenv tai venv)

    1. Avaa VSCodessa uusi terminaali (Terminal -> New Terminal)
    2. Kirjoita terminaaliin: `python -m venv venv`

4. Aktivoi venv

    1. Luo väliaikainen python-tiedosto, esim. `jotain.py`
    2. Avaa kyseinen py-tiedosto VSCodessa ja katso, että
       venv-aktivoituu (alhaalla lukee 'venv': venv)
    3. Sulje edellinen terminaali ikkuna ja avaa uusi (New Terminal)
    4. Tarkista `pip -V` -komennolla, että venv on aktiivinen

5. Asenna Django virtuaaliympäristöön

    1. Aja terminaalissa: `pip install django`

6. Luo uusi django-projekti

    1. Aja: `django-admin startproject sivusto .`
        * Huomaa lopussa oleva piste.
        * Projektin nimi voi tietysti olla muukin kuin "sivusto"

7. Luo app django-projektiin

    1. Aja komento: `python manage.py startapp blogi`
        * `blogi` on apin nimi ja voit korvata sen millä tahansa tekstillä, mutta siinä ei saa olla välilyöntejä tai viivoja

8. Alusta tietokanta (migrate)

    1. Aja komento: `python manage.py migrate`

9. Luo pääkäyttäjä

    1. Aja komento: `python manage.py createsuperuser`

        * Valitse käyttäjätunnus ja salasana. esim. admin ja admin
        * Huom. salasana ei näy ruudulla (ei edes tähtiä)
        * Jos tulee valitus liian huonosta salasanasta, niin ohita
          kysymys kirjoittamalla "y" ja painamalla Enter

10. Luo launch.json runserverin ajamiseen

    1. Valitse debug-välilehti vasemmalta kuvakkeista. Siinä on
       play-ikooni ja ötökkä
    2. Klikkaa "create a launch.json file"
    3. Valitse "Python Debugger"
    4. Valitse "Django"
    5. Vaihda name-kohta mieleiseksi, esim. "Django runserver"
    6. Voit lisätä myös loppuun kohdan `"justMyCode": false`, jos haluat
       nähdä myös Djangon tai Pythonin koodin sisään

11. Poista turha `jotain.py`

12. Commitoi vaikka tässä välissä kaikki Git'iin

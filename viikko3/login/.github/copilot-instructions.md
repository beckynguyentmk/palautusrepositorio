# Copilot instructions for the login exercise

## Projekti ja komennot

Tämä on `uv`-projekti. Kaikki komennot suoritetaan projektikansiosta ja `uv run ...` -muodossa.

- Asenna riippuvuudet: `uv sync`
- Käynnistä Flask-sovellus: `uv run python src/index.py`
- Käynnistä kaikki Robot Framework -testit: `uv run robot src/tests`
- Käynnistä yksi testitiedosto: `uv run robot src/tests/home.robot`
- Käynnistä yksi testitapaus: `uv run robot -t "Click Login Link" src/tests/home.robot`

Sovellus käynnistyy paikallisesti porttiin `5001` (`http://localhost:5001`). Flaskin käynnistys on määritelty tiedostossa `src/index.py` ja se käyttää hostia `0.0.0.0` sekä porttia `5001`.

Robot Framework -testit toimivat vain, jos sovellus on jo käynnissä. Testit käyttävät `localhost:5001` ja kutsuvat testien resetointireittiä ennen testitapausten ajoa.

Tässä projektissa ei ole erillistä lint-komentoa. Validointi tapahtuu Robot Framework -testien kautta.

## Korkean tason arkkitehtuuri

Projekti on pieni Flask-sovellus, jossa logiikka on jaettu kerroksiin:

- `src/app.py` vastaa reiteistä ja HTTP-käsittelystä. Siellä on määritelty `/`, `/login`, `/register`, `/welcome`, `/ohtu`, `/logout` sekä testien resetointireitti `/tests/reset`.
- `src/services/user_service.py` sisältää käyttäjän kirjautumisen ja rekisteröinnin logiikan. Tässä tapahtuu käyttäjätunnuksen ja salasanan validointi.
- `src/repositories/user_repository.py` on tietovarasto, joka pitää käyttäjät in-memory-listassa. Tämä tarkoittaa, että sovelluksen tila nollautuu kun repositoryn sisältö tyhjennetään.
- `src/entities/user.py` on pieni datamalli käyttäjälle.
- `src/templates/*.html` sisältää Flaskin renderöidyt HTML-sivut.
- `src/tests/*.robot` ja `src/AppLibrary.py` ovat selaintason hyväksymistestejä. Ne avaavat sovelluksen selaimessa, täyttävät lomakkeita ja tarkistavat virheviestit.

Suurin kuva: Flask-reitti -> palveluvalidointi -> repository, ja UI-testit tarkastavat koko käyttäjän polun.

## Avainkonventiot

- Pidä `src/app.py` keskittyneenä reiteihin ja virheiden käsittelyyn. Älä siirrä liiketoimintalogiikkaa suoraan route-funktioihin.
- Säilytä repository/service -jako: reitit kutsuvat `user_service.*`, ja repository vastaa vain käyttäjälistan hallinnasta.
- Yhteensopivuus validoinnin kanssa: palvelu heittää `UserInputError` ja `AuthenticationError` -poikkeuksia, ja Flask näyttää ne flash-viesteinä.
- Testit olettavat sovelluksen olevan käynnissä portissa `5001`, ja ne nollaavat sovelluksen tilan ennen testejä `/tests/reset` -reitin kautta.
- Käyttäjät tallennetaan muistiin, joten sovelluksen toiminta perustuu in-memory-kokoelmaan eikä tietokantaan.
- Kun muutat kirjautumis- tai rekisteröintilogiikkaa, pidä virhetekstit ja UI-tekstit yhtenäisinä Robot-testeissä tarkistettujen merkkijonojen kanssa, esimerkiksi `Invalid username or password`, `Username must be at least 3 characters long` ja `Password must be at least 8 characters long`.

## Käyttäjätunnuksen ja salasanan validointi

Validointi tapahtuu `src/services/user_service.py` -tiedoston `UserService.validate` -metodissa.

Metodi tarkistaa ainakin:

- käyttäjänimi ja salasana eivät saa olla tyhjiä
- käyttäjätunnus ei saa olla olemassa jo ennestään
- käyttäjätunnuksen pituuden tulee olla vähintään 3 merkkiä
- salasanan pituuden tulee olla vähintään 8 merkkiä

Tämä logiikka on ydin rekisteröinnin ja kirjautumisen oikeellisuuden tarkistuksessa.

## Paikallinen kehitys-/testausvirta

Perusvirta projektille on:

1. `uv sync`
2. `uv run python src/index.py` sovelluksen käynnistämiseksi
3. `uv run robot src/tests` testien suorittamiseksi

Tämä tiedosto on tärkein ohjeistus Copilotille, kun työskentelet tässä projektissa.

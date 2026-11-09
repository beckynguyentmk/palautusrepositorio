# Kuinka hyödyllisiksi koit koodin täydennyksen ehdotukset?

Koodin täydennyksen ehdotukset toimivat mielestäni todella hyvin. Copilotin antama koodi oli oikeassa syntaksissa, ja se vastasi hyvin pyyntöön. 

# Pitikö Copilotin selitys Pylint-varoituksesta paikkansa?

Sen selitys oli selkeä, ja siinä oli hyviä esimerkkejä tilanteista, joissa pylint antaa varoituksia.

# Tekikö agentti toimivan ratkaisun, ja testit?

Koodi oli toimivaa, vaikka testihakemisto luotiin ilman __init__.py -tiedostoa, mikä aiheutti virheen suorittaessani komentoa uv run pytest src. 

# Eroaako testeissä joku siitä miten testejä tehtiin edellisellä viikolla?

Koska pyysin agenttia tekemään testit samaan muotoon kuin viikolla 1, testit olivat samanlaisia.

# Löysikö Pylint agentin koodista virheitä?

En löytänyt koodista mitään virheitä. Koodista kuitenkin puuttui muutamia testitapauksia, kuten tilanne, jossa top_goal_score -funktion parametrille annetaan arvo 0. Tällöin funktion pitäisi palauttaa tyhjä listä.

# Mitä muuta opit?

Opin, että tekoälyn generoimat terminaalikomennot ja koodi voivat olla virheellisiä. On tärkeää tarkistaa komennot ennen niiden suorittamista ja testata tuotettua koodia itse.

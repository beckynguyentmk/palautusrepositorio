# Minkälaisen ohjetiedoston agentti generoi, ja mitä jouduit korjaamaan?

Agentti generoi ohjetiedoston, joka sisälsi projektin kannalta tarvittavat tiedot. Koska olin määritellyt tiedostossa kaikki olennaiset vaatimukset, minun ei tarvinnut korjata mitään.

# Noudattiko agentti pyyntöä kirjoittaa testit ennen toteutusta?

Agentti noudatti pyyntöä pääosin hyvin. Se kirjoitti ensin testit ja varmisti, että ne epäonnistuivat ennen toiminnallisuuden toteuttamista.

# Kuinka paljon jouduit ohjaamaan agenttia matkan varrella?

Agenttia ei tarvinnut ohjata paljon, koska se noudatti pyyntöjäni vaihe vaiheelta. Jouduin kuitenkin pyytämään sitä vapauttamaan portin 5001, jotta pystyin käynnistämään Flask-sovelluksen itse.

# Hajosivatko testit, kun rikoit toteutuksen tarkoituksella?

Testit epäonnistuivat, kun rikoin toteutuksen tarkoituksella. Esimerkiksi kun muutin password_confirmation-tarkistusta niin, ettei salasanaa ja sen vahvistusta enää verrattu keskenään, rekisteröityminen onnistui eri salasanoilla. Tällöin vastaava testi epäonnistui odotetusti.

# Mitä uutta opit?

Opin, että agenttia voi pyytää generoimaan projektikohtaisen ohjetiedoston, joka sisältää työskentelyn kannalta hyödyllisiä tietoja. Tällainen tiedosto helpottaa agentin kanssa työskentelyä, koska sen avulla agentti ymmärtää paremmin projektin rakennetta, vaatimuksia ja käytäntöjä.

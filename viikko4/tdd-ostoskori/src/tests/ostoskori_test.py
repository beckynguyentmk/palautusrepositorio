import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def maito(self):
        return Tuote("Maito", 3)

    def leipa(self):
        return Tuote("Leipä", 4)

    def assert_empty_cart(self):
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.ostokset(), [])

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = self.maito()
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoksen_hinta(self):
        maito = self.maito()
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = self.maito()
        leipa = self.leipa()
        self.kori.lisaa_tuote(leipa)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_hinnan_summa(self):
        maito = self.maito()
        leipa = self.leipa()
        self.kori.lisaa_tuote(leipa)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 7)

    def test_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = self.maito()
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_saman_tuotteen_lisaamisen_jalkeen_hinnan_summa(self):
        maito = self.maito()
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 6)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_yhden_ostoksen(self):
        maito = self.maito()
        self.kori.lisaa_tuote(maito)
        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoksen_nimi_ja_lukumaara(self):
        maito = self.maito()
        self.kori.lisaa_tuote(maito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_kaksi_ostosta(self):
        maito = self.maito()
        leipa = self.leipa()
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipa)
        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_saman_tuotteen_lisaamisen_kaksi_kertaa_ostoskori_sisaltaa_yhden_ostoksen(self):
        maito = self.maito()
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_saman_tuotteen_kaksi_lisaamista_ostoksen_nimi_ja_lukumaara(self):
        maito = self.maito()
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        self.assertEqual(ostokset[0].tuotteen_nimi(), maito.nimi())
        self.assertEqual(ostokset[0].lukumaara(), 2)

    def test_saman_tuotteen_poistaminen_kerralla_jattaa_yhden_yksikon(self):
        maito = self.maito()
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        self.assertEqual(ostokset[0].lukumaara(), 1)

    def test_tuotteen_lisaamisen_jalkeen_poistaminen_tyhjentaa_korin(self):
        maito = self.maito()
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        self.assert_empty_cart()

    def test_tyhjentaminen_tyhjentaa_kahden_tuotteen_korin(self):
        maito = self.maito()
        leipa = self.leipa()
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipa)
        self.kori.tyhjenna()
        self.assert_empty_cart()

import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_right_name(self):
        tulos=str(self.stats.search("Semenko"))
        self.assertEqual(tulos,"Semenko EDM 4 + 12 = 16")

    def test_search_no_name(self):
        self.assertEqual(self.stats.search("apple"),None)

    def test_team_returns_players(self):
        tulos=self.stats.team('EDM')
        self.assertEqual([str(player) for player in tulos],['Semenko EDM 4 + 12 = 16',
                                                          'Kurri EDM 37 + 53 = 90',
                                                          'Gretzky EDM 35 + 89 = 124'])

    def test_team_not_found(self):
        self.assertEqual(self.stats.team('vnh'),[])

    def test_top_players_by_default(self):
        tulos=self.stats.top(2)
        self.assertEqual([str(player) for player in tulos],['Gretzky EDM 35 + 89 = 124',
                                                            'Lemieux PIT 45 + 54 = 99',
                                                            'Yzerman DET 42 + 56 = 98'])

    def test_top_players_by_points(self):
        tulos=self.stats.top(2,SortBy.POINTS)
        self.assertEqual([str(player) for player in tulos],['Gretzky EDM 35 + 89 = 124',
                                                            'Lemieux PIT 45 + 54 = 99',
                                                            'Yzerman DET 42 + 56 = 98'])

    def test_top_players_by_goals(self):
        tulos=self.stats.top(2,SortBy.GOALS)
        self.assertEqual([str(player) for player in tulos],['Lemieux PIT 45 + 54 = 99',
                                                            'Yzerman DET 42 + 56 = 98',
                                                            'Kurri EDM 37 + 53 = 90'])

    def test_top_players_by_assists(self):
        tulos=self.stats.top(2,SortBy.ASSISTS)
        self.assertEqual([str(player) for player in tulos],['Gretzky EDM 35 + 89 = 124',
                                                            'Yzerman DET 42 + 56 = 98',
                                                            'Lemieux PIT 45 + 54 = 99'])
        
        

import unittest

from player import Player
from player_stats import PlayerStats


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Aho", "FIN", 20, 35, "CAR", 75, 1),
            Player("Malkin", "RUS", 30, 42, "PIT", 82, 2),
            Player("Rantanen", "FIN", 35, 40, "COL", 80, 3),
            Player("Barkov", "FIN", 25, 28, "FLA", 79, 4),
            Player("Caufield", "USA", 24, 30, "MTL", 76, 5),
            Player("Kapanen", "FIN", 18, 22, "TOR", 58, 6),
            Player("Nylander", "SWE", 32, 28, "TOR", 81, 7),
        ]


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        self.stats = PlayerStats(PlayerReaderStub())

    def test_top_scorers_by_nationality_filters_and_sorts_by_points(self):
        players = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual([player.name for player in players], ["Rantanen", "Aho", "Barkov", "Kapanen"])
        self.assertGreater(
            players[0].goals + players[0].assists,
            players[1].goals + players[1].assists,
        )

    def test_top_scorers_by_nationality_returns_empty_list_when_no_match(self):
        players = self.stats.top_scorers_by_nationality("CAN")

        self.assertEqual(players, [])

    def test_top_scorers_by_team_filters_and_sorts_by_points(self):
        players = self.stats.top_scorers_by_team("TOR")

        self.assertEqual([player.name for player in players], ["Nylander", "Kapanen"])
        self.assertGreater(
            players[0].goals + players[0].assists,
            players[1].goals + players[1].assists,
        )

    def test_top_goal_scorers_returns_requested_number_sorted_by_goals(self):
        players = self.stats.top_goal_scorers(3)

        self.assertEqual([player.name for player in players], ["Malkin", "Rantanen", "Aho"])
        self.assertEqual(players[0].goals, 42)
        self.assertEqual(players[1].goals, 40)
        self.assertEqual(players[2].goals, 35)

    def test_top_goal_scorers_return_all_when_how_many_exceeds_players(self):
        players = self.stats.top_goal_scorers(20)

        self.assertEqual(len(players), 7)


if __name__ == "__main__":
    unittest.main()

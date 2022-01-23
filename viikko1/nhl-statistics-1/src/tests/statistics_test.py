from ast import Assert
import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(PlayerReaderStub())

    def test_search(self):
        player = self.statistics.search("Semenko")

        self.assertEqual(player.__str__(), "Semenko EDM 4 + 12 = 16")

    def test_search_none(self):
        player = self.statistics.search("Nobody")

        self.assertEqual(player.__str__(), "None")

    def test_team(self):
        team = self.statistics.team("PIT")
        player_str = ""
        for player in team:
            player_str = player.__str__()

        self.assertEqual(player_str, "Lemieux PIT 45 + 54 = 99")

    def test_team_none(self):
        team = self.statistics.team("ABC")
        test_team = []

        self.assertEqual(team, test_team)

    def test_top_scorers(self):
        top = self.statistics.top_scorers(2)
        self.assertEqual(len(top), 2)
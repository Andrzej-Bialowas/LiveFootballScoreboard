from unittest import TestCase
from Scoreboard import Scoreboard


class TestScoreboard(TestCase):
    def test_get_summary_validation_and_sorting(self):
        scoreboard = Scoreboard()
        scoreboard.startMatch("Patryk", "Andrzej")
        scoreboard.startMatch("Bartek", "Jeremis")
        scoreboard.startMatch("Aniela", "Pan Rudko")
        scoreboard.startMatch("Nikola", "blazej")
        scoreboard.updateMatch("Patryk", "Andrzej", 0, 1)
        scoreboard.updateMatch("Aniela", "Pan Rudko", 10, 1)
        scoreboard.updateMatch("Nikola", "Blazej", 5, 5)
        scoreboard.updateMatch("Bartek", "Jeremis", 6, 5)
        summary = scoreboard.getSummary()
        self.assertEqual(summary, ['Aniela 10 - Pan Rudko 1', 'Bartek 6 - Jeremis 5', 'Nikola 5 - Blazej 5', 'Patryk 0 - Andrzej 1'])

    def test_raise_exception_when_updated_match_does_not_exist(self):
        with self.assertRaises(Exception):
            scoreboard = Scoreboard()
            scoreboard.updateMatch("Nikolka", "Jeremis", 1, 0)

    def test_raise_exception_starting_match_with_the_same_team_twice(self):
        with self.assertRaises(Exception):
            scoreboard = Scoreboard()
            scoreboard.startMatch("Maciek", "Bozenka")
            scoreboard.startMatch("Mariusz", "Bozenka")

    def test_raise_exception_when_update_match_has_wrong_value(self):
        with self.assertRaises(ValueError):
            scoreboard = Scoreboard()
            scoreboard.startMatch("Nikolka", "Jeremis")
            scoreboard.updateMatch("Nikolka", "Jeremis", -3, 0)

    def test_finish_match_happy_path(self):
        scoreboard = Scoreboard()
        scoreboard.startMatch("Zenek", "Muniek")
        summary = scoreboard.getSummary()
        self.assertEqual(summary, ["Zenek 0 - Muniek 0"])
        scoreboard.updateMatch("Zenek", "Muniek", 0, 5)
        scoreboard.finishMatch("Zenek", "Muniek")
        summary = scoreboard.getSummary()
        self.assertEqual(summary, None)

    def test_update_match_happy_path(self):
        scoreboard = Scoreboard()
        scoreboard.startMatch("Jurek", "Heniek")
        summary = scoreboard.getSummary()
        self.assertEqual(summary, ["Jurek 0 - Heniek 0"])
        scoreboard.updateMatch("Jurek", "Heniek", 10, 10)
        summary = scoreboard.getSummary()
        self.assertEqual(summary, ["Jurek 10 - Heniek 10"])


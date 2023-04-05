import unittest
import pytest

class TestTeam(unittest.TestCase):
    def setUp(self):
        self.test_team = self.team(1, "name", "home", "country")

    def test_add_team(self):
        self.assertEqual(self.test_team.addTeam,112)







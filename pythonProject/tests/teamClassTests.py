import unittest
import pytest

from pythonProject.classes.teamClass import Team, check_team_id, get_team_by_id


class TestTeam(unittest.TestCase):

    def test_get_team(self):

        newTeam = Team(203, 'test', 'test', 'test')
        newTeam.addTeam()
        self.assertEqual(get_team_by_id(203).team_id, 203)
        self.assertEqual(get_team_by_id(203).name, 'test')
        self.assertEqual(get_team_by_id(203).country, 'test')
        self.assertEqual(get_team_by_id(203).home, 'test')
        #deleting test data
        newTeam.deleteTeam()

    def test_add_delete_team(self):
        newTeam = Team(204, 'test', 'test', 'test')
        newTeam.addTeam()
        self.assertTrue(check_team_id(204))
        newTeam.deleteTeam()
        self.assertFalse(check_team_id(204))

    def test_update_team(self):
        newTeam = Team(208, 'test', 'test', 'test')
        newTeam.addTeam()
        newTeam = Team(208, 'test2', 'test2', 'test2')
        newTeam.updateTeam()
        self.assertTrue(get_team_by_id(208).name=='test2')
        #deleting test data
        newTeam.deleteTeam()

    def test_check_valid_id(self):
        newTeam = Team(2000, 'test', 'test', 'test')
        newTeam.addTeam()
        self.assertTrue(check_team_id(2000))
        self.assertFalse(check_team_id(3000))
        newTeam.deleteTeam()







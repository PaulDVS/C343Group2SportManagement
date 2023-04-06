import pytest
from classes.playerClass import Player, get_player_by_id, check_player_id

def test_check_valid_id():
    assert check_player_id(1) == True


def test_check_invalid_id():
    assert check_player_id(1000) == False


def test_get_player_by_id():
    player = Player("John Smith", 1, 1, 1)

    assert get_player_by_id(1).name == player.name
    assert get_player_by_id(1).position_id == player.position_id
    assert get_player_by_id(1).team_id == player.team_id
    assert get_player_by_id(1).player_id == player.player_id


def test_update_player():
    # update player with id 1 name
    player = Player("Liam Smith", 1, 1, 1)
    player.update_player()
    assert get_player_by_id(1).name == "Liam Smith"

    # change name back
    player.name = "John Smith"
    player.update_player()
    assert get_player_by_id(1).name == "John Smith"


def test_add_remove_player():

    player = Player("Test Player", 3, 1)  # we don't give id as that will be by default set to 0 (see constructor) and then auto incremented to the correct id value when added to the db
    player_id = player.addPlayer()  # add player and save the latest added id to a variable
    assert check_player_id(player_id) == True  # player should exist

    player = get_player_by_id(player_id)  # get the player we just added
    player.delete_player()  # delete the player
    assert check_player_id(player_id) == False  # player should no longer exist
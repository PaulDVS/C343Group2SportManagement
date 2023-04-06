import pytest

from classes import matchClass


def test_checkById():
    check = matchClass.check_match_id(1)
    assert check == True

def test_getById():
    check = matchClass.get_match_by_id(2)
    assert check.match_id == 2

def test_add():
    #Assume db has been recreated before testing
    testGame = matchClass.Match(0,1,2,1,"A","01:01")
    testGame.addMatch()
    check = matchClass.check_match_id(6)
    assert check == True
    pass

def test_update():
    # Assume db has been recreated before testing
    testGame = matchClass.Match(0, 1, 2, 1, "A", "01:01")
    testGame.addMatch()

    updateGame = matchClass.Match(7, 1, 2, 1, "A", "10:00")
    updateGame.updateMatch()

    check = matchClass.get_match_by_id(7)
    assert check.match_score == "10:00"
    pass


@pytest.mark.xfail
def test_fail():
    check = matchClass.check_match_id(9999)
    assert check == True
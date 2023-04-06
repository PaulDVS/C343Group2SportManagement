import pytest

from classes import competitionClass

def test_checkById():
    check = competitionClass.check_competition_id(1)
    assert check == True

def test_getById():
    check = competitionClass.get_competition_by_id(1)

    assert check.competition_id == 1

def test_add():
    # Assume db has been recreated before testing
    testComp = competitionClass.Competition(0, "New Comp", -1, "Some company", "Basketball", "National")
    testComp.addCompetition()

    check = competitionClass.check_competition_id(4)
    assert check == True

def test_update():
    # Assume db has been recreated before testing
    testComp = competitionClass.Competition(0, "My Comp", -1, "Some company", "Futball", "Local")
    testComp.addCompetition()

    updateComp = competitionClass.Competition(5, "My Comp", -1, "Some company", "Rugby", "Local")
    testComp.updateCompetition()

    check = competitionClass.get_competition_by_id(5)
    assert check.sport =="Rugby"

@pytest.mark.xfail
def test_fail():
    # Assume db has been recreated before testing
    testComp = competitionClass.Competition(0, "New Comp", 9999, "Some company", "Basketball", "National")
    testComp.addCompetition()

    check = competitionClass.check_competition_id(4)
    assert check == True
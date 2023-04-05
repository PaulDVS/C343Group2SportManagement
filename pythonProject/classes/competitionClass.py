def check_competition_id(match_id):
    pass


def get_competition_by_id(match_id):
    pass

class Competition:
    def __init__(self, competition_id, name, body, sport, level):
        self.competition_id = competition_id
        self.name = name
        self.body = body
        self.sport = sport
        self.level = level

    def __str__(self):
        return super().__str__()

    def addCompetition(self):
        pass

    def updateCompetition(self):
        pass

    def printBasic(self):
        pass

    def printDetails(self):
        pass


import pymysql
def check_team_id(match_id):
    pass


def get_team_by_id(match_id):
    pass

class Team:
    def __init__(self, team_id, name, home, country):
        self.team_id = team_id
        self.name = name
        self.home = home
        self.country = country

    def __str__(self):
        return super().__str__()

    def addTeam(self):
        id = int(input("Enter team id: "))


        conn = pymysql.connect(host="localhost", user="root", password="", database="sportManagementSystem")
        cursor = conn.cursor()
        cursor.execute()

    def deleteTeam(self):
        pass

    def getTeamById(self):
        pass

    def getAllTeams(self):
        pass

    def updateTeam(self):
        pass






import pymysql
import connectionData

def check_team_id(team_id):
    config = connectionData.aadil_connection()
    my_db = pymysql.connect(host=config['host'],user=config['user'],passwd=config['password'],database=config['database'])

    my_cursor = my_db.cursor()
    sql = f"SELECT * FROM team WHERE teamId = {team_id}"
    my_cursor.execute(sql)

    result = my_cursor.fetchall()

    if len(result) == 0:
        return False
    return True


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



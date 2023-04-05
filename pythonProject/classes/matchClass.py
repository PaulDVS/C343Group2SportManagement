import pymysql
from pymysql import Error

from pythonProject.classes import connectionData


def check_match_id(match_id):
    try:
        connection = pymysql.connector.connect(**connectionData.myConnection())

        mysql_Query = """
            Select *
            FROM game
            WHERE gameId = %s"""

        cursor = connection.cursor()
        cursor.execute(mysql_Query, (match_id,))
        result = cursor.fetchall()

        if len(result) == 0:
            return False
        return True

    except Error as e:
        print("Error with SQL", e)


def get_match_by_id(match_id):
    try:
        connection = pymysql.connector.connect(**connectionData.myConnection())

        mysql_Query = """
            Select *
            FROM game
            WHERE gameId = %s"""

        cursor = connection.cursor()
        cursor.execute(mysql_Query, (match_id,))
        result = cursor.fetchall()

        return result[0]

    except Error as e:
        print("Error with SQL", e)

class Match:
    def __init__(self,match_id,team1_id,team2_id,competition_id,location,match_score):
        self.match_id = match_id
        self.team1_id = team1_id
        self.team2_id = team2_id
        self.competition_id = competition_id
        self.location = location
        self.match_score = match_score

    def __str__(self):
        return super().__str__()

    def addMatch(self):
        try:
            connection = pymysql.connector.connect(**connectionData.myConnection())

            mysql_Query = """
                INSERT INTO game(location, team1Id, team2Id, score, competitionId) VALUES
                (%s, %s, %s)"""

            cursor = connection.cursor()
            cursor.execute(mysql_Query, (self.location, self.team1_id, self.team2_id, self.match_score, self.competition_id))


        except Error as e:
            print("Error with SQL", e)

    def updateMatch(self):
        try:
            connection = pymysql.connector.connect(**connectionData.myConnection())

            mysql_Query = """
                UPDATE game
                SET location= %s, team1Id= %s, team2Id= %s,  score= %s, competitionId= %s
                WHERE gameId = %s"""

            cursor = connection.cursor()
            cursor.execute(mysql_Query,
                           (self.location, self.team1_id, self.team2_id, self.match_score, self.competition_id, self.match_id))

        except Error as e:
            print("Error with SQL", e)

    def printMatchDetails(self):
        print("Match id: ",self.match_id)
        print("Score:",self.match_score)
        print("Team 1:", end=" ")
        #Get print team 1 name
        print("Team 2:", end=" ")
        # Get print team 2 name
        print("At "+ self.location)
        print("Competition:", end=" ")
        # Get competition name







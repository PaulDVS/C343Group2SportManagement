import pymysql
from pymysql import Error

from classes import connectionData

def check_competition_id(comp_id):
    try:
        connection = pymysql.connect(**connectionData.myConnection())

        mysql_Query = """
            Select *
            FROM competition
            WHERE competitionId = %s"""

        cursor = connection.cursor()
        cursor.execute(mysql_Query, (comp_id,))
        result = cursor.fetchall()

        if len(result) == 0:
            return False
        return True

    except Error as e:
        print("Error with SQL", e)


def get_competition_by_id(comp_id):
    try:
        connection = pymysql.connect(**connectionData.myConnection())

        mysql_Query = """
            Select *
            FROM competition
            WHERE competitionId = %s"""

        cursor = connection.cursor()
        cursor.execute(mysql_Query, (comp_id,))
        result = cursor.fetchall()

        return result[0]

    except Error as e:
        print("Error with SQL", e)

class Competition:
    def __init__(self, competition_id, name, parent_id, body, sport, level):
        self.competition_id = competition_id
        self.name = name
        self.parent_id = parent_id
        self.body = body
        self.sport = sport
        self.level = level

    def __str__(self):
        return super().__str__()

    def addCompetition(self):
        try:
            connection = pymysql.connect(**connectionData.myConnection())

            mysql_Query = """
                INSERT INTO competition(competitionName, parentCompetitionId, competitionBody, sport, compLevel) VALUES
                (%s, %s, %s, %s, %s)"""

            cursor = connection.cursor()
            cursor.execute(mysql_Query,
                           (self.name, self.parent_id, self.body, self.sport, self.level))


        except Error as e:
            print("Error with SQL", e)

    def updateCompetition(self):
        pass

    def printBasic(self):
        print("ID:",self.competition_id,"Name:",self.name)

    def printDetails(self):
        print("Competition ID:", self.competition_id)
        print("Competition name:",self.name)
        print("Sport:",self.sport)

        if(check_competition_id(self.parent_id)):
            print("Part of", end=" ")
            parent = get_competition_by_id(self.parent_id)
            parent.printBasic()

        print("Managed by:",self.body)
        print("Level:",self.level)

    def getAllCompteams(self):
        pass


    def getAllCompMatches(self):
        pass

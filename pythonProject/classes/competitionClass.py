import pymysql
from pymysql import Error

from . import connectionData
from . import matchClass

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

        x = result[0]
        returnComp = Competition(x[0], x[1], x[2], x[3], x[4], x[5])
        return returnComp

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

            cursor = connection.cursor()


            mysql_Query = """
                    INSERT INTO competition(competitionName, parentCompetitionId, competitionBody, sport, compLevel) 
                    VALUES(%s, %s, %s, %s, %s);"""

            if (self.parent_id != -1):
                cursor.execute(mysql_Query,
                           (self.name, self.parent_id, self.body, self.sport, self.level))

            else:
                x= cursor.execute(mysql_Query,
                               (self.name, None, self.body, self.sport, self.level))

        except Error as e:
            print("Error with SQL", e)

    def updateCompetition(self):
        try:
            connection = pymysql.connect(**connectionData.myConnection())
            cursor = connection.cursor()

            mysql_Query = """
                    UPDATE competition
                    SET competitionName= %s, parentCompetitionId= %s, competitionBody= %s,  sport= %s, compLevel= %s
                    WHERE competitionId = %s"""

            if (self.parent_id != -1):
                cursor.execute(mysql_Query,
                               (self.name, self.parent_id, self.body, self.sport, self.level, self.competition_id))
            else:
                cursor.execute(mysql_Query,
                               (self.name, None, self.body, self.sport, self.level, self.competition_id))

        except Error as e:
            print("Error with SQL", e)

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
        try:
            connection = pymysql.connect(**connectionData.myConnection())

            mysql_Query = """
                Select *
                FROM team
                INNER JOIN teamcompetition ON team.teamId = teamcompetition.teamId
                WHERE teamcompetition.competitionId = %s
                """

            cursor = connection.cursor()
            cursor.execute(mysql_Query, (self.competition_id,))
            result = cursor.fetchall()

            for x in result:
                print("ID:",x[0],"Name:",x[1],"Country:",x[3])

        except Error as e:
            print("Error with SQL", e)


    def getAllCompMatches(self):
        try:
            connection = pymysql.connect(**connectionData.myConnection())

            mysql_Query = """
                Select *
                FROM game
                WHERE competitionId = %s"""

            cursor = connection.cursor()
            cursor.execute(mysql_Query, (self.competition_id,))
            result = cursor.fetchall()

            for x in result:
                print()
                currMatch = matchClass.Match(x[0],x[2],x[3],x[5],x[1],x[4])
                currMatch.printMatchDetails()

        except Error as e:
            print("Error with SQL", e)

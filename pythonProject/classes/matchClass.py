import mysql.connector
from mysql.connector import Error

from classes import connectionData

def check_match_id(match_id):
    try:
        connection = mysql.connector.connect(**connectionData.myConnection())

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
        connection = mysql.connector.connect(**connectionData.myConnection())

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
    def __init__(self,match_id,location,match_score):
        self.match_id = match_id
        self.location = location
        self.match_score = match_score

    def __str__(self):
        return super().__str__()

    def addMatch(self):
        pass

    def updateMatch(self):
        pass

    def printBasic(self):
        pass

    def printMatchDetails(self):
        pass








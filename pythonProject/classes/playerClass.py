import pymysql

from pythonProject.classes import connectionData


def check_player_id(match_id):
    pass


def get_player_by_id(match_id):
    pass

class Player:
    def __init__(self,player_id,name,position):
        self.player_id = player_id
        self.name = name
        self.position = position

    def __str__(self):
        return super().__str__()

    def addPlayer(self):
        pass
    def deletePlayer(self):
        pass

    def getPlayerById(self):
        pass

    def getAllPlayers(self):
        pass

    def updatePlayer(self):
        pass



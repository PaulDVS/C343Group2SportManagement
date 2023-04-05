import pymysql

#from pythonProject.classes import connectionData
import connectionData


def check_player_id(match_id):
    pass


def get_player_by_id(match_id):
    pass


class Player:
    def __init__(self,player_id,name,position_id,team_id):
        self.player_id = player_id
        self.name = name
        self.position_id = position_id
        self.team_id = team_id

    def __str__(self):
        return super().__str__()

    def addPlayer(self):
        config = connectionData.myConnection()
        conn = pymysql.connect(host=config['host'], user=config['user'], passwd=config['password'], database=config['database'])
        cursor = conn.cursor()
        sql = f'INSERT into player(playerName,positionId,teamId) values(%s,%s,%s)'
        values = [self.name, self.position_id, self.team_id]
        cursor.execute(sql, values)
        conn.commit()

    def deletePlayer(self):
        config = connectionData.myConnection()
        conn = pymysql.connect(host=config['host'], user=config['user'], passwd=config['password'],database=config['database'])
        cursor = conn.cursor()
        sql = f"DELETE FROM player WHERE playerId={self.player_id};"
        cursor.execute(sql)
        conn.commit()

    def getPlayerById(self):
        pass

    def getAllPlayers(self):
        pass

    def print_player(self):
        pass

    def updatePlayer(self):
        pass



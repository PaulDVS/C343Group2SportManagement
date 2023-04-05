import pymysql

from pythonProject.classes import connectionData


#from pythonProject.classes import connectionData



def check_player_id(player_id):
    try:
        config = connectionData.myConnection()
        my_db = pymysql.connect(host=config['host'], user=config['user'], passwd=config['password'],database=config['database'])

        my_cursor = my_db.cursor()
        sql = f"SELECT * FROM player WHERE playerId = {player_id}"
        my_cursor.execute(sql)

        result = my_cursor.fetchall()

        if len(result) == 0:
            return False
        return True

    except pymysql.err.OperationalError as e:
        print("Database could not be found please ensure it exists")
        print(e)
    except pymysql.err.ProgrammingError as e:
        print("Your SQL syntax is incorrect")
        print(e)


def get_player_by_id(player_id):
    try:
        config = connectionData.myConnection()
        my_db = pymysql.connect(host=config['host'], user=config['user'], passwd=config['password'],database=config['database'])

        my_cursor = my_db.cursor()
        sql = f"SELECT * FROM player WHERE playerId = {player_id}"
        my_cursor.execute(sql)

        # result is just one team as ids are unique hence select the first result([0])
        result = my_cursor.fetchall()[0]

        # first index is id second is name ...etc
        return Player(result[0], result[1], result[2], result[3])
    except:
        print("Record not found!")


class Player:
    def __init__(self,player_id,name,position_id,team_id):
        self.player_id = player_id
        self.name = name
        self.position_id = position_id
        self.team_id = team_id

    def __str__(self):
        return super().__str__()

    def addPlayer(self):
        try:
            config = connectionData.myConnection()
            conn = pymysql.connect(host=config['host'], user=config['user'], passwd=config['password'],database=config['database'])
            cursor = conn.cursor()
            sql = f'INSERT into player(playerName,positionId,teamId) values(%s,%s,%s)'
            values = [self.name, self.position_id, self.team_id]
            cursor.execute(sql, values)
            conn.commit()
        except pymysql.err.OperationalError as e:
            print("Database could not be found please ensure it exists")
            print(e)
        except pymysql.err.ProgrammingError as e:
            print("Your SQL syntax is incorrect")
            print(e)

    def delete_player(self):
        try:
            config = connectionData.myConnection()
            conn = pymysql.connect(host=config['host'], user=config['user'], passwd=config['password'],database=config['database'])
            cursor = conn.cursor()
            sql = f"DELETE FROM player WHERE playerId={self.player_id};"
            cursor.execute(sql)
            conn.commit()
        except pymysql.err.OperationalError as e:
            print("Database could not be found please ensure it exists")
            print(e)
        except pymysql.err.ProgrammingError as e:
            print("Your SQL syntax is incorrect")
            print(e)

    def print_player(self):
        print(f"ID: {self.player_id} | Name: {self.name} | PositionId: {self.position_id} | TeamId: {self.team_id}")

    def print_player_basic(self):
        print(f"ID: {self.player_id} | Name: {self.name}")

    def update_player(self):
        try:
            config = connectionData.myConnection()
            conn = pymysql.connect(host=config['host'], user=config['user'], passwd=config['password'], database=config['database'])
            cursor = conn.cursor()
            sql = "UPDATE player SET playerName = %s, positionId = %s, teamId = %s  WHERE playerId = %s"
            values = [self.name, self.position_id, self.team_id, self.player_id]
            cursor.execute(sql, values)
            conn.commit()
        except pymysql.err.OperationalError as e:
            print("Database could not be found please ensure it exists")
            print(e)
        except pymysql.err.ProgrammingError as e:
            print("Check your SQL syntax")
            print(e)


#p = Player(1,"John Smith",1,1)
#p.updatePlayer()









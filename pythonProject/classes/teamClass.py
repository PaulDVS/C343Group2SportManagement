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


def get_team_by_id(team_id):
    config = connectionData.aadil_connection()
    my_db = pymysql.connect(host=config['host'], user=config['user'], passwd=config['password'],database=config['database'])

    my_cursor = my_db.cursor()
    sql = f"SELECT * FROM team WHERE teamId = {team_id}"
    my_cursor.execute(sql)

    # result is just one team as ids are unique hence select the first result([0])
    result = my_cursor.fetchall()[0]

    # first index is id second is name ..etc
    return Team(result[0], result[1], result[2], result[3])


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

        id = int(input("Enter team id: "))
        name = input("Enter team name: ")
        home = input("Enter team home: ")
        country = input("Enter team country: ")
        cmd = 'insert into team values(%s,%s,%s,%s)'
        rec = [id, name, home, country]
        cursor.execute(cmd,rec)
        conn.commit()

    def deleteTeam(self):
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="sportManagementSystem")
            cursor = conn.cursor()

            cursor.execute('select * from team')
            x = cursor.fetchall()
            ans = int(input('Enter the team id to be deleted:'))
            for i in x:
                i = list(i)
                if i[0] == ans:
                    cmd = 'delete from team where teamId=%s'
                    val = (i[0],)
                    cursor.execute(cmd, val)
                    conn.commit()
                    print('Team deleted.')
                    break
            else:
                print('Record not found.')
        except:
            print("Table doesn't exist.")


    def getAllTeams(self):
        pass

    def updateTeam(self):
        pass




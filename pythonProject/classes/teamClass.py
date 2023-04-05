
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
            conn = pymysql.connect(host="localhost", user="root", password="SaDa2903!", database="sportManagementSystem")
            cursor = conn.cursor()
            cursor.execute('select * from team')
            x = cursor.fetchall()
            ans = int(input('Enter the team to be deleted:'))
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

    def getTeamById(self):
        pass

    def getAllTeams(self):
        pass

    def updateTeam(self):
        pass






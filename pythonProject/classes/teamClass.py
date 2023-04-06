import pymysql
from pymysql import Error

from pythonProject.classes import connectionData


#from classes import connectionData
#import connectionData

def check_team_id(team_id):
    config = connectionData.myConnection()
    my_db = pymysql.connect(host=config['host'],user=config['user'],passwd=config['password'],database=config['database'])

    my_cursor = my_db.cursor()
    sql = f"SELECT * FROM team WHERE teamId = {team_id}"
    my_cursor.execute(sql)

    result = my_cursor.fetchall()

    if len(result) == 0:
        return False
    return True


def get_team_by_id(team_id):
    try:
        config = connectionData.myConnection()
        my_db = pymysql.connect(host=config['host'], user=config['user'], passwd=config['password'],database=config['database'])

        my_cursor = my_db.cursor()
        sql = f"SELECT * FROM team WHERE teamId = {team_id}"
        my_cursor.execute(sql)

        # result is just one team as ids are unique hence select the first result([0])
        result = my_cursor.fetchall()[0]

        # first index is id second is name ...etc
        #print ("Id:",result[0], " Team Name:", result[1], " Team Home:",result[2], " Team Country:",result[3])
        return(Team(result[0],result[1],result[2],result[3]))
    except:
        print("")


class Team:
    def __init__(self, team_id, name, home, country):
        self.team_id = team_id
        self.name = name
        self.home = home
        self.country = country

    def __str__(self):
        return super().__str__()

    def basicPrint(self):
        print(self.id,self.name)
    def printTeamDetails(self):
        print("Team id: ",self.team_id)
        print("Team Name:",self.name)
        print("Team Home:", self.home)
        print("Team Country: ",self.country)

    def addTeam(self):
        try:
            config = connectionData.myConnection()
            conn = pymysql.connect(host=config['host'], user=config['user'], passwd=config['password'],database=config['database'])
            cursor = conn.cursor()

            mysql_Query = 'INSERT INTO team(teamId, teamName, teamHome, teamCountry) VALUES (%s, %s, %s, %s)'
            cursor.execute(mysql_Query,(self.team_id, self.name, self.home, self.country))
            conn.commit()
        except:
            print("Error adding team to database!")

    def deleteTeam(self):
        try:
            config = connectionData.myConnection()
            conn = pymysql.connect(host=config['host'], user=config['user'], passwd=config['password'],database=config['database'])
            cursor = conn.cursor()

            cursor.execute('select * from team')
            x = cursor.fetchall()
            for i in x:
                i = list(i)
                if i[0] == self.team_id:
                    cmd = 'delete from team where teamId=%s'
                    val = (i[0],)
                    cursor.execute(cmd, val)
                    conn.commit()
                    break
        except Error as e:
            print("Error deleting record!",e)



    def getAllTeams(self):
        try:
            config = connectionData.myConnection()
            conn = pymysql.connect(host=config['host'], user=config['user'], passwd=config['password'],database=config['database'])
            cursor = conn.cursor()
            cursor.execute('select * from team order by teamId')
            x = cursor.fetchall()
            if (len(x)==0):
                print("No teams in database!")
            else:
                space = '%18s %18s %18s %18s'
                print(space % ('Id', 'Name', 'Home', 'Country'))
                print('=' * 150)
                for i in x:
                    for j in i:
                        print('%19s' % j, end=' ')
                    print()
                print('=' * 150)
        except Error as e:
            print("Error accessing database!",e)

    def updateTeam(self):
        try:
            config = connectionData.myConnection()
            conn = pymysql.connect(host=config['host'], user=config['user'], passwd=config['password'],database=config['database'])
            cursor = conn.cursor()

            mysql_Query = 'UPDATE team SET teamName= %s, teamHome= %s, teamCountry= %s WHERE teamId = %s'
            cursor.execute(mysql_Query,(self.name, self.home, self.country,self.team_id))
            conn.commit()

        except Error as e:
            print("Error updating database!", e)

    def getAllPlayers(self):
        try:
            config = connectionData.myConnection()
            conn = pymysql.connect(host=config['host'], user=config['user'], passwd=config['password'],database=config['database'])
            cursor = conn.cursor()
            userInput=int(input("Enter team id: "))
            cursor.execute('select * from player where teamId=%s',userInput)
            x = cursor.fetchall()
            if len(x)!=0:
                space = '%18s %18s %18s %18s'
                print(space % ('Id', 'Name', 'Position', 'Team'))
                print('=' * 150)
                for i in x:
                    for j in i:
                        print('%19s' % j, end=' ')
                    print()
                print('=' * 150)
            else:
                print("No such team in database!")
        except:
            print("Error connecting to database!")

    def getTeamMatches(self):
        try:
            config = connectionData.myConnection()
            conn = pymysql.connect(host=config['host'], user=config['user'], passwd=config['password'],database=config['database'])
            cursor = conn.cursor()
            userInput=int(input("Enter team id: "))
            cursor.execute('select * from game where team1Id=%s or team2Id=%s',(userInput,userInput))
            x = cursor.fetchall()
            if len(x) != 0:
                space = '%18s %18s %18s %18s %18s %18s'
                print(space % ('Id', 'Location', 'Team 1 Id', 'Team 2 Id', 'Score', 'Competition Id'))
                print('=' * 150)
                for i in x:
                    for j in i:
                        print('%19s' % j, end=' ')
                    print()
                print('=' * 150)
            else:
                print("No matches found for this team!")
        except:
            print("Error connecting to database!")
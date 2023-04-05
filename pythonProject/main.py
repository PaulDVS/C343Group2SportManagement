from classes.teamClass import check_team_id, get_team_by_id, get_team_by_id
from classes.playerClass import check_player_id,get_player_by_id,Player
from classes.competitionClass import check_competition_id,get_competition_by_id, Competition
from classes.matchClass import check_match_id,get_match_by_id, Match
from pythonProject.classes.teamClass import Team


#Menu functions
def compMenu():
    ch = 0

    while (ch != "9"):
        print("Competition Menu: ")
        print("1: Create Competition, 2: Update Competition, 3: Print Competition Details")
        print("4: Print All Teams in Competition, 5: Print All Matches in Competition")
        print("9: End")
        print("Please enter your choice: ")
        ch = input()
        print()

        if (ch == "1"):
            print("x")
        elif (ch == "2"):
            print("x")
        elif (ch == "3"):
            print("x")
        elif (ch == "4"):
            print("x")
        elif (ch == "5"):
            print("x")
        elif (ch == "9"):
            print("Returning to Main")
        else:
            print("Invalid input")
        print()

def teamMenu():
    ch = 0

    while (ch != "9"):
        print("Team Menu: ")
        print("1: Create Team, 2: Update Team, 3: Print Team Details, 4: Print All Teams")
        print("5: Print Team Players, 6: Print Team Matches, 7: Delete Team")
        print("9: End")
        print("Please enter your choice: ")
        ch = input()
        print()

        if (ch == "1"):
            team_id = int(input("Enter team id: "))
            name = input("Enter team name: ")
            home = input("Enter team home: ")
            country = input("Enter team country: ")
            newTeam = Team(team_id, name, home, country)
            newTeam.addTeam()

        elif (ch == "2"):
            teamId = input("Please enter id of team you want to update: ")

            currMatch = get_team_by_id(teamId)
            currMatch.printTeamDetails()

            name = input("Please enter team name: ")
            home = input("Please enter team home: ")
            country = input("Please enter team country: ")
            updateTeam = Team(teamId,name, home, country)
            updateTeam.updateTeam()

        elif (ch == "3"):
            team_id = int(input("Enter team id: "))
            print(get_team_by_id(team_id))
        elif (ch == "4"):
            Team.getAllTeams(self=None)
        elif (ch == "5"):
            Team.getAllPlayers(self=None)
        elif (ch =='6'):
            Team.getTeamMatches(self=None)
        elif (ch == '7'):
            Team.deleteTeam(self=None)
        elif (ch == "9"):
            print("Returning to Main")
        else:
            print("Invalid input")
        print()

def matchMenu():
    ch = 0

    while (ch != "9"):
        print("Match Menu: ")
        print("1: Create Match, 2: Update Match, 3: Print Match Details")
        print("9: End")
        print("Please enter your choice: ")
        ch = input()
        print()

        if (ch == "1"):
            print("Please enter the id of team 1:")
            id_1 = input()
            if not(check_team_id(id_1)):
                print("Team doesn't exist")
                continue

            print("Please enter the id of team 2:")
            id_2 = input()
            if not (check_team_id(id_2)):
                print("Team doesn't exist")
                continue

            print("Please enter the id of competition:")
            id_comp = input()
            if not (check_competition_id(id_comp)):
                print("Competition doesn't exist")
                continue

            print("Please enter location of the match:")
            location = input()

            print("Please enter the score in the format 00:00")
            match_score = input()

            newMatch = Match(0, id_1, id_2, id_comp, location, match_score)
            newMatch.addMatch()

        elif (ch == "2"):
            print("Please enter the id of the match to view:")
            match_id = input()
            if not (check_match_id(match_id)):
                print("Match doesn't exist")
                continue

            currMatch = get_match_by_id(match_id)
            currMatch.printMatchDetails()

            print("Please enter the id of team 1:")
            id_1 = input()
            if not (check_team_id(id_1)):
                print("Team doesn't exist")
                continue

            print("Please enter the id of team 2:")
            id_2 = input()
            if not (check_team_id(id_2)):
                print("Team doesn't exist")
                continue

            print("Please enter the id of competition:")
            id_comp = input()
            if not (check_competition_id(id_comp)):
                print("Competition doesn't exist")
                continue

            print("Please enter location of the match:")
            location = input()

            print("Please enter the score in the format 00:00")
            match_score = input()

            updateMatch = Match(1, id_1, id_2, id_comp, location, match_score)
            updateMatch.updateMatch()
            
        elif (ch == "3"):
            print("Please enter the id of the match to view:")
            match_id = input()
            if(check_match_id(match_id)):
                currMatch = get_match_by_id(match_id)
                currMatch.printMatchDetails()
            else:
                print("Match doesn't exist")
        elif (ch == "9"):
            print("Returning to Main")
        else:
            print("Invalid input")
        print()

def playerMenu():
    ch = 0

    while (ch != "9"):
        print("Player Menu: ")
        print("1: Create Player, 2: Update Player, 3: Print Player Details")
        print("9: End")
        print("Please enter your choice: ")
        ch = input()
        print()

        if (ch == "1"):
            print("x")
        elif (ch == "2"):
            print("x")
        elif (ch == "3"):
            print("x")
        elif (ch == "9"):
            print("Returning to Main")
        else:
            print("Invalid input")
        print()

#main
ch = 0

while(ch!="9"):
    print("Main Menu: ")
    print("1: Competition Menu, 2: Team Menu, 3: Match Menu")
    print("4: Player Menu")
    print("9: End")
    print("Please enter your choice: ")
    ch = input()
    print()

    if(ch=="1"):
        compMenu()
    elif (ch=="2"):
        teamMenu()
    elif (ch=="3"):
        matchMenu()
    elif (ch=="4"):
        playerMenu()
    elif (ch=="9"):
        print("Thank you for using this program")
    else:
        print("Invalid input")
        print()
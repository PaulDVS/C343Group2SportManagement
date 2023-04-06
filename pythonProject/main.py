from classes.teamClass import check_team_id, get_team_by_id, deleteTeam, addTeam, get_team_by_id, getAllTeams, getAllPlayers, getTeamMatches
from classes.playerClass import check_player_id,get_player_by_id,Player
from classes import competitionClass
from classes import matchClass


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
            print("Please enter the id of the parent Competition, -1 for none")
            parent_id = int(input())
            if(parent_id!=-1 and not(competitionClass.check_competition_id(parent_id))):
                print("Parent competition doesn't exist")
                continue

            print("Please enter competition name")
            compName = input()
            print("Please enter competition sport")
            sport = input()
            print("Please enter Body in charge of this competition")
            body = input()
            print("Please enter competition level")
            compLevel = input()

            newComp = competitionClass.Competition(0,compName,parent_id,body,sport,compLevel)
            newComp.addCompetition()


        elif (ch == "2"):
            print("Please enter the id of the Competition to update:")
            comp_id = int(input())
            if not(competitionClass.check_competition_id(comp_id)):
                print("Competition doesn't exist")
                continue
            currComp = competitionClass.get_competition_by_id(comp_id)
            currComp.printDetails
            print()
            print("Please enter the id of the parent Competition, -1 for none")
            parent_id = int(input())
            if (parent_id != -1 and not (competitionClass.check_competition_id(parent_id))):
                print("Parent competition doesn't exist")
                continue

            print("Please enter competition name")
            compName = input()
            print("Please enter competition sport")
            sport = input()
            print("Please enter Body in charge of this competition")
            body = input()
            print("Please enter competition level")
            compLevel = input()

            updateComp = competitionClass.Competition(comp_id, compName, parent_id, body, sport, compLevel)
            updateComp.updateCompetition()


        elif (ch == "3"):
            print("Please enter the id of the Competition to view:")
            comp_id = int(input())
            if (competitionClass.check_competition_id(comp_id)):
                currComp = competitionClass.get_competition_by_id(comp_id)
                currComp.printDetails()
            else:
                print("Competition doesn't exist")

        elif (ch == "4"):
            print("Please enter the id of the Competition to find teams from:")
            comp_id = int(input())
            if (competitionClass.check_competition_id(comp_id)):
                currComp = competitionClass.get_competition_by_id(comp_id)
                print("All teams for", end=" ")
                currComp.printBasic()
                print()
                currComp.getAllCompteams()
            else:
                print("Competition doesn't exist")

        elif (ch == "5"):
            print("Please enter the id of the Competition to find matches from:")
            comp_id = int(input())
            if (competitionClass.check_competition_id(comp_id)):
                currComp = competitionClass.get_competition_by_id(comp_id)
                print("All Matches for", end=" ")
                currComp.printBasic()
                currComp.getAllCompMatches()
            else:
                print("Competition doesn't exist")

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
            addTeam()
            #print("x")
        elif (ch == "2"):
            print("x")
        elif (ch == "3"):
            team_id = int(input("Enter team id: "))
            get_team_by_id(team_id)
        elif (ch == "4"):
            getAllTeams()
        elif (ch == "5"):
            getAllPlayers()
        elif (ch =='6'):
            getTeamMatches()
            break
        elif (ch == '7'):
            deleteTeam()
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
            id_1 = int(input())
            if not(check_team_id(id_1)):
                print("Team doesn't exist")
                continue

            print("Please enter the id of team 2:")
            id_2 = int(input())
            if not (check_team_id(id_2)):
                print("Team doesn't exist")
                continue

            print("Please enter the id of competition:")
            id_comp = int(input())
            if not (competitionClass.check_competition_id(id_comp)):
                print("Competition doesn't exist")
                continue

            print("Please enter location of the match:")
            location = input()

            print("Please enter the score in the format 00:00")
            match_score = input()

            newMatch = matchClass.Match(0, id_1, id_2, id_comp, location, match_score)
            newMatch.addMatch()

        elif (ch == "2"):
            print("Please enter the id of the match to view:")
            match_id = int(input())
            if not (matchClass.check_match_id(match_id)):
                print("Match doesn't exist")
                continue

            currMatch = matchClass.get_match_by_id(match_id)
            currMatch.printMatchDetails()

            print("Please enter the id of team 1:")
            id_1 = int(input())
            if not (check_team_id(id_1)):
                print("Team doesn't exist")
                continue

            print("Please enter the id of team 2:")
            id_2 = int(input())
            if not (check_team_id(id_2)):
                print("Team doesn't exist")
                continue

            print("Please enter the id of competition:")
            id_comp = int(input())
            if not (competitionClass.check_competition_id(id_comp)):
                print("Competition doesn't exist")
                continue

            print("Please enter location of the match:")
            location = input()

            print("Please enter the score in the format 00:00")
            match_score = input()

            updateMatch = matchClass.Match(match_id, id_1, id_2, id_comp, location, match_score)
            updateMatch.updateMatch()
            
        elif (ch == "3"):
            print("Please enter the id of the match to view:")
            match_id = int(input())
            if(matchClass.check_match_id(match_id)):
                currMatch = matchClass.get_match_by_id(match_id)
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
        print("4: Delete Player")
        print("9: End")
        print("Please enter your choice: ")
        ch = input()
        print()

        if (ch == "1"):
            name = input("Enter player name:\n")

            positionID = int(input("Enter player positionID:\n"))

            while positionID not in [0, 1, 2, 3, 4]:
                print("Invalid positionID")
                print("0 -> Bench\n1 -> Goalie\n2 -> Forward\n3 -> Midfield\n4 -> Defence")
                positionID = int(input("Enter player positionID:\n"))

            teamID = int(input("Enter a valid TeamID:\n"))
            while not get_team_by_id(teamID):
                print("Invalid Team ID - Below you will find all the valids teams:")
                getAllTeams()
                teamID = int(input("Enter a valid TeamID:\n"))

            player = Player(name, positionID, teamID)
            player.addPlayer()

        elif (ch == "2"):
            player_id = int(input("Enter the player id you wish to edit:\n"))
            while not check_player_id(player_id):
                print("This ID is invalid!")
                player_id = int(input("Enter the player id you wish to edit:\n"))

            player = get_player_by_id(player_id)
            player.print_player()

            print("Please enter the same details if you dont wish to change a field")

            name = input("Enter player name:\n")

            positionID = int(input("Enter player positionID:\n"))

            while positionID not in [0, 1, 2, 3, 4]:
                print("Invalid positionID")
                print("0 -> Bench\n1 -> Goalie\n2 -> Forward\n3 -> Midfield\n4 -> Defence")
                positionID = int(input("Enter player positionID:\n"))

            teamID = int(input("Enter a valid TeamID:\n"))
            while not get_team_by_id(teamID):
                print("Invalid Team ID - Below you will find all the valid teams:")
                getAllTeams()
                teamID = int(input("Enter a valid TeamID:\n"))

            player = Player(name, positionID, teamID, player_id)
            player.update_player()


        elif (ch == "3"):
            player_id = int(input("Enter the player id whose details you wish to see"))
            while not check_player_id(player_id) or type(player_id) != int:
                print("This ID is invalid!")
                player_id = input("Enter the player id whose details you wish to see")
            player = get_player_by_id(player_id)
            player.print_player()

        elif (ch == "4"):
            player_id = int(input("Enter the player id you wish to remove:\n"))
            while not check_player_id(player_id) or type(player_id) != int:
                print("This ID is invalid!")
                player_id = input("Enter the player id you wish to remove:\n")
            player = get_player_by_id(player_id)
            player.delete_player()

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
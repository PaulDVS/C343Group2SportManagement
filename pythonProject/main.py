from classes.teamClass import deleteTeam, addTeam, get_team_by_id, getAllTeams, getAllPlayers
from classes.matchClass import check_match_id

#Menu functions
def compMenu():
    ch = 0

    while (ch != "9"):
        print("Competition Menu: ")
        print("1: Create Competition, 2: Update Competition, 3: Print Competition Details")
        print("4: Print All Teams in Competition, 5: Print All Matchs in Competition")
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
            deleteTeam()
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
            check_match_id(1)
        elif (ch == "2"):
            print("x")
        elif (ch == "3"):
            print("x")
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
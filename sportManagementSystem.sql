DROP DATABASE IF EXISTS sportManagementSystem;

CREATE DATABASE sportManagementSystem;
USE sportManagementSystem;

CREATE TABLE competition (
    competitionId INT AUTO_INCREMENT,
    competitionName VARCHAR(50) NOT NULL,
    parentCompetitionId INT,
    competitionBody VARCHAR(50),
    sport VARCHAR(50),
    compLevel VARCHAR(50),
    CONSTRAINT pk_competition 
        PRIMARY KEY (competitionId),
    CONSTRAINT fk_parent 
        FOREIGN KEY (parentCompetitionId)
	REFERENCES competition(competitionId)
);
CREATE TABLE team (
    teamId INT AUTO_INCREMENT,
    teamName VARCHAR(50) NOT NULL,
    teamHome VARCHAR(50),
    teamCountry VARCHAR(50),
    CONSTRAINT pk_team 
        PRIMARY KEY (teamId)
);

CREATE TABLE game (
    gameId INT AUTO_INCREMENT,
    location VARCHAR(50) NOT NULL,
    team1Id INT,
    team2Id INT,
    score VARCHAR(5),
    competitionId INT,
    CONSTRAINT pk_game
        PRIMARY KEY (gameId),
	CONSTRAINT fk_game_team
    	FOREIGN KEY (team1Id)
    	REFERENCES team(teamId),
    	FOREIGN KEY (team2Id)
    	REFERENCES team(teamId),
	CONSTRAINT fk_game_competition
    	FOREIGN KEY (competitionId)
    	REFERENCES competition(competitionId)
);

CREATE TABLE pPosition (
	positionId INT,
    positionName VARCHAR(50),
	CONSTRAINT pk_pPosition 
    	PRIMARY KEY (positionId)
);

CREATE TABLE player (
    playerId INT AUTO_INCREMENT,
    playerName VARCHAR(50) NOT NULL,
    positionId INT,
    teamId INT,
    CONSTRAINT pk_player 
    	PRIMARY KEY (playerId),
    CONSTRAINT fk_player_position
    	FOREIGN KEY (positionId)
    	REFERENCES pPosition(positionId),
	CONSTRAINT fk_player_team
    	FOREIGN KEY (teamId)
    	REFERENCES team(teamId)
);

CREATE TABLE teamCompetition (
	competitionId INT,
    teamId INT,
    CONSTRAINT pk_teamCompetition 
    	PRIMARY KEY (competitionId, teamId),
    CONSTRAINT fk_teamCompetition_competition
    	FOREIGN KEY (competitionId)
    	REFERENCES competition(competitionId),
	CONSTRAINT fk_teamCompetition_team
    	FOREIGN KEY (teamId)
    	REFERENCES team(teamId)
);
INSERT INTO
	team(teamId, teamName, teamHome, teamCountry)
VALUES
	(1,'Arsenal','Emirates','England'),
	(2,'Manchester City','Etihad','England'),
    (3,'Manchester United','Old Trafford','England'),
	(4,'Real Madrid','Santiago Bernabéu','Spain'),
    (5,'Bayern Munich','Allianz Arena','Germany');
    

INSERT INTO pPosition(positionId, positionName)
VALUES
	(0,'Bench'),
	(1,'Goal Keeper'),
    (2,'Forward'),
	(3,'Mid-Field'),
	(4,'Defence');



INSERT INTO competition(competitionId, competitionName, parentCompetitionId, competitionBody, sport, compLevel)
VALUES
	(1,"Championss League",0,"UEFA","Football","InterNational"),
	(2,"Vanarama National League",1,"The Football Association","Football","National"),
	(3,"Bundesliga National League",1,"German Football Association","Football","National");


INSERT INTO player(playerId,playerName,positionId,teamId)
VALUES
	(1,'John Smith',1,1),
	(2,"Alan Smith",2,1),
	(3,"Nelson Smith",3,1),
	(4,"Greg Smith",4,1),
	(5,"Daniel Smith",0,1),
	(6,"Robert Addams",1,2),
	(7,"Jason Addams",2,2),
	(8,"Steve Addams",3,2),
	(9,"Alan Addams",4,2),
	(10,"Jack Addams",0,2),
	(11,"Greg White",1,3),
	(12,"Liam White",2,3),
	(13,"Alex White",3,3),
	(14,"Claude White",4,3),
	(15,"Chris White",0,3),
	(16,"Liam Chance",1,4),
	(17,"Noah Chance",2,4),
	(18,"Steve Chance",3,4),
	(19,"Lucas Chance",4,4),
	(20,"Oliver Chance",0,4),
	(21,"Alex Thatcher",1,5),
	(22,"Greg Thatcher",2,5),
	(23,"Lucas Thatcher",3,5),
	(24,"William Thatcher",4,5),
	(25,"James Thatcher",0,5);

INSERT INTO game(gameId, location, team1Id, team2Id, score, competitionId)
VALUES
	(1,"Bayt Stadium",4,5,"01:01",3),
	(2,"Arsenal Stadium",1,2,"03:05",2),
	(3,"Manchester Stadium",2,3,"02:00",2),
	(4,"Arsenal Stadium",1,5,"05:01",1),
	(5,"Madrid Stadium",3,4,"04:03",1);






            
            




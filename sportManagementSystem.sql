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


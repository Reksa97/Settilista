# CREATE TABLE -lauseet

### Account
CREATE TABLE Account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);

### Song
CREATE TABLE Song (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(63) NOT NULL, 
	artist VARCHAR(63) NOT NULL, 
	length INTEGER NOT NULL, 
	songkey VARCHAR(4) NOT NULL, 
	public BOOLEAN NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (public IN (0, 1)), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);

### Setlist
CREATE TABLE Setlist (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	public BOOLEAN NOT NULL, 
	account_id INTEGER NOT NULL, 
	account_username VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (public IN (0, 1)), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);

### SetlistSong
CREATE TABLE Setlist_Song (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(63) NOT NULL, 
	artist VARCHAR(63) NOT NULL, 
	length INTEGER NOT NULL, 
	songkey VARCHAR(4) NOT NULL, 
	notes VARCHAR(255) NOT NULL, 
	setlist_id INTEGER NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(setlist_id) REFERENCES setlist (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);



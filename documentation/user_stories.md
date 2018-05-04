# Käyttötapaukset

### Ennen kirjautumista:
  - Voin rekisteröityä
```

-- Tarkistetaan onko samaa käyttäjätunnusta jo olemassa

SELECT Account.id FROM Account WHERE Account.username = tunnus;

-- Lisätään käyttäjän tiedot tietokantaan

INSERT INTO account (date_created, date_modified, name, username, password) 
	VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, nimi, tunnus, salasana)
```

  - Voin kirjautua sisään
```
SELECT * FROM Account WHERE Account.username = username AND Account.password = password;
```

### Käyttäjänä:
  - Voin listata itse lisäämäni kappaleet ja julkiset kappaleet tässä järjestyksessä.
```
SELECT * FROM Song WHERE Song.account_id = current_user.id OR Song.public = True
	ORDER BY (NOT Song.account_id = current_user.id);
```

  - Voin lisätä tietokantaan kappaleita ja tietoa niistä (kappaleen nimi, artisti, kesto, sävellaji).
```
INSERT INTO Song (date_created, date_modified, name, artist, length, songkey, public, account_id) 
	VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, nimi, artisti, kesto, sävellaji, False, current_user.id);
``` 

  - Voin tehdä lisäämästäni kappaleesta julkisen, jolloin muut käyttäjät voivat lisätä sen omaan settilistaansa.
```
UPDATE Song SET Song.date_modified = CURRENT_TIMESTAMP, Song.public = True WHERE Song.id = kappaleenId;
```

  - Voin muokata lisäämieni kappaleiden tietoja.
```
Kuten yllä, mutta useammalle sarakkeelle.
```

  - Voin koota kappaleista settilistoja ja muokata kappaleen tietoja settilistaan sopiviksi, sekä halutessani lisätä kappaleen kohdalle muistiinpanoja.
```
INSERT INTO Setlist_Song (date_created, date_modified, name, artist, length, songkey, notes, setlist_id, account_id)
	VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, nimi, artisti, kesto, sävellaji, muistiinpanot, milleSettilistalle, current_user.id);

UPDATE Setlist_Song SET Song.date_modified = CURRENT_TIMESTAMP, Song.length = kesto, ... , Song.notes = muistiinpanot
	WHERE Setlist_Song.id = muokattavanId;
```

  - Voin järjestää settilistan haluamaani järjestykseen. (Settilista järjestetään notes-sarakkeen mukaan)
```
SELECT * FROM Setlist_Song WHERE Setlist_Song.setlist_id = haluttuSettilistaId ORDER BY Setlist_Song.notes;
```

  - Voin pitää settilistaa auki keikalla ja saada siitä tarvitsemani tiedot jokaisen kappaleen kohdalla, sekä nähdä settelistan kokonaiskeston.

```
Sama kuin yllä.
```

  - Voin katsoa mitkä käyttäjät eivät ole lisänneet kappaleita tietokantaan.
```
SELECT Account.username FROM Account LEFT JOIN Song ON Song.account_id = Account.id 
	GROUP BY Account.id HAVING COUNT(Song.id) = 0;
```

# Settilista-tietokanta
[Linkki herokuun](https://tsoha-settilista.herokuapp.com/)

[Tietokantakaavio](https://github.com/Reksa97/Settilista/blob/master/documentation/Tietokantakaavio.png)

[CREATE TABLE -lauseet](https://github.com/Reksa97/Settilista/blob/master/documentation/CREATE_TABLE.md)

[Käyttötapaukset](https://github.com/Reksa97/Settilista/blob/master/documentation/user_stories.md)

Tietokantaan voidaan tallentaa kappaleita ja keikoilla tarvittavaa tietoa niistä (artisti, sävellaji, kesto, muistiinpanot) 
ja luoda niistä settilista-kokonaisuuksia.
Käyttäjät voivat lisätä omiin settilistoihin itse lisäämiä kappaleita ja julkiseksi asetettuja kappaleita.

Toimintoja:
 * Kappaleiden ja niiden tietojen lisääminen
 * Kappaleiden muuttaminen julkisiksi tai yksityisiksi
 * Settilistojen tekeminen
 * Kappaleiden lisääminen settilistoihin
 * Käyttäjän rekisteröityminen ja kirjautuminen
 * Omien kappaleiden ja settilistojen muokkamineen
 * Muiden kappaleiden ja settilistojen katseleminen


## Sovelluksen käyttöönotto
 * Lataa projektin zip-tiedosto.
 * Pura tiedostot kansioon
 * Mene projektin kansioon ja luo sinne Python-virtuaaliympäristö ja ota se käyttöön komennoilla:
```
python3 -m venv venv

pip3 install -r requirements.txt
```

Käynnistä projekti komennolla:
```
python3 run.py
```
Projekti on nyt käynnissä ja voit tarkastella sitä selaimella. Osoite löytyy terminaalista riviltä:
```
 * Running on http://127.0.0.1:5000/
```

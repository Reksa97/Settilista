# Settilista-tietokanta
[Linkki herokuun](https://tsoha-settilista.herokuapp.com/)

[Tietokantakaavio](https://github.com/Reksa97/Settilista/blob/master/documentation/Tietokantakaavio.png)

[CREATE TABLE -lauseet](https://github.com/Reksa97/Settilista/blob/master/documentation/CREATE_TABLE.md)

[Käyttötapaukset](https://github.com/Reksa97/Settilista/blob/master/documentation/user_stories.md)

Settilista-tietokanta on tarkoitettu muusikoille "muistilapuksi" keikoille. Tietokantaan voidaan tallentaa kappaleita ja keikoilla tarvittavaa tietoa niistä (artisti, sävellaji, kesto, muistiinpanot) ja luoda niistä settilista-kokonaisuuksia.
Käyttäjät voivat lisätä omiin settilistoihin itse lisäämiä kappaleita ja julkiseksi asetettuja kappaleita.

Toimintoja:
 * Käyttäjän rekisteröityminen ja kirjautuminen
 * Kappaleiden ja niiden tietojen lisääminen
 * Omien kappaleiden muokkaaminen ja muuttaminen julkisiksi tai yksityisiksi
 * Settilistojen tekeminen
 * Omien settilistojen muokkaaminen ja muuttaminen julkisiksi tai yksityisiksi
 * Omien tai julkisten kappaleiden lisääminen omiin settilistoihin
 * Julkiseksi muutettujen settilistojen katseleminen

Rajoitteet:
 * Käyttäjät voivat nähdä vain itse lisätyt kappaleet ja julkisiksi muutetut kappaleet
 * Käyttäjät voivat nähdä vain itse lisätyt settilistat ja julkisiksi muutetut settilistat
 * Käyttäjä voi muokata vain itse lisättyjä kappaleita ja settilistoja
 * Kaikki toiminnot paitsi etusivun katseleminen vaativat kirjautumisen


### Sovelluksen käyttöönotto
 * Lataa projektin zip-tiedosto.
 * Pura tiedostot kansioon
 * Mene projektin kansioon ja luo sinne Python-virtuaaliympäristö ja ota se käyttöön komennoilla:
```
python3 -m venv venv

source venv/bin/activate
```
 * Asenna projektin riippuvuudet komennolla
```
pip3 install -r requirements.txt
```
 * Käynnistä projekti komennolla:
```
python3 run.py
```
Projekti on nyt käynnissä ja voit tarkastella sitä selaimella. 
Osoite löytyy terminaalista riviltä:
```
 * Running on http://127.0.0.1:5000/
```

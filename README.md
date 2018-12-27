# Settilista-tietokanta
[Linkki herokuun](https://tsoha-settilista.herokuapp.com/)

[Tietokantakaavio](https://github.com/Reksa97/Settilista/blob/master/documentation/Tietokantakaavio.png)

[CREATE TABLE -lauseet](https://github.com/Reksa97/Settilista/blob/master/documentation/CREATE_TABLE.md)

[Käyttötapaukset](https://github.com/Reksa97/Settilista/blob/master/documentation/user_stories.md)

Settilista-tietokanta on tarkoitettu muusikoille "muistilapuksi" keikoille. Tietokantaan voidaan tallentaa kappaleita ja keikoilla tarvittavaa tietoa niistä (artisti, sävellaji, kesto, muistiinpanot) ja luoda niistä settilista-kokonaisuuksia.
Käyttäjät voivat lisätä omiin settilistoihin itse lisäämiä kappaleita ja julkiseksi asetettuja kappaleita.

Toimintoja:
 * Rekisteröityminen ja kirjautuminen
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

#### Docker

Jos Docker on ladattu, pullaa ja käynnistä komennoilla
```
sudo docker pull reksa97/setlist

sudo docker run -it -p 5000:5000 --rm reksa97/setlist
```

#### Venv

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

#### Osoite

Projekti on nyt käynnissä ja voit tarkastella sitä selaimella. 
Osoite löytyy terminaalista riviltä:
```
 * Running on http://0.0.0.0:5000/
```
Projekti pyörii myös osoitteessa:
```
http://localhost:5000/
```

### Puuttuvat ominaisuudet
 * Jonkinlainen admin-käyttäjä
 * Kappaleiden ja settilistojen järjestäminen eri kriteereillä
 * Settilistan kappaleiden järjestyksen muuttaminen nopeasti
 * Katselutila omille settilistoille

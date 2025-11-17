---
title: ✅ Kokeet
layout: default
nav_order: 8
---

# Kokeet
{: .no_toc }

Normaaliin kurssikokeeseen ei tarvitse erikseen ilmoittautua, mutta **mikäli olet uusimassa kurssia, ilmoittaudu aikaisemman toteutuksesi opettajalla viimeistään kaksi viikkoa ennen koetta sähköpostitse.**

{: .huom }
Tällä sivulla on oleellista tietoa kokeisiin valmistautumiseen sekä järjestelyihin ja käytäntöihin liittyen, joten luethan sen kokonaan, vaikka sivu pitkä.

---

## Tällä sivulla:
{: .no_toc .text-delta }

* Sisällysluettelo
{:toc}


## Koealue

Kurssin kokeessa koealueena on koko teoriasisältö, eli mooc.fi:n osat 1-7. Kokeessa välttämätöntä osaamista ovat *funktiot* sekä *perustietotyypit* ja *kontrollirakenteet*. Eri *kokoelmat* ovat myös tyypillisesti edustettuna kokeessa.


## Kokeen aikataulu

Kokeen kesto on 2,5 tuntia. Mikäli sinulla on erityisopettajan lausunto kokeen lisäajasta, voit käyttää lisäksi erityisopettajan suositteleman lisäajan. Jos lausunnossa ei ole eritelty lisäajan kestoa, koeaikasi on 3 tuntia 15 minuuttia.


## Kokeen arvostelu

Hyväksyttyyn suoritukseen eli arvosanaan kokeessa edellytetään vähintään 40 % kokonaispisteistä. Minimipisteet oikeuttavat arvosanaan 1, kun taas 100 % pisteistä oikeuttaa arvosanaan 5. Koearvosanaa ei pyöristetä, eli jokaisella saamallasi pisteellä on merkitystä kurssin loppuarvioinnissa. 

Tarkempi kuvaus laskukaavasta löytyy [arviointi-sivulta](/arviointi/#kokeen-arviointi).


## Kokeen tehtävät ja luova ongelmanratkaisu

Kokeen tehtävät vastaavat tyyliltään kurssin tavanomaisia ohjelmointitehtäviä. Tehtävänannot sisältävät esimerkkisuorituksia sekä automaattisia doctest-testejä, joiden avulla voit kokeilla ratkaisujesi toimivuutta. Esimerkkejä tehtävänannoista sekä doctest-testeistä' löydät [harjoituskokeesta](https://github.com/python-ohjelmointi/harjoituskoe).

Moniin tehtäviin löytyy lukuisia erilaisia ratkaisutapoja. Ennen tehtävän ratkaisua pohdi, voidaanko se ratkaista esimerkiksi listoilla, sanakirjoilla tai kenties jopa ilman kokoelmaa. Jos ratkaisusi kasvaa sadan rivin pituiseksi, löytyisi tehtävään todennäköisesti myös helpompi ratkaisutapa.


## Automaattiset testit ja osittaiset pisteet

Kokeen arvioinnissa hyödynnetään automaattisia testejä, jotka ovat samankaltaisia kuin tehtävänannoissa esitetyt doctest-testit. Arvioinneissa käytettäviä testejä on kuitenkin enemmän ja ne testaavat ratkaisujasi eri syötteillä.

Kunkin tehtävän ratkaisu pisteytetään sen mukaan, kuinka suuren osan tehtävälle kirjoitetuista testeistä ratkaisu läpäisee. On siis mahdollista, että saat osittaisia pisteitä, vaikka ratkaisusi ei täyttäisi kaikkia tehtävänanon vaatimuksia. Tehtävissä mukana olevien doctest-testien läpäiseminen antaa hyvän viitteen siitä, miten hyvin ratkaisusi toimii, mutta lopullisessa arvioinnissa käytettävät testit voivat poiketa niistä.

{: .huom }
Automaattisen arvioinnin vuoksi on välttämätöntä, että toteuttamiesi funktioiden nimet, parametrit ja paluuarvot vastaavat täysin tehtävänantoja. Ohjelmasi ei saa kysyä syötteitä eikä tehdä tulosteita, ellei niitä ole tehtävänannossa erikseen mainittu.


## Pyöristykset, virheelliset syötteet yms.

Tehtävien automaattisessa arvioinnissa on tärkeää, että ohjelmasi esittää esimerkiksi numerot kuten ne on tehtävän esimerkkisuorituksessa esitetty. Tehtävissä ei tarvitse pyöristää tai muuten muotoilla numeroita, ellei tehtävänannossa erikseen sitä pyydetä. Liukuluvut tulostetaan siis tyypillisesti "oletusesityksellä", eli niiden desimaaliosan pituus voi vaihdella.

Oletuksena tehtävissä ei myöskään pidä taivuttaa tekstejä eri yksikköön tai monikkoon ("1 tuote" ja "2 tuotetta"), ellei sitä erikseen tehtävässä pyydetä.

{: .vinkki }
Tehtävissä ei tarvitse varautua virheellisiin syötteisiin tai muihin poikkeustilanteisiin, ellei sitä erikseen pyydetä.


## Harjoituskoe

Olemme valmistelleet kokeeseen valmistautumisen tueksi erillisen harjoituskokeen, jonka voitte halutessanne tehdä itsenäisesti oman aikataulunne mukaan. Harjoituskoe löytyy GitHub-palvelusta osoitteesta [https://github.com/python-ohjelmointi/harjoituskoe](https://github.com/python-ohjelmointi/harjoituskoe).

Kokeessa tehtävät testataan tehtävänantoihin upotettujen doctest-testien avulla. Doctest-testit eivät vaikuta siihen, miten vastaukset laaditaan, mutta teidän on hyvä osata vähintään suorittaa testit ja tulkita niiden tuottamia raportteja. Harjoituskokeen avulla pystyttekin jo etukäteen tutustumaan näihin asioihin. Doctest-testejä sekä harjoituskoetta käsitellään myös kurssin tapaamisissa sekä Teams-keskusteluissa.

Harjoituskokeessa kukin tehtävä koostuu yhdestä Python-tiedostosta. Tehtävätiedostot sisältävät valmiiksi tehtävänannot sekä automaattiset testit, ja omat ratkaisunne kirjoitetaan jatkoksi näihin samoihin tiedostoihin.


## Kokeen pelisäännöt

Kokeessa saa käyttää kurssin tavanomaisia tietolähteitä, kuten Google, Stack Overflow ja mooc.fi. Saat lisäksi tutkia kurssin esimerkkikoodeja ja omia kurssilla kirjoittamiasi koodeja, mutta **koodin suora kopiointi kokeen vastauksiin on kiellettyä**.

**Kokeen ratkaisuissa on sallittua käyttää ainoastaan [Pythonin standardikirjastoa](https://docs.python.org/3/library/index.html).** Erikseen esimerkiksi pip-komennolla asennettavat paketit ja kirjastot, kuten NumPy tai pandas, eivät ole sallittuja. Lisäksi suosittelemme, että käytät kokeessa ainoastaan [Pythonin ylläpidettyjä versioita](https://devguide.python.org/versions/), joita käytetään myös ratkaisujesi automaattisessa arvioinnissa.

**Kaikki viestintä ja kokeesta keskusteleminen on kiellettyä**.

**Tehtävän vastauksen generointi tekoälyn avulla on kokeessa kiellettyä.** Et saa siis käyttää esim. ChatGPT:tä tai Copilot:ia ratkaistaksesi koetehtävän sellaisenaan. Saat kuitenkin hyödyntää näitä palveluita yksittäisten osaongelmien ratkaisemiseksi.

**Ohjelmasi ei saa vilpillisesti harhauttaa tehtävän tarkastimia** siten, että se tuottaa oikean vastauksen tehtävässä käytettäville testisyötteille toteuttamatta tehtävänannossa kuvailtua logiikkaa. Tällaiset ratkaisut hylätään, ja tahalliseksi katsottava vilppi voi johtaa myös koko kokeen hylkäykseen ja tutkintosäännön mukaisiin jatkotoimiin.

{: .esim }
> 🆗 Saat hyödyntää hakukoneita tai tekoälyä selvittääksesi esimerkiksi, miten listalta voidaan poimia tietyn ehdon täyttävät arvot tai kuinka tietyt numerot voidaan käydä läpi suurimmasta pienimpään.
>
> ⛔ Et saa generoida tekoälyn avulla kokonaista ohjelmaa, joka kysyy käyttäjältä tehtävänannossa esitetyt kysymykset ja tulostaa vaaditut tulosteet.
>
> ⛔ Et saa asentaa tai käyttää Pythonin standardikirjaston ulkopuolisia paketteja, kuten NumPy tai pandas.
>
> ⛔ Et saa toteuttaa ohjelmaa siten, että se toimii pelkästään esimerkkisuorituksessa esitetyillä arvoilla ilman, että se toteuttaa tehtävänannossa esitettyä logiikkaa.

Halutessasi voit hyödyntää kurssin valmiiksi annettua LLM-promptia, joka ohjeistaa tekoälyä toimimaan apunasi pelisääntöjen mukaisesti. Prompt löytyy [tältä erilliseltä sivulta](/llm-prompt/).


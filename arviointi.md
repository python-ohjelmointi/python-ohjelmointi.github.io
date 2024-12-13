---
title: 📈 Arviointi
layout: default
nav_order: 6
---

# Opintojakson arviointi

Opintojakson arviointi perustuu seuraaviin tekijöihin:

* Ohjelmointitehtävät 50 %
* Koe 30 %
* Aktiivisuustehtävät 20 %

Aktiivisuustehtävien 20 % tarkoittaa käytännössä, että aktiivisuus vaikuttaa arvosanaasi yhdellä numerolla.

**Minimisuoritukset**

* Ohjelmointitehtävät - minimisuoritus 25 % tehtävistä
* Koe - minimisuoritus 40 % koepisteistä
* Aktiivisuustehtävät - minimisuoritus 50 % tehtäväpisteistä

Kun kaikki kolme minimisuoritusta täyttyvät, opinto on suoritettu arvosanalla 1/5. Esimerkiksi jos aktiivisuus on alle 50 %, suoritus on hylätty.

## Aktiivisuustehtävät

Monipuolisen blended-toteutustavan vuoksi läsnäoloaktiivisuutta seurataan Teamsissa julkaistavilla **aktiivisuustehtävillä**. Aktiivisuustehtävät toteutetaan viikko kerrallaan, joten seuraa Teamsissa tapahtuvaa viestintää sekä oppitunteja. Aktiivisuustehtävien suhteen on voimassa seuraavat pelisäännöt:

* Aktiivisuustehtäviä saa tehdä yksin tai yhdessä muiden kanssa.
* Aktiivisuustehtävissä on sallittua käyttää mitä tahansa oppimateriaaleja sekä tekoälyä.
* Aktiivisuustehtävissä esiintyviä koodiesimerkkejä <del>saa</del> *kannattaa* kopioida omaan koodieditoriin koodin toiminnan kokeilemiseksi.
* Aktiivisuustehtävistä saa käydä vapaasti keskustelua kurssin tapaamisissa ja Teams-kanavalla.

*Taustatietoja*

Syksystä 2024 alkaen Haaga-Helian ohjeistuksen mukaan läsnäolo opetuksessa vaikuttaa arviointiin. Voit lukea linjausten julkisista osista lisää Haaga-Helian verkkosivuilta: [artikkeli 1](https://www.haaga-helia.fi/fi/ajankohtaista/uutiset/lasnaolosta-arvioinnin-edellytys-opintojaksoille-lisaa-elamaa-kampuksille), [artikkeli 2](https://www.haaga-helia.fi/fi/ajankohtaista/uutiset/haaga-helia-tarjoaa-jatkossakin-joustavaa-opiskelua-paivitetty-145).

> *"Opiskelija osoittaa aktiivisuutta esimerkiksi tuntikeskusteluissa, ryhmätöissä ja muissa annetuissa tehtävissä. Opettajat määrittävät, millaista aktiivisuutta kullakin opintojaksolla vaaditaan."*
>
> Haaga-Helia, 2024. [Haaga-Helia tarjoaa jatkossakin joustavaa opiskelua](https://www.haaga-helia.fi/fi/ajankohtaista/uutiset/haaga-helia-tarjoaa-jatkossakin-joustavaa-opiskelua-paivitetty-145)

Läsnäoloa mitataan aktiivisuustehtävillä, eli reaaliaikaista läsnäoloa ei vaadita kuin kokeessa. Haaga-Helian läsnäolovaatimusten mukaisesti hyväksyttyyn suoritukseen vaaditaan vähintään 50 % aktiivisuuspisteistä. Täydelliseen suoritukseen tarvitaan vastaavasti vähintään 75 % saatavilla olevista aktiivisuuspisteistä. Näiden rajojen väliin jäävät arvosanat määräytyvät lineaarisesti: mitä enemmän pisteitä saat, sitä korkeampi on arvosanasi aktiivisuustehtävien osalta.


## Kokeen arviointi

* Hyväksytty koesuoritus edellyttää, että saat vähintään 40 % kokeen pisteistä. Tämä oikeuttaa koearvosanaan 1.
* Jos saavutat 100 % pisteistä, saat kokeesta parhaan arvosanan, eli 5.
* Näiden rajojen väliin jäävät arvosanat määräytyvät lineaarisesti: mitä enemmän pisteitä saat, sitä korkeampi arvosana.
* Koearvosanaa ei pyöristetä, eli jokaisella saamallasi pisteellä on merkitystä kurssin loppuarvioinnissa.

Jokainen prosenttiyksikkö yli minimin (40 %) lisää arvosanaa tasaisesti. Arvosanojen välinen skaala on 4 (arvosanat 1–5) ja 60 % pisteistä jaetaan tasaisesti tälle skaalalle. Tämä tarkoittaa, että jokainen prosenttiyksikkö vastaa arvosanan nousua noin 0,0666666667.

Pythonilla arvosanan voi laskea seuraavasti:

```py
# koepisteiden muuntaminen arvosanaksi, kun omat pisteet ylittävät minimin
koearvosana = 1 + (omat_pisteet_prosentteina - 40) * 0.0666666667
```


## Ohjelmointitehtävien arviointi (TMC/mooc.fi)

* Hyväksytty kurssisuoritus edellyttää, että saavutat vähintään 25 % ohjelmointitehtävien pisteistä. Tämä oikeuttaa tehtävien osalta arvosanaan 1.
* Jos saavutat 100 % pisteistä, saat tehtävien osalta parhaan arvosanan, eli 5.
* Näiden rajojen väliin jäävät arvosanat määräytyvät lineaarisesti: mitä enemmän pisteitä saat, sitä korkeampi arvosana.
* Helsingin yliopiston arvostelusta poiketen Haaga-Helian toteutuksella ei yksittäisiin osioihin liittyviä minimipistemääriä. Pisteitä ei siis tarkastella osiokohtaisesti, vaan 25 % kokonaisuudesta riittää.

Jokainen prosenttiyksikkö yli minimin (25 %) lisää arvosanaa tasaisesti. Arvosanojen välinen skaala on 4 (arvosanat 1–5), ja 75 % pisteistä jaetaan tasaisesti tälle skaalalle. Tämä tarkoittaa, että jokainen prosenttiyksikkö vastaa arvosanan nousua noin 0,05333.

Pythonilla arvosanan voi laskea seuraavasti:

```py
# tehtäväpisteiden muuntaminen arvosanaksi, kun omat pisteet ylittävät minimin
arvosana = 1 + (omat_pisteet_prosentteina - 25) * 0.05333
```


### Mistä näen ohjelmointitehtävien pistemäärän?

Näet omat ohjelmointitehtävien pisteesi TMC-palvelusta kirjautumalla TMC-tunnuksillasi osoitteeseen [https://tmc.mooc.fi/org/haaga-helia/](https://tmc.mooc.fi/org/haaga-helia/). Tehtäväpisteet ovat myös näkyvillä VS Code:n TMC-laajennoksessa "My Courses"-näkymässä [tämän kuvan mukaisesti](/img/points-gained-tmc-plugin.png):

![My courses](/img/points-gained-tmc-plugin.png)


### Ohjelmointitehtävien DL

Mooc.fi:n eri osioiden tehtävillä ei ole tällä kurssilla erillisiä määräaikoja, vaan kaikkien tehtävien yhteinen DL on kurssin lopussa.


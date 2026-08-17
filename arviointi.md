---
title: 📈 Arviointi
layout: default
nav_order: 6
---

# Opintojakson arviointi

Opintojakson arviointi perustuu seuraaviin tekijöihin:

* Ohjelmointitehtävät 50 %
* Koe 50 %

**Minimisuoritukset**

* Ohjelmointitehtävät: minimisuoritus 25 % tehtäväpisteistä
* Koe: minimisuoritus 40 % koepisteistä


## Kokeen arviointi

* Hyväksytty koesuoritus edellyttää, että saat vähintään 40 % kokeen pisteistä. Tämä oikeuttaa koearvosanaan 1.
* Jos saavutat 100 % pisteistä, saat kokeesta parhaan arvosanan, eli 5.
* Näiden rajojen väliin jäävät arvosanat määräytyvät lineaarisesti: mitä enemmän pisteitä saat, sitä korkeampi arvosana.
* Koearvosanaa ei pyöristetä, eli jokaisella saamallasi pisteellä on merkitystä kurssin loppuarvioinnissa.

Jokainen prosenttiyksikkö yli minimin (40 %) lisää arvosanaa tasaisesti. Arvosanojen välinen vaihteluväli on 4 (arvosanat 1–5), ja minimipisteet ylittävä osuus (60 % pisteistä) jaetaan tasaisesti tälle välille. Tämä tarkoittaa, että jokainen prosenttiyksikkö vastaa arvosanan nousua noin 0,0666666667 yksikön verran.

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

Jokainen prosenttiyksikkö yli minimin (25 %) lisää arvosanaa tasaisesti. Hyväksyttyjen arvosanojen vaihteluväli on 4 (arvosanat 1–5), ja minimipisteet ylittävä osuus (75 % pisteistä) jaetaan tasaisesti tälle välille. Tämä tarkoittaa, että jokainen prosenttiyksikkö vastaa arvosanan nousua noin 0,05333 yksikön verran.

Pythonilla arvosanan voi laskea seuraavasti:

```py
# tehtäväpisteiden muuntaminen arvosanaksi, kun omat pisteet ylittävät minimin
arvosana = 1 + (omat_pisteet_prosentteina - 25) * 0.05333
```


### Mistä näen ohjelmointitehtävien pistemäärän?

Näet omat ohjelmointitehtävien pisteesi TMC-palvelusta kirjautumalla TMC-tunnuksillasi osoitteeseen [https://tmc.mooc.fi/org/haaga-helia/](https://tmc.mooc.fi/org/haaga-helia/). Tehtäväpisteet ovat myös näkyvillä VS Code:n TMC-laajennoksessa "My Courses"-näkymässä [tämän kuvan mukaisesti](/img/points-gained-tmc-plugin.png):

![My courses](/img/points-gained-tmc-plugin.png)


### Ohjelmointitehtävien DL

Mooc.fi:n eri osioiden tehtävillä ei ole tällä kurssilla erillisiä määräaikoja, vaan kaikkien tehtävien yhteinen DL on kurssin lopussa. Tarkasta tarkka päivämäärä oman toteutuksesi Moodlesta.


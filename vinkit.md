---
title: 💡 Vinkit
layout: default
nav_order: 9
---

# Kootut vinkit

Olemme koonneet tälle sivulle yleisimpiä vinkkejä, jotka auttavat ratkaisemaan kurssilla toistuvia ongelmia. Päivitämme sivua kurssin edetessä.
{: .fs-6 }

---

## Tehtävän jakaminen TMC:n "paste"-palvelussa

Jos tehtävä ei millään ratkea ja kaipaat apua, voit lähettää koodisi paste-palveluun, jonka kautta opettajat tai muut opiskelijat voivat perehtyä ratkaisuun ja antaa vinkkejä. Lähettäessäsi ratkaisusi paste-palveluun, saat linkin, jonka kautta sinä ja muut voitte avata koodisi nettiselaimella. Paste-pelveluun voi lähettää tiedostoja ainakin kahdella eri tavalla:

Tapa 1:

![Tiedoston lähettäminen TMC:n paste-palveluun](/img/tmc-paste1.png)

Tapa 2:

![Tiedoston lähettäminen TMC:n paste-palveluun](/img/tmc-paste2.png)


## "Pylance has crashed X times in the last Y minutes"

> *Pylance has crashed 5 times in the last 3 minutes. Pylance will not be restarted.*

Pylance on Visual Studio Coden laajennus, joka tarjoaa Python-koodin tarkistusta ja automaattista täydennystä. Jos saat yllä olevan virheilmoituksen, se tarkoittaa, että Pylance-laajennus on kaatunut useita kertoja peräkkäin.

Tämä virhe Pylance-laajennuksen kanssa johtuu usein siitä, että VS Code:ssa on avoinna kerrallaan liian monta hakemistoa. Pylance indeksoi kaikki avatut hakemistot ja jos niitä on liikaa, se voi kaatua. Tämä ongelma on yleinen erityisesti Windows-käyttöjärjestelmässä. Jos sinulla on kerrallaan "avattuna" workspace:ssa kymmeniä tehtäviä, voit kokeilla sulkea osan niistä TMC-näkymässä.


## Error while trying to run tests. Os error 5. Failed to create file at ***\\.tmc.lock

Tämä virhe tarkoittaa, että TMC ei pysty luomaan lukitustiedostoa, jolla varmistetaan, että vain yksi TMC-instanssi käyttää tiettyjä tiedostoja kerrallaan. Ongelma voi johtua puutteellisista käyttöoikeuksista tiedoston luomiseksi tai siitä, että tiedosto on jäänyt auki aikaisemman suorituksen kaatumisen vuoksi.

Ongelman tiedetään korjaantuneen monessa tapauksessa VS Code:n uudelleenkäynnistyksellä. Voit myös yrittää poistaa virheilmoituksessa esiintyvän `.tmc.lock`-tiedoston manuaalisesti.


## Fatal error during TestMyCode extension initialization: Error: ENOTEMPTY: directory not empty, rmdir

Tämä virhe korjaantuu tyypillisesti käynnistämällä VS Code uudelleen. Myös TMC-laajennoksen poisto, VS Coden uudelleenkäynnistys ja TMC:n asentaminen uudelleen ovat mahdollisia ratkaisuja.


## Tehtävästä puuttuu `src`-hakemisto

Jos avaat VS Code:n TMC-pluginin avulla tehtävän, jonka olet jo aikaisemmin ratkaissut mooc.fi:ssä, saattaa tehtävähakemistosta puuttua `src`-hakemisto sekä sen sisältämät tiedostot. Ongelma voi korjaantua klikkaamalla tehtävää hiiren kakkospainikkeella ja valitsemalla "Download old submission". Voit myös valita, haluatko tehdä nykyisestä versiosta kopion TMC-palvelimelle, mikä tuskin on tarpeen hakemiston puuttumisen vuoksi.

![Download old submission](./img/download-old-submission.jpg)


## "An invalid Python interpreter is selected" tai "Exited(9009)"

Mikäli VS Code varoittaa ongelmasta Python-tulkin kanssa tai TMC-laajennos kaatuu "Runtime Error"-virheeseen koodilla 9009, eivät VS Code ja TMC löydä Python-asennustasi.

Tämä johtuu tyypillisesti siitä, että Python ei joko ole asennettuna tai vaihtoehtoisesti Python-komentoa ei löydy käyttöjärjestelmän PATH-muuttujasta:

{: .highlight }
> *"PATH is an environment variable on Unix-like operating systems, DOS, OS/2, and Microsoft Windows, specifying a set of directories where executable programs are located. In general, each executing process or user session has its own PATH setting."*
>
> [https://en.wikipedia.org/wiki/PATH_(variable)](https://en.wikipedia.org/wiki/PATH_(variable))

Windows-asennusohjelmassa PATH-muuttujan asettaminen onnistuu yksinkertaisesti lisäämällä rasti asennusohjelmassa ruutuun "Add python.exe to PATH":

![Add python.exe to PATH](/img/installer-path.png)


## Ohjelmasi ei TMC:n mukaan tulosta mitään tai kysy syötteitä

> Tehtävissä, joissa ei erikseen pyydetä funktioiden toteuttamista, mitään koodia ei tule sijoittaa `if __name__ == "__main__"`-lohkoon.
>
> [mooc.fi](https://ohjelmointi-25.mooc.fi/osa-6/1-tiedostojen-lukeminen)


## Testi jää jumiin ja saat virheen "test timed out"

Ohjelmasi todennäköisesti pyytää syötettä, jota ei tulisi tehtävänannon mukaan pyytää. Tästä johtuen ohjelmasi jää odottamaan syötettä, jota TMC:n testit eivät anna. Lopulta TMC keskeyttää testit aikakatkaisun avulla.

Tarkasta että koodissa ei ole ylimääräisiä `input`-käskyjä. Tarvittaessa siirrä ohjelmaa testaavat tehtävänannon ulkopuoliset koodit `if __name__ == "__main__"`-lohkon sisään.


## Kattavampi testiraportti suorittamalla testit komentorivillä

Jos tehtävän tarkastaminen epäonnistuu virheeseen, kuten "funktiota ei löydy", on ongelman todellinen syy mahdollisesti ohjelmasi kaatuminen odottamattomasti. TMC-laajennoksen käyttöliittymä ei näytä tarkkoja virheilmoituksia, mutta saat virheen näkyviin suorittamalla tehtävän testit komentorivillä.

Testit tulee suorittaa halutun tehtävän ylähakemistossa, eli ei `src`-hakemiston alla. Suorita Python-asennuksestasi riippuen komento `python3 -m tmc` tai `py -m tmc`.

```
python3 -m tmc
```

Mikäli testit epäonnistuvat, saat todennäköisesti tarkemman virheilmoituksen, jonka perusteella voit tehdä korjauksia.

## SSL-virheet tehtävässä "Kurssien tilastot"

Tehtävässä [kurssien tilastot](https://ohjelmointi-25.mooc.fi/osa-7/4-datan-kasittely#netissa-olevan-tiedoston-hakeminen) moni opiskelija törmää SSL-sertifikaattivirheeseen. Tämä johtuu studies.cs.helsinki.fi-palvelimen sertifikaatista.

Voitte kiertää sertifikaattiongelmia vaihtamalla domainin <del>studies.cs.helsinki.fi</del> tilalle **python-ohjelmointi.github.io**. Muuten osoitteet ovat samat ja tehtävä toteutetaan aivan samalla tavalla kuin ohjeistettu. Käyttäkää siis vain näitä osoitteita: `https://python-ohjelmointi.github.io/stats-mock/api/courses/` ja `https://python-ohjelmointi.github.io/stats-mock/api/courses/****/stats`.

Nämä tiedostot ovat Helsingin yliopiston esimerkkidataa.

## TMC-laajennoksen käynnistys Windowsissa

Jos kohtaat seuraavan ongelman TMC-laajennoksen käynnistyksessä, kokeile määritellä laajennoksille ja käyttäjän datalle kansiot, joihin TMC-laajennoksella on varmasti kirjoitusoikeus.

```
[INFO] Starting moocfi.test-my-code in "production" mode.
[INFO] Visual Studio Code version: 1.56.2
[INFO] moocfi.test-my-code version: 2.1.0
[INFO] Currently open workspace: undefined
[INFO] Platform win32 Arch x64
[INFO] Run: "c:\\VSCODE\\settings\\User\\globalStorage\\moocfi.test-my-code\\cli\\tmc-langs-cli-x86_64-pc-windows-msvc-0.21.0-beta-4.exe" "--client-name" "vscode_plugin" "--client-version" "2.1.0" "core" "logged-in"
[ERROR] Failed to check if authenticated:
```

Kansiot voidaan määritellä VS Coden käynnistyksessä `--extensions-dir`- ja `--user-data-dir`-parametreilla. Luo itsellesi uusi pikakuvake Code.exe-tiedostoon esimerkiksi seuraavilla parametreilla:

```
ASENNUSHAKEMISTO\Code.exe --extensions-dir=C:\vscode\extensions --user-data-dir=C:\vscode\settings
```

Voit korvata yllä olevassa komennossa esiintyvät `C:\vscode\`-hakemistot vapaasti valitsemillasi tyhjillä hakemistoilla.

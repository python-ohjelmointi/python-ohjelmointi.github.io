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
> [mooc.fi](https://ohjelmointi-23.mooc.fi/osa-6/1-tiedostojen-lukeminen)


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

Tehtävässä [kurssien tilastot](https://ohjelmointi-23.mooc.fi/osa-7/4-datan-kasittely#netissa-olevan-tiedoston-hakeminen) moni opiskelija törmää SSL-sertifikaattivirheeseen. Tämä johtuu studies.cs.helsinki.fi-palvelimen sertifikaatista.

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

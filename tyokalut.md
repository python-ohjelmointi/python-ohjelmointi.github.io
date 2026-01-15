---
title: 💾 Työkalut ja asennukset
layout: default
nav_order: 4
---

# Kurssin työkalut

Kurssin suorittamiseksi tarvitset [Python 3 -ohjelmointiympäristön](https://www.python.org/downloads/) sekä [VS Code -koodieditorin](https://code.visualstudio.com/download).
{: .fs-6 }

---

## Python 3

Asenna itsellesi Python 3 -ohjelmointiympäristö Pythonin omalta kotisivulta [https://www.python.org/downloads/](https://www.python.org/downloads/). Suosittelemme valitsemaan uusimman 3.x -version. Asennus vaihtelee käyttöjärjestelmän mukaan ja löydät tarvittaessa Pythonin beginners guide -sivustolta [https://wiki.python.org/moin/BeginnersGuide](https://wiki.python.org/moin/BeginnersGuide) ohjeet eri käyttöjärjestelmille.

Käyttöjärjestelmästä riippuen sinulla voi olla myös pakettienhallintaohjelma tai sovelluskauppa, jonka avulla voit asentaa Pythonin.

Käyttöjärjestelmässäsi saattaa olla valmiiksi asennettuna Pythonin vanhempi versio. Voit käyttää myös vanhempia versioita, kunhan ne ovat edelleen Python Software Foundationin tukemia: [https://devguide.python.org/versions/#versions](https://devguide.python.org/versions/#versions).


### Järjestelmän PATH-ympäristömuuttuja

Suosittelemme asentamaan Pythonin niin, että sen asennushakemisto lisätään käyttöjärjetelmän PATH-ympäristömuuttujaan. Näin Python voidaan käynnistää mistä vain hakemistosta suoraan `python`- tai `python3`-komennolla ja myös VS Code sekä TMC-laajennos löytävät Python-työkalusi.

{: .highlight }
> *"PATH is an environment variable on Unix-like operating systems, DOS, OS/2, and Microsoft Windows, specifying a set of directories where executable programs are located. In general, each executing process or user session has its own PATH setting."*
>
> [https://en.wikipedia.org/wiki/PATH_(variable)](https://en.wikipedia.org/wiki/PATH_(variable))

Windows-asennusohjelmassa PATH-muuttujan asettaminen onnistuu yksinkertaisesti lisäämällä rasti asennusohjelmassa ruutuun "Add python.exe to PATH":

![Add python.exe to PATH](/img/installer-path.png)


## VS Code

Kurssin ainoa tuettu koodieditori on Visual Studio Code eli lyhyemmin VS Code:

> *"Visual Studio Code is a lightweight but powerful source code editor which runs on your desktop and is available for Windows, macOS and Linux. It comes with built-in support for JavaScript, TypeScript and Node.js and has a rich ecosystem of extensions for other languages and runtimes (such as C++, C#, Java, Python, PHP, Go, .NET)."*
>
> [https://code.visualstudio.com/docs](https://code.visualstudio.com/docs)

Asenna itsellesi osoitteesta [https://code.visualstudio.com/download](https://code.visualstudio.com/download).

Suosittelemme perehtymään myös [Getting Started -dokumentaatioon](https://code.visualstudio.com/docs) sekä [Introductory Videos -videoihin](https://code.visualstudio.com/docs/getstarted/introvideos).

{: .huom }
VS Code on kurssilla käytännössä pakollinen, koska siihen on saatavilla tehtävien automaattisessa arvioinnissa käytettävä TMC-laajennos. Laajennoksen asennusohjeet löydät sivulta [https://www.mooc.fi/installation/vscode/#TestMyCode-asentaminen](https://www.mooc.fi/installation/vscode/#TestMyCode-asentaminen).


## Mooc.fi ja TestMyCode (TMC)

Kurssin harjoitusten suorittamiseksi sinun tulee rekisteröityä Helsingin yliopiston [TestMyCode-järjestelmään (https://tmc.mooc.fi/)](https://tmc.mooc.fi/), joka huolehtii tehtävien automaattisesta tarkastamisesta ja pitää kirjaa saamistasi tehtäväpisteistä. Jos olet jo aikaisemmin rekisteröitynyt mooc.fi:n kursseille, voit käyttää olemassa olevaa käyttäjätunnustasi.

Käyttämälläsi sähköpostiosoitteella ei ole merkitystä, eli voit käyttää joko Haaga-Helian sähköpostiosoitettasi tai muuta osoitettasi.

{: .huom }
**Vaikka kurssilla hyödynnetään mooc.fi-sivuston tehtäviä, ei niitä voida palauttaa suoraan mooc.fi-sivustolle.** Mooc.fi-sivustolle mahdollisesti lähettämäsi ratkaisut eivät tallennu Haaga-Helian vaan Helsingin yliopiston rekisteriin.

Tehtävien palauttamisessa mooc-sivuston sijasta [**VS Code:n TMC-laajennosta**](/tehtavat/#testmycode-laajennos). Laajennoksen kautta käytössäsi on samat tehtävät ja niille suoritetaan samat testit kuin mooc-sivustolla.

TMC-laajennoksessa Haaga-Helian toteutuksen valinta onnistuu [tämän ohjesivun mukaisesti](/tehtavat/#testmycode-laajennos). Tehtävänannot löytyvät mooc.fi-sivustolta: [https://ohjelmointi-26.mooc.fi/kaikki-tehtavat/](https://ohjelmointi-26.mooc.fi/kaikki-tehtavat/).


### TestMyCode-laajennos

Tehtävien ratkaisut palautetaan VS Code:n TestMyCode (TMC) -laajennuksen avulla. Helsingin yliopiston ohjeista poiketen Haaga-Helian kurssilla tehtäviä **ei voi palauttaa mooc.fi-sivuston kautta**.

TMC-laajennoksen on kehittänyt Helsingin yliopiston Agile Education Research (RAGE) -tutkimusryhmä ja löydät sen lisenssi- ja tietosuojatiedot [GitHubista](https://github.com/rage/tmc-vscode) sekä [VS Code:n marketplace:sta](https://marketplace.visualstudio.com/items?itemName=moocfi.test-my-code).

> *"This extension provides TestMyCode integration for Visual Studio Code. Students can download, complete and submit course exercises directly from the editor."*
>
> [https://github.com/rage/tmc-vscode/](https://github.com/rage/tmc-vscode/), [https://marketplace.visualstudio.com/items?itemName=moocfi.test-my-code](https://marketplace.visualstudio.com/items?itemName=moocfi.test-my-code)


Lue Mooc.fi:n ohjeesta kohdat ["TestMyCode -laajennuksen asentaminen VS Codeen"](https://www.mooc.fi/fi/installation/vscode/#TestMyCode-asentaminen) sekä ["ohjelmoinnin aloittaminen"](https://www.mooc.fi/fi/installation/vscode/#ohjelmoinnin-aloittaminen). **Huom!** Ohjeessa käsitellään eri ohjelmointikieliä, mutta sinulle riittää Pythonia käsittelevä osuus. Et tarvitse Javaa eikä Mavenia.

Varmista lisäksi, että liityt myös VS Codessa oikealle kurssille tämän kuvan mukaisesti:

![Valitse Haaga-Helian kurssitoteutus](/img/kurssin-valinta-tmc.png)

{: .huom }
Haaga-Helian kurssin valitseminen on erittäin tärkeää, koska vain silloin näemme suorituksesi tällä kurssilla.


## Muut VS Code -laajennokset

VS Code suosittelee automaattisesti Python-laajennospaketin asentamista, kun avaat ensimmäisen Python-tiedoston. Suosittelemme asentamaan tämän laajennoksen, koska se tarjoaa monia hyödyllisiä ominaisuuksia Python-kehitykseen, kuten syntaksin korostuksen, koodin täydennyksen, virheiden tarkistuksen ja koodin suorituspainikkeet:

[Python extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

Lisäksi voit harkita seuraavien laajennosten asentamista, jotka voivat parantaa Python-kehityskokemustasi VS Codessa:

* [autopep8](https://marketplace.visualstudio.com/items?itemName=ms-python.autopep8) - "A Visual Studio Code extension with support for the autopep8 formatter." Auttaa koodin automaattisessa muotoilussa Pythonin muotoiluohjeiden (PEP 8) mukaisesti.
* [Pylint](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint) - "A Visual Studio Code extension with support for the Pylint linter." Tarjoaa työkaluja koodin laadun tarkistamiseen ja virheiden löytämiseen.
* [mypy](https://marketplace.visualstudio.com/items?itemName=ms-python.mypy-type-checker) - "A Visual Studio Code extension with support for the Mypy type checker." Auttaa tarkistamaan koodin tyyppivirheitä.

Asentaessasi VS Code -laajennoksia, pyri varmistumaan, että ne ovat luotettavia ja yleisesti käytettyjä, jotta ne eivät aiheuta turvallisuusriskejä tai muita ongelmia. Pyrimme tällä kurssilla käyttämään vain Microsoftin ja Helsingin yliopiston julkaisemia laajennoksia.

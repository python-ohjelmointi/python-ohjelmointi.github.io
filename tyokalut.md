---
title: 💾 Kurssin työkalut
layout: default
nav_order: 5
---

# Kurssin työkalut

Kurssin suorittamiseksi tarvitset [Python 3 -ohjelmointiympäristön](https://www.python.org/downloads/) sekä [VS Code -koodieditorin](https://code.visualstudio.com/download).
{: .fs-6 }

---

## Python 3

Asenna itsellesi Python 3 -ohjelmointiympäristö Pythonin omalta kotisivulta [https://www.python.org/downloads/](https://www.python.org/downloads/). Suosittelemme valitsemaan uusimman 3.x -version. Asennus vaihtelee käyttöjärjestelmän mukaan ja löydät tarvittaessa Pythonin beginners guide -sivustolta [https://wiki.python.org/moin/BeginnersGuide](https://wiki.python.org/moin/BeginnersGuide) ohjeet eri käyttöjärjestelmille.

Käyttöjärjestelmästä riippuen sinulla voi olla myös pakettienhallintaohjelma tai sovelluskauppa, jonka avulla voit asentaa Pythonin.

Käyttöjärjestelmässäsi saattaa olla valmiiksi asennettuna Pythonin vanhempi versio. Voit käyttää myös vanhempia versioita, kunhan ne ovat edelleen Python Software Foundationin tukemia: [https://devguide.python.org/versions/#versions](https://devguide.python.org/versions/#versions).

## Järjestelmän PATH-ympäristömuuttuja

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

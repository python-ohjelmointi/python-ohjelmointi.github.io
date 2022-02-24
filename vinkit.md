[🔙 Takaisin etusivulle](./)

# Kootut vinkit

## Ohjelmasi ei TMC:n mukaan tulosta mitään tai kysy syötteitä

> Tehtävissä, joissa ei erikseen pyydetä funktioiden toteuttamista, mitään koodia ei tule sijoittaa `if __name__ == "__main__"-lohkoon.`
>
> [mooc.fi](https://ohjelmointi-22.mooc.fi/osa-6/1-tiedostojen-lukeminen)

## Kattavampi testiraportti suorittamalla testit komentorivillä

Jos tehtävän tarkastaminen epäonnistuu virheeseen, kuten "funktiota ei löydy", on ongelman todellinen syy mahdollisesti ohjelmasi kaatuminen odottamattomasti. TMC-laajennoksen käyttöliittymä ei näytä tarkkoja virheilmoituksia, mutta saat virheen näkyviin suorittamalla tehtävän testit komentorivillä.

Testit tulee suorittaa halutun tehtävän ylähakemistossa, eli ei `src`-hakemiston alla. Suorita Python-asennuksestasi riippuen komento `python3 -m tmc` tai `py -m tmc`.

```
python3 -m tmc
```

Mikäli testit epäonnistuvat, saat todennäköisesti tarkemman virheilmoituksen, jonka perusteella voit tehdä korjauksia.

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

<script src="scripts.js"></script>
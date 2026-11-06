# MenüPreise24.de

Statische Website mit Speisekarten- und Preisübersichten für Restaurant- und Fast-Food-Ketten in Deutschland. `npm run build` erzeugt die Seiten aus den JSON-Dateien in `data/`. Es gibt keine Datenbank und kein serverseitiges Framework.

Seiten mit gesetztem `pricesCheckedAt` sind verlinkt. Dieselben Seiten wären bei einer späteren Freigabe die Index-Kandidaten. Solange `publicationAuthorized` nicht `true` ist, sendet jede HTML-Seite `noindex`. Seiten ohne Prüfdatum bleiben auch danach `noindex` und werden weiter ausgeliefert.

## Was die Seite kann

- Vorgerendertes HTML, ein Stylesheet und ein Skript für Tabellensuche, Filter und das Cookie-Banner
- JSON-LD (unter anderem FAQ, Menu, BreadcrumbList), `sitemap.xml` und `robots.txt`
- Google Analytics 4 erst nach Einwilligung: `gtag.js` lädt nur, wenn `menupreise24_cookie_consent` den Wert `accepted` hat
- Keine Werbeanzeigen, solange `adSenseId` in `data/site-meta.json` der Platzhalter `ca-pub-XXXXXXXXXXXXXXXX` ist

## Rechtliches

**Status: blockiert, Entwurf.** `publicationAuthorized` in `data/site-meta.json` steht auf `false`. Der Build setzt deshalb auf jeder HTML-Seite `noindex, follow`, lässt `sitemap.xml` leer und gibt keine Anbieterdaten aus. Das ist keine Freigabe und keine Aussage, dass die Seite die Kennzeichnungspflichten erfüllt.

Nicht bestätigt und deshalb nicht eingesetzt: Name des Anbieters, ladungsfähige Anschrift, Kontakt, verantwortliche Person. Eine deutsche Anschrift ist nicht angegeben. Bekannt ist keine Niederlassung in Deutschland; dass keine besteht, ist nicht ausdrücklich bestätigt. Die Beschreibung als persönliches Projekt ersetzt diese Angaben nicht und entscheidet nicht, welches Kennzeichenrecht gilt. Ob deutsches Kennzeichenrecht gilt, ist ungeklärt. Leere Felder gelten nicht als erledigt.

Keine E-Mail-Adresse. `contactEmail` bleibt leer, bis eine bestätigte Adresse zur Veröffentlichung vorliegt. Es wird keine Gesellschaft, kein Sitz und kein privater Ort ergänzt.

Die Datenschutzerklärung beschreibt nur Google Analytics 4 (Mess-ID aus `gaMeasurementId`, derzeit `G-XQZ1FTE721`, Verarbeitung durch Google Ireland Limited, Rechtsgrundlage Art. 6 Abs. 1 lit. a DSGVO, Laden erst nach Einwilligung). Werbe-Cookies werden dort nicht genannt. In diesem Stand ist keine Werbung und kein Verkauf eingebunden. Ein Werbekonto wird erst wieder betrachtet, wenn Anzeigen tatsächlich hinzukommen.

Veröffentlichung läuft weiter nur über `.github/workflows/deploy.yml` bei einem Push auf `main`. Dieser Stand ist dafür nicht freigegeben: nicht mergen, `main` nicht pushen, nicht deployen.

## Lokal bauen

```bash
npm run build
npm run serve
```

Danach liegt die Vorschau auf [http://localhost:3000](http://localhost:3000).

Eine neue Kette ist eine weitere JSON-Datei unter `data/chains/`. Orientierung geben die vorhandenen Dateien, zum Beispiel `data/chains/mcdonalds-preise.json`. Danach erneut `npm run build` ausführen.

Veröffentlichung ist in `.github/workflows/deploy.yml` hinterlegt und läuft bei einem Push auf `main`. Diese README ändert daran nichts.

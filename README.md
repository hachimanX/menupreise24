# MenüPreise24.de

Statische Website mit Speisekarten- und Preisübersichten für Restaurant- und Fast-Food-Ketten in Deutschland. `npm run build` erzeugt die Seiten aus den JSON-Dateien in `data/`. Es gibt keine Datenbank und kein serverseitiges Framework.

Seiten mit gesetztem `pricesCheckedAt` werden indexiert und verlinkt. Seiten ohne Prüfdatum werden weiter ausgeliefert, tragen aber `noindex`.

## Was die Seite kann

- Vorgerendertes HTML, ein Stylesheet und ein Skript für Tabellensuche, Filter und das Cookie-Banner
- JSON-LD (unter anderem FAQ, Menu, BreadcrumbList), `sitemap.xml` und `robots.txt`
- Google Analytics 4 erst nach Einwilligung: `gtag.js` lädt nur, wenn `menupreise24_cookie_consent` den Wert `accepted` hat
- Keine Werbeanzeigen, solange `adSenseId` in `data/site-meta.json` der Platzhalter `ca-pub-XXXXXXXXXXXXXXXX` ist

## Rechtliches

Das Impressum enthält die Platzhalter `{{OPERATOR_NAME}}`, `{{POSTAL_ADDRESS}}` und `{{RESPONSIBLE_PERSON}}` plus den Hinweis, dass die Angaben folgen und die Seite noch nicht rechtssicher freigegeben ist. Es ist keine fertige Anbieterkennzeichnung.

Vor einer öffentlichen Nutzung müssen die echten Betreiberdaten eingetragen werden. Alternativ bleibt die Entscheidung, das Impressum offline zu nehmen oder auf `noindex` zu stellen.

Die Datenschutzerklärung beschreibt Google Analytics 4 (Mess-ID aus `gaMeasurementId`, derzeit `G-XQZ1FTE721`, Verarbeitung durch Google Ireland Limited, Rechtsgrundlage Art. 6 Abs. 1 lit. a DSGVO). Werbe-Cookies werden dort nicht genannt, solange keine Anzeigen laufen.

## Lokal bauen

```bash
npm run build
npm run serve
```

Danach liegt die Vorschau auf [http://localhost:3000](http://localhost:3000).

Eine neue Kette ist eine weitere JSON-Datei unter `data/chains/`. Orientierung geben die vorhandenen Dateien, zum Beispiel `data/chains/mcdonalds-preise.json`. Danach erneut `npm run build` ausführen.

Veröffentlichung ist in `.github/workflows/deploy.yml` hinterlegt und läuft bei einem Push auf `main`. Diese README ändert daran nichts.

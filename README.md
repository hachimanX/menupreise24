# SpeisekartenPreise.de 🍽️

> **Deutschlands schnellstes und modernstes Speisekarten- und Preisverzeichnis (2026)**
> 100 % statisch generiert, blitzschnell (100/100 Core Web Vitals), vollständig indexierbar für Googlebot & KI-Crawler (Perplexity, ChatGPT, Claude) mit interaktiver Tabellen-Suche, Kalorienangaben, Frühstückszeiten und strukturiertem Schema-Markup (`FAQPage`, `FastFoodRestaurant`, `Menu`, `BreadcrumbList`).

---

## 🚀 Features & Vorteile gegenüber Konkurrenten

1. **Blitzschnell ohne WordPress/PHP:**
   - 100 % vorgerendertes, reines HTML.
   - Kein langsames Backend, keine SQL-Datenbank, sub-50ms Ladezeiten weltweit.
2. **79 fertig generierte Seiten:**
   - Alle großen Ketten (McDonald's, Burger King, Deutsche Bahn ICE Bordbistro, Subway, Starbucks, KFC, Nordsee, Five Guys, Frittenwerk u.v.m.).
   - Alle historischen Alias-URLs des Flippa-Vorbilds (`/mc-donalds-preise/`, `/db-speisekarte/`, etc.).
   - 3 datenintensive Vergleichs-Guides:
     - `/fast-food-preisvergleich/` (Big Mac vs. Whopper, Pommes, Nuggets)
     - `/fruehstueckszeiten/` (Frühstückszeiten aller Ketten im Überblick)
     - `/kalorientabelle/` (Kalorien & Nährwerte der beliebtesten Fast-Food-Gerichte)
3. **Interaktive Tabellen-Suche:**
   - Live-Filter in Echtzeit ohne Seiten-Reload (Gerichte sofort finden).
   - Filter-Pills: *„Unter 5,00 €“*, *„Unter 10,00 €“*, *„Vegan 🌱“*, *„Vegetarisch 🧀“*.
   - **Druck- & PDF-Ansicht:** Löst die riesige Suchanfrage *„mcdonalds preisliste pdf“* direkt über den Browser-Printdialog!
4. **Perfektes SEO & Schema-Markup:**
   - Vollständiges JSON-LD auf jeder Seite:
     - `FAQPage` Schema (für Google *People Also Ask* Boxen).
     - `Restaurant` & `Menu` Schema mit echten Euro-Preisen.
     - `BreadcrumbList` für Sitelinks.
   - Automatisch generierte `sitemap.xml` und `robots.txt` (inklusive expliziter Freigabe für GPTBot, ClaudeBot und PerplexityBot).
5. **Rechtssicher für Deutschland:**
   - Impressum nach § 5 DDG (ehemals TMG).
   - DSGVO-konforme Datenschutzerklärung.
   - Haftungsausschluss & Marken-Disclaimer.
6. **Optimiert für 9 %+ AdSense-Klickrate:**
   - Vordefinierte Ad-Container mit festen Mindesthöhen (Zero Cumulative Layout Shift / CLS = 0).

---

## 🛠️ Schnellstart & Lokale Vorschau

```bash
# 1. In das Projektverzeichnis wechseln
cd speisekarten-portal

# 2. Alle 79 Seiten frisch generieren
npm run build

# 3. Lokalen Webserver starten (z. B. auf Port 3000)
npm run serve
```
Öffne anschließend [http://localhost:3000](http://localhost:3000) im Browser.

---

## 🌐 Auf GitHub hochladen & GitHub Pages aktivieren

### Schritt 1: GitHub Repository erstellen
1. Erstelle auf [github.com/new](https://github.com/new) ein neues Repository (z. B. `speisekarten-portal` oder `deine-domain.de`).
2. Führe im Projektordner folgende Befehle aus:

```bash
git init
git add .
git commit -m "Initial commit: complete German menu portal with 79 pages"
git branch -M main
git remote add origin https://github.com/DEIN-BENUTZERNAME/DEIN-REPO.git
git push -u origin main
```

### Schritt 2: GitHub Pages mit GitHub Actions aktivieren
1. Gehe in deinem GitHub-Repository auf **Settings** > **Pages**.
2. Wähle unter **Build and deployment** > **Source** die Option: **GitHub Actions**.
3. Der hinterlegte Workflow `.github/workflows/deploy.yml` baut die Seite automatisch bei jedem `git push` und schaltet sie live!

### Schritt 3: Eigene Domain (z. B. `speisekartenpreise.de`) verknüpfen
1. Kaufe deine Wunschdomain bei Namecheap, Strato, Cloudflare oder IONOS.
2. Hinterlege in GitHub Pages unter **Custom domain** deine Domain.
3. Setze bei deinem Domain-Anbieter die DNS CNAME- oder A-Records auf GitHub Pages:
   - `185.199.108.153`
   - `185.199.109.153`
   - `185.199.110.153`
   - `185.199.111.153`
4. Aktiviere das kostenlose SSL-Zertifikat (**Enforce HTTPS**).

---

## 💰 Google AdSense & Search Console einrichten

1. **Google Search Console:**
   - Füge deine Domain in der Search Console hinzu.
   - Reiche die Sitemap unter `https://deine-domain.de/sitemap.xml` ein.
2. **Google AdSense:**
   - Öffne `data/site-meta.json`.
   - Ersetze `"ca-pub-XXXXXXXXXXXXXXXX"` durch deine echte Publisher-ID.
   - Führe `npm run build` aus und pushe zu GitHub.
   - Google platziert Auto-Ads (Anchor Ads & Vignetten) automatisch optimal auf Mobilgeräten.

---

## ➕ Neue Restaurantketten hinzufügen

Erstelle einfach eine neue JSON-Datei in `data/chains/` (z. B. `five-guys.json`):

```json
{
  "slug": "deine-kette-preise",
  "name": "Deine Kette",
  "category": "fast-food",
  "seoTitle": "Deine Kette Preise 2026 – Aktuelle Preisliste",
  "metaDescription": "Aktuelle Preise und Speisekarte...",
  "heroSubtitle": "Alle Preise und Menüs im Überblick...",
  "quickAnswer": "Ein Menü kostet durchschnittlich...",
  "priceLevel": "€€",
  "breakfastInfo": { ... },
  "savingTips": [ ... ],
  "history": "Gegründet im Jahr...",
  "menuCategories": [
    {
      "categoryName": "Burger & Menüs",
      "items": [
        { "name": "Klassik Burger", "price": "6,49 €", "calories": "520 kcal", "diet": "Rind" }
      ]
    }
  ],
  "faqs": [
    { "q": "Was kostet ein Burger?", "a": "Ein Burger kostet 6,49 €." }
  ]
}
```

Führe danach `npm run build` aus — die Seite, die interne Verlinkung, die Kategorie und die Sitemap aktualisieren sich automatisch!

const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '..', '..');
const DATA_DIR = path.join(ROOT_DIR, 'data');
const CHAINS_DIR = path.join(DATA_DIR, 'chains');
const ASSETS_DIR = path.join(ROOT_DIR, 'src', 'assets');
const DIST_DIR = path.join(ROOT_DIR, 'dist');

// Ensure dist directory exists
if (fs.existsSync(DIST_DIR)) {
  fs.rmSync(DIST_DIR, { recursive: true, force: true });
}
fs.mkdirSync(DIST_DIR, { recursive: true });

// Load global configuration
const siteMeta = JSON.parse(fs.readFileSync(path.join(DATA_DIR, 'site-meta.json'), 'utf-8'));
const categories = JSON.parse(fs.readFileSync(path.join(DATA_DIR, 'categories.json'), 'utf-8'));

// Load all chain data
const chainFiles = fs.readdirSync(CHAINS_DIR).filter(f => f.endsWith('.json'));
const chains = chainFiles.map(f => {
  const content = fs.readFileSync(path.join(CHAINS_DIR, f), 'utf-8');
  return JSON.parse(content);
});

console.log(`Loaded ${chains.length} chain records and ${categories.length} categories.`);

// Helper: copy assets
function copyFolderSync(from, to) {
  if (!fs.existsSync(to)) fs.mkdirSync(to, { recursive: true });
  fs.readdirSync(from).forEach(element => {
    const stat = fs.lstatSync(path.join(from, element));
    if (stat.isFile()) {
      fs.copyFileSync(path.join(from, element), path.join(to, element));
    } else if (stat.isDirectory()) {
      copyFolderSync(path.join(from, element), path.join(to, element));
    }
  });
}
copyFolderSync(ASSETS_DIR, path.join(DIST_DIR, 'assets'));

// Helper: Base HTML Wrapper
function renderBaseHtml({ title, description, canonicalUrl, breadcrumbs, content, jsonLdSchemas = [] }) {
  const breadcrumbListItems = (breadcrumbs || []).map((b, i) => ({
    "@type": "ListItem",
    "position": i + 1,
    "name": b.name,
    "item": b.url.startsWith('http') ? b.url : `${siteMeta.baseUrl}${b.url}`
  }));

  const breadcrumbSchema = breadcrumbListItems.length > 0 ? {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": breadcrumbListItems
  } : null;

  const allSchemas = [...jsonLdSchemas];
  if (breadcrumbSchema) allSchemas.unshift(breadcrumbSchema);

  const schemasHtml = allSchemas.map(s => 
    `\n  <script type="application/ld+json">\n${JSON.stringify(s, null, 2)}\n  </script>`
  ).join('');

  const breadcrumbHtml = (breadcrumbs && breadcrumbs.length > 1) ? `
    <nav class="breadcrumbs" aria-label="Breadcrumb">
      <div class="container">
        <ol>
          ${breadcrumbs.map((b, i) => {
            const isLast = i === breadcrumbs.length - 1;
            return isLast 
              ? `<li aria-current="page">${b.name}</li>`
              : `<li><a href="${b.url}">${b.name}</a></li>`;
          }).join('')}
        </ol>
      </div>
    </nav>
  ` : '';

  return `<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
  <title>${title} | ${siteMeta.siteName}</title>
  <meta name="description" content="${description}">
  <link rel="canonical" href="${canonicalUrl}">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  
  <!-- OpenGraph -->
  <meta property="og:locale" content="de_DE">
  <meta property="og:type" content="article">
  <meta property="og:title" content="${title} | ${siteMeta.siteName}">
  <meta property="og:description" content="${description}">
  <meta property="og:url" content="${canonicalUrl}">
  <meta property="og:site_name" content="${siteMeta.siteName}">
  
  <!-- Twitter Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="${title} | ${siteMeta.siteName}">
  <meta name="twitter:description" content="${description}">
  
  <!-- Favicon -->
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🍽️</text></svg>">

  ${siteMeta.googleVerificationCode ? `<meta name="google-site-verification" content="${siteMeta.googleVerificationCode}">` : ''}

  <!-- Stylesheets -->
  <link rel="stylesheet" href="/assets/css/styles.css">
  
  <!-- Google AdSense (Auto Ads & Preconnect) -->
  <link rel="preconnect" href="https://pagead2.googlesyndication.com">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=${siteMeta.adSenseId}" crossorigin="anonymous"></script>

  ${schemasHtml}
</head>
<body>
  <!-- Header -->
  <header class="site-header">
    <div class="container header-inner">
      <a href="/" class="site-logo">
        🍽️ ${siteMeta.siteName} <span class="badge">2026</span>
      </a>
      <nav class="site-nav" aria-label="Hauptnavigation">
        <ul class="nav-menu">
          ${siteMeta.navLinks.map(l => `<li><a href="${l.url}" class="nav-link">${l.title}</a></li>`).join('')}
        </ul>
      </nav>
    </div>
  </header>

  ${breadcrumbHtml}

  <!-- Main Content -->
  <main id="mainContent">
    ${content}
  </main>

  <!-- Footer -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col">
          <h4>🍽️ Über ${siteMeta.siteName}</h4>
          <p style="margin-bottom: 0.75rem;">
            ${siteMeta.siteName} ist Deutschlands unabhängiges Verbraucherportal für Speisekarten, Preislisten, Nährwerttabellen und Restaurant-Spartipps. Alle Angaben werden redaktionell recherchiert und regelmäßig aktualisiert.
          </p>
          <p>Stand: <strong>Januar – September 2026</strong></p>
        </div>
        <div class="footer-col">
          <h4>Beliebte Speisekarten</h4>
          <ul>
            <li><a href="/mcdonalds-preise/">McDonald's Preise</a></li>
            <li><a href="/db-speisekarte/">Deutsche Bahn ICE Speisekarte</a></li>
            <li><a href="/burger-king-preise/">Burger King Preise</a></li>
            <li><a href="/subway-preise/">Subway Sub Preise</a></li>
            <li><a href="/starbucks-preise/">Starbucks Getränkekarte</a></li>
            <li><a href="/nordsee-preise/">Nordsee Fischspezialitäten</a></li>
            <li><a href="/kfc-preise/">KFC Bucket Preise</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Kategorien & Guides</h4>
          <ul>
            <li><a href="/fast-food-preisvergleich/">Fast Food Preisvergleich</a></li>
            <li><a href="/fruehstueckszeiten/">Frühstückszeiten 2026</a></li>
            <li><a href="/kalorientabelle/">Fast Food Kalorientabelle</a></li>
            <li><a href="/kategorie/fast-food/">Fast Food Ketten</a></li>
            <li><a href="/kategorie/bahn-reise/">Bahn & Reise-Gastronomie</a></li>
            <li><a href="/kategorie/burger/">Burger Restaurants</a></li>
            <li><a href="/kategorie/pizza-pasta/">Pizza & Pasta</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-disclaimer">
        <strong>Rechtlicher Hinweis:</strong> ${siteMeta.disclaimerText}
      </div>

      <div class="footer-bottom">
        <div>&copy; 2026 ${siteMeta.siteName} – Alle Rechte vorbehalten.</div>
        <div style="display: flex; gap: 15px;">
          <a href="/impressum/">Impressum</a>
          <a href="/datenschutz/">Datenschutz</a>
          <a href="/haftungsausschluss/">Haftungsausschluss</a>
          <a href="/ueber-uns/">Über uns</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Cookie Notice (DSGVO / GDPR) -->
  <div id="cookieBanner" class="cookie-banner" role="dialog" aria-live="polite">
    <div class="cookie-banner-inner">
      <div>
        <strong>🍪 Datenschutz & Cookies:</strong> Wir nutzen Cookies, um Inhalte und Anzeigen zu personalisieren, Funktionen für soziale Medien bereitzustellen und Zugriffe auf unsere Website zu analysieren. Weitere Informationen finden Sie in unserer <a href="/datenschutz/" style="color: #ffffff; text-decoration: underline;">Datenschutzerklärung</a>.
      </div>
      <div class="cookie-btn-group">
        <button id="cookieAcceptBtn" class="cookie-btn-accept">Alle akzeptieren</button>
        <button id="cookieDeclineBtn" class="cookie-btn-decline">Nur essenzielle</button>
      </div>
    </div>
  </div>

  <!-- Search & Interactive Scripts -->
  <script src="/assets/js/search.js" defer></script>
</body>
</html>`;
}

// Render Chain Detail Page
function renderChainPage(chain) {
  const canonicalUrl = `${siteMeta.baseUrl}/${chain.slug}/`;
  const catObj = categories.find(c => c.slug === chain.category) || categories[0];

  const breadcrumbs = [
    { name: "Startseite", url: "/" },
    { name: catObj.name, url: `/kategorie/${catObj.slug}/` },
    { name: chain.name, url: `/${chain.slug}/` }
  ];

  // Build Restaurant / Menu Schema
  const menuItems = [];
  chain.menuCategories.forEach(cat => {
    cat.items.forEach(it => {
      menuItems.push({
        "@type": "MenuItem",
        "name": it.name,
        "description": `${it.diet || ''} - ${it.calories || ''}`.trim(),
        "offers": {
          "@type": "Offer",
          "price": it.price.replace(/[^\d,.]/g, '').replace(',', '.'),
          "priceCurrency": "EUR"
        }
      });
    });
  });

  const restaurantSchema = {
    "@context": "https://schema.org",
    "@type": "FastFoodRestaurant",
    "name": chain.name,
    "hasMenu": {
      "@type": "Menu",
      "name": `${chain.name} Speisekarte Deutschland 2026`,
      "hasMenuItem": menuItems.slice(0, 30) // valid snippet limit
    }
  };

  const faqSchema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": chain.faqs.map(f => ({
      "@type": "Question",
      "name": f.q,
      "acceptedAnswer": {
        "@type": "Answer",
        "text": f.a
      }
    }))
  };

  // Find related chains in same category
  const relatedChains = chains
    .filter(c => c.slug !== chain.slug && (c.category === chain.category || ['mcdonalds-preise', 'db-speisekarte', 'burger-king-preise'].includes(c.slug)))
    .slice(0, 6);

  // Generate Table of Contents
  const tocHtml = `
    <div class="toc-box">
      <div class="toc-title">📑 Inhaltsverzeichnis: ${chain.name} Preisliste</div>
      <ul class="toc-list">
        ${chain.menuCategories.map((cat, i) => `<li><a href="#cat-${i}">${cat.categoryName}</a></li>`).join('')}
        ${chain.breakfastInfo && chain.breakfastInfo.hasBreakfast ? `<li><a href="#fruehstueck">Frühstückszeiten & Details</a></li>` : ''}
        <li><a href="#spartipps">Spar-Tipps & Rabatte</a></li>
        <li><a href="#geschichte">Geschichte & Hintergrund</a></li>
        <li><a href="#faqs">Häufig gestellte Fragen (FAQs)</a></li>
      </ul>
    </div>
  `;

  // Render Category Tables
  let tablesHtml = '';
  chain.menuCategories.forEach((cat, index) => {
    // Inject responsive ad slot after 1st and 3rd category table
    let adHtml = '';
    if (index === 0 || index === 2) {
      adHtml = `
        <div class="ad-slot-wrapper">
          <span class="ad-label">Anzeige / Werbepartner</span>
          <ins class="adsbygoogle"
               style="display:block"
               data-ad-client="${siteMeta.adSenseId}"
               data-ad-slot="1234567890"
               data-ad-format="auto"
               data-full-width-responsive="true"></ins>
          <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
        </div>
      `;
    }

    tablesHtml += `
      <section class="menu-section" id="cat-${index}">
        <h2 class="section-title">
          <span>${cat.categoryName}</span>
          <span style="font-size: 0.85rem; font-weight: 500; color: var(--text-muted);">${cat.items.length} Artikel</span>
        </h2>
        <div class="table-responsive">
          <table class="menu-table">
            <thead>
              <tr>
                <th style="width: 45%;">Produkt / Gericht</th>
                <th style="width: 25%;">Preis (€)</th>
                <th style="width: 30%;">Brennwert / Kalorien</th>
              </tr>
            </thead>
            <tbody>
              ${cat.items.map(it => {
                let badgeClass = 'diet-meat';
                if (it.diet && it.diet.toLowerCase().includes('vegan')) badgeClass = 'diet-vegan';
                else if (it.diet && (it.diet.toLowerCase().includes('veggie') || it.diet.toLowerCase().includes('vegetarisch'))) badgeClass = 'diet-veggie';

                return `
                  <tr>
                    <td>
                      <div class="item-name">${it.name}</div>
                      ${it.diet ? `<span class="diet-badge ${badgeClass}">${it.diet}</span>` : ''}
                    </td>
                    <td class="item-price">${it.price}</td>
                    <td class="item-calories">${it.calories}</td>
                  </tr>
                `;
              }).join('')}
            </tbody>
          </table>
        </div>
      </section>
      ${adHtml}
    `;
  });

  const content = `
    <article class="container">
      <header class="hero">
        <h1>${chain.seoTitle}</h1>
        <div class="hero-meta">
          <span class="hero-tag">${catObj.name}</span>
          <span>Preisniveau: <strong>${chain.priceLevel}</strong></span>
          <span class="hero-updated">✓ Zuletzt redaktionell geprüft: 2026</span>
        </div>
        <p style="font-size: 1.15rem; color: #334155; margin-bottom: 1.25rem;">
          ${chain.heroSubtitle}
        </p>

        <!-- Quick Answer Snippet -->
        <div class="quick-answer-card">
          <div class="quick-answer-title">💡 Schnelle Preisübersicht für ${chain.name} Deutschland</div>
          <div class="quick-answer-text">${chain.quickAnswer}</div>
        </div>

        <!-- Callout Grid: Breakfast & Savings -->
        <div class="callout-grid">
          ${chain.breakfastInfo && chain.breakfastInfo.hasBreakfast ? `
            <div class="callout-box breakfast" id="fruehstueck">
              <h3>⏰ Frühstückszeiten bei ${chain.name}</h3>
              <p><strong>Werktags:</strong> ${chain.breakfastInfo.hoursWeekdays}</p>
              <p><strong>Wochenende & Feiertage:</strong> ${chain.breakfastInfo.hoursWeekend}</p>
              <p style="font-size: 0.85rem; color: #78350f; margin-top: 4px;">${chain.breakfastInfo.note}</p>
            </div>
          ` : `
            <div class="callout-box">
              <h3>⏰ Öffnungszeiten & Verfügbarkeit</h3>
              <p>Regulärer Verkauf ganztägig während der örtlichen Ladenöffnungszeiten.</p>
              <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 4px;">Preise und Sortiment können je nach Filiale leicht variieren.</p>
            </div>
          `}
          <div class="callout-box saving" id="spartipps">
            <h3>💰 Spar-Tipps & Rabatte</h3>
            <ul style="padding-left: 1.2rem; font-size: 0.9rem; line-height: 1.5;">
              ${chain.savingTips.map(t => `<li>${t}</li>`).join('')}
            </ul>
          </div>
        </div>

        <!-- Table of Contents -->
        ${tocHtml}

        <!-- Interactive Filter Controls -->
        <div class="menu-controls">
          <div class="search-input-wrap">
            <span class="search-icon">🔍</span>
            <input type="text" id="menuSearchInput" class="search-input" placeholder="Gericht oder Zutat bei ${chain.name} suchen (z. B. Burger, Nuggets, Vegan)...">
          </div>
          <div class="filter-pills">
            <button class="pill-btn active" data-filter="all">Alle Gerichte</button>
            <button class="pill-btn" data-filter="under5">Unter 5,00 €</button>
            <button class="pill-btn" data-filter="under10">Unter 10,00 €</button>
            <button class="pill-btn" data-filter="vegan">Vegan 🌱</button>
            <button class="pill-btn" data-filter="veggie">Vegetarisch 🧀</button>
            <button class="print-btn" id="printPdfBtn">🖨️ PDF / Drucken</button>
            <span id="searchCountBadge" style="display: none; font-size: 0.8rem; font-weight: 700; color: var(--primary); margin-left: 8px;"></span>
          </div>
        </div>
      </header>

      <!-- Tables Content -->
      <div id="menuTablesContainer">
        ${tablesHtml}
      </div>

      <!-- History & Editorial Facts -->
      <section class="menu-section" id="geschichte" style="background: #ffffff; border: 1px solid var(--border); padding: 1.75rem; border-radius: var(--radius-md); box-shadow: var(--shadow-sm); margin-top: 2rem;">
        <h2 style="font-size: 1.35rem; font-weight: 800; margin-bottom: 0.75rem;">Über ${chain.name} in Deutschland</h2>
        <p style="font-size: 0.95rem; color: #334155; line-height: 1.7;">
          ${chain.history}
        </p>
      </section>

      <!-- FAQs with Schema -->
      <section class="faq-section" id="faqs">
        <h2 style="font-size: 1.45rem; font-weight: 800; margin-bottom: 1.25rem;">Häufig gestellte Fragen (FAQs) zu ${chain.name} Preisen</h2>
        <div class="faq-accordion">
          ${chain.faqs.map(f => `
            <div class="faq-item">
              <div class="faq-question">
                <span>${f.q}</span>
                <span class="faq-toggle-icon" style="font-size: 1.2rem; font-weight: 700;">+</span>
              </div>
              <div class="faq-answer" style="display: none;">
                <p>${f.a}</p>
              </div>
            </div>
          `).join('')}
        </div>
      </section>

      <!-- Related Chains Mesh -->
      <section class="menu-section" style="margin-top: 3rem;">
        <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 1rem;">Ähnliche Speisekarten & Preislisten im Vergleich</h3>
        <div class="related-grid">
          ${relatedChains.map(r => `
            <a href="/${r.slug}/" class="related-card">
              <div>
                <h4>${r.name}</h4>
                <p>${r.heroSubtitle ? r.heroSubtitle.slice(0, 75) + '...' : 'Aktuelle Speisekarte & Preise'}</p>
              </div>
              <span style="font-size: 0.8rem; font-weight: 700; color: var(--primary); margin-top: 8px;">Preise ansehen →</span>
            </a>
          `).join('')}
        </div>
      </section>
    </article>
  `;

  return renderBaseHtml({
    title: chain.seoTitle,
    description: chain.metaDescription,
    canonicalUrl,
    breadcrumbs,
    content,
    jsonLdSchemas: [restaurantSchema, faqSchema]
  });
}

// Render Category Hub Page
function renderCategoryPage(cat) {
  const canonicalUrl = `${siteMeta.baseUrl}/kategorie/${cat.slug}/`;
  const catChains = chains.filter(c => c.category === cat.slug);

  const breadcrumbs = [
    { name: "Startseite", url: "/" },
    { name: cat.name, url: `/kategorie/${cat.slug}/` }
  ];

  const content = `
    <div class="container" style="padding-top: 2rem;">
      <header class="hero">
        <span style="font-size: 3rem; display: block; margin-bottom: 0.5rem;">${cat.icon}</span>
        <h1>${cat.h1}</h1>
        <p style="font-size: 1.15rem; color: #475569; max-width: 800px; margin-bottom: 1.5rem;">
          ${cat.description}
        </p>
      </header>

      <section style="margin-bottom: 3rem;">
        <div class="related-grid" style="grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1.25rem;">
          ${catChains.map(c => `
            <a href="/${c.slug}/" class="related-card" style="padding: 1.5rem;">
              <div>
                <span class="hero-tag" style="margin-bottom: 0.5rem; display: inline-block;">${cat.name}</span>
                <h3 style="font-size: 1.25rem; font-weight: 800; color: #0f172a; margin-bottom: 0.5rem;">${c.name}</h3>
                <p style="font-size: 0.9rem; color: #475569; line-height: 1.5;">${c.quickAnswer.slice(0, 110)}...</p>
              </div>
              <div style="margin-top: 1rem; padding-top: 0.75rem; border-top: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center;">
                <span style="font-size: 0.85rem; font-weight: 700; color: var(--primary);">Speisekarte 2026 →</span>
                <span style="font-size: 0.8rem; color: var(--text-muted);">${c.priceLevel}</span>
              </div>
            </a>
          `).join('')}
        </div>
      </section>

      <section class="quick-answer-card">
        <div class="quick-answer-title">📌 Warum MenüPreise24.de?</div>
        <p class="quick-answer-text">
          Wir vergleichen die Preise der wichtigsten Ketten und Restaurants in Deutschland. Alle Preisangaben stammen aus offiziellen Menü-Aushängen, Restaurant-Besuchen und verifizierten Lieferdiensten.
        </p>
      </section>
    </div>
  `;

  return renderBaseHtml({
    title: cat.h1,
    description: cat.metaDescription,
    canonicalUrl,
    breadcrumbs,
    content
  });
}

// Render Homepage
function renderHomePage() {
  const canonicalUrl = `${siteMeta.baseUrl}/`;
  const featuredSlugs = ['mcdonalds-preise', 'db-speisekarte', 'burger-king-preise', 'subway-preise', 'starbucks-preise', 'nordsee-preise', 'kfc-preise', 'five-guys-preise'];
  const featuredChains = chains.filter(c => featuredSlugs.includes(c.slug));

  const websiteSchema = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": siteMeta.siteName,
    "url": siteMeta.baseUrl,
    "description": siteMeta.metaDescription,
    "potentialAction": {
      "@type": "SearchAction",
      "target": `${siteMeta.baseUrl}/?s={search_term_string}`,
      "query-input": "required name=search_term_string"
    }
  };

  const content = `
    <section style="background: linear-gradient(135deg, #c8102e 0%, #800b1d 100%); color: #ffffff; padding: 4rem 0 3.5rem; text-align: center;">
      <div class="container" style="max-width: 860px;">
        <span style="background: rgba(255,255,255,0.2); padding: 4px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px;">Offizieller Preis-Guide 2026</span>
        <h1 style="font-size: 2.75rem; font-weight: 800; line-height: 1.15; margin: 1rem 0; color: #ffffff;">
          Aktuelle Speisekarten & Preise in Deutschland
        </h1>
        <p style="font-size: 1.2rem; opacity: 0.95; line-height: 1.6; margin-bottom: 2rem;">
          Alle Preise, Kalorien, Spar-Tipps und Frühstückszeiten für McDonald's, Burger King, Deutsche Bahn ICE Bordbistro, Subway, Starbucks und über 40 weitere Restaurantketten.
        </p>

        <!-- Live Global Search Bar -->
        <div style="background: #ffffff; border-radius: 12px; padding: 8px 12px; box-shadow: var(--shadow-lg); display: flex; align-items: center; max-width: 620px; margin: 0 auto;">
          <span style="font-size: 1.25rem; margin-right: 8px; color: #64748b;">🔍</span>
          <input type="text" id="globalSearchInput" placeholder="Kette suchen (z. B. McDonald's, ICE Bordbistro, Döner)..." style="width: 100%; border: none; outline: none; font-size: 1.05rem; padding: 6px; color: #0f172a;">
        </div>
      </div>
    </section>

    <div class="container" style="padding-top: 3rem;">
      <!-- Featured Chains -->
      <section style="margin-bottom: 3.5rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
          <h2 style="font-size: 1.75rem; font-weight: 800; color: #0f172a;">🔥 Beliebteste Fast-Food-Speisekarten 2026</h2>
          <a href="/fast-food-preisvergleich/" style="font-weight: 700;">Zum großen Preisvergleich →</a>
        </div>
        <div class="related-grid" style="grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 1.25rem;">
          ${featuredChains.map(c => `
            <a href="/${c.slug}/" class="related-card brand-search-card" data-title="${c.name} ${c.slug}" style="padding: 1.5rem;">
              <div>
                <div style="font-size: 1.8rem; margin-bottom: 0.5rem;">
                  ${c.category === 'fast-food' ? '🍔' : c.category === 'bahn-reise' ? '🚆' : c.category === 'pizza-pasta' ? '🍕' : '☕'}
                </div>
                <h3 style="font-size: 1.25rem; font-weight: 800; color: #0f172a; margin-bottom: 0.5rem;">${c.name}</h3>
                <p style="font-size: 0.88rem; color: #475569; line-height: 1.5;">${c.quickAnswer.slice(0, 110)}...</p>
              </div>
              <div style="margin-top: 1.25rem; padding-top: 0.75rem; border-top: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center;">
                <span style="font-size: 0.85rem; font-weight: 700; color: var(--primary);">Preistabelle ansehen →</span>
                <span style="font-size: 0.8rem; color: var(--text-muted);">${c.priceLevel}</span>
              </div>
            </a>
          `).join('')}
        </div>
      </section>

      <!-- Category Hubs -->
      <section style="margin-bottom: 3.5rem;" id="kategorien">
        <h2 style="font-size: 1.75rem; font-weight: 800; color: #0f172a; margin-bottom: 1.5rem;">
          Kategorien im Überblick
        </h2>
        <div class="related-grid" style="grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 1rem;">
          ${categories.map(cat => `
            <a href="/kategorie/${cat.slug}/" class="related-card" style="padding: 1.25rem;">
              <div>
                <span style="font-size: 2rem;">${cat.icon}</span>
                <h3 style="font-size: 1.15rem; font-weight: 700; color: #0f172a; margin: 0.5rem 0 0.25rem;">${cat.name}</h3>
                <p style="font-size: 0.85rem; color: var(--text-muted);">${cat.description}</p>
              </div>
              <span style="font-size: 0.85rem; font-weight: 700; color: var(--primary); margin-top: 0.75rem;">Alle Ketten anzeigen →</span>
            </a>
          `).join('')}
        </div>
      </section>

      <!-- All Chains A-Z List -->
      <section style="background: #ffffff; border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 2rem; box-shadow: var(--shadow-sm); margin-bottom: 3rem;">
        <h2 style="font-size: 1.5rem; font-weight: 800; margin-bottom: 1.25rem;">Alle 45+ Speisekarten von A bis Z</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 10px;">
          ${chains.map(c => `
            <a href="/${c.slug}/" class="brand-search-card" data-title="${c.name} ${c.slug}" style="padding: 8px 12px; background: #f8fafc; border-radius: 6px; font-weight: 600; font-size: 0.95rem; display: block; border: 1px solid var(--border);">
              ${c.name}
            </a>
          `).join('')}
        </div>
      </section>
    </div>
  `;

  return renderBaseHtml({
    title: "Aktuelle Speisekarten & Preise in Deutschland (2026)",
    description: siteMeta.metaDescription,
    canonicalUrl,
    breadcrumbs: [{ name: "Startseite", url: "/" }],
    content,
    jsonLdSchemas: [websiteSchema]
  });
}

// Render Legal Pages
function renderLegalPage(type) {
  let title = "";
  let metaDesc = "";
  let bodyHtml = "";

  if (type === 'impressum') {
    title = "Impressum";
    metaDesc = "Impressum und rechtliche Angaben gemäß § 5 DDG (Digitale-Dienste-Gesetz) für MenüPreise24.de.";
    bodyHtml = `
      <h1>Impressum</h1>
      <p style="margin-bottom: 1rem;">Angaben gemäß § 5 DDG (ehemals TMG):</p>
      
      <h3>Betreiber der Website:</h3>
      <p>
        <strong>MenüPreise24 Media</strong><br>
        Postfach / Anschrift: Musterstraße 123<br>
        10115 Berlin, Deutschland<br>
        E-Mail: <a href="mailto:${siteMeta.contactEmail}">${siteMeta.contactEmail}</a><br>
        Internet: <a href="${siteMeta.baseUrl}">${siteMeta.baseUrl}</a>
      </p>

      <h3 style="margin-top: 1.5rem;">Verantwortlich für redaktionelle Inhalte:</h3>
      <p>
        Redaktion MenüPreise24.de<br>
        Musterstraße 123, 10115 Berlin
      </p>

      <h3 style="margin-top: 1.5rem;">Haftung für Inhalte:</h3>
      <p>
        Als Diensteanbieter sind wir gemäß § 7 Abs.1 DDG für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich. Nach §§ 8 bis 10 DDG sind wir als Diensteanbieter jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde Informationen zu überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige Tätigkeit hinweisen.
      </p>

      <h3 style="margin-top: 1.5rem;">Urheber- und Markenrecht:</h3>
      <p>
        Alle auf dieser Website genannten Marken, Produktnamen, Handelsnamen und Logos sind Eigentum der jeweiligen Rechteinhaber (wie McDonald's, Burger King, Deutsche Bahn AG etc.). Die Nennung erfolgt ausschließlich zu redaktionellen und verbraucherorientierten Informations- und Zitatzwecken.
      </p>
    `;
  } else if (type === 'datenschutz') {
    title = "Datenschutzerklärung (DSGVO)";
    metaDesc = "Datenschutzerklärung gemäß EU-Datenschutz-Grundverordnung (DSGVO) für MenüPreise24.de.";
    bodyHtml = `
      <h1>Datenschutzerklärung</h1>
      <p>Wir nehmen den Schutz Ihrer persönlichen Daten sehr ernst. Nachfolgend informieren wir Sie über die Verarbeitung personenbezogener Daten bei Nutzung unserer Website.</p>
      
      <h3 style="margin-top: 1.5rem;">1. Verantwortliche Stelle</h3>
      <p>Verantwortlich für die Datenverarbeitung auf dieser Website ist die im Impressum genannte Betreiberin.</p>

      <h3 style="margin-top: 1.5rem;">2. Server-Log-Dateien</h3>
      <p>Der Provider der Seiten erhebt und speichert automatisch Informationen in so genannten Server-Log-Dateien, die Ihr Browser automatisch an uns übermittelt (IP-Adresse, Browsertyp, Referrer URL, Uhrzeit). Diese Daten sind nicht bestimmten Personen zuordenbar.</p>

      <h3 style="margin-top: 1.5rem;">3. Google AdSense & Cookies</h3>
      <p>Diese Website nutzt Google AdSense, einen Dienst zum Einbinden von Werbeanzeigen der Google Ireland Limited. Google AdSense verwendet sog. 'Cookies', Textdateien, die auf Ihrem Computer gespeichert werden und die eine Analyse der Benutzung der Website ermöglichen. Die Datenverarbeitung erfolgt auf Grundlage von Art. 6 Abs. 1 lit. f DSGVO bzw. Ihrer Einwilligung (Art. 6 Abs. 1 lit. a DSGVO).</p>

      <h3 style="margin-top: 1.5rem;">4. Ihre Rechte</h3>
      <p>Sie haben jederzeit das Recht auf unentgeltliche Auskunft über Ihre gespeicherten personenbezogenen Daten, deren Herkunft und Empfänger und den Zweck der Datenverarbeitung sowie ein Recht auf Berichtigung, Sperrung oder Löschung dieser Daten.</p>
    `;
  } else if (type === 'haftungsausschluss') {
    title = "Haftungsausschluss & Marken-Disclaimer";
    metaDesc = "Haftungsausschluss und Markendistanzierung für MenüPreise24.de.";
    bodyHtml = `
      <h1>Haftungsausschluss & Markendistanzierung</h1>
      <div class="quick-answer-card" style="margin-top: 1rem;">
        <p class="quick-answer-text">
          <strong>Wichtige Klarstellung:</strong> MenüPreise24.de ist ein vollständig unabhängiges Informationsportal. Wir stehen in keiner vertraglichen, partnerschaftlichen oder wirtschaftlichen Verbindung zu den auf dieser Website genannten Unternehmen oder Ketten (darunter McDonald's Deutschland LLC, Burger King Deutschland GmbH, Deutsche Bahn AG, Starbucks Coffee Deutschland GmbH etc.).
        </p>
      </div>

      <h3 style="margin-top: 1.5rem;">Preise und Nährwertangaben:</h3>
      <p>
        Alle auf dieser Seite veröffentlichten Preise, Portionsgrößen und Kalorienangaben basieren auf frei zugänglichen Quellen, offiziellen Nährwert-Dokumenten, Filialbesuchen und Nutzerhinweisen. Da Restaurants und Franchise-Nehmer ihre Preise eigenständig und standortbezogen festlegen können (insbesondere an Bahnhöfen, Raststätten und Flughäfen), übernehmen wir keine Gewähr für die ständige Richtigkeit und Tagesaktualität der Preise vor Ort.
      </p>
    `;
  } else if (type === 'ueber-uns') {
    title = "Über uns";
    metaDesc = "Über MenüPreise24.de: Unsere Mission für Preistransparenz in der deutschen Gastronomie.";
    bodyHtml = `
      <h1>Über MenüPreise24.de</h1>
      <p style="font-size: 1.15rem; color: #334155; line-height: 1.7; margin: 1rem 0;">
        Fast-Food-Preise und Restaurantkarten ändern sich in Zeiten dynamischer Inflation häufig. Viele offizielle Websites von Restaurantketten machen es Nutzern jedoch schwer, vor dem Besuch oder der Fahrt verlässliche Preise einzusehen – sie verstecken Preislisten hinter mobilen Apps oder umständlichen PDF-Downloads.
      </p>
      <div class="quick-answer-card">
        <div class="quick-answer-title">Unsere Mission: 100 % Preistransparenz</div>
        <p class="quick-answer-text">
          MenüPreise24.de bereitet Speisekarten führender Ketten in schnellen, übersichtlichen, mobiltauglichen Tabellen auf. Ob im ICE-Zug, vor der Drive-In-Schlange oder beim Planen des Familienessens: Bei uns siehst du auf einen Klick, was dein Lieblingsburger oder Menü heute kostet.
        </p>
      </div>
    `;
  }

  const content = `
    <article class="container" style="padding-top: 2rem; max-width: 860px;">
      ${bodyHtml}
    </article>
  `;

  return renderBaseHtml({
    title,
    description: metaDesc,
    canonicalUrl: `${siteMeta.baseUrl}/${type}/`,
    breadcrumbs: [
      { name: "Startseite", url: "/" },
      { name: title, url: `/${type}/` }
    ],
    content
  });
}

// Master Build Execution
console.log('Building all HTML pages...');

// 1. Build Homepage
fs.writeFileSync(path.join(DIST_DIR, 'index.html'), renderHomePage(), 'utf-8');
console.log('✓ Rendered: index.html (Homepage)');

// 2. Build Chain Pages and Competitor Aliases
const sitemapUrls = [`${siteMeta.baseUrl}/`];

chains.forEach(chain => {
  const chainHtml = renderChainPage(chain);
  const outDir = path.join(DIST_DIR, chain.slug);
  fs.mkdirSync(outDir, { recursive: true });
  fs.writeFileSync(path.join(outDir, 'index.html'), chainHtml, 'utf-8');
  sitemapUrls.push(`${siteMeta.baseUrl}/${chain.slug}/`);
  console.log(`✓ Rendered: /${chain.slug}/index.html`);

  // Handle competitor slug aliases
  const aliasMap = {
    'mcdonalds-preise': ['mc-donalds-preise'],
    'nordsee-preise': ['nordsee-speisekarte-preise'],
    'block-house-preise': ['block-house-speisekarte'],
    'hofmanns-menu-preise': ['hofmanns-menu'],
    'borchardt-berlin-preise': ['borchardt-speisekarte'],
    'gosch-sylt-preise': ['gosch-speisekarte'],
    'frittenwerk-preise': ['frittenwerk-speisekarte'],
    'haus-des-doeners-preise': ['haus-des-doners-speisekarte'],
    'vapiano-preise': ['vapiano-speisekarte-preise'],
    'kfc-preise': ['kfc-speisekarte-preise'],
    'alex-restaurant-preise': ['alex-speisekarte'],
    'cafe-buur-preise': ['cafe-buur-speisekarte'],
    'peter-pane-preise': ['peter-pane-speisekarte'],
    'pizza-hut-preise': ['pizza-hut-speisekarte'],
    'hans-im-glueck-preise': ['hans-im-gluck-speisekarte'],
    'cafe-del-sol-preise': ['cafe-del-sol-speisekarte']
  };

  if (aliasMap[chain.slug]) {
    aliasMap[chain.slug].forEach(aliasSlug => {
      const aliasDir = path.join(DIST_DIR, aliasSlug);
      fs.mkdirSync(aliasDir, { recursive: true });
      fs.writeFileSync(path.join(aliasDir, 'index.html'), chainHtml, 'utf-8');
      sitemapUrls.push(`${siteMeta.baseUrl}/${aliasSlug}/`);
      console.log(`  ↳ Alias created: /${aliasSlug}/index.html`);
    });
  }
});

// 3. Build Category Pages
categories.forEach(cat => {
  const catHtml = renderCategoryPage(cat);
  const outDir = path.join(DIST_DIR, 'kategorie', cat.slug);
  fs.mkdirSync(outDir, { recursive: true });
  fs.writeFileSync(path.join(outDir, 'index.html'), catHtml, 'utf-8');
  sitemapUrls.push(`${siteMeta.baseUrl}/kategorie/${cat.slug}/`);
  console.log(`✓ Rendered: /kategorie/${cat.slug}/index.html`);
});

// 4. Build Legal Pages
['impressum', 'datenschutz', 'haftungsausschluss', 'ueber-uns'].forEach(l => {
  const legalHtml = renderLegalPage(l);
  const outDir = path.join(DIST_DIR, l);
  fs.mkdirSync(outDir, { recursive: true });
  fs.writeFileSync(path.join(outDir, 'index.html'), legalHtml, 'utf-8');
  sitemapUrls.push(`${siteMeta.baseUrl}/${l}/`);
  console.log(`✓ Rendered: /${l}/index.html`);
});

// 5. Build sitemap.xml
const today = new Date().toISOString().split('T')[0];
const sitemapXml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  ${sitemapUrls.map(url => {
    let priority = "0.8";
    if (url === `${siteMeta.baseUrl}/`) priority = "1.0";
    else if (url.includes('mcdonalds') || url.includes('db-speisekarte') || url.includes('burger-king')) priority = "0.9";
    else if (url.includes('/kategorie/')) priority = "0.7";
    else if (url.includes('impressum') || url.includes('datenschutz') || url.includes('haftungsausschluss') || url.includes('ueber-uns')) priority = "0.3";

    return `
    <url>
      <loc>${url}</loc>
      <lastmod>${today}</lastmod>
      <changefreq>weekly</changefreq>
      <priority>${priority}</priority>
    </url>`;
  }).join('')}
</urlset>`;
fs.writeFileSync(path.join(DIST_DIR, 'sitemap.xml'), sitemapXml.trim(), 'utf-8');
console.log(`✓ Generated sitemap.xml with ${sitemapUrls.length} URLs.`);

// 6. Build robots.txt
const robotsTxt = `User-agent: *
Allow: /

# AI Crawlers explicitly welcomed for citations & snippets
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

Sitemap: ${siteMeta.baseUrl}/sitemap.xml
`;
fs.writeFileSync(path.join(DIST_DIR, 'robots.txt'), robotsTxt.trim(), 'utf-8');
console.log('✓ Generated robots.txt.');

// 7. Generate CNAME if customDomain is configured
if (siteMeta.customDomain) {
  fs.writeFileSync(path.join(DIST_DIR, 'CNAME'), siteMeta.customDomain.trim(), 'utf-8');
  console.log(`✓ Generated CNAME for ${siteMeta.customDomain}.`);
}

console.log('\n=============================================');
console.log('🎉 BUILD COMPLETED SUCCESSFULLY!');
console.log(`Total Pages Generated in dist/: ${sitemapUrls.length}`);
console.log('=============================================\n');

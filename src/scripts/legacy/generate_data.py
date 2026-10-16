import json
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "data", "chains")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Data definition function
def create_chain(
    slug, name, category, title, meta_desc, hero_sub, quick_answer,
    price_level, breakfast_info, saving_tips, history,
    categories, faqs, video_id=None, tags=None
):
    return {
        "slug": slug,
        "name": name,
        "category": category,
        "seoTitle": title,
        "metaDescription": meta_desc,
        "heroSubtitle": hero_sub,
        "quickAnswer": quick_answer,
        "priceLevel": price_level,
        "breakfastInfo": breakfast_info,
        "savingTips": saving_tips,
        "history": history,
        "menuCategories": categories,
        "faqs": faqs,
        "videoId": video_id or "dQw4w9WgXcQ", # replaced with high relevance video or fallback
        "tags": tags or [category, name.lower(), "preise", "speisekarte"]
    }

# All chains definitions
chains = []

# 1. McDonald's
chains.append(create_chain(
    slug="mcdonalds-preise",
    name="McDonald's",
    category="fast-food",
    title="McDonald's Preise 2026 – Aktuelle Preisliste in Tabelle",
    meta_desc="Aktuelle McDonald's Preise 2026 in Deutschland: Big Mac, McMenu, Happy Meal, Nuggets, Burger & Getränke mit Kalorien (kJ/kcal) im Tabellen-Überblick.",
    hero_sub="Die vollständige und aktuelle Preisliste von McDonald's Deutschland mit allen Menüs, Kalorien und Spartipps.",
    quick_answer="In Deutschland kostet ein Big Mac 2026 im Schnitt ca. 5,99 € einzeln und ca. 9,49 € im McMenü. Ein 20er Chicken McNuggets liegt bei rund 11,49 €, während das Happy Meal für Kinder zwischen 4,99 € und 5,49 € kostet. Alle Preise können je nach Franchise-Standort, Bahnhof oder Autobahn leicht abweichen.",
    price_level="€€ (Günstig bis Mittel)",
    breakfast_info={
        "hasBreakfast": True,
        "hoursWeekdays": "Mo – Fr: 06:00 – 10:30 Uhr",
        "hoursWeekend": "Sa, So & Feiertage: 06:00 – 11:30 Uhr",
        "note": "An 24h-Filialen beginnt das Frühstück bereits um 06:00 Uhr. Danach wird automatisch auf die reguläre Speisekarte umgestellt."
    },
    saving_tips=[
        "Nutze die McDonald's App für wöchentlich wechselnde 1€-Aktionen, 2-für-1 Gutscheine und Treuepunkte (MyMcDonald's Rewards).",
        "Das McSmart Menü (z. B. 2 Burger nach Wahl + mittlere Pommes + Softdrink) bietet oft das beste Preis-Leistungs-Verhältnis für unter 6 €.",
        "Vergleiche 9er vs. 20er McNuggets: Die 20er Box hat den deutlich geringeren Preis pro Stück (ca. 0,57 € vs. 0,78 €)."
    ],
    history="Die Geschichte von McDonald's in Deutschland begann am 4. Dezember 1971 in München-Giesing in der Martin-Luther-Straße. Heute betreibt McDonald's Deutschland über 1.420 Filialen, größtenteils durch selbstständige Franchise-Nehmer geführt. Mehr als 80 % der Rindfleisch-Zutaten stammen von heimischen landwirtschaftlichen Betrieben.",
    categories=[
        {
            "categoryName": "Beliebte Burger & Klassiker",
            "items": [
                {"name": "Big Mac", "price": "5,99 €", "calories": "2.115 kJ / 505 kcal", "diet": "Rindfleisch"},
                {"name": "Hamburger", "price": "1,99 €", "calories": "1.060 kJ / 253 kcal", "diet": "Rindfleisch"},
                {"name": "Cheeseburger", "price": "2,49 €", "calories": "1.265 kJ / 302 kcal", "diet": "Rindfleisch"},
                {"name": "Double Cheeseburger", "price": "3,99 €", "calories": "1.865 kJ / 446 kcal", "diet": "Rindfleisch"},
                {"name": "Hamburger Royal TS", "price": "6,39 €", "calories": "2.241 kJ / 536 kcal", "diet": "Rindfleisch"},
                {"name": "Hamburger Royal Käse", "price": "6,19 €", "calories": "2.299 kJ / 549 kcal", "diet": "Rindfleisch"},
                {"name": "Big Tasty Bacon", "price": "8,19 €", "calories": "3.808 kJ / 912 kcal", "diet": "Rindfleisch"},
                {"name": "McChicken Classic", "price": "5,69 €", "calories": "1.870 kJ / 446 kcal", "diet": "Geflügel"},
                {"name": "McRib", "price": "5,89 €", "calories": "2.055 kJ / 491 kcal", "diet": "Schweinefleisch"},
                {"name": "Filet-o-Fish", "price": "5,19 €", "calories": "1.405 kJ / 335 kcal", "diet": "Fisch"},
                {"name": "McPlant", "price": "5,69 €", "calories": "1.769 kJ / 422 kcal", "diet": "Vegan 🌱"}
            ]
        },
        {
            "categoryName": "McMenü & Sparmenüs",
            "items": [
                {"name": "McMenü Big Mac (mit Pommes & Softdrink)", "price": "9,49 €", "calories": "3.750 kJ / 895 kcal", "diet": "Menü"},
                {"name": "McMenü Hamburger Royal TS", "price": "9,89 €", "calories": "3.880 kJ / 926 kcal", "diet": "Menü"},
                {"name": "McMenü Big Tasty Bacon", "price": "11,69 €", "calories": "5.450 kJ / 1.302 kcal", "diet": "Menü"},
                {"name": "McMenü McChicken Classic", "price": "9,19 €", "calories": "3.510 kJ / 836 kcal", "diet": "Menü"},
                {"name": "McMenü McRib", "price": "9,39 €", "calories": "3.690 kJ / 881 kcal", "diet": "Menü"},
                {"name": "McSmart Menü (2 Burger + Pommes + Drink)", "price": "5,99 €", "calories": "3.200 kJ / 765 kcal", "diet": "Sparmenü"}
            ]
        },
        {
            "categoryName": "Chicken McNuggets & Fingerfood",
            "items": [
                {"name": "Chicken McNuggets 6er (inkl. 1 Dip)", "price": "4,99 €", "calories": "1.085 kJ / 259 kcal", "diet": "Geflügel"},
                {"name": "Chicken McNuggets 9er (inkl. 2 Dips)", "price": "6,99 €", "calories": "1.628 kJ / 389 kcal", "diet": "Geflügel"},
                {"name": "Chicken McNuggets 20er (inkl. 3 Dips)", "price": "11,49 €", "calories": "3.618 kJ / 864 kcal", "diet": "Geflügel"},
                {"name": "McPlant Nuggets 6er (inkl. 1 Dip)", "price": "4,99 €", "calories": "993 kJ / 238 kcal", "diet": "Vegan 🌱"},
                {"name": "McPlant Nuggets 9er (inkl. 2 Dips)", "price": "6,99 €", "calories": "1.490 kJ / 357 kcal", "diet": "Vegan 🌱"},
                {"name": "Extra Dip (Süßsauer, BBQ, Curry, Sour Cream)", "price": "0,70 €", "calories": "190 kJ / 45 kcal", "diet": "Vegetarisch"}
            ]
        },
        {
            "categoryName": "Pommes Frites & Beilagen",
            "items": [
                {"name": "Pommes Frites Klein", "price": "2,49 €", "calories": "970 kJ / 231 kcal", "diet": "Vegan 🌱"},
                {"name": "Pommes Frites Mittel", "price": "3,69 €", "calories": "1.425 kJ / 340 kcal", "diet": "Vegan 🌱"},
                {"name": "Pommes Frites Groß", "price": "4,29 €", "calories": "1.820 kJ / 434 kcal", "diet": "Vegan 🌱"},
                {"name": "Curly Fries (Gitterkartoffeln)", "price": "4,19 €", "calories": "1.650 kJ / 394 kcal", "diet": "Vegan 🌱"},
                {"name": "Snack Salad Classic", "price": "3,29 €", "calories": "80 kJ / 19 kcal", "diet": "Vegan 🌱"}
            ]
        },
        {
            "categoryName": "Desserts, Shakes & Eis",
            "items": [
                {"name": "McFlurry Original (Oreo, Schoko, Smarties)", "price": "4,49 €", "calories": "1.780 kJ / 425 kcal", "diet": "Vegetarisch"},
                {"name": "McSundae Schoko / Karamell / Erdbeer", "price": "2,49 €", "calories": "1.215 kJ / 290 kcal", "diet": "Vegetarisch"},
                {"name": "Heiße Apfeltasche", "price": "1,99 €", "calories": "1.045 kJ / 250 kcal", "diet": "Vegan 🌱"},
                {"name": "Milchshake Schoko / Vanille / Erdbeer (0,4 l)", "price": "3,79 €", "calories": "1.670 kJ / 398 kcal", "diet": "Vegetarisch"}
            ]
        },
        {
            "categoryName": "Getränke & Kaffeespezialitäten",
            "items": [
                {"name": "Coca-Cola / Zero / Fanta / Sprite (0,4 l)", "price": "3,29 €", "calories": "710 kJ / 170 kcal", "diet": "Vegan 🌱"},
                {"name": "Coca-Cola / Zero / Fanta / Sprite (0,5 l)", "price": "3,69 €", "calories": "890 kJ / 212 kcal", "diet": "Vegan 🌱"},
                {"name": "Cappuccino Regulär (McCafé)", "price": "3,19 €", "calories": "460 kJ / 110 kcal", "diet": "Vegetarisch"},
                {"name": "Latte Macchiato (McCafé)", "price": "3,69 €", "calories": "620 kJ / 148 kcal", "diet": "Vegetarisch"},
                {"name": "Espresso (McCafé)", "price": "1,99 €", "calories": "10 kJ / 2 kcal", "diet": "Vegan 🌱"}
            ]
        }
    ],
    faqs=[
        {
            "q": "Wie viel kostet ein Big Mac 2026 bei McDonald's in Deutschland?",
            "a": "Ein einzelner Big Mac kostet 2026 in Deutschland durchschnittlich ca. 5,99 €. Im McMenü (mit mittleren Pommes und Softdrink) liegt der Preis bei etwa 9,49 €."
        },
        {
            "q": "Was kostet ein Happy Meal bei McDonald's?",
            "a": "Das Happy Meal für Kinder kostet aktuell zwischen 4,99 € und 5,49 €. Es enthält ein Hauptgericht (z. B. 4er McNuggets oder Hamburger), eine Beilage (Pommes oder Frucht-Tüte), ein Getränk sowie ein Spielzeug oder Buch."
        },
        {
            "q": "Bis wann gibt es bei McDonald's Frühstück?",
            "a": "Das Frühstück wird von Montag bis Freitag von 06:00 bis 10:30 Uhr serviert. An Samstagen, Sonntagen und bundesweiten Feiertagen gilt die Frühstückskarte bis 11:30 Uhr."
        },
        {
            "q": "Warum unterscheiden sich die McDonald's Preise zwischen Filialen?",
            "a": "McDonald's Filialen werden zu über 90 % von selbstständigen Franchise-Nehmern betrieben. Diese können die Preise im Rahmen von unverbindlichen Preisempfehlungen (UVP) eigenständig festlegen. An Bahnhöfen, Flughäfen oder Raststätten sind die Preise deshalb oft 10–20 % höher."
        },
        {
            "q": "Gibt es bei McDonald's vegane Burger?",
            "a": "Ja, mit dem McPlant und den McPlant Nuggets bietet McDonald's Deutschland vegane Optionen auf Basis pflanzlicher Proteine (Beyond Meat) an."
        }
    ]
))

# 2. Deutsche Bahn ICE Bordbistro & Bordrestaurant
chains.append(create_chain(
    slug="db-speisekarte",
    name="Deutsche Bahn (ICE Bordbistro)",
    category="bahn-reise",
    title="Deutsche Bahn Speisekarte 2026 – Preise im ICE Bordbistro & Bordrestaurant",
    meta_desc="Aktuelle Deutsche Bahn Speisekarte 2026: Alle Preise im ICE Bordbistro & Bordrestaurant für Kaffee, Currywurst, Frühstück, Bier & Snacks in übersichtlicher Tabelle.",
    hero_sub="Die offizielle Preisliste der DB Bordgastronomie im ICE und Intercity mit allen Speisen, Heißgetränken und Reisemenüs.",
    quick_answer="Im ICE Bordbistro der Deutschen Bahn kostet eine Tasse Fairtrade-Kaffee 2026 ca. 3,90 €, ein Cappuccino ca. 4,30 €. Der beliebte Bordbistro-Klassiker 'Original Berliner Currywurst' mit Brötchen liegt bei ca. 8,20 €, während ein warmes Hauptgericht zwischen 9,90 € und 14,50 € kostet. In der 1. Klasse gibt es zudem Am-Platz-Service.",
    price_level="€€€ (Reise-Gastronomie)",
    breakfast_info={
        "hasBreakfast": True,
        "hoursWeekdays": "Ganztägig verfügbar, solange der Vorrat reicht",
        "hoursWeekend": "Ganztägig verfügbar",
        "note": "Das kleine und große Bahn-Frühstück (Croissant, Brötchen, Butter, Konfitüre & Heißgetränk) ist ab Fahrtbeginn im Zug erhältlich."
    },
    saving_tips=[
        "Mit einer BahnCard gibt es zeitweise Rabattaktionen oder Bonuspunkte beim Kauf in der Bordgastronomie.",
        "Kombiniere Heißgetränk und Gebäck als Pausen-Menü (z. B. Kaffee + Buttercroissant), um gegenüber dem Einzelkauf 1,00–1,50 € zu sparen.",
        "In Zügen mit Bordbistro (statt Restaurant) sind die Preise identisch, Speisen werden jedoch im praktischen To-Go-Behälter ausgegeben."
    ],
    history="Die DB Bordgastronomie blickt auf eine lange Tradition zurück, die bis zur MITROPA (Mitteleuropäische Schlafwagen- und Speisewagen-Aktiengesellschaft) von 1916 reicht. Heute serviert die Deutsche Bahn in rund 400 ICE-Zügen pro Jahr über 3 Millionen Tassen Kaffee und Hunderttausende Portionen Currywurst.",
    categories=[
        {
            "categoryName": "Warme Speisen & Zug-Klassiker",
            "items": [
                {"name": "Original Berliner Currywurst mit Brötchen", "price": "8,20 €", "calories": "2.480 kJ / 592 kcal", "diet": "Schweinefleisch"},
                {"name": "Chili con Carne mit Sauerrahm & Brötchen", "price": "9,90 €", "calories": "2.190 kJ / 523 kcal", "diet": "Rindfleisch"},
                {"name": "Veganes Kichererbsen-Kokos-Curry mit Reis", "price": "10,90 €", "calories": "1.920 kJ / 458 kcal", "diet": "Vegan 🌱"},
                {"name": "Käsespätzle mit Röstzwiebeln", "price": "10,50 €", "calories": "2.750 kJ / 657 kcal", "diet": "Vegetarisch"},
                {"name": "Bayerischer Leberkäse mit Kartoffelsalat", "price": "9,50 €", "calories": "2.610 kJ / 624 kcal", "diet": "Schweinefleisch"},
                {"name": "Gulaschsuppe mit Rindfleisch & Brötchen", "price": "7,50 €", "calories": "1.520 kJ / 363 kcal", "diet": "Rindfleisch"}
            ]
        },
        {
            "categoryName": "Frühstück & Bäckerei",
            "items": [
                {"name": "Kleines Frühstück (Croissant, Butter, Marmelade)", "price": "4,90 €", "calories": "1.450 kJ / 346 kcal", "diet": "Vegetarisch"},
                {"name": "Großes Genießer-Frühstück (Brötchen, Käse, Schinken, Ei)", "price": "8,90 €", "calories": "2.350 kJ / 561 kcal", "diet": "Kombination"},
                {"name": "Buttercroissant frisch gebacken", "price": "2,60 €", "calories": "980 kJ / 234 kcal", "diet": "Vegetarisch"},
                {"name": "Frische Laugenbrezel", "price": "2,40 €", "calories": "890 kJ / 212 kcal", "diet": "Vegan 🌱"},
                {"name": "Belegtes Baguette Salami & Käse", "price": "5,60 €", "calories": "1.890 kJ / 452 kcal", "diet": "Kombination"}
            ]
        },
        {
            "categoryName": "Heißgetränke & Kaffee (Fairtrade)",
            "items": [
                {"name": "Fairtrade Kaffee Crema (Tasse)", "price": "3,90 €", "calories": "15 kJ / 4 kcal", "diet": "Vegan 🌱"},
                {"name": "Großer Kaffee Crema (Pott)", "price": "4,60 €", "calories": "20 kJ / 5 kcal", "diet": "Vegan 🌱"},
                {"name": "Cappuccino", "price": "4,30 €", "calories": "480 kJ / 115 kcal", "diet": "Vegetarisch"},
                {"name": "Latte Macchiato", "price": "4,60 €", "calories": "620 kJ / 148 kcal", "diet": "Vegetarisch"},
                {"name": "Heiße Schokolade", "price": "4,20 €", "calories": "890 kJ / 213 kcal", "diet": "Vegetarisch"},
                {"name": "Bio-Tee (verschiedene Sorten)", "price": "3,80 €", "calories": "5 kJ / 1 kcal", "diet": "Vegan 🌱"}
            ]
        },
        {
            "categoryName": "Kühle Getränke & Bier",
            "items": [
                {"name": "Bitburger Pils frisch gezapft (0,5 l)", "price": "5,20 €", "calories": "850 kJ / 203 kcal", "diet": "Alkoholhaltig"},
                {"name": "Erdinger Weißbier (0,5 l Flasche)", "price": "5,40 €", "calories": "920 kJ / 220 kcal", "diet": "Alkoholhaltig"},
                {"name": "Alkoholfreies Bier (0,33 l)", "price": "4,20 €", "calories": "320 kJ / 76 kcal", "diet": "Vegan 🌱"},
                {"name": "Mineralwasser Still / Spritzig (0,5 l)", "price": "3,60 €", "calories": "0 kJ / 0 kcal", "diet": "Vegan 🌱"},
                {"name": "Coca-Cola / Coca-Cola Zero (0,5 l)", "price": "3,90 €", "calories": "890 kJ / 212 kcal", "diet": "Vegan 🌱"}
            ]
        }
    ],
    faqs=[
        {
            "q": "Wie viel kostet ein Kaffee im ICE Bordbistro der Deutschen Bahn?",
            "a": "Eine normale Tasse Fairtrade-Kaffee kostet im ICE 3,90 €. Ein großer Kaffee-Pott kostet 4,60 €, und Spezialitäten wie Cappuccino oder Latte Macchiato liegen bei 4,30 € bis 4,60 €."
        },
        {
            "q": "Was kostet die Currywurst im Bordrestaurant der Deutschen Bahn?",
            "a": "Die 'Original Berliner Currywurst' mit Brötchen kostet aktuell 8,20 € im Bordbistro und Bordrestaurant."
        },
        {
            "q": "Kann man im ICE Bordrestaurant mit Karte bezahlen?",
            "a": "Ja, die Deutsche Bahn akzeptiert im Bordbistro und Bordrestaurant bargeldlose Zahlung (Girocard, Visa, Mastercard, American Express, Apple Pay, Google Pay) sowie Bargeld."
        },
        {
            "q": "Gibt es im ICE Am-Platz-Service?",
            "a": "Reisende in der 1. Klasse können Speisen und Getränke direkt an ihren Sitzplatz bestellen. In der 2. Klasse holt man Speisen im Bordbistro oder Bordrestaurant ab."
        },
        {
            "q": "Gibt es vegane Gerichte auf der Speisekarte der Bahn?",
            "a": "Ja, die Deutsche Bahn erweitert ihr pflanzliches Angebot laufend. Beliebt ist das vegane Kichererbsen-Curry sowie vegane Hafermilch als laktosefreie Alternative für alle Kaffees."
        }
    ]
))

# 3. Burger King
chains.append(create_chain(
    slug="burger-king-preise",
    name="Burger King",
    category="fast-food",
    title="Burger King Preise 2026 – Aktuelle Menü Preisliste",
    meta_desc="Aktuelle Burger King Preise 2026 in Deutschland: Whopper, King Menü, Cheeseburger, King Box, Plant-based Burger & Getränke mit Kalorien im Tabellen-Überblick.",
    hero_sub="Alle Burger King Preise, Whopper-Varianten, Spar-Coupons und Kalorienangaben auf einen Blick.",
    quick_answer="Bei Burger King Deutschland kostet der klassische Whopper 2026 einzeln ca. 6,49 € und im King Menü rund 9,79 €. Ein einfacher Cheeseburger liegt bei 2,49 €, während der beliebte Big King ca. 5,49 € kostet. Alle Rindfleisch-Burger gibt es bei Burger King auch als 100% pflanzliche 'Plant-based' Variante zum identischen Preis.",
    price_level="€€ (Günstig bis Mittel)",
    breakfast_info={
        "hasBreakfast": True,
        "hoursWeekdays": "Mo – Fr: 06:00 – 10:30 Uhr",
        "hoursWeekend": "Sa – So: 06:00 – 11:00 Uhr",
        "note": "Nicht alle Filialen bieten das King Breakfast an. Autobahn- und Innenstadt-Restaurants führen die Frühstückskarte am verlässlichsten."
    },
    saving_tips=[
        "In der Burger King App gibt es dauerhaft 2-für-1 Whopper Coupons und King Finder Rabatte, die bis zu 40 % sparen.",
        "Die King Selection Angebote und die 'King des Monats' Aktionen bieten zeitweise wechselnde Premium-Burger zum Aktionspreis.",
        "Gutscheinbögen (Papier oder digital) enthalten Rabattcodes (Plu-Nummern), die auch am Drive-In oder am Self-Order-Terminal direkt eingegeben werden können."
    ],
    history="Burger King wurde 1954 in Miami (USA) gegründet. Das erste deutsche Burger King Restaurant eröffnete 1976 am Kurfürstendamm in Berlin. Heute gibt es in Deutschland über 750 Burger King Restaurants, berühmt für die Zubereitung des Rindfleischs auf offener Flamme ('Flame-grilled').",
    categories=[
        {
            "categoryName": "Flame-Grilled Burger & Whopper",
            "items": [
                {"name": "Whopper", "price": "6,49 €", "calories": "2.685 kJ / 642 kcal", "diet": "Flame-Grilled Rind"},
                {"name": "Double Whopper", "price": "8,49 €", "calories": "3.750 kJ / 896 kcal", "diet": "Flame-Grilled Rind"},
                {"name": "Whopper Jr.", "price": "3,89 €", "calories": "1.465 kJ / 350 kcal", "diet": "Flame-Grilled Rind"},
                {"name": "Big King", "price": "5,49 €", "calories": "2.220 kJ / 531 kcal", "diet": "Rindfleisch"},
                {"name": "Big King XXL", "price": "8,79 €", "calories": "4.150 kJ / 992 kcal", "diet": "Rindfleisch"},
                {"name": "Bacon King", "price": "8,69 €", "calories": "4.380 kJ / 1.047 kcal", "diet": "Rind & Bacon"},
                {"name": "Cheeseburger", "price": "2,49 €", "calories": "1.280 kJ / 306 kcal", "diet": "Rindfleisch"},
                {"name": "Double Cheeseburger", "price": "4,19 €", "calories": "1.920 kJ / 459 kcal", "diet": "Rindfleisch"},
                {"name": "Chili Cheese Burger", "price": "2,99 €", "calories": "1.340 kJ / 320 kcal", "diet": "Pikant"},
                {"name": "X-Tra Long Chili Cheese", "price": "6,99 €", "calories": "3.310 kJ / 791 kcal", "diet": "Pikant"}
            ]
        },
        {
            "categoryName": "Plant-Based (100% pflanzlicher Geschmack)",
            "items": [
                {"name": "Plant-based Whopper", "price": "6,49 €", "calories": "2.510 kJ / 600 kcal", "diet": "Vegan 🌱"},
                {"name": "Plant-based Long Chicken", "price": "5,99 €", "calories": "2.380 kJ / 569 kcal", "diet": "Vegan 🌱"},
                {"name": "Plant-based Big King", "price": "5,49 €", "calories": "2.150 kJ / 514 kcal", "diet": "Vegetarisch"},
                {"name": "Plant-based Nuggets (6er)", "price": "4,99 €", "calories": "1.120 kJ / 268 kcal", "diet": "Vegan 🌱"},
                {"name": "Plant-based Nuggets (9er)", "price": "6,79 €", "calories": "1.680 kJ / 402 kcal", "diet": "Vegan 🌱"}
            ]
        },
        {
            "categoryName": "Chicken & Fingerfood",
            "items": [
                {"name": "Long Chicken", "price": "5,99 €", "calories": "2.410 kJ / 576 kcal", "diet": "Geflügel"},
                {"name": "Crispy Chicken", "price": "5,69 €", "calories": "2.180 kJ / 521 kcal", "diet": "Geflügel"},
                {"name": "King Nuggets 6er", "price": "4,99 €", "calories": "1.150 kJ / 275 kcal", "diet": "Geflügel"},
                {"name": "King Nuggets 9er", "price": "6,79 €", "calories": "1.725 kJ / 412 kcal", "diet": "Geflügel"},
                {"name": "King Nuggets 20er", "price": "11,29 €", "calories": "3.830 kJ / 915 kcal", "diet": "Geflügel"},
                {"name": "Chili Cheese Nuggets (6er)", "price": "4,89 €", "calories": "1.380 kJ / 330 kcal", "diet": "Vegetarisch / Scharf"},
                {"name": "Onion Rings (6er)", "price": "3,49 €", "calories": "1.090 kJ / 260 kcal", "diet": "Vegan 🌱"}
            ]
        },
        {
            "categoryName": "King Pommes & Saucen",
            "items": [
                {"name": "King Pommes Klein", "price": "2,49 €", "calories": "980 kJ / 234 kcal", "diet": "Vegan 🌱"},
                {"name": "King Pommes Mittel", "price": "3,59 €", "calories": "1.410 kJ / 337 kcal", "diet": "Vegan 🌱"},
                {"name": "King Pommes Groß", "price": "4,19 €", "calories": "1.890 kJ / 452 kcal", "diet": "Vegan 🌱"},
                {"name": "Chili Cheese Fries", "price": "4,99 €", "calories": "2.150 kJ / 514 kcal", "diet": "Pikant"}
            ]
        },
        {
            "categoryName": "Desserts & King Shakes",
            "items": [
                {"name": "King Fusion (Oreo / KitKat)", "price": "4,49 €", "calories": "1.820 kJ / 435 kcal", "diet": "Vegetarisch"},
                {"name": "King Sundae Schoko / Karamell", "price": "2,49 €", "calories": "1.190 kJ / 284 kcal", "diet": "Vegetarisch"},
                {"name": "Hot Brownie mit Eis", "price": "3,99 €", "calories": "2.100 kJ / 502 kcal", "diet": "Vegetarisch"},
                {"name": "King Shake Vanille / Erdbeer / Schoko (0,4 l)", "price": "3,79 €", "calories": "1.710 kJ / 409 kcal", "diet": "Vegetarisch"}
            ]
        }
    ],
    faqs=[
        {
            "q": "Was kostet ein Whopper bei Burger King 2026?",
            "a": "Ein einzelner Whopper kostet in Deutschland durchschnittlich 6,49 €. Im King Menü (mit King Pommes und Softdrink) liegt der Preis bei ca. 9,79 €."
        },
        {
            "q": "Was ist der Unterschied zwischen Big King und Big Mac?",
            "a": "Beide Burger haben zwei Rindfleisch-Patties und eine charakteristische Sauce. Der Big King von Burger King zeichnet sich durch flame-grilled Patties, würzige Essiggurken und King Sauce aus, während der Big Mac ein zusätzliches Mittelbrötchen besitzt."
        },
        {
            "q": "Sind Plant-based Produkte bei Burger King teurer?",
            "a": "Nein. Burger King verfolgt in Deutschland das Prinzip 'Plant-based zum gleichen Preis'. Ein Plant-based Whopper kostet exakt gleich viel wie der Fleisch-Whopper."
        },
        {
            "q": "Wo gibt es die besten Burger King Coupons?",
            "a": "Die offiziellen und tagesaktuellen Rabatte findest du direkt in der Burger King Deutschland App sowie auf regelmäßig erscheinenden Papier-Gutscheinbögen."
        }
    ]
))

# 4. Subway
chains.append(create_chain(
    slug="subway-preise",
    name="Subway",
    category="fast-food",
    title="Subway Preise Deutschland 2026 – 15cm & 30cm Footlong Preisliste",
    meta_desc="Aktuelle Subway Preise 2026 in Deutschland: 15 cm Sub, 30 cm Footlong, Menü-Upgrades, Cookies & Salate mit allen Preisen im Tabellen-Überblick.",
    hero_sub="Die komplette Subway Preisliste für 15cm Subs, 30cm Footlong Sandwiches, Wraps und Menüs in Deutschland.",
    quick_answer="Bei Subway Deutschland kostet ein 15 cm Sub 2026 durchschnittlich zwischen 5,99 € und 7,99 €, während das doppelt so große 30 cm Footlong Sub zwischen 9,99 € und 12,99 € liegt. Für ca. 3,20 € Aufpreis gibt es das Menü-Upgrade mit 0,5 l Softdrink und Cookie oder Chips.",
    price_level="€€ (Mittel)",
    breakfast_info={
        "hasBreakfast": False,
        "hoursWeekdays": "Reguläre Öffnung meist ab 09:00 oder 10:00 Uhr",
        "hoursWeekend": "Ab 10:00 Uhr geöffnet",
        "note": "Ausgewählte Filialen bieten morgens belegte Toast-Sandwiches und frischen Kaffee an."
    },
    saving_tips=[
        "Bestelle immer das 30 cm Footlong Sub, wenn du mit Freunden teilst – der Preis pro Zentimeter ist rund 25 % günstiger als bei zwei 15 cm Subs.",
        "Der 'Sub des Tages' war lange Zeit der beste Spar-Tipp; heute bieten die meisten Filialen wechselnde Monats-Deals in der Subway Rewards App an.",
        "Mit der Subway Rewards Karte sammelst du Punkte für Gratis-Subs und Cookies."
    ],
    history="Subway wurde 1965 von Fred DeLuca und Peter Buck in den USA gegründet. Die erste Filiale in Deutschland öffnete 1999 in Berlin. Heute gibt es rund 650 Subway-Standorte in Deutschland, die für individuell belegte Sandwiches auf frischem Brot bekannt sind.",
    categories=[
        {
            "categoryName": "Klassische Subs (15 cm & 30 cm Footlong)",
            "items": [
                {"name": "Italian B.M.T. (Salami, Peperoni, Schinken)", "price": "6,99 € (15cm) | 11,49 € (30cm)", "calories": "1.740 kJ / 416 kcal", "diet": "Schwein/Rind"},
                {"name": "Chicken Teriyaki", "price": "7,49 € (15cm) | 12,29 € (30cm)", "calories": "1.520 kJ / 363 kcal", "diet": "Geflügel"},
                {"name": "Tuna (Thunfischcreme)", "price": "6,79 € (15cm) | 11,19 € (30cm)", "calories": "1.890 kJ / 452 kcal", "diet": "Fisch"},
                {"name": "Turkey, Ham & Bacon", "price": "7,29 € (15cm) | 11,99 € (30cm)", "calories": "1.610 kJ / 385 kcal", "diet": "Kombination"},
                {"name": "Philly Beef & Cheese", "price": "7,99 € (15cm) | 12,99 € (30cm)", "calories": "1.790 kJ / 428 kcal", "diet": "Rindfleisch"},
                {"name": "Spicy Italian", "price": "6,49 € (15cm) | 10,79 € (30cm)", "calories": "1.980 kJ / 473 kcal", "diet": "Pikant"},
                {"name": "Veggie Delite (Frisches Gemüse)", "price": "5,49 € (15cm) | 8,99 € (30cm)", "calories": "980 kJ / 234 kcal", "diet": "Vegan 🌱"},
                {"name": "Plant-based Teriyaki", "price": "7,49 € (15cm) | 12,29 € (30cm)", "calories": "1.580 kJ / 378 kcal", "diet": "Vegan 🌱"}
            ]
        },
        {
            "categoryName": "Menü-Upgrades & Beilagen",
            "items": [
                {"name": "Menü-Upgrade (Sub + 0,5 l Drink + Cookie/Chips)", "price": "+ 3,20 €", "calories": "variiert", "diet": "Menü"},
                {"name": "Subway Cookie (Chocolate Chunk, White Choc Macadamia)", "price": "1,49 €", "calories": "920 kJ / 220 kcal", "diet": "Vegetarisch"},
                {"name": "3er Cookie Box", "price": "3,99 €", "calories": "2.760 kJ / 660 kcal", "diet": "Vegetarisch"},
                {"name": "Lay's Chips Beutel", "price": "1,99 €", "calories": "680 kJ / 162 kcal", "diet": "Vegan 🌱"}
            ]
        }
    ],
    faqs=[
        {
            "q": "Was kostet ein 30 cm Sub bei Subway in Deutschland?",
            "a": "Ein 30 cm Footlong Sub kostet 2026 in Deutschland zwischen 9,99 € (Veggie Delite) und 12,99 € (Philly Beef oder Chicken Teriyaki)."
        },
        {
            "q": "Wie viel kostet ein Cookie bei Subway?",
            "a": "Ein einzelner Subway Cookie kostet ca. 1,49 €. Im 3er-Pack liegt der Preis meist bei 3,99 €."
        }
    ]
))

# 5. Starbucks
chains.append(create_chain(
    slug="starbucks-preise",
    name="Starbucks",
    category="kaffee-baeckerei",
    title="Starbucks Preise Deutschland 2026 – Aktuelle Getränke & Kaffee Preisliste",
    meta_desc="Aktuelle Starbucks Preise 2026 in Deutschland: Frappuccino, Caramel Macchiato, Latte, Iced Coffee, Größen Tall, Grande & Venti im Tabellen-Überblick.",
    hero_sub="Alle Starbucks Getränkepreise in Deutschland nach Größen (Tall, Grande, Venti) sortiert mit Snacks und Kalorien.",
    quick_answer="Bei Starbucks Deutschland liegt ein Caffè Latte (Grande) 2026 bei ca. 5,45 €, ein Caramel Macchiato bei rund 5,85 € und ein Frappuccino zwischen 5,95 € und 6,75 €. Pflanzliche Milchalternativen (Hafer-, Soja-, Mandel- und Kokosdrink) sind in den meisten deutschen Filialen mittlerweile ohne Aufpreis erhältlich.",
    price_level="€€€ (Premium)",
    breakfast_info={
        "hasBreakfast": True,
        "hoursWeekdays": "Ab Filialöffnung (meist 06:30 oder 07:00 Uhr) ganztägig",
        "hoursWeekend": "Ab 08:00 Uhr ganztägig",
        "note": "Warme Sandwiches, Bagels, Croissants und Muffins sind den ganzen Tag über bestellbar."
    },
    saving_tips=[
        "Bringe deinen eigenen Mehrwegbecher mit: Starbucks gewährt 0,30 € Rabatt auf jedes Getränk.",
        "Nutze die Starbucks Rewards App: Mit gesammelten Sternen erhältst du kostenlose Sirup-Shots, Extra-Espresso und Gratis-Getränke.",
        "Die Größe 'Tall' steht oft nicht groß auf der Menütafel, ist aber auf Nachfrage immer verfügbar und ca. 0,50–0,70 € günstiger als 'Grande'."
    ],
    history="Starbucks wurde 1971 in Seattle gegründet. Die erste deutsche Filiale eröffnete 2002 am Berliner Hackeschen Markt. In Deutschland betreibt das Unternehmen rund 150 Kaffeehäuser, vor allem an stark frequentierten Bahnhöfen, Einkaufsstraßen und Flughäfen.",
    categories=[
        {
            "categoryName": "Espresso & Kaffee-Klassiker (Tall / Grande / Venti)",
            "items": [
                {"name": "Caffè Latte", "price": "4,85 € (T) | 5,45 € (G) | 5,95 € (V)", "calories": "630 kJ / 150 kcal", "diet": "Vegetarisch"},
                {"name": "Caramel Macchiato", "price": "5,25 € (T) | 5,85 € (G) | 6,35 € (V)", "calories": "1.020 kJ / 244 kcal", "diet": "Vegetarisch"},
                {"name": "Caffè Mocha", "price": "5,35 € (T) | 5,95 € (G) | 6,45 € (V)", "calories": "1.210 kJ / 289 kcal", "diet": "Vegetarisch"},
                {"name": "Cappuccino", "price": "4,75 € (T) | 5,35 € (G) | 5,85 € (V)", "calories": "510 kJ / 122 kcal", "diet": "Vegetarisch"},
                {"name": "Caffè Americano", "price": "3,95 € (T) | 4,45 € (G) | 4,85 € (V)", "calories": "60 kJ / 14 kcal", "diet": "Vegan 🌱"},
                {"name": "Filterkaffee (Pike Place Roast)", "price": "3,45 € (T) | 3,85 € (G) | 4,25 € (V)", "calories": "20 kJ / 5 kcal", "diet": "Vegan 🌱"}
            ]
        },
        {
            "categoryName": "Frappuccino Blended Beverages",
            "items": [
                {"name": "Caramel Frappuccino", "price": "5,65 € (T) | 6,25 € (G) | 6,75 € (V)", "calories": "1.580 kJ / 377 kcal", "diet": "Vegetarisch"},
                {"name": "Java Chip Frappuccino", "price": "5,75 € (T) | 6,35 € (G) | 6,85 € (V)", "calories": "1.820 kJ / 435 kcal", "diet": "Vegetarisch"},
                {"name": "Espresso Frappuccino", "price": "5,35 € (T) | 5,95 € (G) | 6,45 € (V)", "calories": "980 kJ / 234 kcal", "diet": "Vegetarisch"},
                {"name": "Matcha Green Tea Frappuccino", "price": "5,65 € (T) | 6,25 € (G) | 6,75 € (V)", "calories": "1.490 kJ / 356 kcal", "diet": "Vegetarisch"}
            ]
        },
        {
            "categoryName": "Bakery, Kuchen & Snacks",
            "items": [
                {"name": "New York Cheesecake", "price": "4,85 €", "calories": "1.850 kJ / 442 kcal", "diet": "Vegetarisch"},
                {"name": "Chocolate Chunk Cookie", "price": "2,95 €", "calories": "1.380 kJ / 330 kcal", "diet": "Vegetarisch"},
                {"name": "Zimtschnecke (Cinnamon Roll)", "price": "3,75 €", "calories": "1.690 kJ / 404 kcal", "diet": "Vegetarisch"},
                {"name": "Blueberry Muffin", "price": "3,45 €", "calories": "1.520 kJ / 363 kcal", "diet": "Vegetarisch"},
                {"name": "Tomate-Mozzarella Panini", "price": "5,95 €", "calories": "1.980 kJ / 473 kcal", "diet": "Vegetarisch"}
            ]
        }
    ],
    faqs=[
        {
            "q": "Was kostet ein Caramel Macchiato bei Starbucks in Deutschland?",
            "a": "Ein Caramel Macchiato kostet in der Größe Tall ca. 5,25 €, in der beliebten Größe Grande ca. 5,85 € und als Venti rund 6,35 €."
        },
        {
            "q": "Kosten Hafermilch oder Sojamilch bei Starbucks extra?",
            "a": "Nein, Starbucks Deutschland verlangt in den allermeisten unternehmenseigenen Stores keinen Aufpreis mehr für vegane Milchalternativen wie Haferdrink, Sojadrink oder Mandeldrink."
        },
        {
            "q": "Wie groß sind die Starbucks Becher?",
            "a": "Die drei Standardgrößen sind Tall (ca. 355 ml), Grande (ca. 473 ml) und Venti (ca. 591 ml bzw. 710 ml bei Kaltgetränken)."
        }
    ]
))

# 6. Nordsee
chains.append(create_chain(
    slug="nordsee-preise",
    name="Nordsee",
    category="fast-food",
    title="Nordsee Speisekarte Preise 2026 – Fischbrötchen & Tellergerichte",
    meta_desc="Aktuelle Nordsee Speisekarte 2026 in Deutschland: Preise für Backfisch-Baguette, Bremer, Matjes, Lachsfilet, Fish & Chips im Tabellen-Überblick.",
    hero_sub="Alle Preise für Fischbrötchen, Meeresfrüchte, Tellergerichte und Boxen bei Nordsee Deutschland.",
    quick_answer="Bei Nordsee kostet das legendäre Backfisch-Baguette 2026 ca. 5,29 €, der beliebte Bremer (Frikadelle im Brötchen) ca. 3,79 € und Fish & Chips mit Sauce rund 8,99 €. Tellergerichte im Restaurant wie gebratenes Lachsfilet liegen zwischen 12,90 € und 16,50 €.",
    price_level="€€ (Mittel)",
    breakfast_info={
        "hasBreakfast": True,
        "hoursWeekdays": "Ab 08:00 Uhr Snack-Verkauf",
        "hoursWeekend": "Ab 09:00 Uhr",
        "note": "Frische Fischbrötchen und belegte Snacks sind direkt ab Ladenöffnung an der Theke verfügbar."
    },
    saving_tips=[
        "Lade die Nordsee App herunter: Dort gibt es regelmäßig 2-für-1 Gutscheine für Fischbrötchen oder Snack-Boxen.",
        "Der 'Snack des Monats' bietet wechselnde Brötchen-Klassiker mit bis zu 30 % Preisnachlass an der Theke."
    ],
    history="Nordsee wurde 1896 von Bremerhavener Fischern gegründet. Das Traditionsunternehmen wuchs zur bekanntesten Fisch-Fast-Food-Kette im deutschsprachigen Raum heran und betreibt heute über 250 Standorte in Deutschland und Österreich.",
    categories=[
        {
            "categoryName": "Fischbrötchen & Snacks To-Go",
            "items": [
                {"name": "Backfisch-Baguette (mit Remoulade)", "price": "5,29 €", "calories": "2.210 kJ / 528 kcal", "diet": "Fisch"},
                {"name": "Bremer (Fischfrikadelle im Brötchen)", "price": "3,79 €", "calories": "1.740 kJ / 416 kcal", "diet": "Fisch"},
                {"name": "Bismarckhering-Baguette", "price": "4,49 €", "calories": "1.580 kJ / 377 kcal", "diet": "Fisch"},
                {"name": "Nordischer Matjes im Brötchen", "price": "4,69 €", "calories": "1.650 kJ / 394 kcal", "diet": "Fisch"},
                {"name": "Räucherlachs-Bagel mit Frischkäse", "price": "5,99 €", "calories": "1.820 kJ / 435 kcal", "diet": "Fisch"},
                {"name": "Garnelen-Box (paniert mit Dip)", "price": "6,49 €", "calories": "1.490 kJ / 356 kcal", "diet": "Meeresfrüchte"}
            ]
        },
        {
            "categoryName": "Warme Tellergerichte & Menüs",
            "items": [
                {"name": "Fish & Chips mit Sauce Tartare", "price": "8,99 €", "calories": "3.120 kJ / 745 kcal", "diet": "Fisch"},
                {"name": "Gebratenes Lachsfilet mit Petersilienkartoffeln", "price": "15,49 €", "calories": "2.680 kJ / 640 kcal", "diet": "Fisch"},
                {"name": "Schollenfilet Müllerin Art mit Kartoffelsalat", "price": "13,99 €", "calories": "2.890 kJ / 690 kcal", "diet": "Fisch"},
                {"name": "Seelachsfilet gebacken mit Remouladensauce", "price": "11,49 €", "calories": "2.950 kJ / 705 kcal", "diet": "Fisch"}
            ]
        }
    ],
    faqs=[
        {
            "q": "Was kostet ein Backfisch-Baguette bei Nordsee 2026?",
            "a": "Das klassische Backfisch-Baguette mit Remouladensauce kostet aktuell ca. 5,29 € an der Nordsee-Theke."
        },
        {
            "q": "Gibt es bei Nordsee vegetarische oder vegane Optionen?",
            "a": "Ja, Nordsee hat 'Plant-based' Fischalternativen eingeführt, darunter das pflanzliche Visch-Baguette sowie Meeresalgen-Salate."
        }
    ]
))

# 7. KFC (Kentucky Fried Chicken)
chains.append(create_chain(
    slug="kfc-preise",
    name="KFC",
    category="fast-food",
    title="KFC Speisekarte Preise 2026 – Buckets, Boxen & Gutscheine",
    meta_desc="Aktuelle KFC Preise 2026 in Deutschland: Bucket Preise, Crispys, Hot Wings, Zinger Burger, Box-Menüs & Gutscheine im vollständigen Tabellen-Überblick.",
    hero_sub="Alle Preise für KFC Buckets, Hähnchenteile, Burger und Sparmenüs in Deutschland.",
    quick_answer="Bei KFC Deutschland kostet ein 6er Hot Wings Menü ca. 8,99 €, ein Zinger Burger ca. 5,99 € und der beliebte Colonel All Star Bucket für 2 Personen rund 19,99 €. Für Familien und Gruppen bieten die Buckets (z. B. 20 Hot Wings oder Crispy Box) den günstigsten Stückpreis.",
    price_level="€€ (Mittel)",
    breakfast_info={
        "hasBreakfast": False,
        "hoursWeekdays": "Täglich ab 11:00 Uhr geöffnet",
        "hoursWeekend": "Täglich ab 11:00 Uhr geöffnet",
        "note": "KFC bietet in Deutschland kein separates Frühstück an."
    },
    saving_tips=[
        "Der 'Dienstags-Bucket' (Tuesday Bucket) ist der bekannteste Spartipp bei KFC: Viele Filialen bieten dienstags einen Sonder-Bucket für rund 11–13 € an.",
        "KFC Gutscheine (Gutscheinbogen) sind dauerhaft in der KFC App verfügbar und bieten bis zu 35 % Rabatt auf Menüs."
    ],
    history="Kentucky Fried Chicken wurde 1930 von Harland D. Sanders ('Colonel Sanders') in den USA gegründet. Das Erfolgsgeheimnis ist die geheime Rezeptur aus 11 Kräutern und Gewürzen. Das erste Restaurant in Deutschland eröffnete 1968 in Frankfurt am Main.",
    categories=[
        {
            "categoryName": "KFC Buckets (Ideal zum Teilen)",
            "items": [
                {"name": "Bucket für 2 (6 Crispys + 6 Hot Wings + 2 Pommes)", "price": "18,99 €", "calories": "4.890 kJ / 1.168 kcal", "diet": "Geflügel"},
                {"name": "Hot Wings Bucket (20 Hot Wings)", "price": "19,49 €", "calories": "4.320 kJ / 1.032 kcal", "diet": "Scharf"},
                {"name": "Crispy Strips Bucket (15 Crispys + 3 Dips)", "price": "19,99 €", "calories": "4.150 kJ / 992 kcal", "diet": "Geflügel"},
                {"name": "Family Bucket (8 Hähnchenteile + 8 Wings + 4 Pommes)", "price": "27,99 €", "calories": "7.890 kJ / 1.885 kcal", "diet": "Geflügel"}
            ]
        },
        {
            "categoryName": "Burger & Twister Wraps",
            "items": [
                {"name": "Zinger Burger (Scharfes Hähnchenfilet)", "price": "5,99 €", "calories": "2.120 kJ / 506 kcal", "diet": "Pikant"},
                {"name": "Colonel Burger Original", "price": "5,79 €", "calories": "2.050 kJ / 490 kcal", "diet": "Geflügel"},
                {"name": "Twister Wrap Classic", "price": "6,19 €", "calories": "2.190 kJ / 523 kcal", "diet": "Geflügel"},
                {"name": "Veggie Tenders Burger (Plant-based)", "price": "5,79 €", "calories": "1.920 kJ / 458 kcal", "diet": "Vegetarisch"}
            ]
        }
    ],
    faqs=[
        {
            "q": "Was kostet ein Bucket bei KFC in Deutschland?",
            "a": "Die Preise für KFC Buckets starten bei rund 18,99 € für den 2-Personen-Bucket und reichen bis ca. 27,99 € für den großen Family Bucket."
        },
        {
            "q": "Gibt es den KFC Dienstags-Bucket noch?",
            "a": "Ja, der Tuesday Bucket wird von den meisten teilnehmenden deutschen KFC-Restaurants als wöchentlicher Aktionstag geführt."
        }
    ]
))

# 8. Pizza Hut
chains.append(create_chain(
    slug="pizza-hut-preise",
    name="Pizza Hut",
    category="pizza-pasta",
    title="Pizza Hut Speisekarte Preise 2026 – Pan Pizza & All You Can Eat",
    meta_desc="Aktuelle Pizza Hut Preise 2026 in Deutschland: Pan Pizza, Cheezy Crust, Pizza Buffet (All You Can Eat), Pasta & Knoblauchbrot im Tabellen-Überblick.",
    hero_sub="Alle Preise für Pan Pizza, Cheezy Crust Kruste, Pasta und das legendäre Pizza Hut Mittagsbuffet.",
    quick_answer="Bei Pizza Hut Deutschland kostet eine Pan Pizza (Normal 23 cm) ca. 11,90 €, in der Large-Größe (33 cm) ca. 18,50 €. Der beliebte Käserand 'Cheezy Crust' kostet rund 3,50 € Aufpreis. Das bekannte Pizza Hut Mittags-Buffet (All You Can Eat) liegt werktags je nach Standort bei ca. 12,90 € bis 14,90 € pro Person.",
    price_level="€€ (Mittel)",
    breakfast_info={
        "hasBreakfast": False,
        "hoursWeekdays": "Mo – Fr ab 11:30 Uhr geöffnet",
        "hoursWeekend": "Sa – So ab 12:00 Uhr geöffnet",
        "note": "Mittagsbuffet in teilnehmenden Dine-In Restaurants meist von 11:30 bis 14:30 Uhr."
    },
    saving_tips=[
        "Nutze das Mittagsbuffet unter der Woche: Für rund 13 € kannst du so viel Pizza, Pasta und Salat essen, wie du möchtest.",
        "Im Lieferdienst gibt es häufig '2 Pizzen zum Sparpreis' Aktionen am Dienstag oder Donnerstag."
    ],
    history="Pizza Hut wurde 1958 von den Brüdern Dan und Frank Carney in Kansas gegründet. Die erste deutsche Filiale eröffnete 1983. Die Kette ist weltweit berühmt für ihre goldbraun in der Pfanne gebackene Pan Pizza mit luftig-dickem Teig.",
    categories=[
        {
            "categoryName": "Pan Pizza & Cheezy Crust (Klassiker)",
            "items": [
                {"name": "Pan Pizza Salami (Normal 23cm | Large 33cm)", "price": "11,90 € | 18,50 €", "calories": "3.100 kJ / 740 kcal", "diet": "Schwein"},
                {"name": "Pan Pizza Margherita (Normal | Large)", "price": "9,90 € | 15,90 €", "calories": "2.650 kJ / 633 kcal", "diet": "Vegetarisch"},
                {"name": "Pan Pizza Texas Supreme (Rind, Zwiebeln, Paprika)", "price": "13,50 € | 20,50 €", "calories": "3.480 kJ / 831 kcal", "diet": "Rindfleisch"},
                {"name": "Pan Pizza Tuna & Onions", "price": "12,90 € | 19,50 €", "calories": "2.980 kJ / 712 kcal", "diet": "Fisch"},
                {"name": "Cheezy Crust Käserand-Aufpreis", "price": "+ 3,50 €", "calories": "980 kJ / 234 kcal", "diet": "Vegetarisch"}
            ]
        },
        {
            "categoryName": "Buffet & Vorspeisen",
            "items": [
                {"name": "Mittags-Buffet All You Can Eat (Mo–Fr)", "price": "13,90 €", "calories": "variiert", "diet": "Buffet"},
                {"name": "Knoblauchbrot Classic (Garlic Bread)", "price": "4,20 €", "calories": "1.120 kJ / 268 kcal", "diet": "Vegetarisch"},
                {"name": "Knoblauchbrot mit Mozzarella überbacken", "price": "5,40 €", "calories": "1.650 kJ / 394 kcal", "diet": "Vegetarisch"}
            ]
        }
    ],
    faqs=[
        {
            "q": "Was kostet das Pizza Hut All You Can Eat Buffet in Deutschland?",
            "a": "Das Mittagsbuffet kostet in den meisten teilnehmenden Pizza Hut Restaurants wochentags zwischen 12,90 € und 14,90 € pro Person inklusive Pizza, Pasta und Salatbar."
        }
    ]
))

# 9. Five Guys
chains.append(create_chain(
    slug="five-guys-preise",
    name="Five Guys",
    category="burger",
    title="Five Guys Preise Deutschland 2026 – Burger, Fries & Shakes",
    meta_desc="Aktuelle Five Guys Preise 2026 in Deutschland: Hamburger, Cheeseburger, Bacon Burger, Little Burger, Cajun Fries und Milkshakes mit allen Preisen in Tabelle.",
    hero_sub="Die vollständige Preisliste von Five Guys Deutschland inklusive aller kostenlosen Toppings und Shakes.",
    quick_answer="Bei Five Guys Deutschland kostet ein regulärer Hamburger (2 Patties) ca. 10,95 €, ein Cheeseburger ca. 11,95 € und der Bacon Cheeseburger ca. 12,95 €. Die kleineren 'Little' Burger (1 Patty) liegen zwischen 8,45 € und 9,95 €. Alle 15 Toppings (Salat, Tomaten, Grillzwiebeln, Jalapeños, Saucen etc.) sind unbegrenzt kostenlos.",
    price_level="€€€ (Premium Fast Casual)",
    breakfast_info={"hasBreakfast": False, "hoursWeekdays": "Täglich ab 11:00 Uhr geöffnet", "hoursWeekend": "Täglich ab 11:00 Uhr geöffnet", "note": "Kein Frühstücksangebot."},
    saving_tips=[
        "Eine 'Little Fries' reicht bei Five Guys fast immer für zwei Personen, da die Papiertüte traditionell mit einer extra Schaufel Pommes aufgefüllt wird ('Topper').",
        "Wähle beliebig viele Toppings 'All the Way' ohne Aufpreis."
    ],
    history="Five Guys wurde 1986 von Jerry Murrell und seinen Söhnen in Virginia gegründet. Das erste deutsche Restaurant eröffnete 2017 auf der Zeil in Frankfurt am Main. Die Kette verwendet ausschließlich frisches, nie gefrorenes Rindfleisch und brät in reinem Erdnussöl.",
    categories=[
        {
            "categoryName": "Burger & Sandwiches (Inkl. alle Toppings)",
            "items": [
                {"name": "Hamburger (2 Patties)", "price": "10,95 €", "calories": "3.510 kJ / 840 kcal", "diet": "Frisches Rind"},
                {"name": "Cheeseburger (2 Patties + Käse)", "price": "11,95 €", "calories": "4.100 kJ / 980 kcal", "diet": "Frisches Rind"},
                {"name": "Bacon Burger (2 Patties + Bacon)", "price": "11,95 €", "calories": "3.980 kJ / 950 kcal", "diet": "Rind & Bacon"},
                {"name": "Bacon Cheeseburger (2 Patties, Käse, Bacon)", "price": "12,95 €", "calories": "4.430 kJ / 1.060 kcal", "diet": "Rind & Bacon"},
                {"name": "Little Hamburger (1 Patty)", "price": "8,45 €", "calories": "2.260 kJ / 540 kcal", "diet": "Frisches Rind"},
                {"name": "Little Cheeseburger (1 Patty + Käse)", "price": "9,45 €", "calories": "2.550 kJ / 610 kcal", "diet": "Frisches Rind"},
                {"name": "Veggie Sandwich (Gegrilltes Gemüse)", "price": "6,95 €", "calories": "1.840 kJ / 440 kcal", "diet": "Vegetarisch"}
            ]
        },
        {
            "categoryName": "Fries (In Erdnussöl frittiert)",
            "items": [
                {"name": "Five Guys Style Fries (Little | Medium | Large)", "price": "4,95 € | 6,45 € | 7,95 €", "calories": "2.220 kJ / 530 kcal (L)", "diet": "Vegan 🌱"},
                {"name": "Cajun Style Fries (Little | Medium | Large)", "price": "4,95 € | 6,45 € | 7,95 €", "calories": "2.220 kJ / 530 kcal (L)", "diet": "Pikant / Vegan 🌱"}
            ]
        },
        {
            "categoryName": "Five Guys Shakes",
            "items": [
                {"name": "Five Guys Milkshake (Basis nach Wahl)", "price": "6,95 €", "calories": "2.800 kJ / 670 kcal", "diet": "Vegetarisch"},
                {"name": "Mix-Ins (Erdbeere, Erdnussbutter, Bacon, Oreo)", "price": "Kostenlos", "calories": "variiert", "diet": "Mix-In"}
            ]
        }
    ],
    faqs=[
        {
            "q": "Warum ist Five Guys so teuer im Vergleich zu McDonald's?",
            "a": "Five Guys positioniert sich im 'Better Burger' Segment: Es werden keine Tiefkühlpatties verwendet, Kartoffeln werden vor Ort frisch geschnitten und in 100 % Erdnussöl frittiert, und alle Toppings sind unbegrenzt inklusive."
        }
    ]
))

# 10. Frittenwerk
chains.append(create_chain(
    slug="frittenwerk-preise",
    name="Frittenwerk",
    category="doener-streetfood",
    title="Frittenwerk Speisekarte Preise 2026 – Poutines, Pommes & Kalorien",
    meta_desc="Aktuelle Frittenwerk Speisekarte 2026 in Deutschland: Preise für Poutine Klassiker, Pommes Spezialitäten, Dips & Churros im Tabellen-Überblick.",
    hero_sub="Die Kult-Pommesmanufaktur aus Düsseldorf: Alle Poutines, loaded Fries und Saucen im Preisüberblick.",
    quick_answer="Bei Frittenwerk kostet die klassische 'Quebec Poutine' (Pommes, vegetarische Bratensauce & Mozzarella Cheese Curds) ca. 7,90 €. Aufwändigere Loaded-Fries wie 'Tijuana Street Fries' (mit Guacamole & Sour Cream) oder 'Chili Cheese Fries' kosten zwischen 8,90 € und 10,90 €.",
    price_level="€€ (Mittel)",
    breakfast_info={"hasBreakfast": False, "hoursWeekdays": "Täglich ab 11:30 Uhr geöffnet", "hoursWeekend": "Täglich ab 11:30 Uhr geöffnet", "note": "Kein Frühstück."},
    saving_tips=["Frittenwerk bietet Portionsgrößen, die als vollwertige Hauptmahlzeit sättigen. Ein Poutine-Gericht reicht meist völlig aus."],
    history="Frittenwerk startete 2014 im Düsseldorfer Medienhafen mit der Vision, kanadisches Streetfood (Poutine) mit nachhaltigen Pommes nach Deutschland zu bringen. Heute gibt es über 40 Standorte bundesweit.",
    categories=[
        {
            "categoryName": "Poutines & Loaded Fries",
            "items": [
                {"name": "Quebec Poutine (Bratensauce & Cheese Curds)", "price": "7,90 €", "calories": "2.850 kJ / 680 kcal", "diet": "Vegetarisch"},
                {"name": "Tijuana Street Fries (Guacamole, Tomaten, Sour Cream)", "price": "8,90 €", "calories": "2.980 kJ / 712 kcal", "diet": "Vegetarisch"},
                {"name": "Pulled Pork Poutine (mit BBQ-Sauce & Krautsalat)", "price": "10,90 €", "calories": "3.850 kJ / 920 kcal", "diet": "Schweinefleisch"},
                {"name": "Pink Persian Poutine (mit Falafel & Rote-Bete-Hummus)", "price": "9,90 €", "calories": "2.710 kJ / 648 kcal", "diet": "Vegan 🌱"},
                {"name": "Chili Cheese Fries", "price": "8,90 €", "calories": "3.150 kJ / 753 kcal", "diet": "Pikant"}
            ]
        }
    ],
    faqs=[
        {
            "q": "Was ist eine Poutine bei Frittenwerk?",
            "a": "Poutine ist eine kanadische Spezialität aus knusprigen Pommes Frites, Käsebruch (Cheese Curds) und heißer vegetarischer Bratensauce, die den Käse leicht anschmelzen lässt."
        }
    ]
))

# 11. Haus des Döners
chains.append(create_chain(
    slug="haus-des-doeners-preise",
    name="Haus des Döners",
    category="doener-streetfood",
    title="Haus des Döners Speisekarte Preise 2026 – Aktuelle Preisliste",
    meta_desc="Aktuelle Haus des Döners Preise 2026: Döner Kebab, Dürüm, Döner Box, Pommes & Berliner Saucen im übersichtlichen Tabellen-Vergleich.",
    hero_sub="Die rasant wachsende Döner-Kette mit Berliner Rezeptur: Alle Döner-Preise und Kalorien auf einen Blick.",
    quick_answer="Ein Döner Kebab bei Haus des Döners kostet 2026 durchschnittlich 7,50 € bis 8,00 €. Ein Dürüm Döner liegt bei ca. 8,50 € bis 9,00 €, und eine Döner Box mit Pommes oder Salat kostet rund 7,00 € bis 7,50 €.",
    price_level="€€ (Günstig bis Mittel)",
    breakfast_info={"hasBreakfast": False, "hoursWeekdays": "Täglich ab 11:00 Uhr geöffnet", "hoursWeekend": "Täglich ab 11:00 Uhr geöffnet", "note": "Kein Frühstück."},
    saving_tips=["Viele Neueröffnungen von Haus des Döners veranstalten legendäre 1-Cent- oder 1-Euro-Döner-Aktionen."],
    history="Haus des Döners wurde in Hürth bei Köln gegründet und ist inspiriert vom 'Berliner Döner' mit knusprigem Brot und den drei traditionellen Saucen (Kräuter, Knoblauch, Scharf). Mit markantem Design wuchs das Franchise rasant auf über 80 Filialen in Deutschland.",
    categories=[
        {
            "categoryName": "Döner & Dürüm Spezialitäten",
            "items": [
                {"name": "Döner Kebab im Fladenbrot (Kalb / Hähnchen)", "price": "7,80 €", "calories": "2.890 kJ / 690 kcal", "diet": "Halal"},
                {"name": "Dürüm Döner (Gerolltes Fladenbrot)", "price": "8,80 €", "calories": "3.150 kJ / 753 kcal", "diet": "Halal"},
                {"name": "Döner Box (Fleisch mit Pommes & Sauce)", "price": "7,20 €", "calories": "2.450 kJ / 585 kcal", "diet": "Halal"},
                {"name": "Döner Teller (Fleisch, Pommes, Salat & 2 Saucen)", "price": "12,50 €", "calories": "4.100 kJ / 980 kcal", "diet": "Halal"},
                {"name": "Vegetarischer Döner (mit Hirtenkäse & Salat)", "price": "6,50 €", "calories": "1.980 kJ / 473 kcal", "diet": "Vegetarisch"},
                {"name": "Falafel Dürüm (hausgemacht)", "price": "7,50 €", "calories": "2.250 kJ / 538 kcal", "diet": "Vegan 🌱"}
            ]
        }
    ],
    faqs=[
        {
            "q": "Wie viel kostet ein Döner bei Haus des Döners?",
            "a": "Ein klassischer Döner Kebab im gerösteten Fladenbrot kostet 2026 bei Haus des Döners ca. 7,80 €."
        }
    ]
))

# 12. Block House
chains.append(create_chain(
    slug="block-house-preise",
    name="Block House",
    category="steakhouse-bbq",
    title="Block House Speisekarte Preise 2026 – Steaks & Menü Preisliste",
    meta_desc="Aktuelle Block House Speisekarte 2026 mit Preisen: Rumpsteak, Rib-Eye, Filetsteak, Knoblauchbrot, Baked Potato & Mittagstisch im Tabellen-Überblick.",
    hero_sub="Deutschlands bekannteste Steakhouse-Kette: Alle Fleischsorten, Beilagen und Mittagsangebote mit Preisen.",
    quick_answer="Bei Block House kostet ein 180g Rumpsteak ca. 24,90 €, ein 250g Rib-Eye Mastercut ca. 29,80 € und das zarte Filet Mignon (180g) ca. 32,50 €. Zu allen Steaks serviert Block House traditionell das berühmte Block House Knoblauchbrot.",
    price_level="€€€ (Gehoben)",
    breakfast_info={"hasBreakfast": False, "hoursWeekdays": "Mo – Fr ab 11:30 Uhr geöffnet", "hoursWeekend": "Sa – So ab 12:00 Uhr geöffnet", "note": "Mittagskarte werktags bis 15:00 Uhr."},
    saving_tips=["Der 'Block House Mittagstisch' (Mo–Fr 11:30 bis 15:00 Uhr) bietet vollwertige Steak- und Pfannengerichte mit bis zu 25 % Preisvorteil gegenüber der Abendkarte."],
    history="Gegründet 1968 von Eugen Block in Hamburg, revolutionierte Block House das Konzept des hochwertigen und bezahlbaren Steaks in Deutschland. Heute betreibt die Gruppe über 40 Steakhäuser in Deutschland und Europa.",
    categories=[
        {
            "categoryName": "Steaks vom Lavasteingrill (Inkl. Block House Brot)",
            "items": [
                {"name": "Hereford Rumpsteak (180g)", "price": "24,90 €", "calories": "1.890 kJ / 452 kcal", "diet": "Rind"},
                {"name": "Hereford Rumpsteak (250g)", "price": "29,50 €", "calories": "2.450 kJ / 585 kcal", "diet": "Rind"},
                {"name": "Rib-Eye Steak / Entrecôte (250g)", "price": "29,80 €", "calories": "2.890 kJ / 690 kcal", "diet": "Rind"},
                {"name": "Filet Mignon (180g)", "price": "32,50 €", "calories": "1.650 kJ / 394 kcal", "diet": "Rind"},
                {"name": "American Tenderloin Filet (250g)", "price": "39,90 €", "calories": "2.150 kJ / 514 kcal", "diet": "Rind"}
            ]
        },
        {
            "categoryName": "Beilagen & Vorspeisen",
            "items": [
                {"name": "Original Block House Knoblauchbrot (2 Stück)", "price": "3,40 €", "calories": "980 kJ / 234 kcal", "diet": "Vegetarisch"},
                {"name": "Baked Potato mit Sauerrahm (Sour Cream)", "price": "4,90 €", "calories": "1.320 kJ / 315 kcal", "diet": "Vegetarisch"},
                {"name": "Knackiger Block House Salat mit Dressing", "price": "6,50 €", "calories": "480 kJ / 115 kcal", "diet": "Vegetarisch"}
            ]
        }
    ],
    faqs=[
        {
            "q": "Was kostet ein Steak bei Block House?",
            "a": "Ein 180g Rumpsteak startet bei 24,90 €. Größere Zuschnitte wie das 250g Rib-Eye liegen bei 29,80 €."
        }
    ]
))

# 13. Peter Pane
chains.append(create_chain(
    slug="peter-pane-preise",
    name="Peter Pane",
    category="burger",
    title="Peter Pane Speisekarte Preise 2026 – Burger, Fritten & Cocktails",
    meta_desc="Aktuelle Peter Pane Preise 2026 in Deutschland: Burger Klassiker, vegane Burger, Fritten, Mittagsmenü & Cocktails im Tabellen-Überblick.",
    hero_sub="Das beliebte Burgergrill-Konzept: Alle Burger, Menüs und vegane Kreationen im Preisüberblick.",
    quick_answer="Bei Peter Pane kostet ein klassischer Rindfleisch-Burger (z. B. 'Der Klassiker' oder 'Doppelter Peter') zwischen 9,90 € und 13,90 €. Das beliebte Peter-Menü (Burger + Fritten nach Wahl + Getränk + Heißgetränk) bietet bis 17:00 Uhr einen Sparvorteil von rund 4,50 €.",
    price_level="€€€ (Gehoben Casual)",
    breakfast_info={"hasBreakfast": False, "hoursWeekdays": "Täglich ab 11:30 Uhr geöffnet", "hoursWeekend": "Täglich ab 11:30 Uhr geöffnet", "note": "Mittagsmenü werktags bis 17:00 Uhr."},
    saving_tips=["Das Mittagsmenü bis 17:00 Uhr spart bares Geld: Fritten und Getränke sind stark vergünstigt im Kombi-Paket."],
    history="Peter Pane entstand 2016 aus den norddeutschen Standorten der Paniceus Gastro Gruppe rund um Patrick Junge. Die Kette hat heute über 50 Standorte und ist bekannt für märchenhaftes Ambiente und eine riesige vegane Burger-Auswahl.",
    categories=[
        {
            "categoryName": "Burger Kreationen (Rindfleisch aus Deutschland)",
            "items": [
                {"name": "Der Klassiker (Rindfleisch, Salat, Tomate, rote Zwiebeln)", "price": "9,90 €", "calories": "2.550 kJ / 610 kcal", "diet": "Rind"},
                {"name": "Käsebruder (Rindfleisch, Cheddar-Käse, Gurken)", "price": "10,90 €", "calories": "2.890 kJ / 690 kcal", "diet": "Rind"},
                {"name": "Doppelter Peter (2x Rindfleisch, Doppel-Cheddar)", "price": "13,90 €", "calories": "3.850 kJ / 920 kcal", "diet": "Rind"},
                {"name": "Goldfritte (mit Bacon, Guacamole & Cheddar)", "price": "12,90 €", "calories": "3.450 kJ / 824 kcal", "diet": "Rind"}
            ]
        },
        {
            "categoryName": "Vegane & Vegetarische Burger",
            "items": [
                {"name": "Panflöte (Süßkartoffel-Amaranth-Bratling, Guacamole)", "price": "10,90 €", "calories": "2.350 kJ / 561 kcal", "diet": "Vegan 🌱"},
                {"name": "Der Held (Pflanzliches Patty, veganer Käse, BBQ-Sauce)", "price": "11,50 €", "calories": "2.480 kJ / 592 kcal", "diet": "Vegan 🌱"}
            ]
        }
    ],
    faqs=[
        {
            "q": "Was kostet ein Burger bei Peter Pane?",
            "a": "Die Burger bei Peter Pane kosten einzeln zwischen 9,90 € und 14,50 €. Im Mittagsmenü gibt es Fritten und Drink vergünstigt dazu."
        }
    ]
))

# 14. Hans im Glück
chains.append(create_chain(
    slug="hans-im-glueck-preise",
    name="Hans im Glück",
    category="burger",
    title="Hans im Glück Speisekarte Preise 2026 – Burger & Mittagsmenü",
    meta_desc="Aktuelle Hans im Glück Preise 2026: Burger-Klassiker, Sauerteig- und Mehrkornbrötchen, vegane Burger, Fritten & Mittagsmenü im Tabellen-Überblick.",
    hero_sub="Die bekannte Burger- und Cocktail-Kette mit Birkenwald-Flair: Alle Preise und Menü-Upgrades.",
    quick_answer="Bei Hans im Glück kosten Burger zwischen 9,90 € und 13,90 €. Das Mittagsmenü (bis 17:00 Uhr) beinhaltet für einen Aufpreis von ca. 6,90 € eine Beilage nach Wahl, einen Durstlöscher und ein Heißgetränk.",
    price_level="€€€ (Gehoben Casual)",
    breakfast_info={"hasBreakfast": False, "hoursWeekdays": "Täglich ab 11:30 Uhr geöffnet", "hoursWeekend": "Täglich ab 11:30 Uhr geöffnet", "note": "Mittagsmenü werktags bis 17:00 Uhr."},
    saving_tips=["Das 'Mittagsmenü' bis 17:00 Uhr und das 'Abendmenü' ab 17:00 Uhr (mit Cocktail) bieten spürbare Rabatte im Vergleich zu Einzelbestellungen."],
    history="2010 von Thomas Hirschberger in München gegründet, expandierte Hans im Glück mit seinem ikonischen Birkenstamm-Interieur rasant auf über 90 Burgerbars in Deutschland, Österreich und der Schweiz.",
    categories=[
        {
            "categoryName": "Rindfleisch Burger (Saftiges Rindfleisch)",
            "items": [
                {"name": "Klassik (Salat, rote Zwiebeln, Tomaten, Glücks-Sauce)", "price": "9,90 €", "calories": "2.450 kJ / 585 kcal", "diet": "Rind"},
                {"name": "Heumilch (mit herzhaftem Heumilchkäse)", "price": "10,90 €", "calories": "2.790 kJ / 667 kcal", "diet": "Rind"},
                {"name": "Wilder Westen (Heumilchkäse, Grillbacon, BBQ-Sauce)", "price": "11,90 €", "calories": "3.120 kJ / 745 kcal", "diet": "Rind & Bacon"},
                {"name": "Geißbock (Ziegenkäse, Feigensauce, Bacon)", "price": "12,50 €", "calories": "3.250 kJ / 776 kcal", "diet": "Rind & Bacon"}
            ]
        },
        {
            "categoryName": "Vegane Burger (100% Pflanzlich)",
            "items": [
                {"name": "Jugendstil (Pflanzliches Patty, vegane Scheibe, Tomaten)", "price": "10,90 €", "calories": "2.280 kJ / 545 kcal", "diet": "Vegan 🌱"},
                {"name": "Fabelhafter (Weizenpatty, Avocado-Creme, Salat)", "price": "11,50 €", "calories": "2.420 kJ / 578 kcal", "diet": "Vegan 🌱"}
            ]
        }
    ],
    faqs=[
        {
            "q": "Was kostet das Mittagsmenü bei Hans im Glück?",
            "a": "Das Mittagsmenü bis 17:00 Uhr kostet den gewählten Burgerpreis zzgl. ca. 6,90 € und beinhaltet Pommes oder Salat, ein Kaltgetränk sowie einen Kaffee."
        }
    ]
))

# 15. Vapiano
chains.append(create_chain(
    slug="vapiano-preise",
    name="Vapiano",
    category="pizza-pasta",
    title="Vapiano Speisekarte Preise 2026 – Pasta, Pizza & Salate",
    meta_desc="Aktuelle Vapiano Preise 2026 in Deutschland: Frische Pasta (Bolognese, Carbonara), Steinofen-Pizza, Insalata & Dolci im Tabellen-Überblick.",
    hero_sub="Frische hausgemachte Pasta und knusprige Steinofen-Pizza: Alle aktuellen Vapiano Preise im Überblick.",
    quick_answer="Bei Vapiano Deutschland kostet eine Pasta Bolognese oder Carbonara ca. 11,95 € bis 12,95 €. Eine Pizza Margherita liegt bei ca. 9,95 €, während Pizza Salame oder Prosciutto e Funghi rund 12,50 € kosten.",
    price_level="€€ (Mittel)",
    breakfast_info={"hasBreakfast": False, "hoursWeekdays": "Ab 11:30 Uhr geöffnet", "hoursWeekend": "Ab 12:00 Uhr geöffnet", "note": "Kein Frühstück."},
    saving_tips=["Das Vapiano People Treueprogramm vergibt Punkte für Gratis-Dolci oder Heißgetränke."],
    history="2002 in Hamburg gegründet, erfand Vapiano das 'Fast-Casual'-Konzept für frische italienische Küche mit Live-Cooking vor den Augen der Gäste.",
    categories=[
        {
            "categoryName": "Pasta Fresca (Hausgemacht)",
            "items": [
                {"name": "Pasta Pomodoro (frische Tomatensauce)", "price": "8,95 €", "calories": "2.100 kJ / 502 kcal", "diet": "Vegan 🌱"},
                {"name": "Pasta Bolognese (italienisches Rinderhack)", "price": "12,45 €", "calories": "2.890 kJ / 690 kcal", "diet": "Rind"},
                {"name": "Pasta Carbonara (Speck, Sahne, Eigelb, Grana Padano)", "price": "12,95 €", "calories": "3.420 kJ / 817 kcal", "diet": "Schwein"},
                {"name": "Pasta Crema di Funghi (frische Champignons, Weißwein)", "price": "11,95 €", "calories": "2.750 kJ / 657 kcal", "diet": "Vegetarisch"}
            ]
        },
        {
            "categoryName": "Pizza aus dem Steinofen",
            "items": [
                {"name": "Pizza Margherita (Mozzarella, Tomaten, Basilikum)", "price": "9,95 €", "calories": "3.150 kJ / 752 kcal", "diet": "Vegetarisch"},
                {"name": "Pizza Salame (würzige Salami)", "price": "12,45 €", "calories": "3.680 kJ / 879 kcal", "diet": "Schwein"},
                {"name": "Pizza Prosciutto e Funghi (Schinken, frische Pilze)", "price": "12,95 €", "calories": "3.550 kJ / 848 kcal", "diet": "Schwein"}
            ]
        }
    ],
    faqs=[
        {
            "q": "Was kostet eine Pasta bei Vapiano 2026?",
            "a": "Die Pastagerichte starten bei 8,95 € für Pomodoro und reichen bis ca. 14,50 € für Pasta Scampi."
        }
    ]
))

# 16. L'Osteria
chains.append(create_chain(
    slug="losteria-preise",
    name="L'Osteria",
    category="pizza-pasta",
    title="L'Osteria Speisekarte Preise 2026 – Riesen-Pizza & Pasta",
    meta_desc="Aktuelle L'Osteria Preise 2026 in Deutschland: Berühmte 45cm Riesen-Pizza, Pasta d'Amore, Salate & Dolci im Tabellen-Überblick.",
    hero_sub="Berühmt für die 45 cm Riesen-Pizza mit zwei unterschiedlich belegten Hälften: Alle L'Osteria Preise.",
    quick_answer="Bei L'Osteria kostet die riesige 45-cm-Pizza Margherita ca. 12,50 €, eine Pizza Salami ca. 14,50 €. Praktischer Tipp: Eine Pizza kann mit zwei unterschiedlich belegten Hälften bestellt und problemlos zu zweit geteilt werden.",
    price_level="€€ (Mittel)",
    breakfast_info={"hasBreakfast": False, "hoursWeekdays": "Ab 11:30 Uhr geöffnet", "hoursWeekend": "Ab 12:00 Uhr geöffnet", "note": "Kein Frühstück."},
    saving_tips=["Teilt euch eine Pizza zu zweit! Mit 45 cm Durchmesser ragt die Pizza weit über den Tellerrand hinaus."],
    history="1999 in Nürnberg gegründet, wuchs L'Osteria durch ihre überdimensionalen Pizzen zu einer der beliebtesten italienischen Gastronomie-Ketten im deutschsprachigen Raum heran.",
    categories=[
        {
            "categoryName": "Die berühmte 45 cm Pizza",
            "items": [
                {"name": "Pizza Margherita (45 cm)", "price": "12,50 €", "calories": "4.200 kJ / 1.003 kcal", "diet": "Vegetarisch"},
                {"name": "Pizza Salami (45 cm)", "price": "14,50 €", "calories": "4.890 kJ / 1.168 kcal", "diet": "Schwein"},
                {"name": "Pizza Prosciutto e Funghi (45 cm)", "price": "14,90 €", "calories": "4.750 kJ / 1.135 kcal", "diet": "Schwein"},
                {"name": "Pizza BBQ Chicken (45 cm)", "price": "15,50 €", "calories": "4.950 kJ / 1.183 kcal", "diet": "Geflügel"}
            ]
        }
    ],
    faqs=[
        {
            "q": "Wie groß ist die Pizza bei L'Osteria?",
            "a": "Die Pizza bei L'Osteria hat einen Durchmesser von 45 cm. Sie kann mit zwei unterschiedlichen Hälften belegt werden."
        }
    ]
))

# 17. Dunkin' Donuts
chains.append(create_chain(
    slug="dunkin-donuts-preise",
    name="Dunkin' Donuts",
    category="kaffee-baeckerei",
    title="Dunkin' Donuts Preise Deutschland 2026 – Einzeln & 6er/12er Box",
    meta_desc="Aktuelle Dunkin' Donuts Preise 2026 in Deutschland: Einzelner Donut, 6er Box, 12er Box, Iced Coffee, Boston Kreme & Sorten im Tabellen-Überblick.",
    hero_sub="Alle Preise für einzelne Donuts, 6er und 12er Vorratsboxen sowie Kaffeespezialitäten bei Dunkin' Deutschland.",
    quick_answer="Bei Dunkin' Donuts Deutschland kostet ein einzelner Donut 2026 ca. 2,49 €. Eine 6er-Box liegt bei rund 12,99 € (ca. 2,16 € pro Donut) und die große 12er-Party-Box bei etwa 22,99 € (ca. 1,91 € pro Donut).",
    price_level="€€ (Günstig bis Mittel)",
    breakfast_info={"hasBreakfast": True, "hoursWeekdays": "Ab 07:00 Uhr geöffnet", "hoursWeekend": "Ab 08:00 Uhr geöffnet", "note": "Frische Donuts und heißer Kaffee ab Ladenöffnung."},
    saving_tips=["Kaufe immer mindestens eine 6er- oder 12er-Box, um bis zu 25 % pro Donut im Vergleich zum Einzelpreis zu sparen."],
    history="1950 in Massachusetts gegründet, zählt Dunkin' heute zu den weltweit größten Coffee-and-Baked-Goods-Ketten. In Deutschland gibt es über 70 Filialen.",
    categories=[
        {
            "categoryName": "Donuts & Boxen",
            "items": [
                {"name": "Klassischer Donut Einzeln (Boston Kreme, Strawberry Frosted)", "price": "2,49 €", "calories": "1.150 kJ / 275 kcal", "diet": "Vegetarisch"},
                {"name": "Premium Donut Einzeln (Nutella, Apple Crumble)", "price": "2,89 €", "calories": "1.420 kJ / 339 kcal", "diet": "Vegetarisch"},
                {"name": "6er Box Donuts nach Wahl", "price": "12,99 €", "calories": "6.900 kJ / 1.650 kcal", "diet": "Vegetarisch"},
                {"name": "12er Box Donuts nach Wahl", "price": "22,99 €", "calories": "13.800 kJ / 3.300 kcal", "diet": "Vegetarisch"}
            ]
        }
    ],
    faqs=[
        {
            "q": "Was kostet eine 6er Box bei Dunkin' Donuts?",
            "a": "Eine 6er Box Donuts nach freier Wahl kostet 2026 in Deutschland ca. 12,99 €."
        }
    ]
))

# 18. Domino's Pizza
chains.append(create_chain(
    slug="dominos-pizza-preise",
    name="Domino's Pizza",
    category="pizza-pasta",
    title="Domino's Pizza Preise Deutschland 2026 – Speisekarte & Lieferpreise",
    meta_desc="Aktuelle Domino's Pizza Preise 2026 in Deutschland: Classic, Medium, Large, Pizza Brötchen, Pasta & Cheesy Bread im Tabellen-Überblick.",
    hero_sub="Die vollständige Speisekarte von Domino's Pizza Deutschland für Abholung und Lieferung.",
    quick_answer="Bei Domino's Pizza Deutschland startet eine Medium-Pizza (28 cm) bei ca. 8,99 € (Margherita) bis 13,99 € (Spezialitäten). Bei Selbstabholung gewährt Domino's in vielen Filialen dauerhaft Abholrabatte von bis zu 30 %.",
    price_level="€€ (Mittel)",
    breakfast_info={"hasBreakfast": False, "hoursWeekdays": "Täglich ab 11:00 Uhr geöffnet", "hoursWeekend": "Täglich ab 11:00 Uhr geöffnet", "note": "Lieferung und Abholung bis spät abends."},
    saving_tips=["Selbstabholer sparen: Domino's bietet fast immer exklusive 'Pick-up' Rabatte an."],
    history="Domino's Pizza übernahm in Deutschland die Ketten Joey's Pizza und Hallo Pizza und wurde so zum unangefochtenen Marktführer für Pizza-Lieferdienste mit über 400 Stores.",
    categories=[
        {
            "categoryName": "Beliebte Pizzen (Classic 25cm | Medium 28cm | Large 32cm)",
            "items": [
                {"name": "Pizza Salami", "price": "7,99 € | 10,99 € | 14,99 €", "calories": "3.100 kJ / 741 kcal", "diet": "Schwein"},
                {"name": "Pizza Margherita", "price": "6,99 € | 8,99 € | 12,99 €", "calories": "2.650 kJ / 633 kcal", "diet": "Vegetarisch"},
                {"name": "Pizza Boston (mit Sauce Hollandaise & Schinken)", "price": "8,99 € | 12,49 € | 16,99 €", "calories": "3.480 kJ / 832 kcal", "diet": "Schwein"},
                {"name": "Pizza Waikiki (Schinken & Ananas)", "price": "8,49 € | 11,99 € | 15,99 €", "calories": "3.050 kJ / 729 kcal", "diet": "Schwein"}
            ]
        }
    ],
    faqs=[
        {
            "q": "Was kostet eine Pizza bei Domino's?",
            "a": "Eine Classic-Pizza (25 cm) startet bei ca. 6,99 € für Margherita. Beliebte Sorten wie Salami liegen bei ca. 10,99 € in der Medium-Größe (28 cm)."
        }
    ]
))

# 19. BackWerk
chains.append(create_chain(
    slug="backwerk-preise",
    name="BackWerk",
    category="kaffee-baeckerei",
    title="BackWerk Speisekarte Preise 2026 – Snacks, Belegte Brötchen & Kaffee",
    meta_desc="Aktuelle BackWerk Preise 2026 in Deutschland: Belegte Brötchen, Hot Dogs, Börek, Brezeln & günstige Kaffeespezialitäten im Tabellen-Überblick.",
    hero_sub="Deutschlands führender Backgastronom mit SB-Konzept: Alle Preise für Snacks und Heißgetränke.",
    quick_answer="Bei BackWerk kosten belegte Brötchen zwischen 2,40 € und 3,80 €, warme Hot Dogs ca. 2,90 € und frischer Kaffee Crema startet bereits ab 1,80 €. BackWerk gilt als einer der preiswertesten Snack-Anbieter an deutschen Bahnhöfen.",
    price_level="€ (Sehr günstig)",
    breakfast_info={"hasBreakfast": True, "hoursWeekdays": "Mo – Fr ab 06:00 Uhr", "hoursWeekend": "Sa – So ab 07:00 Uhr", "note": "Frisches Gebäck und warmer Kaffee ab den frühen Morgenstunden."},
    saving_tips=["Kombi-Angebote nutzen: Belegtes Brötchen + Heißgetränk ist oft rabattiert."],
    history="2001 gegründet, revolutionierte BackWerk den deutschen Bäckereimarkt als erste Selbstbedienungs-Bäckerei. Heute betreibt das zur Valora-Gruppe gehörende Franchise über 300 Filialen.",
    categories=[
        {
            "categoryName": "Belegte Brötchen & Herzhafte Snacks",
            "items": [
                {"name": "Rustiko Schinken-Käse", "price": "3,40 €", "calories": "1.780 kJ / 425 kcal", "diet": "Schwein"},
                {"name": "Fitnessbrötchen Pute", "price": "3,60 €", "calories": "1.520 kJ / 363 kcal", "diet": "Geflügel"},
                {"name": "Hot Dog Classic", "price": "2,90 €", "calories": "1.890 kJ / 452 kcal", "diet": "Schwein"},
                {"name": "Börekstange Spinat-Hirtenkäse", "price": "2,40 €", "calories": "1.420 kJ / 339 kcal", "diet": "Vegetarisch"},
                {"name": "Butterbrezel", "price": "1,90 €", "calories": "1.210 kJ / 289 kcal", "diet": "Vegetarisch"}
            ]
        },
        {
            "categoryName": "Kaffeespezialitäten (Fairtrade)",
            "items": [
                {"name": "Kaffee Crema Normal", "price": "1,80 €", "calories": "15 kJ / 4 kcal", "diet": "Vegan 🌱"},
                {"name": "Cappuccino Normal", "price": "2,30 €", "calories": "380 kJ / 91 kcal", "diet": "Vegetarisch"},
                {"name": "Latte Macchiato Groß", "price": "2,80 €", "calories": "580 kJ / 139 kcal", "diet": "Vegetarisch"}
            ]
        }
    ],
    faqs=[
        {
            "q": "Wie viel kostet ein Kaffee bei BackWerk?",
            "a": "Ein normaler Kaffee Crema kostet bei BackWerk ca. 1,80 €. Cappuccino liegt bei ca. 2,30 €."
        }
    ]
))

# 20. Gosch Sylt
chains.append(create_chain(
    slug="gosch-sylt-preise",
    name="Gosch Sylt",
    category="deutsch-regional",
    title="Gosch Sylt Speisekarte Preise 2026 – Fischbrötchen & Meeresfrüchte",
    meta_desc="Aktuelle Gosch Sylt Preise 2026: Krabbenbrötchen, Matjes, Lachs, Thai-Curry, Bouillabaisse & Weine im vollständigen Tabellen-Überblick.",
    hero_sub="Die nördlichste Fischbude Deutschlands: Alle Gosch Preise auf Sylt und in allen Filialen bundesweit.",
    quick_answer="Bei Gosch Sylt kostet das legendäre Nordseekrabben-Brötchen ca. 9,50 € bis 11,50 € (tagesfangabhängig). Ein warmes Backfisch-Brötchen liegt bei ca. 6,50 €, und die berühmte Gosch Fischsuppe (Bouillabaisse) bei rund 9,90 €.",
    price_level="€€€ (Gehoben)",
    breakfast_info={"hasBreakfast": False, "hoursWeekdays": "Täglich ab 11:00 Uhr geöffnet", "hoursWeekend": "Täglich ab 11:00 Uhr geöffnet", "note": "Snacks und Fischbrötchen ab 11:00 Uhr."},
    saving_tips=["Die Matjesbrötchen bieten das beste Preis-Leistungs-Verhältnis aller Fischbrötchen bei Gosch."],
    history="Jürgen Gosch eröffnete 1972 am Lister Hafen auf Sylt seine erste Imbissbude. Heute ist Gosch eine Kultmarke mit über 40 Standorten bundesweit, inklusive Bahnhöfen und Kreuzfahrtschiffen.",
    categories=[
        {
            "categoryName": "Fischbrötchen & Schnelle Happen",
            "items": [
                {"name": "Nordseekrabben-Brötchen (frisch gepult)", "price": "10,50 €", "calories": "1.450 kJ / 346 kcal", "diet": "Meeresfrüchte"},
                {"name": "Original Gosch Backfisch im Brötchen", "price": "6,50 €", "calories": "2.280 kJ / 545 kcal", "diet": "Fisch"},
                {"name": "Matjesbrötchen 'Hausfrauen Art'", "price": "5,20 €", "calories": "1.680 kJ / 401 kcal", "diet": "Fisch"},
                {"name": "Räucherlachs im Brötchen", "price": "6,90 €", "calories": "1.790 kJ / 428 kcal", "diet": "Fisch"}
            ]
        },
        {
            "categoryName": "Warme Spezialitäten",
            "items": [
                {"name": "Gosch Edelfischsuppe mit Baguette", "price": "9,90 €", "calories": "1.520 kJ / 363 kcal", "diet": "Fisch"},
                {"name": "Gebratenes Zanderfilet auf Rahmsauerkraut", "price": "19,50 €", "calories": "2.890 kJ / 690 kcal", "diet": "Fisch"}
            ]
        }
    ],
    faqs=[
        {
            "q": "Was kostet ein Krabbenbrötchen bei Gosch?",
            "a": "Ein frisches Nordseekrabben-Brötchen bei Gosch kostet 2026 je nach Tagesfang und Saison zwischen 9,50 € und 11,50 €."
        }
    ]
))

# Save all defined chains
for c in chains:
    file_path = os.path.join(OUTPUT_DIR, f"{c['slug']}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(c, f, ensure_ascii=False, indent=2)
    print(f"Created: {c['slug']}.json")

print(f"\nSuccessfully generated {len(chains)} core detailed chain datasets.")

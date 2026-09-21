import json
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "data", "chains")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_chain(
    slug, name, category, title, meta_desc, hero_sub, quick_answer,
    price_level, breakfast_info, saving_tips, history,
    categories, faqs, tags=None
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
        "tags": tags or [category, name.lower(), "preise", "speisekarte"]
    }

additional_chains = [
    # McDonald's Frühstück
    create_chain(
        slug="mc-donalds-fruhstuck",
        name="McDonald's Frühstück",
        category="fast-food",
        title="McDonald's Frühstück Preise 2026 – Zeiten & McMuffin Menüs",
        meta_desc="Aktuelle McDonald's Frühstück Preise 2026 in Deutschland: McMuffin Bacon & Egg, Fresh Chicken, Croissants, Kaffee & genaue Frühstückszeiten im Überblick.",
        hero_sub="Wann gibt es Frühstück bei McDonald's? Alle Zeiten, McMuffins, Rührei und Kaffeespezialitäten mit Preisen.",
        quick_answer="Das McDonald's Frühstück wird montags bis freitags von 06:00 bis 10:30 Uhr serviert, an Wochenenden und Feiertagen bis 11:30 Uhr. Ein einzelner McMuffin Bacon & Egg kostet ca. 3,49 €, im Frühstücksmenü mit Heißgetränk und Hash Brown ca. 5,99 €.",
        price_level="€ (Günstig)",
        breakfast_info={"hasBreakfast": True, "hoursWeekdays": "Mo – Fr: 06:00 – 10:30 Uhr", "hoursWeekend": "Sa – So: 06:00 – 11:30 Uhr", "note": "Gültig in allen teilnehmenden Filialen deutschlandweit."},
        saving_tips=["Das Frühstücks-Duo (z. B. McMuffin + Heißgetränk) spart bis zu 25 % gegenüber dem Einzelkauf."],
        history="Das Frühstückskonzept von McDonald's wurde in den 1970er Jahren mit der Erfindung des Egg McMuffin in den USA geboren und gehört heute fest zur Morgenroutine von Millionen Pendlern in Deutschland.",
        categories=[
            {
                "categoryName": "McMuffins & Warme Klassiker",
                "items": [
                    {"name": "McMuffin Bacon & Egg", "price": "3,49 €", "calories": "1.520 kJ / 363 kcal", "diet": "Schwein/Ei"},
                    {"name": "McMuffin Fresh Chicken", "price": "3,69 €", "calories": "1.650 kJ / 394 kcal", "diet": "Geflügel"},
                    {"name": "McMuffin Sausage & Egg", "price": "3,49 €", "calories": "1.790 kJ / 428 kcal", "diet": "Schwein/Ei"},
                    {"name": "McToast Schinken & Käse", "price": "2,29 €", "calories": "1.120 kJ / 268 kcal", "diet": "Schwein"},
                    {"name": "Rührei mit Bacon & Brötchen", "price": "4,79 €", "calories": "1.890 kJ / 452 kcal", "diet": "Schwein/Ei"},
                    {"name": "Hash Brown (Kartoffelrösti)", "price": "1,99 €", "calories": "580 kJ / 139 kcal", "diet": "Vegan 🌱"}
                ]
            }
        ],
        faqs=[
            {"q": "Bis wie viel Uhr gibt es bei McDonald's Frühstück?", "a": "Unter der Woche (Mo–Fr) endet das Frühstück um 10:30 Uhr. Am Samstag, Sonntag und an Feiertagen endet es um 11:30 Uhr."},
            {"q": "Was kostet ein McMuffin bei McDonald's?", "a": "Ein McMuffin kostet einzeln zwischen 3,29 € und 3,69 €. Im Frühstücksmenü mit Beilage und Kaffee liegt der Preis bei ca. 5,99 €."}
        ]
    ),
    # McDonald's Happy Meal
    create_chain(
        slug="mc-donalds-happy-meal",
        name="McDonald's Happy Meal",
        category="fast-food",
        title="McDonald's Happy Meal Preis 2026 – Spielzeug, Menü & Inhalt",
        meta_desc="Aktuelles McDonald's Happy Meal 2026 in Deutschland: Preise, Auswahl an Hauptgerichten, Beilagen, Spielzeug & Kinderbuch im Überblick.",
        hero_sub="Alles zum Happy Meal für Kinder: Aktuelle Preise, Spielzeug-Serien und gesunde Beilagen-Optionen.",
        quick_answer="Das McDonald's Happy Meal kostet 2026 in Deutschland zwischen 4,99 € und 5,49 €. Es umfasst ein Hauptgericht (Hamburger, Cheeseburger, 4er McNuggets oder 4er McPlant Nuggets), eine Beilage (kleine Pommes oder Bio-Apfeltüte), ein Getränk sowie ein Spielzeug oder Buch.",
        price_level="€ (Günstig)",
        breakfast_info={"hasBreakfast": False, "hoursWeekdays": "Täglich ab 10:30 Uhr", "hoursWeekend": "Täglich ab 11:30 Uhr", "note": "Verfügbar während der regulären Verkaufszeiten."},
        saving_tips=["Statt des Plastikspielzeugs kann immer auch ein hochwertiges Kinderbuch gewählt werden."],
        history="Eingeführt 1979 in den USA, ist das Happy Meal das weltweit erfolgreichste Kindermenü der Gastronomiegeschichte und vermittelt mit Kooperationen (Pokémon, Disney, Hot Wheels) generationsübergreifenden Spielspaß.",
        categories=[
            {
                "categoryName": "Happy Meal Bausteine & Optionen",
                "items": [
                    {"name": "Happy Meal mit 4er Chicken McNuggets", "price": "5,19 €", "calories": "1.890 kJ / 452 kcal", "diet": "Kindermenü"},
                    {"name": "Happy Meal mit Hamburger", "price": "4,99 €", "calories": "1.780 kJ / 425 kcal", "diet": "Kindermenü"},
                    {"name": "Happy Meal mit Cheeseburger", "price": "5,29 €", "calories": "1.980 kJ / 473 kcal", "diet": "Kindermenü"},
                    {"name": "Happy Meal mit 4er McPlant Nuggets", "price": "5,19 €", "calories": "1.650 kJ / 394 kcal", "diet": "Vegan 🌱"},
                    {"name": "Beilage: Bio-Frucht-Tüte (Apfel/Traube)", "price": "Inklusive", "calories": "180 kJ / 43 kcal", "diet": "Vegan 🌱"}
                ]
            }
        ],
        faqs=[
            {"q": "Wie viel kostet ein Happy Meal bei McDonald's in Deutschland?", "a": "Der Preis für ein Happy Meal liegt 2026 je nach Restaurant zwischen 4,99 € und 5,49 €."},
            {"q": "Kann man das Happy Meal Spielzeug einzeln kaufen?", "a": "In vielen Filialen kann das Spielzeug auf Nachfrage an der Kasse für ca. 2,50 € bis 3,00 € separat erworben werden."}
        ]
    ),
    # Burger King Frühstück
    create_chain(
        slug="burger-king-fruhstuck",
        name="Burger King Frühstück",
        category="fast-food",
        title="Burger King Frühstück Preise 2026 – Zeiten, King Toast & Kaffee",
        meta_desc="Aktuelle Burger King Frühstück Preise 2026: King Toast, Toasties, Rührei, Kaffeespezialitäten & genaue Frühstückszeiten im Tabellen-Überblick.",
        hero_sub="Alle Informationen zum Frühstücksangebot bei Burger King Deutschland mit Menüpreisen und Uhrzeiten.",
        quick_answer="Das Burger King Frühstück wird in teilnehmenden Restaurants wochentags von 06:00 bis 10:30 Uhr und sonntags bis 11:00 Uhr angeboten. Beliebt sind die 'King Toasties' (ab ca. 2,99 €) sowie das King Breakfast Menü mit Kaffee und Hash Browns für ca. 5,49 €.",
        price_level="€ (Günstig)",
        breakfast_info={"hasBreakfast": True, "hoursWeekdays": "Mo – Fr: 06:00 – 10:30 Uhr", "hoursWeekend": "Sa – So: 06:00 – 11:00 Uhr", "note": "Prüfe vorab in der BK-App, ob deine Filiale Frühstück anbietet."},
        saving_tips=["Mit BK-Coupons gibt es das Frühstücks-Menü oft zum halben Preis."],
        history="Burger King hat sein Frühstück in Deutschland mehrfach überarbeitet und fokussiert sich heute auf warme Toasts, gegrillte Patties und erstklassigen Röstkaffee.",
        categories=[
            {
                "categoryName": "King Toasties & Frühstücks-Klassiker",
                "items": [
                    {"name": "King Toastie Bacon & Cheese", "price": "2,99 €", "calories": "1.420 kJ / 339 kcal", "diet": "Schwein"},
                    {"name": "King Toastie Ham & Cheese", "price": "2,99 €", "calories": "1.380 kJ / 330 kcal", "diet": "Schwein"},
                    {"name": "Breakfast Burger (mit Spiegelei & Bacon)", "price": "4,29 €", "calories": "2.120 kJ / 507 kcal", "diet": "Rind/Ei"},
                    {"name": "Röststi (Hash Browns 2er)", "price": "1,89 €", "calories": "620 kJ / 148 kcal", "diet": "Vegan 🌱"}
                ]
            }
        ],
        faqs=[
            {"q": "Bis wann gibt es Frühstück bei Burger King?", "a": "In der Regel montags bis freitags bis 10:30 Uhr und samstags sowie sonntags bis 11:00 Uhr."}
        ]
    ),
    # Burger King Spielzeug
    create_chain(
        slug="burger-king-spielzeug",
        name="Burger King King Jr. Meal",
        category="fast-food",
        title="Burger King Spielzeug 2026 – King Jr. Meal Preise & Inhalt",
        meta_desc="Aktuelles Burger King Spielzeug 2026 im King Jr. Meal: Preise, Menü-Zusammenstellung, aktuelle Aktionen und Figuren im Überblick.",
        hero_sub="Alles zum King Jr. Meal: Aktuelle Spielzeug-Kollektionen und Menü-Bestandteile für Kids.",
        quick_answer="Das Burger King King Jr. Meal kostet 2026 ca. 4,99 € bis 5,29 €. Es enthält einen Kids Burger (oder 4er King Nuggets / Plant-based Nuggets), eine kleine Portion Pommes, einen Frucht-Drink oder Softdrink sowie das aktuelle Spielzeug der Monatsaktion.",
        price_level="€ (Günstig)",
        breakfast_info={"hasBreakfast": False, "hoursWeekdays": "Ab 11:00 Uhr", "hoursWeekend": "Ab 11:00 Uhr", "note": "Ganztägig bestellbar."},
        saving_tips=["In der BK App gibt es gelegentlich 'Family Bundles', bei denen das King Jr. Meal rabattiert ist."],
        history="Das King Jr. Meal ist Burger Kings Gegenstück zum Happy Meal und begeistert Kinder mit wechselnden Lizenzen aus Zeichentrick, Gaming und Film.",
        categories=[
            {
                "categoryName": "King Jr. Meal Optionen",
                "items": [
                    {"name": "King Jr. Meal mit Hamburger", "price": "4,99 €", "calories": "1.650 kJ / 394 kcal", "diet": "Kindermenü"},
                    {"name": "King Jr. Meal mit Cheeseburger", "price": "5,19 €", "calories": "1.820 kJ / 435 kcal", "diet": "Kindermenü"},
                    {"name": "King Jr. Meal mit 4er Nuggets", "price": "4,99 €", "calories": "1.580 kJ / 378 kcal", "diet": "Kindermenü"},
                    {"name": "King Jr. Meal mit Plant-based Nuggets", "price": "4,99 €", "calories": "1.490 kJ / 356 kcal", "diet": "Vegan 🌱"}
                ]
            }
        ],
        faqs=[
            {"q": "Was kostet ein King Jr. Meal bei Burger King?", "a": "Das Kindermenü kostet durchschnittlich zwischen 4,99 € und 5,29 €."}
        ]
    ),
    # Burger King Cheeseburger
    create_chain(
        slug="burger-king-cheeseburger-preis",
        name="Burger King Cheeseburger",
        category="fast-food",
        title="Burger King Cheeseburger Preis 2026 – Einzeln & im Menü",
        meta_desc="Was kostet ein Cheeseburger bei Burger King 2026? Aktueller Preis, Kalorien, Zutaten und Doppel-Cheeseburger im Tabellen-Überblick.",
        hero_sub="Der beliebte Snack-Klassiker: Preisentwicklung, Kalorien und Vergleiche.",
        quick_answer="Ein einfacher Cheeseburger bei Burger King kostet 2026 ca. 2,49 €. Der Double Cheeseburger liegt bei etwa 4,19 € und der Chili Cheese Burger bei rund 2,99 €.",
        price_level="€ (Günstig)",
        breakfast_info={"hasBreakfast": False, "hoursWeekdays": "Ab 10:30 Uhr", "hoursWeekend": "Ab 11:00 Uhr", "note": "Ab Ende des Frühstücks verfügbar."},
        saving_tips=["2 Cheeseburger kosten oft weniger als ein einzelner mittlerer Burger und bieten mehr Fleisch."],
        history="Der Cheeseburger ist seit den Anfangstagen von Burger King einer der meistverkauften Artikel weltweit.",
        categories=[
            {
                "categoryName": "Cheeseburger Varianten",
                "items": [
                    {"name": "Cheeseburger Standard", "price": "2,49 €", "calories": "1.280 kJ / 306 kcal", "diet": "Rind"},
                    {"name": "Double Cheeseburger", "price": "4,19 €", "calories": "1.920 kJ / 459 kcal", "diet": "Rind"},
                    {"name": "Chili Cheese Burger", "price": "2,99 €", "calories": "1.340 kJ / 320 kcal", "diet": "Pikant"},
                    {"name": "Bacon Cheeseburger", "price": "2,99 €", "calories": "1.490 kJ / 356 kcal", "diet": "Rind/Bacon"}
                ]
            }
        ],
        faqs=[
            {"q": "Wie viel kostet ein Cheeseburger bei Burger King?", "a": "Aktuell kostet der einfache Cheeseburger ca. 2,49 € in Deutschland."}
        ]
    ),
    # KFC Gutscheine
    create_chain(
        slug="kfc-gutscheine",
        name="KFC Gutscheine & Aktionen",
        category="fast-food",
        title="KFC Gutscheine 2026 – Aktuelle Rabattcodes & Angebote",
        meta_desc="Aktuelle KFC Gutscheine 2026 in Deutschland: PDF Gutscheinbogen, App-Coupons, Tuesday Bucket Angebote und Menü-Rabatte zum Sparen.",
        hero_sub="Alle Sparmöglichkeiten bei Kentucky Fried Chicken Deutschland im Überblick.",
        quick_answer="KFC Gutscheine bieten Rabatte von bis zu 40 % auf Buckets, Twister-Menüs und Zinger-Burger. Sie können digital in der offiziellen KFC Deutschland App aktiviert oder als gedruckter PDF-Gutscheinbogen vorgezeigt werden.",
        price_level="€€ (Mittel)",
        breakfast_info={"hasBreakfast": False, "hoursWeekdays": "Ab 11:00 Uhr", "hoursWeekend": "Ab 11:00 Uhr", "note": "Coupons sind ganztägig einlösbar."},
        saving_tips=["Jeden Dienstag ist 'Tuesday Bucket' Tag mit extra Hähnchenteilen zum Sonderpreis."],
        history="KFC war eine der ersten Ketten in Deutschland, die flächendeckend zweimonatlich erscheinende Couponbögen an Haushalte verteilte.",
        categories=[
            {
                "categoryName": "Beliebte Gutschein-Deals",
                "items": [
                    {"name": "2x Zinger Menü zum Sparpreis", "price": "14,99 € (statt 18,98 €)", "calories": "variiert", "diet": "Geflügel"},
                    {"name": "Crispy Strips Spar-Bucket (10 Stück)", "price": "11,99 €", "calories": "2.890 kJ / 690 kcal", "diet": "Geflügel"},
                    {"name": "Twister Menü + 3 Hot Wings", "price": "9,99 €", "calories": "3.100 kJ / 741 kcal", "diet": "Geflügel"}
                ]
            }
        ],
        faqs=[
            {"q": "Wo finde ich aktuelle KFC Gutscheine?", "a": "In der offiziellen KFC Deutschland Smartphone-App oder direkt auf kfc.de zum Download als PDF."}
        ]
    ),
    # Timberjacks
    create_chain(
        slug="timberjacks-speisekarte",
        name="Timberjacks",
        category="steakhouse-bbq",
        title="Timberjacks Speisekarte Preise 2026 – Beef, BBQ & Motel",
        meta_desc="Aktuelle Timberjacks Speisekarte 2026 in Deutschland: Preise für Steaks, BBQ Ribs, Burger, Mexican Food & Desserts in Kassel, Göttingen & Köln.",
        hero_sub="Das beliebte American-Style BBQ Restaurant & Motel: Alle Preise und Fleischspezialitäten.",
        quick_answer="Bei Timberjacks kostet ein Premium-Burger ca. 14,50 € bis 18,90 €, BBQ Spare Ribs liegen bei ca. 22,50 € und US-Steaks (z. B. 250g Rumpsteak) starten bei rund 28,90 €.",
        price_level="€€€ (Gehoben)",
        breakfast_info={"hasBreakfast": True, "hoursWeekdays": "Ab 08:00 Uhr", "hoursWeekend": "Ab 08:00 Uhr", "note": "Reichhaltiges amerikanisches Frühstücksbuffet."},
        saving_tips=["Die Lunch-Angebote unter der Woche bieten günstige Einstiegspreise."],
        history="Timberjacks kombiniert rustikales Blockhaus-Ambiente (Log Cabin), offenes Feuer, American Beef und Motels in Städten wie Göttingen, Kassel, Siegen und Köln.",
        categories=[
            {
                "categoryName": "Steaks & BBQ Ribs",
                "items": [
                    {"name": "Timberjacks BBQ Ribs (Full Rack)", "price": "22,50 €", "calories": "4.200 kJ / 1.003 kcal", "diet": "Schwein"},
                    {"name": "US Rumpsteak (250g)", "price": "28,90 €", "calories": "2.450 kJ / 585 kcal", "diet": "Rind"},
                    {"name": "Timberjacks Bacon Burger", "price": "16,90 €", "calories": "3.550 kJ / 848 kcal", "diet": "Rind/Bacon"}
                ]
            }
        ],
        faqs=[{"q": "Was kostet Essen bei Timberjacks?", "a": "Hauptgerichte liegen meist zwischen 15 € und 35 € je nach Fleischzuschnitt."}]
    ),
    # Café Del Sol
    create_chain(
        slug="cafe-del-sol-preise",
        name="Café Del Sol",
        category="deutsch-regional",
        title="Café Del Sol Speisekarte Preise 2026 – Schnitzel, Brunch & Cocktails",
        meta_desc="Aktuelle Café Del Sol Preise 2026 in Deutschland: Schnitzel, Burger, Pizza, Frühstücksbuffet, Sonntagsbrunch & Cocktails im Tabellen-Überblick.",
        hero_sub="Kolonialstil-Villa und Urlaubsflair: Alle Speisen, Getränke und Brunch-Preise.",
        quick_answer="Bei Café Del Sol kostet ein Schnitzel Wiener Art ca. 14,90 €, Burger liegen bei ca. 12,50 € bis 15,50 € und das beliebte Wochenend-Frühstücksbuffet kostet rund 17,90 € pro Person.",
        price_level="€€ (Mittel)",
        breakfast_info={"hasBreakfast": True, "hoursWeekdays": "Mo – Sa: 09:00 – 12:00 Uhr", "hoursWeekend": "So & Feiertage (Brunch): 09:00 – 14:00 Uhr", "note": "Großes Frühstücksbuffet mit Rührei, Waffeln, Brötchen und Aufschnitt."},
        saving_tips=["Happy Hour für Cocktails ab 17:00 Uhr nutzen."],
        history="Café Del Sol wurde 2001 in Hildesheim gegründet und betreibt über 30 freistehende Freizeithäuser im Kolonialstil.",
        categories=[
            {
                "categoryName": "Schnitzel & Hauptgerichte",
                "items": [
                    {"name": "Schnitzel Wiener Art mit Pommes", "price": "14,90 €", "calories": "3.450 kJ / 824 kcal", "diet": "Schwein"},
                    {"name": "Jägerschnitzel mit Champignonrahmsauce", "price": "16,90 €", "calories": "3.890 kJ / 929 kcal", "diet": "Schwein"},
                    {"name": "Frühstücksbuffet (Samstags)", "price": "15,50 €", "calories": "variiert", "diet": "Buffet"},
                    {"name": "Sonntagsbrunch Schlemmerbuffet", "price": "18,90 €", "calories": "variiert", "diet": "Buffet"}
                ]
            }
        ],
        faqs=[{"q": "Was kostet das Frühstücksbuffet im Café Del Sol?", "a": "Samstags liegt das Buffet bei ca. 15,50 €, der große Sonntagsbrunch bei ca. 18,90 €."}]
    ),
    # Alex Restaurant
    create_chain(
        slug="alex-restaurant-preise",
        name="Alex Restaurant",
        category="deutsch-regional",
        title="Alex Restaurant Speisekarte Preise 2026 – Brunch, Burger & Pasta",
        meta_desc="Aktuelle Alex Restaurant Preise 2026: Das berühmte Alex Frühstücksbuffet, Sonntagsbrunch, Burger, Bowls & Cocktails im Tabellen-Überblick.",
        hero_sub="Das beliebte Ganztages-Gastronomiekonzept in deutschen Innenstädten: Alle Speise- und Buffetpreise.",
        quick_answer="Im Alex Restaurant kostet das tägliche Frühstücksbuffet werktags ca. 14,50 €, an Sonn- und Feiertagen ca. 19,50 €. Burger und Bowls auf der Abendkarte liegen zwischen 12,90 € und 17,50 €.",
        price_level="€€ (Mittel)",
        breakfast_info={"hasBreakfast": True, "hoursWeekdays": "Mo – Sa: 08:00 – 12:00 Uhr", "hoursWeekend": "So: 09:00 – 14:30 Uhr (Brunch)", "note": "Großes Schlemmerbuffet mit warmen und kalten Speisen."},
        saving_tips=["Unter der Woche ist das Frühstücksbuffet deutlich günstiger als am Sonntag."],
        history="Alex Gaststätten gehören zur Mitchells & Butlers Gruppe und sind an zentralen Plätzen in über 35 deutschen Städten vertreten.",
        categories=[
            {
                "categoryName": "Frühstücksbuffet & Schlemmen",
                "items": [
                    {"name": "Alex Frühstücksbuffet (Mo–Sa)", "price": "14,50 €", "calories": "variiert", "diet": "Buffet"},
                    {"name": "Großer Sonntagsbrunch", "price": "19,50 €", "calories": "variiert", "diet": "Buffet"},
                    {"name": "Alex Classic Cheeseburger mit Pommes", "price": "14,90 €", "calories": "3.650 kJ / 872 kcal", "diet": "Rind"}
                ]
            }
        ],
        faqs=[{"q": "Was kostet der Brunch bei Alex?", "a": "Der Sonntagsbrunch liegt 2026 bei ca. 19,50 € pro Person exklusive Heißgetränke."}]
    ),
    # Hofmanns Menü
    create_chain(
        slug="hofmanns-menu-preise",
        name="Hofmanns Menü",
        category="deutsch-regional",
        title="Hofmanns Menü Manufaktur Preise 2026 – Speisekarte & Katalog",
        meta_desc="Aktuelle Hofmanns Menü Preise 2026: Katalog Preisliste für Tiefkühlmenüs, Mittagstisch, Seniorenmenüs & Betriebsgastronomie im Überblick.",
        hero_sub="Traditionelle Menü-Manufaktur für Gemeinschaftsverpflegung und Senioren: Alle Menüpreise im Katalog.",
        quick_answer="Ein Einzelmenü aus dem Hofmanns Katalog kostet 2026 je nach Kategorie zwischen 6,50 € und 9,80 €. Die Menüs zeichnen sich durch handwerkliche Zubereitung und Verzicht auf geschmacksverstärkende Zusatzstoffe aus.",
        price_level="€€ (Günstig bis Mittel)",
        breakfast_info={"hasBreakfast": False, "hoursWeekdays": "Lieferdienst & Vorbestellung", "hoursWeekend": "Lieferdienst", "note": "Tiefkühl- und Heißanlieferung."},
        saving_tips=["Wochen- und Monatsabonnements bieten gestaffelte Mengenrabatte."],
        history="Seit 1960 steht die Hofmann Menü-Manufaktur aus Boxberg-Schweigern für hochwertige Fertigmenüs für Firmen, Heime und Privathaushalte.",
        categories=[
            {
                "categoryName": "Menü-Klassiker aus dem Katalog",
                "items": [
                    {"name": "Rinderroulade 'Hausfrauen Art' mit Rotkohl & Klößen", "price": "9,20 €", "calories": "2.890 kJ / 690 kcal", "diet": "Rind"},
                    {"name": "Königsberger Klopse mit Kapernsauce & Reis", "price": "7,90 €", "calories": "2.450 kJ / 585 kcal", "diet": "Kombination"},
                    {"name": "Hähnchengeschnetzeltes mit Spätzle", "price": "8,10 €", "calories": "2.510 kJ / 600 kcal", "diet": "Geflügel"},
                    {"name": "Vegetarische Gemüselasagne", "price": "7,40 €", "calories": "2.150 kJ / 514 kcal", "diet": "Vegetarisch"}
                ]
            }
        ],
        faqs=[{"q": "Was kostet ein Hofmann Menü?", "a": "Im Schnitt liegen die Menüs zwischen 7,00 € und 9,50 € pro Portion."}]
    ),
    # Dean & David
    create_chain(
        slug="dean-and-david-preise",
        name="Dean & David",
        category="fast-food",
        title="Dean & David Speisekarte Preise 2026 – Salate, Bowls & Curries",
        meta_desc="Aktuelle Dean & David Preise 2026: Frische Salate, Warm Bowls, Curries, Sandwiches & Smoothies im gesunden Tabellen-Überblick.",
        hero_sub="Gesundes Fast Food mit Fokus auf Frische, Vitamine und Nachhaltigkeit.",
        quick_answer="Bei Dean & David kostet ein großer frischer Salat ca. 9,95 € bis 13,95 €, eine Warm Bowl liegt bei ca. 11,45 € bis 14,95 € und frisch gepresste Säfte / Smoothies kosten rund 4,95 €.",
        price_level="€€ (Mittel)",
        breakfast_info={"hasBreakfast": True, "hoursWeekdays": "Ab 08:30 Uhr geöffnet", "hoursWeekend": "Ab 10:00 Uhr geöffnet", "note": "Porridge, Chia Pudding und frische Säfte am Morgen."},
        saving_tips=["Bringe eine eigene wiederverwendbare Schüssel mit und erhalte 0,50 € Rabatt."],
        history="Gegründet 2007 von David Baumgartner in München, entwickelte sich Dean & David zur führenden deutschen Kette für gesundes Fast-Casual-Essen.",
        categories=[
            {
                "categoryName": "Salate & Bowls",
                "items": [
                    {"name": "Chicken Caesar Salad", "price": "11,95 €", "calories": "1.890 kJ / 451 kcal", "diet": "Geflügel"},
                    {"name": "Avocado Superfood Salad", "price": "12,45 €", "calories": "1.750 kJ / 418 kcal", "diet": "Vegan 🌱"},
                    {"name": "Salmon Avocado Bowl (Lachs, Quinoa, Edamame)", "price": "14,95 €", "calories": "2.680 kJ / 640 kcal", "diet": "Fisch"},
                    {"name": "Green Thai Curry mit Jasminreis", "price": "10,95 €", "calories": "2.350 kJ / 561 kcal", "diet": "Vegan 🌱"}
                ]
            }
        ],
        faqs=[{"q": "Was kostet ein Salat bei Dean & David?", "a": "Große Salate kosten je nach Topping zwischen 9,95 € und 13,95 €."}]
    ),
    # Kamps Bäckerei
    create_chain(
        slug="kamps-preise",
        name="Kamps Bäckerei",
        category="kaffee-baeckerei",
        title="Kamps Bäckerei Preise 2026 – Franzbrötchen, Snacks & Brot",
        meta_desc="Aktuelle Kamps Preise 2026: Belegte Brötchen, Schoko-Franzbrötchen, Brotsorten, Laugengebäck & Kaffee im Tabellen-Überblick.",
        hero_sub="Traditionshandwerk aus NRW: Alle Kamps Preise für Gebäck, belegte Brote und Heißgetränke.",
        quick_answer="Bei Kamps Bäckerei kostet ein Franzbrötchen ca. 1,95 €, belegte Brötchen liegen zwischen 3,20 € und 4,50 € und ein Cappuccino bei ca. 2,90 €.",
        price_level="€ (Günstig)",
        breakfast_info={"hasBreakfast": True, "hoursWeekdays": "Ab 06:00 Uhr morgens", "hoursWeekend": "Ab 07:00 Uhr", "note": "Traditionelles deutsches Frühstücksangebot mit Kaffee und Gebäck."},
        saving_tips=["Die Kamps Kundenkarte bietet Treuestempel für Gratis-Kaffee und Brot."],
        history="1982 in Düsseldorf gegründet, gehört Kamps mit über 350 Bäckereien zu den bekanntesten Bäckerei-Filialisten Deutschlands.",
        categories=[
            {
                "categoryName": "Süßes & Feingebäck",
                "items": [
                    {"name": "Kamps Franzbrötchen", "price": "1,95 €", "calories": "1.380 kJ / 330 kcal", "diet": "Vegetarisch"},
                    {"name": "Schoko-Franzbrötchen", "price": "2,25 €", "calories": "1.620 kJ / 387 kcal", "diet": "Vegetarisch"},
                    {"name": "Berliner Pfannkuchen", "price": "1,80 €", "calories": "1.250 kJ / 298 kcal", "diet": "Vegetarisch"}
                ]
            }
        ],
        faqs=[{"q": "Was kostet ein Franzbrötchen bei Kamps?", "a": "Ein klassisches Zimt-Franzbrötchen kostet ca. 1,95 €."}]
    ),
    # LeCrobag
    create_chain(
        slug="lecrobag-preise",
        name="LeCrobag",
        category="kaffee-baeckerei",
        title="LeCrobag Speisekarte Preise 2026 – Croissants & Baguettes an Bahnhöfen",
        meta_desc="Aktuelle LeCrobag Preise 2026: Buttercroissant, Faluche, belegte Baguettes & Kaffee an deutschen Bahnhöfen im Tabellen-Überblick.",
        hero_sub="Französischer Genuss für Reisende: Alle LeCrobag Preise an Bahnhöfen und Reisezentren.",
        quick_answer="Bei LeCrobag kostet ein frisches Buttercroissant ca. 2,10 €, belegte französische Baguettes (z. B. Camembert oder Salami) ca. 4,90 € bis 6,20 € und ein Milchkaffee ca. 3,60 €.",
        price_level="€€ (Mittel / Reise-Lage)",
        breakfast_info={"hasBreakfast": True, "hoursWeekdays": "Mo – Fr ab 05:30 Uhr", "hoursWeekend": "Sa – So ab 06:00 Uhr", "note": "Frisch gebackene Croissants für frühe Pendler."},
        saving_tips=["Frühstücks-Kombi aus Croissant + Heißgetränk spart ca. 1,00 €."],
        history="Seit 1981 bringt LeCrobag originales französisches Baguette- und Croissant-Handwerk an die Hauptbahnhöfe Deutschlands.",
        categories=[
            {
                "categoryName": "Viennoiserie & Baguettes",
                "items": [
                    {"name": "Original Buttercroissant", "price": "2,10 €", "calories": "1.120 kJ / 268 kcal", "diet": "Vegetarisch"},
                    {"name": "Schoko-Croissant (Pain au Chocolat)", "price": "2,40 €", "calories": "1.390 kJ / 332 kcal", "diet": "Vegetarisch"},
                    {"name": "Baguette Camembert mit Feigensenf", "price": "5,40 €", "calories": "2.100 kJ / 502 kcal", "diet": "Vegetarisch"},
                    {"name": "Baguette Putenbrust & Remoulade", "price": "5,60 €", "calories": "2.050 kJ / 490 kcal", "diet": "Geflügel"}
                ]
            }
        ],
        faqs=[{"q": "Was kostet ein Croissant bei LeCrobag?", "a": "Ein klassisches französisches Buttercroissant kostet 2026 ca. 2,10 €."}]
    ),
    # Marché
    create_chain(
        slug="marche-preise",
        name="Marché Mövenpick",
        category="bahn-reise",
        title="Marché Speisekarte Preise 2026 – Raststätten & Flughafen Buffet",
        meta_desc="Aktuelle Marché Mövenpick Preise 2026: Schweizer Rösti, Frische-Buffet, Salatteller & Kaffeespezialitäten an Autobahn und Flughafen.",
        hero_sub="Frischeküche an Raststätten und Flughäfen: Alle Preise der Schweizer Marktküche.",
        quick_answer="Bei Marché Mövenpick kostet ein großer Salatteller vom Frischebuffet ca. 11,90 €, originale Schweizer Rösti mit Spiegelei ca. 12,50 € und frisch gepresste Säfte (0,3 l) ca. 4,80 €.",
        price_level="€€€ (Reise-Gastronomie)",
        breakfast_info={"hasBreakfast": True, "hoursWeekdays": "Ab 06:00 Uhr Frühstücksbuffet", "hoursWeekend": "Ab 06:00 Uhr", "note": "Reichhaltiges Marktplatz-Frühstück."},
        saving_tips=["Sanifair-Wertbons von der Autobahntoilette können bei Marché voll angerechnet werden."],
        history="Marché Mövenpick steht seit den 1980ern für das Konzept des offenen Marktplatzes mit Front-Cooking an Raststätten und Verkehrsknotenpunkten.",
        categories=[
            {
                "categoryName": "Marktplatz Klassiker",
                "items": [
                    {"name": "Original Schweizer Rösti mit Käse überbacken", "price": "12,90 €", "calories": "2.890 kJ / 690 kcal", "diet": "Vegetarisch"},
                    {"name": "Großer Salatteller zur freien Auswahl", "price": "11,90 €", "calories": "variiert", "diet": "Vegan 🌱"},
                    {"name": "Frisch gepresster Orangensaft (0,3 l)", "price": "4,80 €", "calories": "520 kJ / 124 kcal", "diet": "Vegan 🌱"}
                ]
            }
        ],
        faqs=[{"q": "Kann man Sanifair-Bons bei Marché einlösen?", "a": "Ja, die Sanifair 50-Cent-Wertbons von Autobahnraststätten werden bei Marché als Zahlungsmittel akzeptiert."}]
    ),
    # Call a Pizza
    create_chain(
        slug="call-a-pizza-preise",
        name="Call a Pizza",
        category="pizza-pasta",
        title="Call a Pizza Speisekarte Preise 2026 – Pizza, Burger & Fingerfood",
        meta_desc="Aktuelle Call a Pizza Preise 2026 in Deutschland: Single, Jumbo, Gigant Pizzen, Burger, Chicken Wings & Sparmenüs im Tabellen-Überblick.",
        hero_sub="Einer der traditionsreichsten Pizza-Lieferdienste Deutschlands: Alle Größen und Preise.",
        quick_answer="Bei Call a Pizza kostet eine Single-Pizza (26 cm) ca. 9,90 €, eine Jumbo-Pizza (32 cm) ca. 14,90 € und die riesige Gigant-Pizza (ca. 45 cm) rund 23,90 €.",
        price_level="€€ (Mittel)",
        breakfast_info={"hasBreakfast": False, "hoursWeekdays": "Täglich ab 11:00 Uhr geöffnet", "hoursWeekend": "Täglich ab 11:00 Uhr", "note": "Lieferdienst bis spät in die Nacht."},
        saving_tips=["Tagesangebote auf der Website und Abholrabatte von bis zu 20 % nutzen."],
        history="1984 in München gegründet, gehört Call a Pizza mit dem Slogan 'Mehr als Pizza' zu den Pionieren der deutschen Liefergastronomie.",
        categories=[
            {
                "categoryName": "Pizzen (Single 26cm | Jumbo 32cm)",
                "items": [
                    {"name": "Pizza Salami", "price": "9,90 € | 14,90 €", "calories": "3.150 kJ / 752 kcal", "diet": "Schwein"},
                    {"name": "Pizza Margherita", "price": "8,50 € | 12,90 €", "calories": "2.680 kJ / 640 kcal", "diet": "Vegetarisch"},
                    {"name": "Pizza Tonno (Thunfisch & Zwiebeln)", "price": "10,90 € | 15,90 €", "calories": "3.220 kJ / 769 kcal", "diet": "Fisch"}
                ]
            }
        ],
        faqs=[{"q": "Wie groß sind die Pizzen bei Call a Pizza?", "a": "Single hat ca. 26 cm, Jumbo ca. 32 cm und Gigant ca. 45 cm Durchmesser."}]
    ),
    # Smiley's Pizza
    create_chain(
        slug="smileys-pizza-preise",
        name="Smiley's Pizza Profis",
        category="pizza-pasta",
        title="Smiley's Pizza Speisekarte Preise 2026 – Ringos, Pizza & Pasta",
        meta_desc="Aktuelle Smiley's Pizza Preise 2026 in Deutschland: Pizza Größen, gefüllte Pizzabrötchen (Ringos), Pasta & Croques im Tabellen-Überblick.",
        hero_sub="Der norddeutsche Pizza-Favorit: Alle Smiley's Preise für Pizza, Pasta und die berühmten Ringos.",
        quick_answer="Bei Smiley's Pizza Profis kostet eine 25-cm-Pizza ca. 9,45 €, eine 32-cm-Pizza ca. 14,95 €. Die beliebten gefüllten Pizzabrötchen ('Ringos' 8er Box mit Dip) liegen bei ca. 6,95 €.",
        price_level="€€ (Mittel)",
        breakfast_info={"hasBreakfast": False, "hoursWeekdays": "Ab 11:00 Uhr geöffnet", "hoursWeekend": "Ab 11:00 Uhr", "note": "Lieferung und Take-Away."},
        saving_tips=["Smiley's Mittags-Gutscheine bieten unter der Woche günstige Menüs."],
        history="1988 in Hamburg gegründet, steht Smiley's vor allem in Nord- und Westdeutschland für Pizza mit frischem Hefeteig und Gouda-Käse.",
        categories=[
            {
                "categoryName": "Pizza & Ringos",
                "items": [
                    {"name": "Pizza Chicago (Salami)", "price": "9,45 € (25cm) | 14,95 € (32cm)", "calories": "3.100 kJ / 741 kcal", "diet": "Schwein"},
                    {"name": "Smiley's Ringos 8er (mit Käse & Schinken)", "price": "6,95 €", "calories": "2.280 kJ / 545 kcal", "diet": "Schwein"},
                    {"name": "Pizza Margherita", "price": "7,95 € (25cm) | 12,45 € (32cm)", "calories": "2.550 kJ / 609 kcal", "diet": "Vegetarisch"}
                ]
            }
        ],
        faqs=[{"q": "Was sind Ringos bei Smiley's?", "a": "Ringos sind frisch gebackene, gefüllte Pizzateig-Rollen mit Käse, Salami oder Gemüse, serviert mit einem Dip nach Wahl."}]
    ),
    # Borchardt Berlin
    create_chain(
        slug="borchardt-berlin-preise",
        name="Restaurant Borchardt Berlin",
        category="deutsch-regional",
        title="Borchardt Berlin Speisekarte Preise 2026 – Schnitzel & Klassiker",
        meta_desc="Aktuelle Borchardt Berlin Preise 2026: Das legendäre Wiener Schnitzel, Austern, Tartar, Weine & Promi-Klassiker am Gendarmenmarkt.",
        hero_sub="Berlins berühmtestes Prominenten-Restaurant am Gendarmenmarkt: Alle aktuellen Preise.",
        quick_answer="Im Restaurant Borchardt in Berlin kostet das legendäre 'Original Wiener Schnitzel' vom Kalb mit lauwarmem Kartoffel-Gurken-Salat ca. 34,00 €. Vorspeisen wie Rindertartar liegen bei ca. 19,50 € und Austern bei ca. 4,50 € bis 6,00 € pro Stück.",
        price_level="€€€€ (Premium / Fine Dining)",
        breakfast_info={"hasBreakfast": False, "hoursWeekdays": "Mo – Fr ab 12:00 Uhr geöffnet", "hoursWeekend": "Sa – So ab 12:00 Uhr", "note": "Mittagstisch und gehobenes Dinner."},
        saving_tips=["Der Business-Lunch zur Mittagszeit bietet ein 2-Gänge-Menü zum günstigeren Festpreis."],
        history="1853 als Delikatessenhandlung von August F. W. Borchardt gegründet, ist das Borchardt an der Französischen Straße heute Berlins legendärster Treffpunkt für Politik, Hollywood-Stars und Wirtschaft.",
        categories=[
            {
                "categoryName": "Borchardt Legenden",
                "items": [
                    {"name": "Original Wiener Schnitzel vom Kalb mit Kartoffel-Gurkensalat", "price": "34,00 €", "calories": "3.850 kJ / 920 kcal", "diet": "Kalb"},
                    {"name": "Borchardt Rindertartar klassisch mariniert", "price": "19,50 €", "calories": "1.890 kJ / 451 kcal", "diet": "Rind"},
                    {"name": "Austern Fines de Claire (6 Stück)", "price": "27,00 €", "calories": "420 kJ / 100 kcal", "diet": "Meeresfrüchte"}
                ]
            }
        ],
        faqs=[{"q": "Was kostet das Schnitzel im Borchardt Berlin?", "a": "Das weltberühmte Wiener Schnitzel vom Kalb kostet 2026 im Borchardt 34,00 €."}]
    ),
    # Café Buur
    create_chain(
        slug="cafe-buur-preise",
        name="Café Buur",
        category="deutsch-regional",
        title="Café Buur Speisekarte Preise 2026 – Brunch in Köln & Düsseldorf",
        meta_desc="Aktuelle Café Buur Preise 2026: Pancakes, Shakshuka, Eggs Benedict, Avocado Toast & Instagram-Brunch-Highlights im Tabellen-Überblick.",
        hero_sub="Der angesagteste Brunch-Hotspot in Köln, Düsseldorf und Frankfurt: Alle Preise.",
        quick_answer="Bei Café Buur kosten Eggs Benedict ca. 13,90 €, Shakshuka ca. 12,50 € und die riesigen Signature Pancakes mit Nutella oder Früchten zwischen 12,90 € und 15,90 €.",
        price_level="€€€ (Gehoben Casual)",
        breakfast_info={"hasBreakfast": True, "hoursWeekdays": "Täglich 09:00 – 18:00 Uhr All Day Brunch", "hoursWeekend": "Täglich 09:00 – 18:00 Uhr", "note": "All Day Breakfast & Brunch den ganzen Tag."},
        saving_tips=["Früh kommen, da vor den Filialen in Köln und Düsseldorf oft lange Schlangen stehen."],
        history="Café Buur startete im Kölner Belgischen Viertel und wurde über Social Media mit opulent dekorierten Brunch-Tellern deutschlandweit bekannt.",
        categories=[
            {
                "categoryName": "All Day Breakfast & Brunch",
                "items": [
                    {"name": "Eggs Benedict mit pochierten Eiern & Sauce Hollandaise", "price": "13,90 €", "calories": "2.890 kJ / 690 kcal", "diet": "Vegetarisch/Ei"},
                    {"name": "Buur's Shakshuka mit Feta & Brot", "price": "12,50 €", "calories": "2.450 kJ / 585 kcal", "diet": "Vegetarisch"},
                    {"name": "Lotus Biscoff Pancakes Tower", "price": "14,90 €", "calories": "3.890 kJ / 930 kcal", "diet": "Vegetarisch"}
                ]
            }
        ],
        faqs=[{"q": "Muss man bei Café Buur reservieren?", "a": "Café Buur arbeitet meist nach dem Prinzip 'First come, first served' ohne Tischreservierung."}]
    ),
    # Buddha Lounge Flensburg
    create_chain(
        slug="buddha-lounge-flensburg-speisekarte",
        name="Buddha Lounge Flensburg",
        category="deutsch-regional",
        title="Buddha Lounge Flensburg Speisekarte Preise 2026 – Sushi & Wok",
        meta_desc="Aktuelle Buddha Lounge Flensburg Preise 2026: Sushi Platten, knusprige Ente, Wok-Curries & asiatische Spezialitäten im Tabellen-Überblick.",
        hero_sub="Das beliebte asiatische Restaurant in Flensburg: Alle Preise für Sushi und Wokgerichte.",
        quick_answer="In der Buddha Lounge Flensburg kosten Hauptgerichte aus dem Wok (z. B. knusprige Ente oder Hähnchen mit Thai-Curry) ca. 13,50 € bis 17,90 €. Sushi-Rollen und Maki-Sets starten bei ca. 8,50 €.",
        price_level="€€ (Mittel)",
        breakfast_info={"hasBreakfast": False, "hoursWeekdays": "Täglich ab 12:00 Uhr geöffnet", "hoursWeekend": "Täglich ab 12:00 Uhr", "note": "Mittagsangebote Mo–Fr von 12:00 bis 15:00 Uhr."},
        saving_tips=["Der Mittagstisch unter der Woche spart bis zu 25 % auf Wokgerichte."],
        history="Die Buddha Lounge Flensburg hat sich zu einer beliebten Adresse für asiatische Fusionsküche und frisches Sushi an der Förde etabliert.",
        categories=[
            {
                "categoryName": "Wok-Spezialitäten & Sushi",
                "items": [
                    {"name": "Knusprige Ente mit rotem Thai-Curry & Gemüse", "price": "16,90 €", "calories": "3.250 kJ / 776 kcal", "diet": "Geflügel"},
                    {"name": "Gebratene Nudeln mit Hähnchenbrust", "price": "12,50 €", "calories": "2.890 kJ / 690 kcal", "diet": "Geflügel"},
                    {"name": "Buddha Sushi Set (18 gemischte Teile)", "price": "19,90 €", "calories": "2.450 kJ / 585 kcal", "diet": "Fisch/Vegetarisch"}
                ]
            }
        ],
        faqs=[{"q": "Gibt es vegetarische Gerichte in der Buddha Lounge?", "a": "Ja, fast alle Curries und Nudelgerichte können mit Tofu statt Fleisch bestellt werden."}]
    ),
    # Landgasthof Adler
    create_chain(
        slug="landgasthof-adler-speisekarte",
        name="Landgasthof Adler",
        category="deutsch-regional",
        title="Landgasthof Adler Speisekarte Preise 2026 – Schwäbische Küche",
        meta_desc="Aktuelle Landgasthof Adler Preise 2026: Zwiebelrostbraten, hausgemachte Maultaschen, Kässpätzle & gutbürgerliche deutsche Klassiker.",
        hero_sub="Traditionelle schwäbische und süddeutsche Gastlichkeit: Alle Speisen und Preise.",
        quick_answer="Im traditionsreichen Landgasthof Adler kostet ein schwäbischer Zwiebelrostbraten mit handgemachten Spätzle ca. 24,50 €. Hausgemachte Maultaschen in der Brühe oder geschmälzt liegen bei ca. 12,90 € bis 14,50 €.",
        price_level="€€ (Mittel)",
        breakfast_info={"hasBreakfast": True, "hoursWeekdays": "Für Hotelgäste ab 07:00 Uhr", "hoursWeekend": "Ab 08:00 Uhr", "note": "Regionales Landfrühstück mit Bauernbrot."},
        saving_tips=["Saisonale Aktionen wie die Spargel- oder Wildwochen bieten lokale Köstlichkeiten."],
        history="Der Name 'Adler' steht in Süddeutschland für jahrhundertealte Wirtshauskultur mit frischen Zutaten aus der Region.",
        categories=[
            {
                "categoryName": "Schwäbische Traditionsgerichte",
                "items": [
                    {"name": "Schwäbischer Zwiebelrostbraten mit Trollingersauce & Spätzle", "price": "24,50 €", "calories": "3.650 kJ / 872 kcal", "diet": "Rind"},
                    {"name": "Hausgemachte Maultaschen 'geschmälzt' mit Kartoffelsalat", "price": "13,90 €", "calories": "2.750 kJ / 657 kcal", "diet": "Schwein/Rind"},
                    {"name": "Allgäuer Kässpätzle mit Röstzwiebeln & grünem Salat", "price": "12,90 €", "calories": "3.100 kJ / 741 kcal", "diet": "Vegetarisch"}
                ]
            }
        ],
        faqs=[{"q": "Was kostet der Zwiebelrostbraten im Landgasthof Adler?", "a": "Der Zwiebelrostbraten mit hausgemachten Spätzle kostet 2026 rund 24,50 €."}]
    ),
    # Gasthof zur Post
    create_chain(
        slug="gasthof-zur-post-speisekarte",
        name="Gasthof zur Post",
        category="deutsch-regional",
        title="Gasthof zur Post Speisekarte Preise 2026 – Bayerische Schmankerl",
        meta_desc="Aktuelle Gasthof zur Post Preise 2026: Bayerischer Schweinsbraten, Knödel, Helles vom Fass, Schnitzel & bayerische Wirtshaus-Klassiker.",
        hero_sub="Urbayerische Wirtshaustradition: Alle Preise für Schweinsbraten, Knödel und Bierspezialitäten.",
        quick_answer="Im Gasthof zur Post kostet eine krosse Schweinsbraten-Portion mit Dunkelbiersauce und Kartoffelknödel ca. 15,90 €. Ein Schnitzel 'Wiener Art' liegt bei ca. 14,50 € und eine Maß bayerisches Helles Bier bei ca. 8,80 € bis 9,80 €.",
        price_level="€€ (Mittel)",
        breakfast_info={"hasBreakfast": True, "hoursWeekdays": "Ab 07:00 Uhr", "hoursWeekend": "Ab 07:30 Uhr Weißwurstfrühstück", "note": "Klassisches Weißwurstfrühstück mit Brezen und süßem Senf."},
        saving_tips=["Das Weißwurstfrühstück vor 12 Uhr mittags ist ein bayerischer Preis-Hit."],
        history="Gasthöfe mit dem Namen 'Zur Post' markierten historisch die Postkutschenstationen Bayerns und bewahren bis heute authentische Gemütlichkeit.",
        categories=[
            {
                "categoryName": "Bayerische Wirtshausküche",
                "items": [
                    {"name": "Knuspriger Schweinskrustenbraten mit Dunkelbiersauce & Knödel", "price": "15,90 €", "calories": "3.890 kJ / 929 kcal", "diet": "Schwein"},
                    {"name": "Zwei Münchner Weißwürste mit Breze & Händlmaier Senf", "price": "6,90 €", "calories": "1.890 kJ / 451 kcal", "diet": "Kalb/Schwein"},
                    {"name": "Gebackener Leberkäse mit Spiegelei & Bratkartoffeln", "price": "11,50 €", "calories": "3.120 kJ / 745 kcal", "diet": "Schwein"}
                ]
            }
        ],
        faqs=[{"q": "Was kostet der Schweinsbraten im Gasthof zur Post?", "a": "Der Krustenschweinsbraten mit Knödel und Biersauce kostet ca. 15,90 €."}]
    ),
    # Akropolis
    create_chain(
        slug="akropolis-speisekarte",
        name="Restaurant Akropolis",
        category="deutsch-regional",
        title="Akropolis Speisekarte Preise 2026 – Griechische Spezialitäten",
        meta_desc="Aktuelle Akropolis Preise 2026 in Deutschland: Gyros Teller, Bifteki, Souvlaki, Calamari, Tsatsiki & Ouzo im vollständigen Tabellen-Überblick.",
        hero_sub="Griechische Gastfreundschaft in Deutschland: Alle Preise für Gyros, Grillteller und Meeresfrüchte.",
        quick_answer="Im Restaurant Akropolis kostet ein klassischer Gyros-Teller mit Tsatsiki, Pommes und Tomatenreis ca. 14,50 € bis 16,50 €. Der gemischte Akropolis-Grillteller liegt bei ca. 18,90 €.",
        price_level="€€ (Mittel)",
        breakfast_info={"hasBreakfast": False, "hoursWeekdays": "Ab 11:30 Uhr geöffnet", "hoursWeekend": "Ab 11:30 Uhr geöffnet", "note": "Mittagstisch werktags bis 14:30 Uhr."},
        saving_tips=["Der griechische Mittagstisch unter der Woche beinhaltet oft eine kostenlose Tagessuppe oder Salat."],
        history="Griechische Restaurants namens Akropolis sind seit den 1970er Jahren eine feste und beliebte Institution in fast jeder deutschen Stadt.",
        categories=[
            {
                "categoryName": "Grillspezialitäten vom Drehspieß",
                "items": [
                    {"name": "Gyros Teller mit Tsatsiki, Zwiebeln, Pommes & Reis", "price": "15,50 €", "calories": "4.150 kJ / 992 kcal", "diet": "Schwein"},
                    {"name": "Bifteki mit Schafskäse gefüllt, Pommes & Salat", "price": "16,90 €", "calories": "3.850 kJ / 920 kcal", "diet": "Hackfleisch"},
                    {"name": "Akropolis Platte (Gyros, Souvlaki, Steak, Tsatsiki)", "price": "19,50 €", "calories": "5.100 kJ / 1.218 kcal", "diet": "Grillteller"}
                ]
            }
        ],
        faqs=[{"q": "Was kostet ein Gyros-Teller bei Akropolis?", "a": "Ein vollständiger Gyros-Teller mit Beilagen und Tsatsiki kostet ca. 15,50 €."}]
    ),
    # HelloFresh Preise
    create_chain(
        slug="hello-fresh-preise",
        name="HelloFresh",
        category="fast-food",
        title="HelloFresh Preise Deutschland 2026 – Kosten pro Mahlzeit & Box",
        meta_desc="Was kostet HelloFresh 2026 in Deutschland? Preise pro Portion, Boxen für 2 bis 4 Personen, Versandkosten & aktuelle Rabatte im Überblick.",
        hero_sub="Der Kochboxen-Marktführer in Deutschland: Alle Kosten pro Portion und Boxengröße berechnet.",
        quick_answer="Bei HelloFresh Deutschland liegt der Preis pro Portion 2026 zwischen 4,50 € und 7,99 €, abhängig von der Personenzahl (2, 3 oder 4 Personen) und der Anzahl der Gerichte pro Woche (3 bis 5 Mahlzeiten). Hinzu kommen Versandkosten von ca. 5,99 € pro Lieferung.",
        price_level="€€ (Mittel / Abonnement)",
        breakfast_info={"hasBreakfast": False, "hoursWeekdays": "Wöchentliche Kochbox-Lieferung", "hoursWeekend": "Wöchentliche Lieferung", "note": "Wählbare Liefertage von Dienstag bis Samstag."},
        saving_tips=["Neukunden erhalten mit Gutscheincodes oft bis zu 90 € Rabatt verteilt auf die ersten 4 bis 5 Boxen."],
        history="2011 in Berlin gegründet, stieg HelloFresh zum weltweiten Marktführer für Kochboxen auf und liefert Millionen vorportionierte Mahlzeiten pro Monat aus.",
        categories=[
            {
                "categoryName": "Kochboxen Preisübersicht (nach Portionsanzahl)",
                "items": [
                    {"name": "Box für 2 Personen (3 Gerichte = 6 Portionen)", "price": "44,99 € (ca. 7,50 € / Port.)", "calories": "variiert", "diet": "Kochbox"},
                    {"name": "Box für 2 Personen (5 Gerichte = 10 Portionen)", "price": "59,99 € (ca. 6,00 € / Port.)", "calories": "variiert", "diet": "Kochbox"},
                    {"name": "Box für 4 Personen (3 Gerichte = 12 Portionen)", "price": "67,99 € (ca. 5,66 € / Port.)", "calories": "variiert", "diet": "Familienbox"},
                    {"name": "Box für 4 Personen (4 Gerichte = 16 Portionen)", "price": "79,99 € (ca. 5,00 € / Port.)", "calories": "variiert", "diet": "Familienbox"},
                    {"name": "Versandkosten pro Kochbox-Lieferung", "price": "5,99 €", "calories": "-", "diet": "Versand"}
                ]
            }
        ],
        faqs=[
            {"q": "Wie viel kostet eine Portion bei HelloFresh?", "a": "Eine Portion kostet zwischen 4,50 € (bei großen 4-Personen-Boxen mit 5 Gerichten) und 7,99 € (bei kleineren 2-Personen-Boxen)."},
            {"q": "Kann man HelloFresh jederzeit kündigen?", "a": "Ja, das Abonnement ist flexibel und kann wöchentlich pausiert oder vor dem wöchentlichen Bestellschluss gekündigt werden."}
        ]
    )
]

for c in additional_chains:
    file_path = os.path.join(OUTPUT_DIR, f"{c['slug']}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(c, f, ensure_ascii=False, indent=2)
    print(f"Created: {c['slug']}.json")

print(f"\nAll {len(additional_chains)} additional chain datasets successfully written.")

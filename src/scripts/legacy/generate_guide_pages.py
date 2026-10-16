import json
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "data", "chains")

def write_guide(slug, data):
    with open(os.path.join(OUTPUT_DIR, f"{slug}.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Created guide: {slug}.json")

# 1. Fast Food Preisvergleich 2026
write_guide("fast-food-preisvergleich", {
    "slug": "fast-food-preisvergleich",
    "name": "Großer Fast Food Preisvergleich 2026",
    "category": "fast-food",
    "seoTitle": "Fast Food Preisvergleich 2026 – McDonald's vs. Burger King & Co.",
    "metaDescription": "Der große Fast Food Preisvergleich 2026 in Deutschland: Big Mac vs. Whopper, Nuggets, Pommes, Menüpreise & Spartipps im direkten Tabellen-Vergleich.",
    "hero_sub": "Wer ist günstiger? Der direkte Vergleich zwischen McDonald's, Burger King, Subway, KFC und Five Guys.",
    "quickAnswer": "Im direkten Vergleich 2026 ist McDonald's beim Standard-Burger mit 5,99 € (Big Mac) ca. 0,50 € günstiger als Burger King mit 6,49 € (Whopper). Bei den Sparmenüs punktet McDonald's mit dem McSmart Menü (5,99 €), während Burger King mit der King App und 2-für-1 Whopper Aktionen die stärksten Rabatte für Vielesser liefert. Five Guys liegt mit ca. 11,95 € pro Cheeseburger im gehobenen Preissegment.",
    "priceLevel": "Vergleichs-Guide",
    "breakfastInfo": {"hasBreakfast": False, "hoursWeekdays": "-", "hoursWeekend": "-", "note": "Übersicht aller Ketten."},
    "savingTips": [
        "Vergleiche stets die App-Coupons: McDonald's und Burger King bieten fast wöchentlich 2-für-1 Gutscheine.",
        "Bei Subway bietet das 30cm Sub rund 25 % Ersparnis pro Zentimeter im Vergleich zu zwei 15cm Subs.",
        "KFC Tuesday Bucket bietet das beste Preis-Leistungs-Verhältnis für Hähnchenteile."
    ],
    "history": "In den letzten 3 Jahren sind die Fast-Food-Preise in Deutschland inflationsbedingt um rund 18–25 % gestiegen. Verbraucher achten daher heute mehr denn je auf Rabatte, Apps und Sparmenüs.",
    "menuCategories": [
        {
            "categoryName": "Direkter Burger- & Menü-Vergleich",
            "items": [
                {"name": "Flaggschiff-Burger: Big Mac vs. Whopper", "price": "McDonald's 5,99 € | Burger King 6,49 €", "calories": "Big Mac: 505 kcal | Whopper: 642 kcal", "diet": "Rind"},
                {"name": "Standard Cheeseburger", "price": "McDonald's 2,49 € | Burger King 2,49 €", "calories": "McD: 302 kcal | BK: 306 kcal", "diet": "Gleichstand"},
                {"name": "Doppel-Cheeseburger", "price": "McDonald's 3,99 € | Burger King 4,19 €", "calories": "McD: 446 kcal | BK: 459 kcal", "diet": "Rind"},
                {"name": "Großes Standard-Menü (Burger + Pommes + 0,5l Drink)", "price": "McDonald's 9,49 € | Burger King 9,79 €", "calories": "ca. 900–950 kcal", "diet": "Kombi"},
                {"name": "20er Chicken Nuggets Box", "price": "McDonald's 11,49 € | Burger King 11,29 €", "calories": "McD: 864 kcal | BK: 915 kcal", "diet": "Geflügel"},
                {"name": "Kleine Pommes Frites", "price": "McDonald's 2,49 € | Burger King 2,49 €", "calories": "ca. 230–235 kcal", "diet": "Vegan 🌱"}
            ]
        }
    ],
    "faqs": [
        {"q": "Was ist günstiger: McDonald's oder Burger King?", "a": "Bei Einzel-Klassikern ist McDonald's (Big Mac 5,99 €) minimal günstiger als Burger King (Whopper 6,49 €). Burger King bietet jedoch oft aggressivere 2-für-1 Gutscheine in der App."},
        {"q": "Welche Kette hat das günstigste Sparmenü?", "a": "Das McDonald's McSmart Menü für 5,99 € (2 Burger + Pommes + Drink) ist derzeit eines der preiswertesten Fast-Food-Kombi-Angebote in Deutschland."}
    ],
    "tags": ["vergleich", "fast food", "mcdonalds", "burger king", "preise"]
})

# 2. Frühstückszeiten Guide
write_guide("fruehstueckszeiten", {
    "slug": "fruehstueckszeiten",
    "name": "Frühstückszeiten aller Fast Food Ketten 2026",
    "category": "fast-food",
    "seoTitle": "Frühstückszeiten 2026: McDonald's, Burger King & Co. im Überblick",
    "metaDescription": "Bis wann gibt es Frühstück bei McDonald's, Burger King & Co.? Alle Frühstückszeiten für Werktage, Samstage, Sonntage & Feiertage in Deutschland.",
    "hero_sub": "Nie wieder das Frühstück verpassen: Alle Uhrzeiten, wann Frühstück serviert wird und wann die reguläre Speisekarte startet.",
    "quickAnswer": "Bei McDonald's gibt es Frühstück werktags von 06:00 bis 10:30 Uhr, an Wochenenden und Feiertagen bis 11:30 Uhr. Burger King bietet Frühstück meist bis 10:30 Uhr (werktags) bzw. 11:00 Uhr (sonntags) an. In der Deutschen Bahn (ICE Bordbistro) ist Frühstück ganztägig erhältlich, solange der Vorrat reicht.",
    "priceLevel": "Übersichts-Guide",
    "breakfastInfo": {"hasBreakfast": True, "hoursWeekdays": "Siehe Tabelle unten", "hoursWeekend": "Siehe Tabelle unten", "note": "Übersicht aller Anbieter."},
    "savingTips": ["Wer kurz vor Frühstücksende bestellt, kann oft sowohl Frühstücks- als auch reguläre Burger zeitgleich kombinieren."],
    "history": "In Deutschland haben die großen Fast-Food-Ketten ihre Frühstückszeiten in den letzten Jahren am Wochenende verlängert, um Langschläfern entgegenzukommen.",
    "menuCategories": [
        {
            "categoryName": "Frühstückszeiten im direkten Vergleich",
            "items": [
                {"name": "McDonald's Deutschland", "price": "Mo–Fr: 06:00 – 10:30 Uhr", "calories": "Sa, So & Feiertag: bis 11:30 Uhr", "diet": "McMuffin, Rührei"},
                {"name": "Burger King Deutschland", "price": "Mo–Fr: 06:00 – 10:30 Uhr", "calories": "Sa & So: bis 11:00 Uhr", "diet": "King Toasties"},
                {"name": "Deutsche Bahn ICE Bordbistro", "price": "Ganztägig ab Zugabfahrt", "calories": "Solange Vorrat reicht", "diet": "Großes Frühstück"},
                {"name": "Café Del Sol (Frühstücksbuffet)", "price": "Mo–Sa: 09:00 – 12:00 Uhr", "calories": "Sonntagsbrunch: bis 14:00 Uhr", "diet": "Buffet (ca. 15,50–18,90 €)"},
                {"name": "Alex Restaurant (Brunch)", "price": "Mo–Sa: 08:00 – 12:00 Uhr", "calories": "Sonn- & Feiertag: bis 14:30 Uhr", "diet": "Schlemmerbuffet"},
                {"name": "BackWerk & Bäckereien", "price": "Täglich ab 05:30 / 06:00 Uhr", "calories": "Ganztägig belegte Snacks", "diet": "Kaffee & Brezeln"}
            ]
        }
    ],
    "faqs": [
        {"q": "Bis wann gibt es sonntags Frühstück bei McDonald's?", "a": "Sonntags und an Feiertagen wird das McDonald's Frühstück bis 11:30 Uhr serviert."},
        {"q": "Gibt es Burger während der Frühstückszeit?", "a": "In der Regel nicht: Die Grillflächen sind während der Frühstückszeit für Rührei, Bacon und McMuffin-Patties reserviert. Die reguläre Burgerkarte startet exakt nach dem Frühstück."}
    ],
    "tags": ["fruehstueck", "zeiten", "mcdonalds", "burger king", "deutsche bahn"]
})

# 3. Kalorientabelle Fast Food
write_guide("kalorientabelle", {
    "slug": "kalorientabelle",
    "name": "Fast Food Kalorientabelle 2026",
    "category": "fast-food",
    "seoTitle": "Fast Food Kalorientabelle 2026 – Alle Kalorien (kJ & kcal) im Vergleich",
    "metaDescription": "Fast Food Kalorientabelle 2026: Kalorien (kcal & kJ) von McDonald's, Burger King, Subway, Pizza Hut & Five Guys. Kalorienbomben und gesunde Alternativen.",
    "hero_sub": "Wissen, was drinsteckt: Kalorien, Nährwerte und die leichtesten Optionen bekannter Fast-Food-Ketten.",
    "quickAnswer": "Der Burger mit den meisten Kalorien im regulären Fast-Food-Angebot ist der Big Tasty Bacon (McDonald's) mit 912 kcal bzw. der Big King XXL (Burger King) mit 992 kcal. Zu den kalorienärmsten Optionen zählen der Standard-Hamburger (ca. 253 kcal), das Subway 15cm Veggie Delite (ca. 234 kcal) und der Snack Salad Classic (ca. 19 kcal ohne Dressing).",
    "priceLevel": "Nährwert-Guide",
    "breakfastInfo": {"hasBreakfast": False, "hoursWeekdays": "-", "hoursWeekend": "-", "note": "Kalorien aller Speisen."},
    "savingTips": ["Wer Kalorien sparen möchte, tauscht zuckerhaltige Softdrinks gegen Zero-Getränke oder Wasser – das spart auf einen Schlag 170 bis 210 kcal pro Becher."],
    "history": "In Deutschland sind Fast-Food-Ketten verpflichtet, Nährwerttabellen bereitzuhalten. Seit einigen Jahren weisen Ketten wie McDonald's und Burger King die Brennwerte in kJ und kcal direkt an den Menütafeln aus.",
    "menuCategories": [
        {
            "categoryName": "Top Kalorienbomben vs. Leichte Alternativen",
            "items": [
                {"name": "Big King XXL (Burger King)", "price": "8,79 €", "calories": "4.150 kJ / 992 kcal", "diet": "Sehr kalorienreich ⚠️"},
                {"name": "Big Tasty Bacon (McDonald's)", "price": "8,19 €", "calories": "3.808 kJ / 912 kcal", "diet": "Sehr kalorienreich ⚠️"},
                {"name": "Bacon Cheeseburger (Five Guys)", "price": "12,95 €", "calories": "4.430 kJ / 1.060 kcal", "diet": "Sehr kalorienreich ⚠️"},
                {"name": "Whopper (Burger King)", "price": "6,49 €", "calories": "2.685 kJ / 642 kcal", "diet": "Mittel"},
                {"name": "Big Mac (McDonald's)", "price": "5,99 €", "calories": "2.115 kJ / 505 kcal", "diet": "Mittel"},
                {"name": "McChicken Classic (McDonald's)", "price": "5,69 €", "calories": "1.870 kJ / 446 kcal", "diet": "Mittel"},
                {"name": "Hamburger (McDonald's)", "price": "1,99 €", "calories": "1.060 kJ / 253 kcal", "diet": "Kalorienarm ✅"},
                {"name": "Subway 15cm Veggie Delite", "price": "5,49 €", "calories": "980 kJ / 234 kcal", "diet": "Kalorienarm ✅"}
            ]
        }
    ],
    "faqs": [
        {"q": "Welcher Burger hat die meisten Kalorien?", "a": "In Deutschland gehören der Big King XXL von Burger King (992 kcal) und der Five Guys Bacon Cheeseburger (1.060 kcal) zu den Spitzenreitern."},
        {"q": "Wie viele Kalorien hat ein Big Mac?", "a": "Ein McDonald's Big Mac hat in Deutschland exakt 2.115 kJ bzw. 505 kcal."}
    ],
    "tags": ["kalorien", "naehrwerte", "fast food", "diaet", "gesund"]
})

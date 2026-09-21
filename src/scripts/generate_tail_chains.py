import json
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "data", "chains")

def write_chain(slug, data):
    with open(os.path.join(OUTPUT_DIR, f"{slug}.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Created: {slug}.json")

# Edmondo Hamburg
write_chain("edmondo-speisekarte", {
    "slug": "edmondo-speisekarte",
    "name": "Edmondo Hamburg",
    "category": "pizza-pasta",
    "seoTitle": "Edmondo Hamburg Speisekarte Preise 2026 – Big Mamma Group",
    "metaDescription": "Aktuelle Edmondo Hamburg Speisekarte 2026: Trüffelpasta, neapolitanische Pizza, Tiramisu & Cocktail-Preise des Big Mamma Restaurants am Hohen Wall.",
    "hero_sub": "Das spektakuläre italienische Restaurant der Big Mamma Group in Hamburg: Alle Speisen und Preise.",
    "quickAnswer": "Im Restaurant Edmondo in Hamburg kostet die berühmte Trüffelpasta (Mafaldine al Tartufo) ca. 21,50 €, eine neapolitanische Pizza Margherita ca. 13,00 € und hausgemachtes Tiramisu rund 8,50 €.",
    "priceLevel": "€€€ (Gehoben Casual)",
    "breakfastInfo": {"hasBreakfast": False, "hoursWeekdays": "Mo – Fr ab 12:00 Uhr", "hoursWeekend": "Sa – So ab 12:00 Uhr", "note": "Lunch und Dinner."},
    "savingTips": ["Mittags gibt es ein wechselndes Lunch-Menü mit hervorragendem Preis-Leistungs-Verhältnis."],
    "history": "Edmondo ist das erste Hamburger Restaurant der erfolgreichen europäischen Big Mamma Group (u. a. Circolo Popolare London, Pink Mamma Paris) in einem opulenten ehemaligen Bankgebäude.",
    "menuCategories": [
        {
            "categoryName": "Antipasti & Pizza Napoletana",
            "items": [
                {"name": "Burrata pugliese mit Pesto", "price": "14,50 €", "calories": "2.100 kJ / 502 kcal", "diet": "Vegetarisch"},
                {"name": "Pizza Margherita DOP (San Marzano Tomaten, Fior di Latte)", "price": "13,00 €", "calories": "3.100 kJ / 741 kcal", "diet": "Vegetarisch"},
                {"name": "Pizza Queen Tartufo (Frische Trüffel & Ricotta)", "price": "21,00 €", "calories": "3.650 kJ / 872 kcal", "diet": "Vegetarisch"}
            ]
        },
        {
            "categoryName": "Pasta Fresca & Dolci",
            "items": [
                {"name": "Mafaldine al Tartufo (Frische Trüffelpasta)", "price": "21,50 €", "calories": "3.450 kJ / 824 kcal", "diet": "Vegetarisch"},
                {"name": "Il Tiramisù tradizionale", "price": "8,50 €", "calories": "1.890 kJ / 452 kcal", "diet": "Vegetarisch"}
            ]
        }
    ],
    "faqs": [
        {"q": "Was kostet die Trüffelpasta im Edmondo Hamburg?", "a": "Die beliebte Mafaldine al Tartufo mit frischen Sommertrüffeln kostet 2026 ca. 21,50 €."}
    ],
    "tags": ["pizza-pasta", "edmondo", "hamburg", "speisekarte", "preise"]
})

# Deutsches Haus
write_chain("deutsches-haus-speisekarte", {
    "slug": "deutsches-haus-speisekarte",
    "name": "Deutsches Haus",
    "category": "deutsch-regional",
    "seoTitle": "Deutsches Haus Speisekarte Preise 2026 – Regionale Hausmannskost",
    "metaDescription": "Aktuelle Deutsches Haus Speisekarte 2026 mit Preisen: Rinderbraten, Schnitzel, Fischgerichte, Pfannengerichte & deutsche Klassiker im Tabellen-Überblick.",
    "hero_sub": "Gutbürgerliche Küche und herzhafte Hausmannskost: Alle traditionellen Gerichte und Preise.",
    "quickAnswer": "Im Restaurant Deutsches Haus kostet ein herzhafter Sauerbraten mit Apfelrotkohl und Klößen ca. 18,90 €, ein Schnitzel 'Wiener Art' mit Bratkartoffeln ca. 15,50 € und hausgemachte Suppen starten bei 6,20 €.",
    "priceLevel": "€€ (Mittel)",
    "breakfastInfo": {"hasBreakfast": True, "hoursWeekdays": "Für Hausgäste ab 07:00 Uhr", "hoursWeekend": "Ab 08:00 Uhr", "note": "Klassisches deutsches Frühstücksbuffet."},
    "savingTips": ["Tagesmenüs und Seniorenportionen bieten attraktive Preisnachlässe."],
    "history": "Gaststätten mit dem Namen 'Deutsches Haus' blicken in ganz Deutschland auf über ein Jahrhundert Tradition bürgerlicher Gastlichkeit zurück.",
    "menuCategories": [
        {
            "categoryName": "Regionale Spezialitäten & Braten",
            "items": [
                {"name": "Rheinischer Sauerbraten mit Kartoffelklößen & Rotkohl", "price": "18,90 €", "calories": "3.450 kJ / 824 kcal", "diet": "Rind"},
                {"name": "Schnitzel 'Wiener Art' mit Bratkartoffeln & Preiselbeeren", "price": "15,50 €", "calories": "3.890 kJ / 929 kcal", "diet": "Schwein"},
                {"name": "Gebratenes Zanderfilet auf Rahmgemüse", "price": "19,50 €", "calories": "2.680 kJ / 640 kcal", "diet": "Fisch"}
            ]
        }
    ],
    "faqs": [{"q": "Welche Gerichte gibt es im Deutschen Haus?", "a": "Typisch deutsche Klassiker wie Schnitzel, Rinderbraten, Sauerbraten und regionale Pfannengerichte."}],
    "tags": ["deutsch-regional", "deutsches haus", "speisekarte", "preise"]
})

# Brauhaus
write_chain("brauhaus-speisekarte", {
    "slug": "brauhaus-speisekarte",
    "name": "Traditionelles Brauhaus",
    "category": "deutsch-regional",
    "seoTitle": "Brauhaus Speisekarte Preise 2026 – Haxe, Schnitzel & Bierpreise",
    "meta_desc": "Aktuelle Brauhaus Speisekarte 2026: Knusprige Schweinshaxe, Brauhaus-Schnitzel, Weißwürste & Bierpreise im zünftigen Tabellen-Überblick.",
    "hero_sub": "Zünftige Brauhausküche und frisch gebrautes Bier: Alle Speisen und Getränke im Preisvergleich.",
    "quickAnswer": "In typischen deutschen Brauhäusern (z. B. Köln, München, Düsseldorf) kostet eine knusprige Schweinshaxe mit Sauerkraut und Knödeln ca. 18,90 € bis 22,50 €. Ein frisch gezapftes Bier (0,5 l bzw. Kölsch/Alt 0,2 l) liegt bei 2,40 € bis 5,20 €.",
    "priceLevel": "€€ (Mittel)",
    "breakfastInfo": {"hasBreakfast": True, "hoursWeekdays": "Ab 10:00 Uhr Weißwurstfrühstück", "hoursWeekend": "Ab 09:30 Uhr Frühschoppen", "note": "Frische Brezen und Weißwürste."},
    "savingTips": ["Frühschoppen und Mittagstisch bieten oft reduzierte Getränke- und Essenspreise."],
    "history": "Deutsche Brauhäuser sind seit Jahrhunderten der Mittelpunkt geselligen Lebens und verbinden Braukunst mit deftigen regionalen Spezialitäten.",
    "menuCategories": [
        {
            "categoryName": "Brauhaus Schmankerl & Haxen",
            "items": [
                {"name": "Ganze knusprige Schweinshaxe mit Biersauce & Knödel", "price": "21,50 €", "calories": "4.890 kJ / 1.168 kcal", "diet": "Schwein"},
                {"name": "Braumeister-Schnitzel mit Röstzwiebeln & Bratkartoffeln", "price": "16,90 €", "calories": "3.950 kJ / 944 kcal", "diet": "Schwein"},
                {"name": "Himmel un Ääd (Blutwurst, Kartoffelstampf, Apfelkompott)", "price": "14,50 €", "calories": "2.890 kJ / 690 kcal", "diet": "Schwein"}
            ]
        }
    ],
    "faqs": [{"q": "Was kostet eine Haxe im Brauhaus?", "a": "Eine ganze Grill-Schweinshaxe mit Beilagen kostet 2026 im Schnitt ca. 21,50 €."}],
    "tags": ["deutsch-regional", "brauhaus", "speisekarte", "preise"]
})

# Poseidon
write_chain("poseidon-speisekarte", {
    "slug": "poseidon-speisekarte",
    "name": "Restaurant Poseidon",
    "category": "deutsch-regional",
    "seoTitle": "Poseidon Speisekarte Preise 2026 – Griechische Küche & Grillteller",
    "metaDescription": "Aktuelle Poseidon Speisekarte 2026: Gyros Spezialitäten, Suflaki, Lammkoteletts, Calamari & Meze im Tabellen-Überblick.",
    "hero_sub": "Griechische Meeresfrüchte und Spezialitäten vom Holzkohlegrill.",
    "quickAnswer": "Im Restaurant Poseidon kostet ein Gyros-Teller ca. 15,20 €, Lammkoteletts vom Grill ca. 21,90 € und gebratene Calamari mit Tsatsiki ca. 16,50 €.",
    "priceLevel": "€€ (Mittel)",
    "breakfastInfo": {"hasBreakfast": False, "hoursWeekdays": "Ab 11:30 Uhr geöffnet", "hoursWeekend": "Ab 11:30 Uhr", "note": "Mittagstisch mit Ouzo zur Begrüßung."},
    "savingTips": ["Günstiger Mittagstisch von Dienstag bis Freitag."],
    "history": "Poseidon ist einer der traditionsreichsten Namen für griechische Gastronomie in ganz Deutschland.",
    "menuCategories": [
        {
            "categoryName": "Grill & Gyros",
            "items": [
                {"name": "Poseidon Grillteller (Gyros, Souvlaki, Lammkrone, Tsatsiki)", "price": "19,90 €", "calories": "4.950 kJ / 1.183 kcal", "diet": "Fleisch"},
                {"name": "Gyros in Metaxasauce mit Käse überbacken", "price": "16,50 €", "calories": "4.120 kJ / 984 kcal", "diet": "Schwein"}
            ]
        }
    ],
    "faqs": [{"q": "Was kostet ein Grillteller bei Poseidon?", "a": "Ein gemischter Grillteller kostet ca. 19,90 € inklusive Beilagen und Salat."}],
    "tags": ["deutsch-regional", "poseidon", "griechisch", "speisekarte", "preise"]
})
